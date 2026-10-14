# SunshineCTF Archive — Combined Port Assignments

All hosted challenges from every SunshineCTF year (2017–2025), revived for the
archive at **ctf.hackucf.org**. See each repo's own `ports.md` for details and
the full convention write-up. Raw-TCP challenges are reached with
`nc ctf.hackucf.org <port>`; HTTP(S) challenges live on a
`<slug>.ctf.hackucf.org` subdomain (nginx fragments in each repo's
`nginx/`), still bound to the listed port on the host.

Port convention: `yycnn` — `yy` = year, `c` = category
(0 pwn, 1 reversing, 2 scripting, 3 web, 4 crypto, 5 misc, 6 speedrun/i95, 7 pegasus),
`nn` = index within category. Distinct `yy` per year makes cross-year collisions impossible.

| Year | Challenge | Category | Directory | Host | Port | Connection |
|------|-----------|----------|-----------|------|-----:|------------|
| 2017 | Prepared | Pwn | `Pwn/Prepared` | ctf.hackucf.org | 17001 | `nc ctf.hackucf.org 17001` |
| 2017 | The Memory Remains | Pwn | `Pwn/The-Memory-Remains` | ctf.hackucf.org | 17002 | `nc ctf.hackucf.org 17002` |
| 2017 | Notetorious | Pwn | `Pwn/Notetorious` | ctf.hackucf.org | 17003 | `nc ctf.hackucf.org 17003` |
| 2017 | Alternative Solution | Reversing | `Reversing/Alternative-Solution` | ctf.hackucf.org | 17101 | `nc ctf.hackucf.org 17101` |
| 2017 | Wasteland | Reversing | `Reversing/Wasteland` | ctf.hackucf.org | 17102 | `nc ctf.hackucf.org 17102` |
| 2017 | Fallout Comrade | Scripting | `Scripting/falloutcomrade` | ctf.hackucf.org | 17201 | `nc ctf.hackucf.org 17201` |
| 2017 | Low High | Scripting | `Scripting/lowhigh` | ctf.hackucf.org | 17202 | `nc ctf.hackucf.org 17202` |
| 2017 | Maze Runner | Scripting | `Scripting/mazerunner` | ctf.hackucf.org | 17203 | `nc ctf.hackucf.org 17203` |
| 2017 | Easy1 | Web | `Web/easy1` | easy1.ctf.hackucf.org | 17301 | https://easy1.ctf.hackucf.org |
| 2017 | Easy2 | Web | `Web/easy2` | easy2.ctf.hackucf.org | 17302 | https://easy2.ctf.hackucf.org |
| 2017 | Zombiedex | Web | `Web/zombiedex` | zombiedex.ctf.hackucf.org | 17303 | https://zombiedex.ctf.hackucf.org |
| 2017 | Vanity | Crypto | `Crypto/vanity` | ctf.hackucf.org | 17401 | `nc ctf.hackucf.org 17401` |
| 2017 | The Oracle | Crypto | `Crypto/the_oracle` | ctf.hackucf.org | 17402 | `nc ctf.hackucf.org 17402` |
| 2018 | Hacker Name | Pwn | `Pwn/hacker-name` | ctf.hackucf.org | 18001 | `nc ctf.hackucf.org 18001` |
| 2018 | Log Search | Pwn | `Pwn/Log-Search` | ctf.hackucf.org | 18002 | `nc ctf.hackucf.org 18002` |
| 2018 | Rot13 | Pwn | `Pwn/Rot13` | ctf.hackucf.org | 18003 | `nc ctf.hackucf.org 18003` |
| 2018 | Hexalicious | Pwn | `Pwn/Hexalicious` | ctf.hackucf.org | 18004 | `nc ctf.hackucf.org 18004` |
| 2018 | UAF | Pwn | `Pwn/UAF` | ctf.hackucf.org | 18005 | `nc ctf.hackucf.org 18005` |
| 2018 | Bookwriter | Pwn | `Pwn/BookWriter` | ctf.hackucf.org | 18006 | `nc ctf.hackucf.org 18006` |
| 2018 | Missing Bytes | Scripting | `Scripting/missing-bytes` | ctf.hackucf.org | 18201 | `nc ctf.hackucf.org 18201` |
| 2018 | Workshop Helper | Scripting | `Scripting/WorkshopHelper` | workshophelper.ctf.hackucf.org | 18202 | https://workshophelper.ctf.hackucf.org |
| 2018 | Evaluation | Web | `Web/Evaluation` | evaluation.ctf.hackucf.org | 18301 | https://evaluation.ctf.hackucf.org |
| 2018 | Marceau | Web | `Web/Marceau` | marceau.ctf.hackucf.org | 18302 | https://marceau.ctf.hackucf.org |
| 2018 | SearchBox | Web | `Web/SearchBox` | searchbox.ctf.hackucf.org | 18303 | https://searchbox.ctf.hackucf.org |
| 2018 | Home Sweet Home | Web | `Web/HomeSweetHome` | homesweethome.ctf.hackucf.org | 18304 | https://homesweethome.ctf.hackucf.org |
| 2019 | return-to-mania | Pwn | `Pwn/return-to-mania` | ctf.hackucf.org | 19001 | `nc ctf.hackucf.org 19001` |
| 2019 | CyberRumble | Pwn | `Pwn/CyberRumble` | ctf.hackucf.org | 19002 | `nc ctf.hackucf.org 19002` |
| 2019 | TimeWarp | Scripting | `Scripting/TimeWarp` | ctf.hackucf.org | 19201 | `nc ctf.hackucf.org 19201` |
| 2019 | Entry Exam | Scripting | `Scripting/EntryExam` | entryexam.ctf.hackucf.org | 19202 | https://entryexam.ctf.hackucf.org |
| 2019 | WrestlerBook | Web | `Web/WrestlerBook` | wrestlerbook.ctf.hackucf.org | 19301 | https://wrestlerbook.ctf.hackucf.org |
| 2019 | Wrestler Name Generator | Web | `Web/WrestlerNameGenerator` | wrestlernamegenerator.ctf.hackucf.org | 19302 | https://wrestlernamegenerator.ctf.hackucf.org |
| 2019 | Enter the Polygon | Web | `Web/EnterthePolygon` | enterthepolygon.ctf.hackucf.org | 19303 | https://enterthepolygon.ctf.hackucf.org |
| 2019 | portfolio | Web | `Web/portfolio` | portfolio.ctf.hackucf.org | 19304 | https://portfolio.ctf.hackucf.org |
| 2019 | 16-bit AES | Crypto | `Crypto/16BitAES` | ctf.hackucf.org | 19401 | `nc ctf.hackucf.org 19401` |
| 2020 | OOMG SPACE! 2 | Pwn | `Pwn/OOMG_SPACE2` | ctf.hackucf.org | 20001 | `nc ctf.hackucf.org 20001` |
| 2020 | Florida Forecaster | Pwn | `Pwn/FloridaForecaster` | ctf.hackucf.org | 20002 | `nc ctf.hackucf.org 20002` |
| 2020 | OOMG SPACE! | Pwn | `Pwn/OOMG_SPACE` | ctf.hackucf.org | 20003 | `nc ctf.hackucf.org 20003` |
| 2020 | LilChompy's | Pwn | `Pwn/LilChompys` | ctf.hackucf.org | 20004 | `nc ctf.hackucf.org 20004` |
| 2020 | PasswordPandemonium | Web | `Web/PasswordPandemonium` | passwordpandemonium.ctf.hackucf.org | 20301 | https://passwordpandemonium.ctf.hackucf.org |
| 2020 | TSATechie | Misc | `Misc/TSATechie` | tsatechie.ctf.hackucf.org | 20501 | https://tsatechie.ctf.hackucf.org |
| 2020 | speedrun-00 | Speedrun | `Speedrun/00` | ctf.hackucf.org | 20600 | `nc ctf.hackucf.org 20600` |
| 2020 | speedrun-01 | Speedrun | `Speedrun/01` | ctf.hackucf.org | 20601 | `nc ctf.hackucf.org 20601` |
| 2020 | speedrun-02 | Speedrun | `Speedrun/02` | ctf.hackucf.org | 20602 | `nc ctf.hackucf.org 20602` |
| 2020 | speedrun-03 | Speedrun | `Speedrun/03` | ctf.hackucf.org | 20603 | `nc ctf.hackucf.org 20603` |
| 2020 | speedrun-04 | Speedrun | `Speedrun/04` | ctf.hackucf.org | 20604 | `nc ctf.hackucf.org 20604` |
| 2020 | speedrun-05 | Speedrun | `Speedrun/05` | ctf.hackucf.org | 20605 | `nc ctf.hackucf.org 20605` |
| 2020 | speedrun-06 | Speedrun | `Speedrun/06` | ctf.hackucf.org | 20606 | `nc ctf.hackucf.org 20606` |
| 2020 | speedrun-07 | Speedrun | `Speedrun/07` | ctf.hackucf.org | 20607 | `nc ctf.hackucf.org 20607` |
| 2020 | speedrun-08 | Speedrun | `Speedrun/08` | ctf.hackucf.org | 20608 | `nc ctf.hackucf.org 20608` |
| 2020 | speedrun-09 | Speedrun | `Speedrun/09` | ctf.hackucf.org | 20609 | `nc ctf.hackucf.org 20609` |
| 2020 | speedrun-10 | Speedrun | `Speedrun/10` | ctf.hackucf.org | 20610 | `nc ctf.hackucf.org 20610` |
| 2020 | speedrun-11 | Speedrun | `Speedrun/11` | ctf.hackucf.org | 20611 | `nc ctf.hackucf.org 20611` |
| 2020 | speedrun-12 | Speedrun | `Speedrun/12` | ctf.hackucf.org | 20612 | `nc ctf.hackucf.org 20612` |
| 2020 | speedrun-13 | Speedrun | `Speedrun/13` | ctf.hackucf.org | 20613 | `nc ctf.hackucf.org 20613` |
| 2020 | speedrun-14 | Speedrun | `Speedrun/14` | ctf.hackucf.org | 20614 | `nc ctf.hackucf.org 20614` |
| 2020 | speedrun-15 | Speedrun | `Speedrun/15` | ctf.hackucf.org | 20615 | `nc ctf.hackucf.org 20615` |
| 2020 | speedrun-16 | Speedrun | `Speedrun/16` | ctf.hackucf.org | 20616 | `nc ctf.hackucf.org 20616` |
| 2020 | speedrun-17 | Speedrun | `Speedrun/17` | ctf.hackucf.org | 20617 | `nc ctf.hackucf.org 20617` |
| 2021 | DynamicTypeLibraRII | Pwn | `Pwn/DynamicTypeLibraRII` | ctf.hackucf.org | 21001 | `nc ctf.hackucf.org 21001` |
| 2021 | UselessVM | Reversing | `Reversing/UselessVM` | ctf.hackucf.org | 21101 | `nc ctf.hackucf.org 21101` |
| 2021 | ProcrastinatorProgrammer (part 1) | Scripting | `Scripting/ProcrastinatorProgrammer` | ctf.hackucf.org | 21201 | `nc ctf.hackucf.org 21201` |
| 2021 | ProcrastinatorProgrammer (part 2) | Scripting | `Scripting/ProcrastinatorProgrammer` | ctf.hackucf.org | 21202 | `nc ctf.hackucf.org 21202` |
| 2021 | ProcrastinatorProgrammer (part 3) | Scripting | `Scripting/ProcrastinatorProgrammer` | ctf.hackucf.org | 21203 | `nc ctf.hackucf.org 21203` |
| 2021 | emoji-browser | Web | `Web/emoji-browser` | emoji-browser.ctf.hackucf.org | 21301 | https://emoji-browser.ctf.hackucf.org |
| 2021 | Flag Vault 1 | Web | `Web/flag-vault-1` | flag-vault-1.ctf.hackucf.org | 21302 | https://flag-vault-1.ctf.hackucf.org |
| 2021 | typing | Misc | `Misc/typing` | typing.ctf.hackucf.org | 21501 | https://typing.ctf.hackucf.org |
| 2022 | CTF Simulator | Pwn | `Pwn/CTFSim` | ctf.hackucf.org | 22000 | `nc ctf.hackucf.org 22000` |
| 2022 | ChessFEN | Pwn | `Pwn/ChessFEN` | ctf.hackucf.org | 22001 | `nc ctf.hackucf.org 22001` |
| 2022 | [RII] MagicTheGatheRIIng | Pwn | `Pwn/RII-MagicTheGatheRIIng` | ctf.hackucf.org | 22002 | `nc ctf.hackucf.org 22002` |
| 2022 | [RII] EldenRIIngLite | Pwn | `Pwn/RII-EldenRIIngLite` | ctf.hackucf.org | 22003 | `nc ctf.hackucf.org 22003` |
| 2022 | Predictor Programmer 1 | Scripting | `Scripting/PredictorProgrammer1` | ctf.hackucf.org | 22201 | `nc ctf.hackucf.org 22201` |
| 2022 | Predictor Programmer 2 | Scripting | `Scripting/PredictorProgrammer2` | ctf.hackucf.org | 22202 | `nc ctf.hackucf.org 22202` |
| 2022 | Predictor Programmer 3 | Scripting | `Scripting/PredictorProgrammer3` | ctf.hackucf.org | 22203 | `nc ctf.hackucf.org 22203` |
| 2022 | Inspect Element | Web | `Web/inspect-element` | inspect-element.ctf.hackucf.org | 22300 | https://inspect-element.ctf.hackucf.org |
| 2022 | Network Pong | Web | `Web/network-pong` | network-pong.ctf.hackucf.org | 22301 | https://network-pong.ctf.hackucf.org |
| 2022 | Timely | Web | `Web/timely` | timely.ctf.hackucf.org | 22302 | https://timely.ctf.hackucf.org |
| 2022 | PEG_DEBUG | Pegasus |  | ctf.hackucf.org | 22700-22702 | managed separately |
| 2022 | PEG_AUTOREV | Pegasus |  | ctf.hackucf.org | 22703 | managed separately |
| 2022 | PEG_CHEAT | Pegasus |  | ctf.hackucf.org | 22704 | managed separately |
| 2022 | PEG_AUTOREV 2 | Pegasus |  | ctf.hackucf.org | 22705 | managed separately |
| 2023 | Robot Assembly Line | Pwn | `Pwn/RobotAssemblyLine` | ctf.hackucf.org | 23000 | `nc ctf.hackucf.org 23000` |
| 2023 | House of Sus | Pwn | `Pwn/House_of_Sus` | ctf.hackucf.org | 23001 | `nc ctf.hackucf.org 23001` |
| 2023 | flock | Pwn | `Pwn/flock` | ctf.hackucf.org | 23002 | `nc ctf.hackucf.org 23002` |
| 2023 | Array of Sunshine | Pwn | `Pwn/array_of_sunshine` | ctf.hackucf.org | 23003 | `nc ctf.hackucf.org 23003` |
| 2023 | Bugspray | Pwn | `Pwn/bugspray` | ctf.hackucf.org | 23004 | `nc ctf.hackucf.org 23004` |
| 2023 | DDR | Scripting | `Scripting/ddr` | ctf.hackucf.org | 23200 | `nc ctf.hackucf.org 23200` |
| 2023 | Simon Programmer 1 | Scripting | `Scripting/SimonProgrammer1` | simon-programmer-1.ctf.hackucf.org | 23201 | https://simon-programmer-1.ctf.hackucf.org |
| 2023 | Simon Programmer 2 | Scripting | `Scripting/SimonProgrammer2` | simon-programmer-2.ctf.hackucf.org | 23202 | https://simon-programmer-2.ctf.hackucf.org |
| 2023 | Simon Programmer 3 | Scripting | `Scripting/SimonProgrammer3` | simon-programmer-3.ctf.hackucf.org | 23203 | https://simon-programmer-3.ctf.hackucf.org |
| 2023 | BeepBoop Blog | Web | `Web/beepboop_blog` | beepboop-blog.ctf.hackucf.org | 23300 | https://beepboop-blog.ctf.hackucf.org |
| 2023 | Hotdog Stand | Web | `Web/hotdog_stand` | hotdog-stand.ctf.hackucf.org | 23301 | https://hotdog-stand.ctf.hackucf.org |
| 2024 | FlagShop | Pwn | `Pwn/FlagShop` | ctf.hackucf.org | 24001 | `nc ctf.hackucf.org 24001` |
| 2024 | Secure Flag Terminal | Pwn | `Pwn/Secure_Flag_Terminal` | ctf.hackucf.org | 24002 | `nc ctf.hackucf.org 24002` |
| 2024 | Adventure on the High C | Pwn | `Pwn/adventure-on-the-high-c` | ctf.hackucf.org | 24003 | `nc ctf.hackucf.org 24003` |
| 2024 | Drone Adventure | Pwn | `Pwn/drone-adventure` | ctf.hackucf.org | 24004 | `nc ctf.hackucf.org 24004` |
| 2024 | Welcome to the Jungle | Pwn | `Pwn/jungle-adventure` | ctf.hackucf.org | 24005 | `nc ctf.hackucf.org 24005` |
| 2024 | Heap 1 | Pwn | `Pwn/heap-01` | ctf.hackucf.org | 24006 | `nc ctf.hackucf.org 24006` |
| 2024 | Dungeon Keymaster | Reversing | `Reversing/dungeon-keymaster` | dungeon-keymaster.ctf.hackucf.org | 24101 | https://dungeon-keymaster.ctf.hackucf.org |
| 2024 | BotNet (flag 1) | Web | `Web/botnet_1` | botnet.ctf.hackucf.org | 24301 | https://botnet.ctf.hackucf.org |
| 2024 | BotNet (flag 2) | Web | `Web/botnet_2` | botnet.ctf.hackucf.org | 24301 | https://botnet.ctf.hackucf.org |
| 2024 | File Islands | Web | `Web/File_Islands_1` | file-islands.ctf.hackucf.org | 24303 | https://file-islands.ctf.hackucf.org |
| 2024 | Puzzling | Web | `Web/Puzzling` | puzzling.ctf.hackucf.org | 24304 | https://puzzling.ctf.hackucf.org |
| 2024 | Doubly Secure | Crypto | `Crypto/doubly-secure` | doubly-secure.ctf.hackucf.org | 24401 | https://doubly-secure.ctf.hackucf.org |
| 2024 | Mariner | Misc | `Misc/mariner` | ctf.hackucf.org | 24501 | `https://ctf.hackucf.org:24501` (Kubernetes API) |
| 2024 | Melbourne | i95 | `i95/i95-melbourne` | ctf.hackucf.org | 24601 | `nc ctf.hackucf.org 24601` |
| 2024 | Canaveral | i95 | `i95/i95-canaveral` | ctf.hackucf.org | 24602 | `nc ctf.hackucf.org 24602` |
| 2024 | Palm Beach | i95 | `i95/i95-palmbeach` | ctf.hackucf.org | 24603 | `nc ctf.hackucf.org 24603` |
| 2024 | Daytona Beach | i95 | `i95/i95-daytonabeach` | ctf.hackucf.org | 24605 | `nc ctf.hackucf.org 24605` |
| 2024 | Fort Pierce | i95 | `i95/i95-fortpierce` | ctf.hackucf.org | 24606 | `nc ctf.hackucf.org 24606` |
| 2024 | Titusville | i95 | `i95/i95-titusville` | ctf.hackucf.org | 24607 | `nc ctf.hackucf.org 24607` |
| 2024 | Jacksonville | i95 | `i95/i95-jacksonville` | ctf.hackucf.org | 24608 | `nc ctf.hackucf.org 24608` |
| 2024 | Jupiter | i95 | `i95/i95-jupiter` | ctf.hackucf.org | 24609 | `nc ctf.hackucf.org 24609` |
| 2024 | Boca Raton | i95 | `i95/i95-bocaraton` | ctf.hackucf.org | 24610 | `nc ctf.hackucf.org 24610` |
| 2025 | Clone Army | Pwn | `Pwn/CloneArmy` | ctf.hackucf.org | 25001 | `nc ctf.hackucf.org 25001` |
| 2025 | SpaceIsMyBanner | Pwn | `Pwn/SpaceIsMyBanner` | ctf.hackucf.org | 25002 | `nc ctf.hackucf.org 25002` |
| 2025 | SpaceIsLessThanIdeal | Pwn | `Pwn/SpaceIsLessThanIdeal` | ctf.hackucf.org | 25003 | `nc ctf.hackucf.org 25003` |
| 2025 | HeapX | Pwn | `Pwn/HeapX` | ctf.hackucf.org | 25004 | `nc ctf.hackucf.org 25004` |
| 2025 | HAL9000 | Pwn | `Pwn/HAL9000` | ctf.hackucf.org | 25005 | `nc ctf.hackucf.org 25005` |
| 2025 | AstroJIT AI | Pwn | `Pwn/AstroJitAi` | ctf.hackucf.org | 25006 | `nc ctf.hackucf.org 25006` |
| 2025 | Numbers Game | Reversing | `Reversing/NumbersGame` | ctf.hackucf.org | 25101 | `nc ctf.hackucf.org 25101` |
| 2025 | Space Race | Reversing | `RE/SpaceRace` | ctf.hackucf.org | 25102 | `nc ctf.hackucf.org 25102` |
| 2025 | Hail Mary | Scripting | `Scripting/HailMary` | ctf.hackucf.org | 25201 | `nc ctf.hackucf.org 25201` |
| 2025 | Web Forge | Web | `Web/WebForge` | webforge.ctf.hackucf.org | 25303 | https://webforge.ctf.hackucf.org |
| 2025 | Intergalactic Webhook Service | Web | `Web/Intergalactic_Webhook_Service` | webhook.ctf.hackucf.org | 25304 | https://webhook.ctf.hackucf.org |
| 2025 | Lunar Auth | Web | `Web/Lunar_Auth` | lunarauth.ctf.hackucf.org | 25305 | https://lunarauth.ctf.hackucf.org |
| 2025 | Lunar Shop | Web | `Web/Lunar_Shop` | lunarshop.ctf.hackucf.org | 25306 | https://lunarshop.ctf.hackucf.org |
| 2025 | Lunar File Invasion | Web | `Web/Lunar_File_Invasion` | lunarfileinvasion.ctf.hackucf.org | 25307 | https://lunarfileinvasion.ctf.hackucf.org |
| 2025 | BitsOfSpace | Crypto | `Crypto/BitsOfSpace` | ctf.hackucf.org | 25401 | `nc ctf.hackucf.org 25401` |
| 2025 | MoonClicker | Crypto | `Crypto/MoonClicker` | moonclicker.ctf.hackucf.org | 25402 | https://moonclicker.ctf.hackucf.org |
| 2025 | Plutonian | Crypto | `Crypto/Plutonian` | ctf.hackucf.org | 25403 | `nc ctf.hackucf.org 25403` |
| 2025 | Miami | i95 | `i95/Miami` | ctf.hackucf.org | 25601 | `nc ctf.hackucf.org 25601` |
| 2025 | Jacksonville | i95 | `i95/Jacksonville` | ctf.hackucf.org | 25602 | `nc ctf.hackucf.org 25602` |
| 2025 | Canaveral | i95 | `i95/Canaveral` | ctf.hackucf.org | 25603 | `nc ctf.hackucf.org 25603` |
| 2025 | Daytona | i95 | `i95/Daytona` | ctf.hackucf.org | 25606 | `nc ctf.hackucf.org 25606` |
| 2025 | Jupiter | i95 | `i95/Jupiter` | ctf.hackucf.org | 25607 | `nc ctf.hackucf.org 25607` |
| 2025 | Login Screen | Pegasus | `Pegasus/challenges/LoginScreen` | ctf.hackucf.org | 25701 | `nc ctf.hackucf.org 25701` |

_Total: 136 hosted challenge entries._

Pegasus challenges (category 7, ports `yy7nn`) are managed separately by the
organizers and are not included here except where a year's own `ports.md` lists them.
