#!/usr/bin/env python3
"""Validate challenge.yml files by installing them into a (test) CTFd.

Run from the Archive repo root with ctfcli's Python (it imports ctfcli), with
CTFCLI_URL and CTFCLI_ACCESS_TOKEN pointing at a CTFd admin token:

    uv tool install ctfcli
    ~/.local/share/uv/tools/ctfcli/bin/python tools/ctfd_validate.py [paths...]

WARNING: this creates/updates challenges and submits flags as the token's user,
so point it at a throwaway CTFd, not a live event.

Each path is a challenge yml file, a challenge dir, or a year dir (searched
recursively, skipping Pegasus/publish/.build). For every challenge yml:
  1. schema checks (required fields, flags present, files are real files, each
     /files/ handout link in the description names a published file; run
     `pwnmake publish` first)
  2. ctfcli lint (Dockerfile/image mismatch ignored), plus a leak check: a
     handout containing a challenge's exact flag fails unless the challenge is
     listed in FLAG_IN_HANDOUT_OK; a bare "sun{" (decoys, format strings) only warns
  3. install into CTFd (create, or sync if it already exists)
  4. ctfcli verify (remote matches local)
  5. submit every static flag and confirm CTFd says "correct"
Also checks that challenge names are unique across the whole archive.

Handouts are published by each challenge's Build.mk and served by the web
server, not CTFd, at /files/<prefix>/<challenge dir>/<file name>. The prefix is
sun/<year> here; to validate another challenge repo, pass
--files-prefix=<prefix> (e.g. hackucf).
Exit status is nonzero if anything failed.
"""
import os, re, sys, glob
from pathlib import Path
import yaml

from ctfcli.core.challenge import Challenge
from ctfcli.core.exceptions import LintException, ChallengeException
from ctfcli.core.api import API

ROOT = Path.cwd()
SKIP_PARTS = {"Pegasus", "publish", ".build", "node_modules", ".git"}
YEARS = ["17", "18", "19", "20", "21", "22", "23", "24", "25"]

# Handouts linked from descriptions that aren't in git: the old ctf.hackucf.org
# served them, and they have to be copied onto the web server by hand.
HANDOUTS_NOT_IN_GIT = {
    "/files/sun/18/Forensics/OldFavorites/OldFavorites.mp4",
    "/files/sun/18/Forensics/OldFavorites2/OldFavorites2.mp4",
    "/files/sun/18/Forensics/phishy-phishy/phishy_chall.zip",
}

# Challenges whose handout is *supposed* to contain the full flag (e.g. a pcap
# where finding the flag in the capture is the whole challenge).
FLAG_IN_HANDOUT_OK = {
    "24/Forensics/icmp1/challenge.yml",      # flag is in the pcap
    "24/Reversing/twine/challenge.yml",      # intended solve is `strings`
}

DIFFICULTY_TAGS = ("beginner", "intermediate", "expert")

# URL prefix for handouts of challenges outside the year dirs (--files-prefix)
FILES_PREFIX = None


def find_ymls(paths):
    out = []
    for p in paths:
        p = Path(p)
        if p.is_file():
            out.append(p)
            continue
        for f in sorted(p.rglob("challenge*.yml")):
            rel = f.relative_to(ROOT) if f.is_absolute() else f
            if SKIP_PARTS & set(rel.parts):
                continue
            out.append(f)
    return out


def all_archive_ymls():
    return find_ymls([ROOT / y for y in YEARS])


def check_names():
    names = {}
    for f in all_archive_ymls():
        try:
            n = yaml.safe_load(f.read_text()).get("name")
        except Exception:
            continue
        names.setdefault(n, []).append(str(f.relative_to(ROOT)))
    return {n: fs for n, fs in names.items() if len(fs) > 1}


def schema_issues(f, d):
    issues = []
    for k in ("name", "author", "category", "description", "attribution", "flags", "tags", "version"):
        if not d.get(k):
            issues.append(f"missing {k}")
    if d.get("type") != "standard":
        issues.append("archive challenges must use static scoring (type: standard)")
    if not isinstance(d.get("value"), int) or not 0 < d["value"] <= 500:
        issues.append("challenge needs a static value from 1 to 500")
    if "extra" in d:
        issues.append("standard challenges shouldn't set extra")
    rel = f.resolve().relative_to(ROOT.resolve()).parts if f.resolve().is_relative_to(ROOT.resolve()) else ()
    if rel and rel[0] in YEARS:
        events = [t for t in d.get("tags") or [] if str(t).startswith("sunshinectf-")]
        if events != [f"sunshinectf-20{rel[0]}"]:
            issues.append(f"needs exactly one event tag, sunshinectf-20{rel[0]}")
    tiers = [t for t in d.get("tags") or [] if t in DIFFICULTY_TAGS]
    if len(tiers) != 1:
        issues.append(f"needs exactly one difficulty tag ({', '.join(DIFFICULTY_TAGS)})")
    for fl in d.get("files") or []:
        p = f.parent / fl
        if not p.is_file():
            issues.append(f"file missing or not a file: {fl}")
    for k in ("image", "host", "healthcheck"):
        if d.get(k):
            issues.append(f"{k} should not be set (hosting is done by pwnmake)")
    return issues


HANDOUT_LINK_RE = re.compile(r"^\* \[([^\]\n]+)\]\((/files/[^)\s]+)\)$")


