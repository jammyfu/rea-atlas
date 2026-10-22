[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# REA Atlas：逆向工程專案地圖（含 rea 標記）

開源逆向工程專案地圖：遊戲反編譯、靜態重編譯、重新實作、資源擷取工具、通用逆向工具，以及應用程式/協定/韌體逆向。每條標註是否使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）：**Uses rea: Yes / No / Unverified**，僅有公開證據（README、官方 showcase 或倉庫文件）才標 Yes。

> 非官方，與 morluto/rea 無關聯。不收錄、不託管破解、盜版、ROM 或版權素材。為維持各語言清單一致，條目簡介統一保留英文。

<img src="https://raw.githubusercontent.com/morluto/rea/main/docs/assets/rea-showcases.png" alt="REA showcases" width="720" />

<sub>圖片：REA showcase 插圖，來自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未轉存。</sub>

## REA 官方 Showcase

- [DX-Ball: sound-pan function](https://rea.tools/showcase/dx-ball/) — **Uses rea: Yes**. Official showcase; C reconstruction matching 3,205 x86 cases.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="DX-Ball: sound-pan function"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/dx-ball/), not a screenshot</sub>
- [Notion: Electron clipboard bridge](https://rea.tools/showcase/notion/) — **Uses rea: Yes**. Official showcase; renderer → preload → IPC trace.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="Notion: Electron clipboard bridge"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/notion/), not a screenshot</sub>
- [TH04: PC-98 bullet-ring maths](https://rea.tools/showcase/th04/) — **Uses rea: Yes**. Official showcase; 16-bit angle helpers.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="TH04: PC-98 bullet-ring maths"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/th04/), not a screenshot</sub>
- [Aegis: TOTP code generation](https://rea.tools/showcase/aegis/) — **Uses rea: Yes**. Official showcase; Android app.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="Aegis: TOTP code generation"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/aegis/), not a screenshot</sub>
- [CTF: flag checker](https://rea.tools/showcase/ctf/) — **Uses rea: Yes**. Official showcase; DownUnderCTF 2023 challenge.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="CTF: flag checker"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/ctf/), not a screenshot</sub>

## 遊戲

### NES / FC

#### 反編譯 / 重編譯

- [aldonunez/zelda1-disassembly](https://github.com/aldonunez/zelda1-disassembly) — **Uses rea: No**. The Legend of Zelda (NES) disassembly.<br><img src="https://opengraph.githubassets.com/1/aldonunez/zelda1-disassembly" width="240" alt="aldonunez/zelda1-disassembly"><br><sub>GitHub repo card for [aldonunez/zelda1-disassembly](https://github.com/aldonunez/zelda1-disassembly), not a screenshot</sub>

#### 資源擷取與工具

- [SourMesen/Mesen2](https://github.com/SourMesen/Mesen2) — **Uses rea: No**. Multi-system emulator with strong debugging tools (NES/SNES/GB/GBA/PCE) (archived). GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/SourMesen/Mesen2" width="240" alt="SourMesen/Mesen2"><br><sub>GitHub repo card for [SourMesen/Mesen2](https://github.com/SourMesen/Mesen2), not a screenshot</sub>

### SFC / SNES

#### 反編譯 / 重編譯

- [snesrev/zelda3](https://github.com/snesrev/zelda3) — **Uses rea: No**. A Link to the Past C reimplementation; asset extraction from your own ROM.<br><img src="https://opengraph.githubassets.com/1/snesrev/zelda3" width="240" alt="snesrev/zelda3"><br><sub>GitHub repo card for [snesrev/zelda3](https://github.com/snesrev/zelda3), not a screenshot</sub>
- [snesrev/sm](https://github.com/snesrev/sm) — **Uses rea: No**. Super Metroid C reimplementation; needs your own ROM.<br><img src="https://opengraph.githubassets.com/1/snesrev/sm" width="240" alt="snesrev/sm"><br><sub>GitHub repo card for [snesrev/sm](https://github.com/snesrev/sm), not a screenshot</sub>

#### 重製 / 移植

- [snesrev/smw](https://github.com/snesrev/smw) — **Uses rea: No**. Super Mario World C reimplementation; needs your own ROM.<br><img src="https://opengraph.githubassets.com/1/snesrev/smw" width="240" alt="snesrev/smw"><br><sub>GitHub repo card for [snesrev/smw](https://github.com/snesrev/smw), not a screenshot</sub>

### MD / Genesis

#### 反編譯 / 重編譯

- [sonicretro/s1disasm](https://github.com/sonicretro/s1disasm) — **Uses rea: No**. Sonic the Hedgehog (Mega Drive) disassembly.<br><img src="https://opengraph.githubassets.com/1/sonicretro/s1disasm" width="240" alt="sonicretro/s1disasm"><br><sub>GitHub repo card for [sonicretro/s1disasm](https://github.com/sonicretro/s1disasm), not a screenshot</sub>
- [sonicretro/s2disasm](https://github.com/sonicretro/s2disasm) — **Uses rea: No**. Sonic 2 (Mega Drive) disassembly.<br><img src="https://opengraph.githubassets.com/1/sonicretro/s2disasm" width="240" alt="sonicretro/s2disasm"><br><sub>GitHub repo card for [sonicretro/s2disasm](https://github.com/sonicretro/s2disasm), not a screenshot</sub>
- [sonicretro/skdisasm](https://github.com/sonicretro/skdisasm) — **Uses rea: No**. Sonic 3 & Knuckles disassembly.<br><img src="https://opengraph.githubassets.com/1/sonicretro/skdisasm" width="240" alt="sonicretro/skdisasm"><br><sub>GitHub repo card for [sonicretro/skdisasm](https://github.com/sonicretro/skdisasm), not a screenshot</sub>

#### 重製 / 移植

- [RSDKModding/RSDKv5-Decompilation](https://github.com/RSDKModding/RSDKv5-Decompilation) — **Uses rea: No**. Retro Engine v5 decompilation (Sonic Mania); needs your own data files.<br><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv5-Decompilation/master/header.png?raw=true" width="240" alt="RSDKModding/RSDKv5-Decompilation"><br><sub>Image: RSDKModding/RSDKv5-Decompilation ([source](https://github.com/RSDKModding/RSDKv5-Decompilation))</sub>
- [RSDKModding/RSDKv4-Decompilation](https://github.com/RSDKModding/RSDKv4-Decompilation) — **Uses rea: No**. Retro Engine v4 decompilation (Sonic 1/2 mobile remasters).<br><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv4-Decompilation/main/header.png?raw=true" width="240" alt="RSDKModding/RSDKv4-Decompilation"><br><sub>Image: RSDKModding/RSDKv4-Decompilation ([source](https://github.com/RSDKModding/RSDKv4-Decompilation))</sub>

### 世嘉土星

#### 反編譯 / 重編譯

- [yaz0r/Azel](https://github.com/yaz0r/Azel) — **Uses rea: No**. Panzer Dragoon Saga reimplementation. MIT.<br><img src="https://github.com/user-attachments/assets/71f6a246-24cc-4d64-9673-53b9e4c3e4df" width="240" alt="yaz0r/Azel"><br><sub>Image: yaz0r/Azel ([source](https://github.com/yaz0r/Azel))</sub>

### Game Boy

#### 反編譯 / 重編譯

- [pret/pokered](https://github.com/pret/pokered) — **Uses rea: No**. Pokémon Red/Blue disassembly.<br><img src="https://opengraph.githubassets.com/1/pret/pokered" width="240" alt="pret/pokered"><br><sub>GitHub repo card for [pret/pokered](https://github.com/pret/pokered), not a screenshot</sub>
- [pret/pokegold](https://github.com/pret/pokegold) — **Uses rea: No**. Pokémon Gold/Silver disassembly.<br><img src="https://opengraph.githubassets.com/1/pret/pokegold" width="240" alt="pret/pokegold"><br><sub>GitHub repo card for [pret/pokegold](https://github.com/pret/pokegold), not a screenshot</sub>
- [pret/pokeyellow](https://github.com/pret/pokeyellow) — **Uses rea: No**. Pokémon Yellow disassembly.<br><img src="https://opengraph.githubassets.com/1/pret/pokeyellow" width="240" alt="pret/pokeyellow"><br><sub>GitHub repo card for [pret/pokeyellow](https://github.com/pret/pokeyellow), not a screenshot</sub>
- [pret/pokecrystal](https://github.com/pret/pokecrystal) — **Uses rea: No**. Pokémon Crystal disassembly.<br><img src="https://opengraph.githubassets.com/1/pret/pokecrystal" width="240" alt="pret/pokecrystal"><br><sub>GitHub repo card for [pret/pokecrystal](https://github.com/pret/pokecrystal), not a screenshot</sub>
- [zladx/LADX-Disassembly](https://github.com/zladx/LADX-Disassembly) — **Uses rea: No**. Link's Awakening DX disassembly.<br><img src="https://opengraph.githubassets.com/1/zladx/LADX-Disassembly" width="240" alt="zladx/LADX-Disassembly"><br><sub>GitHub repo card for [zladx/LADX-Disassembly](https://github.com/zladx/LADX-Disassembly), not a screenshot</sub>

### GBA

#### 反編譯 / 重編譯

- [pret/pokeemerald](https://github.com/pret/pokeemerald) — **Uses rea: No**. Pokémon Emerald decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokeemerald" width="240" alt="pret/pokeemerald"><br><sub>GitHub repo card for [pret/pokeemerald](https://github.com/pret/pokeemerald), not a screenshot</sub>
- [pret/pokefirered](https://github.com/pret/pokefirered) — **Uses rea: No**. Pokémon FireRed/LeafGreen decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokefirered" width="240" alt="pret/pokefirered"><br><sub>GitHub repo card for [pret/pokefirered](https://github.com/pret/pokefirered), not a screenshot</sub>
- [zeldaret/tmc](https://github.com/zeldaret/tmc) — **Uses rea: No**. The Minish Cap decompilation.<br><img src="https://opengraph.githubassets.com/1/zeldaret/tmc" width="240" alt="zeldaret/tmc"><br><sub>GitHub repo card for [zeldaret/tmc](https://github.com/zeldaret/tmc), not a screenshot</sub>
- [pret/pokeruby](https://github.com/pret/pokeruby) — **Uses rea: No**. Pokémon Ruby/Sapphire decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokeruby" width="240" alt="pret/pokeruby"><br><sub>GitHub repo card for [pret/pokeruby](https://github.com/pret/pokeruby), not a screenshot</sub>
- [jiangzhengwenjz/katam](https://github.com/jiangzhengwenjz/katam) — **Uses rea: No**. Kirby & the Amazing Mirror decompilation.<br><img src="https://opengraph.githubassets.com/1/jiangzhengwenjz/katam" width="240" alt="jiangzhengwenjz/katam"><br><sub>GitHub repo card for [jiangzhengwenjz/katam](https://github.com/jiangzhengwenjz/katam), not a screenshot</sub>
- [pret/pmd-red](https://github.com/pret/pmd-red) — **Uses rea: No**. Pokémon Mystery Dungeon: Red Rescue Team decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pmd-red" width="240" alt="pret/pmd-red"><br><sub>GitHub repo card for [pret/pmd-red](https://github.com/pret/pmd-red), not a screenshot</sub>

### 任天堂 64

#### 反編譯 / 重編譯

- [zeldaret/oot](https://github.com/zeldaret/oot) — **Uses rea: No**. Ocarina of Time decompilation; ROM not included.<br><img src="https://opengraph.githubassets.com/1/zeldaret/oot" width="240" alt="zeldaret/oot"><br><sub>GitHub repo card for [zeldaret/oot](https://github.com/zeldaret/oot), not a screenshot</sub>
- [n64decomp/sm64](https://github.com/n64decomp/sm64) — **Uses rea: No**. Super Mario 64 decompilation; ROM not included. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/n64decomp/sm64" width="240" alt="n64decomp/sm64"><br><sub>GitHub repo card for [n64decomp/sm64](https://github.com/n64decomp/sm64), not a screenshot</sub>
- [HarbourMasters/Starship](https://github.com/HarbourMasters/Starship) — **Uses rea: No**. Star Fox 64 PC port based on the sf64 decomp. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/HarbourMasters/Starship" width="240" alt="HarbourMasters/Starship"><br><sub>GitHub repo card for [HarbourMasters/Starship](https://github.com/HarbourMasters/Starship), not a screenshot</sub>
- [n64decomp/mk64](https://github.com/n64decomp/mk64) — **Uses rea: No**. Mario Kart 64 decompilation.<br><img src="https://opengraph.githubassets.com/1/n64decomp/mk64" width="240" alt="n64decomp/mk64"><br><sub>GitHub repo card for [n64decomp/mk64](https://github.com/n64decomp/mk64), not a screenshot</sub>
- [zeldaret/mm](https://github.com/zeldaret/mm) — **Uses rea: No**. Majora's Mask decompilation.<br><img src="https://opengraph.githubassets.com/1/zeldaret/mm" width="240" alt="zeldaret/mm"><br><sub>GitHub repo card for [zeldaret/mm](https://github.com/zeldaret/mm), not a screenshot</sub>
- [pmret/papermario](https://github.com/pmret/papermario) — **Uses rea: No**. Paper Mario decompilation.<br><img src="https://opengraph.githubassets.com/1/pmret/papermario" width="240" alt="pmret/papermario"><br><sub>GitHub repo card for [pmret/papermario](https://github.com/pmret/papermario), not a screenshot</sub>
- [N64Recomp/N64Recomp](https://github.com/N64Recomp/N64Recomp) — **Uses rea: No**. Static recompiler from N64 binaries to C. MIT.<br><img src="https://opengraph.githubassets.com/1/N64Recomp/N64Recomp" width="240" alt="N64Recomp/N64Recomp"><br><sub>GitHub repo card for [N64Recomp/N64Recomp](https://github.com/N64Recomp/N64Recomp), not a screenshot</sub>
- [n64decomp/perfect_dark](https://github.com/n64decomp/perfect_dark) — **Uses rea: No**. Perfect Dark decompilation. MIT.<br><img src="https://opengraph.githubassets.com/1/n64decomp/perfect_dark" width="240" alt="n64decomp/perfect_dark"><br><sub>GitHub repo card for [n64decomp/perfect_dark](https://github.com/n64decomp/perfect_dark), not a screenshot</sub>

#### 重製 / 移植

- [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) — **Uses rea: No**. Ship of Harkinian PC port of OoT; requires your own ROM.<br><img src="https://opengraph.githubassets.com/1/HarbourMasters/Shipwright" width="240" alt="HarbourMasters/Shipwright"><br><sub>GitHub repo card for [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright), not a screenshot</sub>
- [Zelda64Recomp/Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) — **Uses rea: No**. Majora's Mask static recompilation PC port; needs your own ROM. GPL-3.0.<br><img src="https://raw.githubusercontent.com/Zelda64Recomp/Zelda64Recomp/dev/docs/deck_gyro_1.jpg" width="240" alt="Zelda64Recomp/Zelda64Recomp"><br><sub>Image: Zelda64Recomp/Zelda64Recomp ([source](https://github.com/Zelda64Recomp/Zelda64Recomp))</sub>
- [2ship2harkinian/2ship2harkinian](https://github.com/2ship2harkinian/2ship2harkinian) — **Uses rea: No**. Majora's Mask PC port. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/2ship2harkinian/2ship2harkinian" width="240" alt="2ship2harkinian/2ship2harkinian"><br><sub>GitHub repo card for [2ship2harkinian/2ship2harkinian](https://github.com/2ship2harkinian/2ship2harkinian), not a screenshot</sub>

#### 資源擷取與工具

- [ethteck/splat](https://github.com/ethteck/splat) — **Uses rea: No**. Binary splitting tool for N64/PSX decomp projects. MIT.<br><img src="https://opengraph.githubassets.com/1/ethteck/splat" width="240" alt="ethteck/splat"><br><sub>GitHub repo card for [ethteck/splat](https://github.com/ethteck/splat), not a screenshot</sub>
- [NEstelami/ZAPD](https://github.com/NEstelami/ZAPD) — **Uses rea: No**. Zelda asset processor used by decomp projects. MIT.<br><img src="https://raw.githubusercontent.com/NEstelami/ZAPD/master/docs/zapd_warning_example.png?raw=true" width="240" alt="NEstelami/ZAPD"><br><sub>Image: NEstelami/ZAPD ([source](https://github.com/NEstelami/ZAPD))</sub>

### GameCube

#### 反編譯 / 重編譯

- [zeldaret/tww](https://github.com/zeldaret/tww) — **Uses rea: No**. The Wind Waker decompilation. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/zeldaret/tww" width="240" alt="zeldaret/tww"><br><sub>GitHub repo card for [zeldaret/tww](https://github.com/zeldaret/tww), not a screenshot</sub>
- [doldecomp/sms](https://github.com/doldecomp/sms) — **Uses rea: No**. Super Mario Sunshine decompilation. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/doldecomp/sms" width="240" alt="doldecomp/sms"><br><sub>GitHub repo card for [doldecomp/sms](https://github.com/doldecomp/sms), not a screenshot</sub>
- [doldecomp/melee](https://github.com/doldecomp/melee) — **Uses rea: No**. Super Smash Bros. Melee decompilation.<br><img src="https://opengraph.githubassets.com/1/doldecomp/melee" width="240" alt="doldecomp/melee"><br><sub>GitHub repo card for [doldecomp/melee](https://github.com/doldecomp/melee), not a screenshot</sub>
- [zeldaret/tp](https://github.com/zeldaret/tp) — **Uses rea: No**. Twilight Princess decompilation. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/zeldaret/tp" width="240" alt="zeldaret/tp"><br><sub>GitHub repo card for [zeldaret/tp](https://github.com/zeldaret/tp), not a screenshot</sub>
- [projectPiki/pikmin2](https://github.com/projectPiki/pikmin2) — **Uses rea: No**. Pikmin 2 decompilation. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/projectPiki/pikmin2" width="240" alt="projectPiki/pikmin2"><br><sub>GitHub repo card for [projectPiki/pikmin2](https://github.com/projectPiki/pikmin2), not a screenshot</sub>

#### 資源擷取與工具

- [encounter/decomp-toolkit](https://github.com/encounter/decomp-toolkit) — **Uses rea: No**. Toolkit for GameCube/Wii decompilation. Apache-2.0.<br><img src="https://opengraph.githubassets.com/1/encounter/decomp-toolkit" width="240" alt="encounter/decomp-toolkit"><br><sub>GitHub repo card for [encounter/decomp-toolkit](https://github.com/encounter/decomp-toolkit), not a screenshot</sub>
- [encounter/objdiff](https://github.com/encounter/objdiff) — **Uses rea: No**. Object-file diffing tool used across decomp projects. Apache-2.0.<br><img src="https://raw.githubusercontent.com/encounter/objdiff/main/assets/screen-symbols.png" width="240" alt="encounter/objdiff"><br><sub>Image: encounter/objdiff ([source](https://github.com/encounter/objdiff))</sub>

### Wii

#### 反編譯 / 重編譯

- [zeldaret/ss](https://github.com/zeldaret/ss) — **Uses rea: No**. Skyward Sword decompilation. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/zeldaret/ss" width="240" alt="zeldaret/ss"><br><sub>GitHub repo card for [zeldaret/ss](https://github.com/zeldaret/ss), not a screenshot</sub>
- [DarkRTA/rb3](https://github.com/DarkRTA/rb3) — **Uses rea: No**. Rock Band 3 (Wii) decompilation.<br><img src="https://opengraph.githubassets.com/1/DarkRTA/rb3" width="240" alt="DarkRTA/rb3"><br><sub>GitHub repo card for [DarkRTA/rb3](https://github.com/DarkRTA/rb3), not a screenshot</sub>

### NDS

#### 反編譯 / 重編譯

- [pret/pokeplatinum](https://github.com/pret/pokeplatinum) — **Uses rea: No**. Pokémon Platinum decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokeplatinum" width="240" alt="pret/pokeplatinum"><br><sub>GitHub repo card for [pret/pokeplatinum](https://github.com/pret/pokeplatinum), not a screenshot</sub>
- [zeldaret/ph](https://github.com/zeldaret/ph) — **Uses rea: No**. Phantom Hourglass decompilation. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/zeldaret/ph" width="240" alt="zeldaret/ph"><br><sub>GitHub repo card for [zeldaret/ph](https://github.com/zeldaret/ph), not a screenshot</sub>
- [pret/pokeheartgold](https://github.com/pret/pokeheartgold) — **Uses rea: No**. Pokémon HeartGold/SoulSilver decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokeheartgold" width="240" alt="pret/pokeheartgold"><br><sub>GitHub repo card for [pret/pokeheartgold](https://github.com/pret/pokeheartgold), not a screenshot</sub>

### 3DS

#### 資源擷取與工具

- [3DSGuy/Project_CTR](https://github.com/3DSGuy/Project_CTR) — **Uses rea: No**. 3DS file tools (ctrtool / makerom).<br><img src="https://opengraph.githubassets.com/1/3DSGuy/Project_CTR" width="240" alt="3DSGuy/Project_CTR"><br><sub>GitHub repo card for [3DSGuy/Project_CTR](https://github.com/3DSGuy/Project_CTR), not a screenshot</sub>

### PS1

#### 反編譯 / 重編譯

- [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp) — **Uses rea: No**. Castlevania: Symphony of the Night decompilation. AGPL-3.0.<br><img src="https://opengraph.githubassets.com/1/Xeeynamo/sotn-decomp" width="240" alt="Xeeynamo/sotn-decomp"><br><sub>GitHub repo card for [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp), not a screenshot</sub>
- [shdecompilations/silent-hill-decomp](https://github.com/shdecompilations/silent-hill-decomp) — **Uses rea: No**. Silent Hill decompilation.<br><img src="https://opengraph.githubassets.com/1/shdecompilations/silent-hill-decomp" width="240" alt="shdecompilations/silent-hill-decomp"><br><sub>GitHub repo card for [shdecompilations/silent-hill-decomp](https://github.com/shdecompilations/silent-hill-decomp), not a screenshot</sub>

### PS2

#### 反編譯 / 重編譯

- [ran-j/PS2Recomp](https://github.com/ran-j/PS2Recomp) — **Uses rea: No**. PS2 static recompiler. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/ran-j/PS2Recomp" width="240" alt="ran-j/PS2Recomp"><br><sub>GitHub repo card for [ran-j/PS2Recomp](https://github.com/ran-j/PS2Recomp), not a screenshot</sub>
- [open-goal/jak-project](https://github.com/open-goal/jak-project) — **Uses rea: No**. Jak and Daxter / Jak II PC port via GOAL decompiler; needs your own disc. ISC.<br><img src="https://raw.githubusercontent.com/open-goal/jak-project/master/docs/img/promosmall1.png" width="240" alt="open-goal/jak-project"><br><sub>Image: open-goal/jak-project ([source](https://github.com/open-goal/jak-project))</sub>

### Xbox / Xbox 360

#### 反編譯 / 重編譯

- [hedge-dev/XenonRecomp](https://github.com/hedge-dev/XenonRecomp) — **Uses rea: No**. Xbox 360 PPC to C++ static recompiler. MIT.<br><img src="https://opengraph.githubassets.com/1/hedge-dev/XenonRecomp" width="240" alt="hedge-dev/XenonRecomp"><br><sub>GitHub repo card for [hedge-dev/XenonRecomp](https://github.com/hedge-dev/XenonRecomp), not a screenshot</sub>

#### 重製 / 移植

- [hedge-dev/UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp) — **Uses rea: No**. Sonic Unleashed (X360) recompilation PC port; needs your own copy. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/hedge-dev/UnleashedRecomp" width="240" alt="hedge-dev/UnleashedRecomp"><br><sub>GitHub repo card for [hedge-dev/UnleashedRecomp](https://github.com/hedge-dev/UnleashedRecomp), not a screenshot</sub>

#### 資源擷取與工具

- [xemu-project/xemu](https://github.com/xemu-project/xemu) — **Uses rea: No**. Original Xbox emulator.<br><img src="https://opengraph.githubassets.com/1/xemu-project/xemu" width="240" alt="xemu-project/xemu"><br><sub>GitHub repo card for [xemu-project/xemu](https://github.com/xemu-project/xemu), not a screenshot</sub>

### PC / DOS / PC-98

#### 反編譯 / 重編譯

- [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) — **Uses rea: Yes**. DX-Ball 1.07 reconstruction; README states REA. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="240" alt="N0zoM1z0/dx-ball"><br><sub>Image: N0zoM1z0/dx-ball ([source](https://github.com/N0zoM1z0/dx-ball))</sub>
- [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) — **Uses rea: Yes**. Touhou 4 (PC-98) source reconstruction; REA via official showcase. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="240" alt="N0zoM1z0/th04"><br><sub>Image: N0zoM1z0/th04 ([source](https://github.com/N0zoM1z0/th04))</sub>
- [N0zoM1z0/th08](https://github.com/N0zoM1z0/th08) — **Uses rea: Unverified**. Touhou 8 reconstruction (agent + IDA/Ghidra); README does not mention REA. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/th08/main/resources/title-screen.png" width="240" alt="N0zoM1z0/th08"><br><sub>Image: N0zoM1z0/th08 ([source](https://github.com/N0zoM1z0/th08))</sub>
- [N0zoM1z0/th10](https://github.com/N0zoM1z0/th10) — **Uses rea: Unverified**. Touhou 10 reconstruction; README does not mention REA. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/th10/main/resources/title-screen.png" width="240" alt="N0zoM1z0/th10"><br><sub>Image: N0zoM1z0/th10 ([source](https://github.com/N0zoM1z0/th10))</sub>
- [isledecomp/isle](https://github.com/isledecomp/isle) — **Uses rea: No**. LEGO Island decompilation. LGPL-3.0.<br><img src="https://opengraph.githubassets.com/1/isledecomp/isle" width="240" alt="isledecomp/isle"><br><sub>GitHub repo card for [isledecomp/isle](https://github.com/isledecomp/isle), not a screenshot</sub>
- [diasurgical/DevilutionX](https://github.com/diasurgical/DevilutionX) — **Uses rea: No**. Diablo engine reconstruction; needs your own DIABDAT.MPQ.<br><img src="https://github.com/user-attachments/assets/7ac73801-ef7b-4cc1-8442-a191a2a0a1ce" width="240" alt="diasurgical/DevilutionX"><br><sub>Image: diasurgical/DevilutionX ([source](https://github.com/diasurgical/DevilutionX))</sub>

#### 重製 / 移植

- [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) — **Uses rea: Yes**. Gemtree Desktop Games (2000) ported to macOS/browser; README cites REA + Ghidra.<br><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="240" alt="ucodia/desktop-games-nostalgia"><br><sub>Image: ucodia/desktop-games-nostalgia ([source](https://github.com/ucodia/desktop-games-nostalgia))</sub>
- [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) — **Uses rea: Yes**. Ski or Die (DOS) minigame rebuilt in Rust + SDL2; uses your own assets.<br><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="240" alt="tuunanet/rea-ski-or-die-reconstruction"><br><sub>Image: tuunanet/rea-ski-or-die-reconstruction ([source](https://github.com/tuunanet/rea-ski-or-die-reconstruction))</sub>
- [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) — **Uses rea: Yes**. Clean-room Refractor 2 engine; REA documented in CLAUDE.md / tools/rea.sh. Needs your own copy.<br><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="240" alt="Moxnatiy/OpenBattlefield2"><br><sub>Image: Moxnatiy/OpenBattlefield2 ([source](https://github.com/Moxnatiy/OpenBattlefield2))</sub>
- [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) — **Uses rea: Yes**. GunZ: The Duel in Rust + Bevy; README mentions REA. Apache-2.0.<br><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="240" alt="OpenRsG/GunZRs"><br><sub>Image: OpenRsG/GunZRs ([source](https://github.com/OpenRsG/GunZRs))</sub>
- [a-barzanti/ai-rebuilds](https://github.com/a-barzanti/ai-rebuilds) — **Uses rea: Yes**. Abandoned games rebuilt for the web from REA-written specs; no original files committed.<br><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="240" alt="a-barzanti/ai-rebuilds"><br><sub>GitHub repo card for [a-barzanti/ai-rebuilds](https://github.com/a-barzanti/ai-rebuilds), not a screenshot</sub>
- [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) — **Uses rea: No**. RollerCoaster Tycoon 2 re-implementation (pre-REA). GPL-3.0.<br><img src="https://github.com/user-attachments/assets/fa893cc8-1484-4751-94be-4ead00a6c8f9" width="240" alt="OpenRCT2/OpenRCT2"><br><sub>Image: OpenRCT2/OpenRCT2 ([source](https://github.com/OpenRCT2/OpenRCT2))</sub>
- [OpenMW/openmw](https://github.com/OpenMW/openmw) — **Uses rea: No**. Morrowind engine re-implementation. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/OpenMW/openmw" width="240" alt="OpenMW/openmw"><br><sub>GitHub repo card for [OpenMW/openmw](https://github.com/OpenMW/openmw), not a screenshot</sub>
- [julianxhokaxhiu/FFNx](https://github.com/julianxhokaxhiu/FFNx) — **Uses rea: No**. FF7/FF8 PC driver. GPL-3.0.<br><img src="https://raw.githubusercontent.com/julianxhokaxhiu/FFNx/master/.screens/ff7.png" width="240" alt="julianxhokaxhiu/FFNx"><br><sub>Image: julianxhokaxhiu/FFNx ([source](https://github.com/julianxhokaxhiu/FFNx))</sub>
- [Interkarma/daggerfall-unity](https://github.com/Interkarma/daggerfall-unity) — **Uses rea: No**. Daggerfall in Unity; needs your own data. MIT.<br><img src="https://github.com/Interkarma/daggerfall-unity/assets/10426244/4f176f9d-6332-47b3-a4d7-317ed8d6b38b" width="240" alt="Interkarma/daggerfall-unity"><br><sub>Image: Interkarma/daggerfall-unity ([source](https://github.com/Interkarma/daggerfall-unity))</sub>
- [OpenXcom/OpenXcom](https://github.com/OpenXcom/OpenXcom) — **Uses rea: No**. UFO / X-COM re-implementation. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/OpenXcom/OpenXcom" width="240" alt="OpenXcom/OpenXcom"><br><sub>GitHub repo card for [OpenXcom/OpenXcom](https://github.com/OpenXcom/OpenXcom), not a screenshot</sub>
- [scummvm/scummvm](https://github.com/scummvm/scummvm) — **Uses rea: No**. Engine re-implementations for classic adventure games. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/scummvm/scummvm" width="240" alt="scummvm/scummvm"><br><sub>GitHub repo card for [scummvm/scummvm](https://github.com/scummvm/scummvm), not a screenshot</sub>
- [fallout2-ce/fallout2-ce](https://github.com/fallout2-ce/fallout2-ce) — **Uses rea: No**. Fallout 2 re-implementation; needs your own data.<br><img src="https://raw.githubusercontent.com/fallout2-ce/fallout2-ce/main/docs/images/two-column-inventory.jpg" width="240" alt="fallout2-ce/fallout2-ce"><br><sub>Image: fallout2-ce/fallout2-ce ([source](https://github.com/fallout2-ce/fallout2-ce))</sub>
- [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD) — **Uses rea: No**. Transport Tycoon Deluxe open re-implementation.<br><img src="https://opengraph.githubassets.com/1/OpenTTD/OpenTTD" width="240" alt="OpenTTD/OpenTTD"><br><sub>GitHub repo card for [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD), not a screenshot</sub>
- [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) — **Uses rea: No**. Red Alert / C&C engine re-implementation. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/OpenRA/OpenRA" width="240" alt="OpenRA/OpenRA"><br><sub>GitHub repo card for [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA), not a screenshot</sub>
- [perfect-dark-pc-port/perfect_dark](https://github.com/perfect-dark-pc-port/perfect_dark) — **Uses rea: No**. Perfect Dark PC port from decomp. MIT.<br><img src="https://opengraph.githubassets.com/1/perfect-dark-pc-port/perfect_dark" width="240" alt="perfect-dark-pc-port/perfect_dark"><br><sub>GitHub repo card for [perfect-dark-pc-port/perfect_dark](https://github.com/perfect-dark-pc-port/perfect_dark), not a screenshot</sub>

#### 資源擷取與工具

- [ata4/disunity](https://github.com/ata4/disunity) — **Uses rea: No**. Unity asset tools (archived). Unlicense.<br><img src="https://opengraph.githubassets.com/1/ata4/disunity" width="240" alt="ata4/disunity"><br><sub>GitHub repo card for [ata4/disunity](https://github.com/ata4/disunity), not a screenshot</sub>
- [Perfare/AssetStudio](https://github.com/Perfare/AssetStudio) — **Uses rea: No**. Unity asset explorer (archived). MIT.<br><img src="https://opengraph.githubassets.com/1/Perfare/AssetStudio" width="240" alt="Perfare/AssetStudio"><br><sub>GitHub repo card for [Perfare/AssetStudio](https://github.com/Perfare/AssetStudio), not a screenshot</sub>
- [AssetRipper/AssetRipper](https://github.com/AssetRipper/AssetRipper) — **Uses rea: No**. Unity asset ripping tool for your own projects. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/AssetRipper/AssetRipper" width="240" alt="AssetRipper/AssetRipper"><br><sub>GitHub repo card for [AssetRipper/AssetRipper](https://github.com/AssetRipper/AssetRipper), not a screenshot</sub>
- [ladislav-zezula/CascLib](https://github.com/ladislav-zezula/CascLib) — **Uses rea: No**. CASC storage library. MIT.<br><img src="https://opengraph.githubassets.com/1/ladislav-zezula/CascLib" width="240" alt="ladislav-zezula/CascLib"><br><sub>GitHub repo card for [ladislav-zezula/CascLib](https://github.com/ladislav-zezula/CascLib), not a screenshot</sub>

## 應用程式 / Electron / 桌面

- [michaelshimeles/sketch](https://github.com/michaelshimeles/sketch) — **Uses rea: Yes**. Rust infinite-canvas design app, clean-room from Paper; README mentions REA (formerly paper-rs).<br><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="240" alt="michaelshimeles/sketch"><br><sub>Image: michaelshimeles/sketch ([source](https://github.com/michaelshimeles/sketch))</sub>
- [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) — **Uses rea: Yes**. Rust macOS recorder modelled on OBS Studio; README mentions REA.<br><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="240" alt="michaelshimeles/rec-rs"><br><sub>Image: michaelshimeles/rec-rs ([source](https://github.com/michaelshimeles/rec-rs))</sub>
- [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) — **Uses rea: Yes**. .NET 10 colour picker from a REA study of PowerToys. MIT.<br><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="240" alt="iammukeshm/hexgrab"><br><sub>GitHub repo card for [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab), not a screenshot</sub>
- [AdamLinCodes/AdamTerm](https://github.com/AdamLinCodes/AdamTerm) — **Uses rea: Yes**. Minimal macOS terminal after studying Ghostty with REA.<br><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="240" alt="AdamLinCodes/AdamTerm"><br><sub>Image: AdamLinCodes/AdamTerm ([source](https://github.com/AdamLinCodes/AdamTerm))</sub>
- [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) — **Uses rea: Yes**. Wispr Flow static teardown + 64-line local rebuild.<br><img src="https://opengraph.githubassets.com/1/az9713/wispr-flow-rea-teardown" width="240" alt="az9713/wispr-flow-rea-teardown"><br><sub>GitHub repo card for [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown), not a screenshot</sub>
- [cudanexus/vd-streamer-linux](https://github.com/cudanexus/vd-streamer-linux) — **Uses rea: Yes**. Unofficial Linux port of Virtual Desktop Streamer; Claude Code + REA.<br><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="240" alt="cudanexus/vd-streamer-linux"><br><sub>GitHub repo card for [cudanexus/vd-streamer-linux](https://github.com/cudanexus/vd-streamer-linux), not a screenshot</sub>
- [electron/asar](https://github.com/electron/asar) — **Uses rea: No**. Electron ASAR archive tool. MIT.<br><img src="https://opengraph.githubassets.com/1/electron/asar" width="240" alt="electron/asar"><br><sub>GitHub repo card for [electron/asar](https://github.com/electron/asar), not a screenshot</sub>

## 協定 / 硬體

- [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) — **Uses rea: Unverified**. First-gen Siri Remote on Linux (Bluetooth protocol). MIT.<br><img src="https://opengraph.githubassets.com/1/a-funk/open-appleremote" width="240" alt="a-funk/open-appleremote"><br><sub>GitHub repo card for [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote), not a screenshot</sub>
- [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) — **Uses rea: No**. Linux Logitech G HUB replacement over HID++ 2.0. MIT.<br><img src="https://raw.githubusercontent.com/Slyvan25/OpenGHub/master/docs/screenshots/devices.png" width="240" alt="Slyvan25/OpenGHub"><br><sub>Image: Slyvan25/OpenGHub ([source](https://github.com/Slyvan25/OpenGHub))</sub>
- [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) — **Uses rea: No**. Interactive HTTPS proxy for protocol analysis. MIT.<br><img src="https://opengraph.githubassets.com/1/mitmproxy/mitmproxy" width="240" alt="mitmproxy/mitmproxy"><br><sub>GitHub repo card for [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy), not a screenshot</sub>
- [postlund/pyatv](https://github.com/postlund/pyatv) — **Uses rea: No**. Apple TV protocol library. MIT.<br><img src="https://opengraph.githubassets.com/1/postlund/pyatv" width="240" alt="postlund/pyatv"><br><sub>GitHub repo card for [postlund/pyatv](https://github.com/postlund/pyatv), not a screenshot</sub>
- [wireshark/wireshark](https://github.com/wireshark/wireshark) — **Uses rea: No**. Network protocol analyzer. GPL-2.0.<br><img src="https://opengraph.githubassets.com/1/wireshark/wireshark" width="240" alt="wireshark/wireshark"><br><sub>GitHub repo card for [wireshark/wireshark](https://github.com/wireshark/wireshark), not a screenshot</sub>

## 韌體 / 驅動

- [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) — **Uses rea: Yes**. PreSonus AudioBox VSL kernel module; REA used for part of the vendor-library findings. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="240" alt="grisuno/VSL-DSP"><br><sub>GitHub repo card for [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP), not a screenshot</sub>
- [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) — **Uses rea: No**. Firmware analysis/extraction tool. MIT.<br><img src="https://raw.githubusercontent.com/ReFirmLabs/binwalk/master/images/output.png" width="240" alt="ReFirmLabs/binwalk"><br><sub>Image: ReFirmLabs/binwalk ([source](https://github.com/ReFirmLabs/binwalk))</sub>
- [qilingframework/qiling](https://github.com/qilingframework/qiling) — **Uses rea: No**. Binary emulation framework. GPL-2.0.<br><img src="https://raw.githubusercontent.com/qilingframework/theme.qiling.io/master/source/img/fuzzer.jpg?raw=true" width="240" alt="qilingframework/qiling"><br><sub>Image: qilingframework/qiling ([source](https://github.com/qilingframework/qiling))</sub>
- [ghidraninja/game-and-watch-backup](https://github.com/ghidraninja/game-and-watch-backup) — **Uses rea: No**. Game & Watch backup tool for your own device.<br><img src="https://opengraph.githubassets.com/1/ghidraninja/game-and-watch-backup" width="240" alt="ghidraninja/game-and-watch-backup"><br><sub>GitHub repo card for [ghidraninja/game-and-watch-backup](https://github.com/ghidraninja/game-and-watch-backup), not a screenshot</sub>
- [attify/firmware-analysis-toolkit](https://github.com/attify/firmware-analysis-toolkit) — **Uses rea: No**. Firmware emulation toolkit for security research.<br><img src="https://opengraph.githubassets.com/1/attify/firmware-analysis-toolkit" width="240" alt="attify/firmware-analysis-toolkit"><br><sub>GitHub repo card for [attify/firmware-analysis-toolkit](https://github.com/attify/firmware-analysis-toolkit), not a screenshot</sub>
- [onekey-sec/unblob](https://github.com/onekey-sec/unblob) — **Uses rea: No**. Extraction suite for firmware blobs. MIT.<br><img src="https://opengraph.githubassets.com/1/onekey-sec/unblob" width="240" alt="onekey-sec/unblob"><br><sub>GitHub repo card for [onekey-sec/unblob](https://github.com/onekey-sec/unblob), not a screenshot</sub>
- [travisgoodspeed/md380tools](https://github.com/travisgoodspeed/md380tools) — **Uses rea: No**. MD380 radio firmware patches.<br><img src="https://opengraph.githubassets.com/1/travisgoodspeed/md380tools" width="240" alt="travisgoodspeed/md380tools"><br><sub>GitHub repo card for [travisgoodspeed/md380tools](https://github.com/travisgoodspeed/md380tools), not a screenshot</sub>

## 資安 / 評測

- [NullLabTests/OpenBSD_netcat_REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) — **Uses rea: Yes**. Static analysis of netcat-openbsd with REA + Ghidra. MIT.<br><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="240" alt="NullLabTests/OpenBSD_netcat_REA"><br><sub>Image: NullLabTests/OpenBSD_netcat_REA ([source](https://github.com/NullLabTests/OpenBSD_netcat_REA))</sub>
- [REA discussion #2254](https://github.com/morluto/rea/discussions/2254) — **Uses rea: Yes**. Stripped bzip2 analysed and checked against an unstripped build.<br><sub>No image.</sub>

## REA 周邊工具

- [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) — **Uses rea: Yes**. Agent skill for evidence-based reconstruction with REA. MIT.<br><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="240" alt="ShadowSwaps/REA-Reconstruction-Companion"><br><sub>GitHub repo card for [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion), not a screenshot</sub>
- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) — **Uses rea: No**. Decompiler REA can drive. Apache-2.0.<br><img src="https://opengraph.githubassets.com/1/NationalSecurityAgency/ghidra" width="240" alt="NationalSecurityAgency/ghidra"><br><sub>GitHub repo card for [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra), not a screenshot</sub>
- [skylot/jadx](https://github.com/skylot/jadx) — **Uses rea: No**. Android DEX decompiler REA can drive. Apache-2.0.<br><img src="https://user-images.githubusercontent.com/118523/142730720-839f017e-38db-423e-b53f-39f5f0a0316f.png" width="240" alt="skylot/jadx"><br><sub>Image: skylot/jadx ([source](https://github.com/skylot/jadx))</sub>
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) — **Uses rea: No**. MCP server for Ghidra. Apache-2.0.<br><img src="https://github.com/user-attachments/assets/4986d702-be3f-4697-acce-aea55cd79ad3" width="240" alt="LaurieWired/GhidraMCP"><br><sub>Image: LaurieWired/GhidraMCP ([source](https://github.com/LaurieWired/GhidraMCP))</sub>
- [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg) — **Uses rea: No**. Windows debugger.<br><img src="https://raw.githubusercontent.com/x64dbg/x64dbg/development/.github/screenshots/cpu-light.png" width="240" alt="x64dbg/x64dbg"><br><sub>Image: x64dbg/x64dbg ([source](https://github.com/x64dbg/x64dbg))</sub>
- [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) — **Uses rea: No**. Android APK reverse-engineering tool. Apache-2.0.<br><img src="https://opengraph.githubassets.com/1/iBotPeaches/Apktool" width="240" alt="iBotPeaches/Apktool"><br><sub>GitHub repo card for [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool), not a screenshot</sub>
- [angr/angr](https://github.com/angr/angr) — **Uses rea: No**. Binary analysis platform. BSD-2-Clause.<br><img src="https://opengraph.githubassets.com/1/angr/angr" width="240" alt="angr/angr"><br><sub>GitHub repo card for [angr/angr](https://github.com/angr/angr), not a screenshot</sub>
- [avast/retdec](https://github.com/avast/retdec) — **Uses rea: No**. Retargetable machine-code decompiler. MIT.<br><img src="https://opengraph.githubassets.com/1/avast/retdec" width="240" alt="avast/retdec"><br><sub>GitHub repo card for [avast/retdec](https://github.com/avast/retdec), not a screenshot</sub>
- [rizinorg/cutter](https://github.com/rizinorg/cutter) — **Uses rea: No**. Qt GUI for Rizin. GPL-3.0.<br><img src="https://raw.githubusercontent.com/rizinorg/cutter/dev/docs/source/images/screenshot.png" width="240" alt="rizinorg/cutter"><br><sub>Image: rizinorg/cutter ([source](https://github.com/rizinorg/cutter))</sub>
- [ghidraninja/ghidra_scripts](https://github.com/ghidraninja/ghidra_scripts) — **Uses rea: No**. Ghidra scripts. GPL-3.0.<br><img src="https://raw.githubusercontent.com/ghidraninja/ghidra_scripts/master/images/binwalk.png" width="240" alt="ghidraninja/ghidra_scripts"><br><sub>Image: ghidraninja/ghidra_scripts ([source](https://github.com/ghidraninja/ghidra_scripts))</sub>
- [radareorg/radare2](https://github.com/radareorg/radare2) — **Uses rea: No**. Reverse-engineering framework.<br><img src="https://opengraph.githubassets.com/1/radareorg/radare2" width="240" alt="radareorg/radare2"><br><sub>GitHub repo card for [radareorg/radare2](https://github.com/radareorg/radare2), not a screenshot</sub>
- [mandiant/flare-floss](https://github.com/mandiant/flare-floss) — **Uses rea: No**. Obfuscated string extraction. Apache-2.0.<br><img src="https://github.com/mandiant/flare-floss/assets/156560/f2d471a3-2624-498c-aaa9-928e2909c338" width="240" alt="mandiant/flare-floss"><br><sub>Image: mandiant/flare-floss ([source](https://github.com/mandiant/flare-floss))</sub>
- [WerWolv/ImHex](https://github.com/WerWolv/ImHex) — **Uses rea: No**. Hex editor for reverse engineers. GPL-2.0.<br><img src="https://opengraph.githubassets.com/1/WerWolv/ImHex" width="240" alt="WerWolv/ImHex"><br><sub>GitHub repo card for [WerWolv/ImHex](https://github.com/WerWolv/ImHex), not a screenshot</sub>
- [mandiant/capa](https://github.com/mandiant/capa) — **Uses rea: No**. Capability detection in executables. Apache-2.0.<br><img src="https://raw.githubusercontent.com/mandiant/capa/master/doc/img/capa_web_explorer.png" width="240" alt="mandiant/capa"><br><sub>Image: mandiant/capa ([source](https://github.com/mandiant/capa))</sub>
- [frida/frida](https://github.com/frida/frida) — **Uses rea: No**. Dynamic instrumentation toolkit.<br><img src="https://opengraph.githubassets.com/1/frida/frida" width="240" alt="frida/frida"><br><sub>GitHub repo card for [frida/frida](https://github.com/frida/frida), not a screenshot</sub>
- [dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy) — **Uses rea: No**. .NET debugger and assembly editor. GPL-3.0.<br><img src="https://raw.githubusercontent.com/dnSpyEx/dnSpy/master/images/debug-animated.gif" width="240" alt="dnSpyEx/dnSpy"><br><sub>Image: dnSpyEx/dnSpy ([source](https://github.com/dnSpyEx/dnSpy))</sub>
- [decompme/decomp.me](https://github.com/decompme/decomp.me) — **Uses rea: No**. Collaborative decompilation website. MIT.<br><img src="https://opengraph.githubassets.com/1/decompme/decomp.me" width="240" alt="decompme/decomp.me"><br><sub>GitHub repo card for [decompme/decomp.me](https://github.com/decompme/decomp.me), not a screenshot</sub>
- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) — **Uses rea: No**. MCP server for IDA Pro. MIT.<br><img src="https://img.youtube.com/vi/iFxNuk3kxhk/0.jpg" width="240" alt="mrexodia/ida-pro-mcp"><br><sub>Image: mrexodia/ida-pro-mcp ([source](https://github.com/mrexodia/ida-pro-mcp))</sub>
- [rizinorg/jsdec](https://github.com/rizinorg/jsdec) — **Uses rea: No**. Simple decompiler for Rizin. It's capable of generating readable pseudo code even on handmade assembly.<br><img src="https://opengraph.githubassets.com/1/rizinorg/jsdec" width="240" alt="rizinorg/jsdec"><br><sub>GitHub repo card for [rizinorg/jsdec](https://github.com/rizinorg/jsdec), not a screenshot</sub>
- [rizinorg/rizin](https://github.com/rizinorg/rizin) — **Uses rea: No**. radare2 fork / RE framework. LGPL-3.0.<br><img src="https://opengraph.githubassets.com/1/rizinorg/rizin" width="240" alt="rizinorg/rizin"><br><sub>GitHub repo card for [rizinorg/rizin](https://github.com/rizinorg/rizin), not a screenshot</sub>
- [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy) — **Uses rea: No**. .NET decompiler. MIT.<br><img src="https://opengraph.githubassets.com/1/icsharpcode/ILSpy" width="240" alt="icsharpcode/ILSpy"><br><sub>GitHub repo card for [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy), not a screenshot</sub>
- [google/bindiff](https://github.com/google/bindiff) — **Uses rea: No**. Binary diffing. Apache-2.0.<br><img src="https://opengraph.githubassets.com/1/google/bindiff" width="240" alt="google/bindiff"><br><sub>GitHub repo card for [google/bindiff](https://github.com/google/bindiff), not a screenshot</sub>

---

貢獻指南見 [CONTRIBUTING.md](CONTRIBUTING.md)。授權：[CC0-1.0](LICENSE)。
