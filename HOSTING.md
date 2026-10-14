# SunshineCTF archive — hosting & verifying

Everything is driven by `pwnmake`. This repo's root is a single PwnableHarness
workspace (see `.pwnmake` / `Config.mk`), and each year repo (`17`..`25`, each a
`SunshineCTF-<year>-Public` submodule) also works standalone. There is no separate deploy
script — PwnableHarness builds, hosts, and verifies every challenge (PwnableHarness
*and* docker-compose), because the pwnmake builder image carries a `docker compose`
plugin (installed by the top-level `prebuild.sh`).

All commands below run from the root of this repo unless they `cd` into a year.

## Get the code

```bash
git clone https://github.com/SunshineCTF/Archive.git
cd Archive
git submodule update --init   # the year repos (not recursive: their Pegasus submodules aren't needed here)
```

Install `pwnmake` by following the instructions at https://github.com/C0deH4cker/PwnableHarness.

## Host the challenges (leave them running, for players)

```bash
pwnmake -j8 docker-start      # build + start EVERY year's challenges (PH + compose)
pwnmake docker-stop           # stop them all
```

Scope it as needed:

```bash
pwnmake docker-start[23/Pwn/flock]          # just one challenge
pwnmake docker-start[23/Web/hotdog_stand]   # a compose challenge
cd 23 && pwnmake -j8 docker-start           # just one year (paths are then relative to 23/)
```

Every hosted container has CPU, memory and process limits. PwnableHarness
challenges get 0.5 CPU, 500 MB and 512 processes (the process cap is set in each
year's `Config.mk`). Each docker-compose service sets `mem_limit`, `cpus` and
`pids_limit` (or the `deploy.resources.limits` equivalents); keep that true when
adding a service.

TCP challenges publish `0.0.0.0:<port>`; web/compose challenges publish
`127.0.0.1:<port>` and are fronted by nginx, routed by `Host`. Each web
challenge's route is declared in its `Build.mk` (`ctf_check_web` registers it
from its host + port; a challenge without a check calls
`$(call nginx_service,<host>,<port>)` directly), and `pwnmake publish` writes
one `publish/nginx/<host>.http` line per host (`<host> <port>;`) for the
proxy's `Host` → port map. Collect `publish/nginx/*.http` (and any `*.xff`)
into the reverse proxy's include directory; there are no hand-kept nginx
fragments in the year repos. Ports follow the `yycnn` convention; the combined
list is in `ports.md`.

> Hosting ALL compose challenges at once creates ~40 docker networks, which exceeds
> docker's default address pool. On the archive server, widen it in
> `/etc/docker/daemon.json`, e.g.
> `{"default-address-pools":[{"base":"10.200.0.0/16","size":24}]}`.

## Verify the challenges (ephemeral — build, start, solve, tear down)

```bash
pwnmake -j8 check             # run every quick solver, assert each prints its flag
pwnmake -j8 check-full        # include the slow solvers (padding oracles, brute force, ...)
pwnmake check[23/Pwn/flock]   # one challenge
pwnmake check REMOTE=1        # solve against the live ctf.hackucf.org instead of locally
```

Each `check` brings its own challenge up (PwnableHarness via `docker run`,
docker-compose via `docker compose up`), waits for it to answer, runs the solver, and
tears it down — so checks are self-contained and don't disturb anything you're hosting
with `docker-start` (though running a check for a challenge you're currently hosting
will stop that instance, since it tears down what it started).

Slow solvers are registered under `check-full` only; `check` stays quick. A solver reads
its challenge's build output and published files through the `.build/` and `publish/`
symlinks that the check creates in the challenge directory (both gitignored).

If a challenge answers with `fakeflag{now_try_on_the_real_challenge_server}`,
its flag volume (`<image>-workdir`) was deleted after PwnableHarness filled it:
the `.build/.../.docker_workdir_volume_marker` file still says it's ready, so
Docker creates an empty volume and fills it from the image, whose `flag.txt` is
the fake one. Delete the marker (or all of them) and start the challenge again.
Docker image, container and volume names are per challenge, so they're shared
by every checkout on the host (a year folder, the archive root, or a parent
workspace).

## Upload the challenges to CTFd (ctfcli)

Every challenge has a `challenge.yml` (folders that hold several challenges have
one `challenge-<part>.yml` per part), and `.ctf/config` lists them all, at the
root for the whole archive and in each year folder for that year alone.

Most handouts aren't uploaded to CTFd. Each challenge's `Build.mk` publishes
them (`PUBLISH` for files in git, `PUBLISH_BUILD` for build outputs), and its
description ends with a link to each one:

```yaml
description: |-
  ...
  * [rot13](/files/sun/18/Pwn/Rot13/rot13)
```

The site's web server serves `/files/sun/<year>/<challenge folder>/<file>` from
the published files, and the archive's CTFd theme shows the links as file
attachments. Only the handful of challenges that already had files uploaded to
ctf.hackucf.org's CTFd keep them under `files:`. Three handouts aren't in git at
all (Old Favorites 1 and 2, Phishy Phishy): they have to be copied onto the web
server by hand.

For the web server, run `pwnmake publish` from the top of the site's checkout
of all the challenge repos, so the paths match the `/files/` URLs. The validator
below checks the links against each year's own published files instead, so
publish those **from inside each year folder** (a root-level `pwnmake publish`
writes to a different place):

```bash
for y in 17 18 19 20 21 22 23 24 25; do (cd $y && pwnmake -j8 publish); done
```

Then point ctfcli at the CTFd (an admin access token) and install:

```bash
uv tool install ctfcli        # or: pipx install ctfcli
export CTFCLI_URL=https://ctf.example.org CTFCLI_ACCESS_TOKEN=ctfd_...
ctf challenge install         # everything (run inside a year folder for one year)
ctf challenge sync            # push later edits to challenges that already exist
ctf challenge verify --ignore='("extra","logic")'   # compare CTFd with the ymls
```

`install` skips challenges that already exist (it reports them as failures), so
run `sync` after it to update those. `sync` also sets each challenge's `next:`
link, which can name a challenge from another repo. `verify` needs the ignore
list because it otherwise reports every standard challenge as out of sync.

Keep the URL and token in the environment; don't write them into `.ctf/config`.
Each challenge is tagged with its event, `sunshinectf-<year>`, and every challenge has a static point value (at most 500) and exactly one
difficulty tag: `beginner` (up to 100 points), `intermediate` (125-250) or
`expert` (275-500). Challenges that were already on ctf.hackucf.org before this
archive keep their point values from there; the rest were calibrated against
them, starting from the original SunshineCTF points where those are known. ctfcli matches challenges by name, so names are unique across all years (the
i95 cities used in both 2024 and 2025 carry the year, e.g. `Canaveral (2024)`).
Pegasus challenges aren't included; they live in the separate PEGASUS repo.

To test against a throwaway local CTFd:

```bash
docker run -d --name ctfd-test -p 127.0.0.1:8000:8000 ctfd/ctfd
# finish setup at http://127.0.0.1:8000, then Settings > Access Tokens
export CTFCLI_URL=http://127.0.0.1:8000 CTFCLI_ACCESS_TOKEN=ctfd_...
~/.local/share/uv/tools/ctfcli/bin/python tools/ctfd_validate.py   # all years, or a path
tools/ctfd_wipe.sh                                                 # delete every challenge
```

The validator installs or syncs each challenge, checks it with `ctf challenge
verify`, submits every flag, and fails if a handout contains its challenge's
exact flag (except for challenges where that's the point, listed in the script).
It also checks that each description's handout link names a file that
`pwnmake publish` published.