def handout_base(f):
    """(URL prefix, repo's publish dir, challenge's publish dir) for the
    challenge's handouts, or None."""
    rel = f.resolve().relative_to(ROOT.resolve()).parts[:-1]
    if rel and rel[0] in YEARS:
        repo_pub = ROOT / rel[0] / "publish"
        return "/".join(("/files/sun",) + rel), repo_pub, repo_pub.joinpath(*rel[1:])
    if FILES_PREFIX:
        repo_pub = ROOT / "publish"
        return "/".join(("/files", FILES_PREFIX) + rel), repo_pub, repo_pub.joinpath(*rel)
    return None


def handout_issues(f, d):
    """(problems, warnings, published handout paths) for the description's
    /files/ handout links."""
    problems, warnings, paths = [], [], []
    desc = d.get("description") or ""
    links = [m.groups() for m in map(HANDOUT_LINK_RE.match, desc.split("\n")) if m]
    if desc.count("](/files/") != len(links):
        problems.append("a /files/ handout link must be a list item on a line of its own")
    if not links:
        return problems, warnings, paths
    base = handout_base(f)
    if base is None:
        warnings.append("can't check handout links without --files-prefix")
        return problems, warnings, paths
    url_base, repo_pub, pub = base
    published = repo_pub.is_dir()
    for name, url in links:
        if url != f"{url_base}/{name}":
            problems.append(f"handout link {url} should be {url_base}/{name}")
            continue
        if url in HANDOUTS_NOT_IN_GIT:
            warnings.append(f"handout {name} isn't in git; copy it onto the web server by hand")
        elif not published:
            warnings.append(f"can't check handout {name}: run `pwnmake publish` first")
        elif not (pub / name).is_file():
            problems.append(f"handout {name} isn't published; add it to PUBLISH in Build.mk")
        else:
            paths.append(pub / name)
    return problems, warnings, paths


def static_flags(d):
    out = []
    for fl in d.get("flags") or []:
        if isinstance(fl, str):
            out.append(fl)
        elif isinstance(fl, dict) and fl.get("type", "static") == "static":
            out.append(fl["content"])
    return out


def main(argv):
    global FILES_PREFIX
    for a in [a for a in argv if a.startswith("--files-prefix=")]:
        FILES_PREFIX = a.split("=", 1)[1].strip("/")
        argv.remove(a)
    targets = find_ymls(argv or [ROOT / y for y in YEARS])
    api = API()
    failures = 0

    dups = check_names()
    if dups:
        failures += 1
        print("[FAIL] duplicate challenge names across archive:")
        for n, fs in dups.items():
            print(f"    {n!r}: {', '.join(fs)}")

    for f in targets:
        rel = f.relative_to(ROOT) if f.is_absolute() else f
        problems = []
        warnings = []
        try:
            d = yaml.safe_load(f.read_text())
        except Exception as e:
            print(f"[FAIL] {rel}: yaml: {e}")
            failures += 1
            continue
        problems += schema_issues(f, d)
        more, warn, handout_paths = handout_issues(f, d)
        problems += more
        warnings += warn

        try:
            ch = Challenge(f)
        except ChallengeException as e:
            print(f"[FAIL] {rel}: load: {e}")
            failures += 1
            continue

        try:
            ch.lint(skip_hadolint=True, flag_format="sun{")
        except LintException as e:
            for cat, msgs in e.issues.items():
                if cat == "dockerfile":
                    continue
                for m in msgs:
                    # ctfcli flags any "sun{" string in a handout. A bare prefix or
                    # format string is common (decoys, checkers, printf formats);
                    # the exact-flag scan below decides what's a real leak.
                    if m.startswith("Potential flag found"):
                        warnings.append(f"handout contains 'sun{{': {m.strip()}")
                    else:
                        problems.append(f"lint {cat}: {m.strip()}")

        flags_exact = [fl.encode() for fl in static_flags(d)]
        for p in [f.parent / fl for fl in d.get("files") or []] + handout_paths:
            fl = p.name
            if p.is_file():
                data = p.read_bytes()
                for flag in flags_exact:
                    if flag in data:
                        msg = f"handout {fl} contains the exact flag"
                        if str(rel) in FLAG_IN_HANDOUT_OK:
                            warnings.append(msg + " (allowed)")
                        else:
                            problems.append(msg)

        if not problems:
            try:
                remote = {c["name"]: c["id"] for c in Challenge.load_installed_challenges()}
                if ch["name"] in remote:
                    ch.sync()
                else:
                    ch.create()
            except Exception as e:
                problems.append(f"install: {e}")

        if not problems:
            try:
                # ctfcli 0.1.8 vs CTFd 3.8: logic=any isn't treated as a default, and
                # standard challenges come back with null initial/decay/minimum ("extra"),
                # and dynamic ones report their current value.
                ignore = ("logic", "value") if d.get("type") == "dynamic" else ("logic", "extra")
                if not ch.verify(ignore=ignore):
                    problems.append("verify: remote differs from challenge.yml")
            except Exception as e:
                problems.append(f"verify: {e}")

        if not problems:
            cid = {c["name"]: c["id"] for c in Challenge.load_installed_challenges()}[ch["name"]]
            for flag in static_flags(d):
                r = api.post("/api/v1/challenges/attempt", json={"challenge_id": cid, "submission": flag})
                st = (r.json().get("data") or {}).get("status")
                if st not in ("correct", "already_solved"):
                    problems.append(f"flag {flag!r} not accepted (status={st})")

        if problems:
            failures += 1
            print(f"[FAIL] {rel}")
            for p in problems:
                print(f"    - {p}")
        else:
            print(f"[ OK ] {rel}  ({d['name']})")
            for w in warnings:
                print(f"    ~ {w}")

    print(f"\n{len(targets)} checked, {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
