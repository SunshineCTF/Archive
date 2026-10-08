SunshineCTF Archive
-----

Every [SunshineCTF](https://ctftime.org/ctf/137) from 2017 through 2025 in one place,
with all of the server-based challenges rebuilt to run on modern infrastructure.
SunshineCTF is run by [Hack@UCF](https://hackucf.org), the Collegiate Cyber Defense Club
at the University of Central Florida.

Each year lives in its own public repo, pulled in here as a git submodule:

| Folder | Year | Event | Source repo | Server-based challenges |
|--------|------|-------|-------------|------------------------:|
| [`17`](17) | 2017 | [CTFtime](https://ctftime.org/event/449)  | [SunshineCTF-2017-Public](https://github.com/SunshineCTF/SunshineCTF-2017-Public) | 13 |
| [`18`](18) | 2018 | [CTFtime](https://ctftime.org/event/593)  | [SunshineCTF-2018-Public](https://github.com/SunshineCTF/SunshineCTF-2018-Public) | 12 |
| [`19`](19) | 2019 | [CTFtime](https://ctftime.org/event/767)  | [SunshineCTF-2019-Public](https://github.com/SunshineCTF/SunshineCTF-2019-Public) | 9 |
| [`20`](20) | 2020 | [CTFtime](https://ctftime.org/event/992)  | [SunshineCTF-2020-Public](https://github.com/SunshineCTF/SunshineCTF-2020-Public) | 24 |
| [`21`](21) | 2021 | [CTFtime](https://ctftime.org/event/1441) | [SunshineCTF-2021-Public](https://github.com/SunshineCTF/SunshineCTF-2021-Public) | 8 |
| [`22`](22) | 2022 | [CTFtime](https://ctftime.org/event/1629) | [SunshineCTF-2022-Public](https://github.com/SunshineCTF/SunshineCTF-2022-Public) | 14 |
| [`23`](23) | 2023 | [CTFtime](https://ctftime.org/event/2079) | [SunshineCTF-2023-Public](https://github.com/SunshineCTF/SunshineCTF-2023-Public) | 11 |
| [`24`](24) | 2024 | [CTFtime](https://ctftime.org/event/2485) | [SunshineCTF-2024-Public](https://github.com/SunshineCTF/SunshineCTF-2024-Public) | 22 |
| [`25`](25) | 2025 | [CTFtime](https://ctftime.org/event/2863) | [SunshineCTF-2025-Public](https://github.com/SunshineCTF/SunshineCTF-2025-Public) | 23 |

Challenges are organized as `<year>/<Category>/<ChallengeName>`. A challenge folder
usually holds the player-facing `description.md`, the author's `README.md` with the
intended solution, the source, a solver, and `flag.txt`. Each year's own README covers
anything specific to that year, such as its license.
This repo's own files (docs, tooling, configuration) are released under the
[MIT license](LICENSE).

### Playing the challenges

[`ports.md`](ports.md) lists every server-based challenge with its port and how to
connect to it on `ctf.hackucf.org`:

* Raw TCP challenges: `nc ctf.hackucf.org <port>`
* Web challenges: `https://<slug>.ctf.hackucf.org`

Ports follow a `yycnn` scheme: `yy` is the year, `c` is the category (0 pwn,
1 reversing, 2 scripting, 3 web, 4 crypto, 5 misc, 6 speedrun/i95, 7 Pegasus), and
`nn` numbers the challenges within that category. For example, `23002` is the 2023
pwn challenge `flock`.

Want to run them yourself instead? See below.

### Running the challenges locally

Everything builds and runs with `pwnmake` from
[PwnableHarness](https://github.com/C0deH4cker/PwnableHarness), which needs Docker.

```bash
git clone https://github.com/SunshineCTF/Archive.git
cd Archive
git submodule update --init

pwnmake -j8 docker-start            # build and start every server-based challenge
pwnmake docker-start[23/Pwn/flock]  # or just one
pwnmake -j8 check                   # solve each one against a local container
```

This repo's root is one big PwnableHarness workspace spanning every year, and each
year folder also works on its own. Every challenge also has a ctfcli `challenge.yml`,
so the whole archive can be loaded into a CTFd with `ctf challenge install`. [`HOSTING.md`](HOSTING.md) has the details for
hosting and verifying the archive, including the nginx setup for web challenges.
