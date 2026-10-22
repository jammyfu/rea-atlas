[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# REA Atlas

[morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）を使ったリバースエンジニアリング事例と、同種の逆コンパイル／再実装プロジェクトの一覧です。各項目に **Uses rea: Yes / No / Unverified** を付け、公開された根拠（README、公式ショーケース、リポジトリ文書）がある場合のみ Yes とします。

> 非公式であり、morluto/rea とは無関係です。クラック、海賊版、ROM、著作権素材は掲載・配布しません。各言語版で一覧を同一に保つため、項目の説明は英語のままです。

<img src="https://raw.githubusercontent.com/morluto/rea/main/docs/assets/rea-showcases.png" alt="REA showcases" width="720" />

<sub>画像：[morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png) の REA ショーケース図（MIT）を直接参照しています（再ホストなし）。</sub>

## REA 公式ショーケース

- [DX-Ball: sound-pan function](https://rea.tools/showcase/dx-ball/) — **Uses rea: Yes**. Official showcase; C reconstruction matching 3,205 x86 cases.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="DX-Ball: sound-pan function"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/dx-ball/), not a screenshot</sub>
- [Notion: Electron clipboard bridge](https://rea.tools/showcase/notion/) — **Uses rea: Yes**. Official showcase; renderer → preload → IPC trace.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="Notion: Electron clipboard bridge"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/notion/), not a screenshot</sub>
- [TH04: PC-98 bullet-ring maths](https://rea.tools/showcase/th04/) — **Uses rea: Yes**. Official showcase; 16-bit angle helpers.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="TH04: PC-98 bullet-ring maths"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/th04/), not a screenshot</sub>
- [Aegis: TOTP code generation](https://rea.tools/showcase/aegis/) — **Uses rea: Yes**. Official showcase; Android app.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="Aegis: TOTP code generation"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/aegis/), not a screenshot</sub>
- [CTF: flag checker](https://rea.tools/showcase/ctf/) — **Uses rea: Yes**. Official showcase; DownUnderCTF 2023 challenge.<br><img src="https://rea.tools/assets/social-card.png" width="240" alt="CTF: flag checker"><br><sub>Site social card from [rea.tools](https://rea.tools/showcase/ctf/), not a screenshot</sub>

## ゲーム

### PC / DOS / PC-98

#### 逆コンパイル / 再コンパイル

- [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) — **Uses rea: Yes**. DX-Ball 1.07 reconstruction; README states REA. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="240" alt="N0zoM1z0/dx-ball"><br><sub>Image: N0zoM1z0/dx-ball ([source](https://github.com/N0zoM1z0/dx-ball))</sub>
- [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) — **Uses rea: Yes**. Touhou 4 (PC-98) source reconstruction; REA via official showcase. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="240" alt="N0zoM1z0/th04"><br><sub>Image: N0zoM1z0/th04 ([source](https://github.com/N0zoM1z0/th04))</sub>
- [N0zoM1z0/th08](https://github.com/N0zoM1z0/th08) — **Uses rea: Unverified**. Touhou 8 reconstruction (agent + IDA/Ghidra); README does not mention REA. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/th08/main/resources/title-screen.png" width="240" alt="N0zoM1z0/th08"><br><sub>Image: N0zoM1z0/th08 ([source](https://github.com/N0zoM1z0/th08))</sub>
- [N0zoM1z0/th10](https://github.com/N0zoM1z0/th10) — **Uses rea: Unverified**. Touhou 10 reconstruction; README does not mention REA. MIT.<br><img src="https://raw.githubusercontent.com/N0zoM1z0/th10/main/resources/title-screen.png" width="240" alt="N0zoM1z0/th10"><br><sub>Image: N0zoM1z0/th10 ([source](https://github.com/N0zoM1z0/th10))</sub>

#### リメイク / 移植

- [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) — **Uses rea: Yes**. Gemtree Desktop Games (2000) ported to macOS/browser; README cites REA + Ghidra.<br><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="240" alt="ucodia/desktop-games-nostalgia"><br><sub>Image: ucodia/desktop-games-nostalgia ([source](https://github.com/ucodia/desktop-games-nostalgia))</sub>
- [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) — **Uses rea: Yes**. Ski or Die (DOS) minigame rebuilt in Rust + SDL2; uses your own assets.<br><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="240" alt="tuunanet/rea-ski-or-die-reconstruction"><br><sub>Image: tuunanet/rea-ski-or-die-reconstruction ([source](https://github.com/tuunanet/rea-ski-or-die-reconstruction))</sub>
- [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) — **Uses rea: Yes**. Clean-room Refractor 2 engine; REA documented in CLAUDE.md / tools/rea.sh. Needs your own copy.<br><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="240" alt="Moxnatiy/OpenBattlefield2"><br><sub>Image: Moxnatiy/OpenBattlefield2 ([source](https://github.com/Moxnatiy/OpenBattlefield2))</sub>
- [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) — **Uses rea: Yes**. GunZ: The Duel in Rust + Bevy; README mentions REA. Apache-2.0.<br><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="240" alt="OpenRsG/GunZRs"><br><sub>Image: OpenRsG/GunZRs ([source](https://github.com/OpenRsG/GunZRs))</sub>
- [a-barzanti/ai-rebuilds](https://github.com/a-barzanti/ai-rebuilds) — **Uses rea: Yes**. Abandoned games rebuilt for the web from REA-written specs; no original files committed.<br><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="240" alt="a-barzanti/ai-rebuilds"><br><sub>GitHub repo card for [a-barzanti/ai-rebuilds](https://github.com/a-barzanti/ai-rebuilds), not a screenshot</sub>
- [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) — **Uses rea: No**. RollerCoaster Tycoon 2 re-implementation (pre-REA). GPL-3.0.<br><img src="https://github.com/user-attachments/assets/fa893cc8-1484-4751-94be-4ead00a6c8f9" width="240" alt="OpenRCT2/OpenRCT2"><br><sub>Image: OpenRCT2/OpenRCT2 ([source](https://github.com/OpenRCT2/OpenRCT2))</sub>
- [OpenMW/openmw](https://github.com/OpenMW/openmw) — **Uses rea: No**. Morrowind engine re-implementation. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/OpenMW/openmw" width="240" alt="OpenMW/openmw"><br><sub>GitHub repo card for [OpenMW/openmw](https://github.com/OpenMW/openmw), not a screenshot</sub>

### NINTENDO64

#### 逆コンパイル / 再コンパイル

- [zeldaret/oot](https://github.com/zeldaret/oot) — **Uses rea: No**. Ocarina of Time decompilation; ROM not included.<br><img src="https://opengraph.githubassets.com/1/zeldaret/oot" width="240" alt="zeldaret/oot"><br><sub>GitHub repo card for [zeldaret/oot](https://github.com/zeldaret/oot), not a screenshot</sub>
- [n64decomp/sm64](https://github.com/n64decomp/sm64) — **Uses rea: No**. Super Mario 64 decompilation; ROM not included. CC0-1.0.<br><img src="https://opengraph.githubassets.com/1/n64decomp/sm64" width="240" alt="n64decomp/sm64"><br><sub>GitHub repo card for [n64decomp/sm64](https://github.com/n64decomp/sm64), not a screenshot</sub>

#### リメイク / 移植

- [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) — **Uses rea: No**. Ship of Harkinian PC port of OoT; requires your own ROM.<br><img src="https://raw.githubusercontent.com/HarbourMasters/Shipwright/develop/docs/shiptitle.darkmode.png" width="240" alt="HarbourMasters/Shipwright"><br><sub>Image: HarbourMasters/Shipwright ([source](https://github.com/HarbourMasters/Shipwright))</sub>

#### アセット抽出・ツール

- [ethteck/splat](https://github.com/ethteck/splat) — **Uses rea: No**. Binary splitting tool for N64/PSX decomp projects. MIT.<br><img src="https://opengraph.githubassets.com/1/ethteck/splat" width="240" alt="ethteck/splat"><br><sub>GitHub repo card for [ethteck/splat](https://github.com/ethteck/splat), not a screenshot</sub>
- [NEstelami/ZAPD](https://github.com/NEstelami/ZAPD) — **Uses rea: No**. Zelda asset processor used by decomp projects. MIT.<br><img src="https://raw.githubusercontent.com/NEstelami/ZAPD/master/docs/zapd_warning_example.png?raw=true" width="240" alt="NEstelami/ZAPD"><br><sub>Image: NEstelami/ZAPD ([source](https://github.com/NEstelami/ZAPD))</sub>

### メガドライブ / Genesis

#### 逆コンパイル / 再コンパイル

- [sonicretro/s1disasm](https://github.com/sonicretro/s1disasm) — **Uses rea: No**. Sonic the Hedgehog (Mega Drive) disassembly.<br><img src="https://opengraph.githubassets.com/1/sonicretro/s1disasm" width="240" alt="sonicretro/s1disasm"><br><sub>GitHub repo card for [sonicretro/s1disasm](https://github.com/sonicretro/s1disasm), not a screenshot</sub>
- [sonicretro/s2disasm](https://github.com/sonicretro/s2disasm) — **Uses rea: No**. Sonic 2 (Mega Drive) disassembly.<br><img src="https://opengraph.githubassets.com/1/sonicretro/s2disasm" width="240" alt="sonicretro/s2disasm"><br><sub>GitHub repo card for [sonicretro/s2disasm](https://github.com/sonicretro/s2disasm), not a screenshot</sub>

### スーパーファミコン / SNES

#### 逆コンパイル / 再コンパイル

- [snesrev/zelda3](https://github.com/snesrev/zelda3) — **Uses rea: No**. A Link to the Past C reimplementation; asset extraction from your own ROM.<br><img src="https://opengraph.githubassets.com/1/snesrev/zelda3" width="240" alt="snesrev/zelda3"><br><sub>GitHub repo card for [snesrev/zelda3](https://github.com/snesrev/zelda3), not a screenshot</sub>
- [snesrev/sm](https://github.com/snesrev/sm) — **Uses rea: No**. Super Metroid C reimplementation; needs your own ROM.<br><img src="https://opengraph.githubassets.com/1/snesrev/sm" width="240" alt="snesrev/sm"><br><sub>GitHub repo card for [snesrev/sm](https://github.com/snesrev/sm), not a screenshot</sub>

### ファミコン / NES

_検証済みの項目はまだありません。追加歓迎です。_

### ゲームボーイアドバンス

#### 逆コンパイル / 再コンパイル

- [pret/pokeemerald](https://github.com/pret/pokeemerald) — **Uses rea: No**. Pokémon Emerald decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokeemerald" width="240" alt="pret/pokeemerald"><br><sub>GitHub repo card for [pret/pokeemerald](https://github.com/pret/pokeemerald), not a screenshot</sub>
- [pret/pokefirered](https://github.com/pret/pokefirered) — **Uses rea: No**. Pokémon FireRed/LeafGreen decompilation.<br><img src="https://opengraph.githubassets.com/1/pret/pokefirered" width="240" alt="pret/pokefirered"><br><sub>GitHub repo card for [pret/pokefirered](https://github.com/pret/pokefirered), not a screenshot</sub>
- [zeldaret/tmc](https://github.com/zeldaret/tmc) — **Uses rea: No**. The Minish Cap decompilation.<br><img src="https://opengraph.githubassets.com/1/zeldaret/tmc" width="240" alt="zeldaret/tmc"><br><sub>GitHub repo card for [zeldaret/tmc](https://github.com/zeldaret/tmc), not a screenshot</sub>

### ゲームボーイ

#### 逆コンパイル / 再コンパイル

- [pret/pokered](https://github.com/pret/pokered) — **Uses rea: No**. Pokémon Red/Blue disassembly.<br><img src="https://opengraph.githubassets.com/1/pret/pokered" width="240" alt="pret/pokered"><br><sub>GitHub repo card for [pret/pokered](https://github.com/pret/pokered), not a screenshot</sub>
- [pret/pokegold](https://github.com/pret/pokegold) — **Uses rea: No**. Pokémon Gold/Silver disassembly.<br><img src="https://opengraph.githubassets.com/1/pret/pokegold" width="240" alt="pret/pokegold"><br><sub>GitHub repo card for [pret/pokegold](https://github.com/pret/pokegold), not a screenshot</sub>

### PlayStation

#### 逆コンパイル / 再コンパイル

- [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp) — **Uses rea: No**. Castlevania: Symphony of the Night decompilation. AGPL-3.0.<br><img src="https://opengraph.githubassets.com/1/Xeeynamo/sotn-decomp" width="240" alt="Xeeynamo/sotn-decomp"><br><sub>GitHub repo card for [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp), not a screenshot</sub>

## アプリ / Electron / デスクトップ

- [michaelshimeles/sketch](https://github.com/michaelshimeles/sketch) — **Uses rea: Yes**. Rust infinite-canvas design app, clean-room from Paper; README mentions REA (formerly paper-rs).<br><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="240" alt="michaelshimeles/sketch"><br><sub>Image: michaelshimeles/sketch ([source](https://github.com/michaelshimeles/sketch))</sub>
- [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) — **Uses rea: Yes**. Rust macOS recorder modelled on OBS Studio; README mentions REA.<br><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="240" alt="michaelshimeles/rec-rs"><br><sub>Image: michaelshimeles/rec-rs ([source](https://github.com/michaelshimeles/rec-rs))</sub>
- [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) — **Uses rea: Yes**. .NET 10 colour picker from a REA study of PowerToys. MIT.<br><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="240" alt="iammukeshm/hexgrab"><br><sub>GitHub repo card for [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab), not a screenshot</sub>
- [AdamLinCodes/AdamTerm](https://github.com/AdamLinCodes/AdamTerm) — **Uses rea: Yes**. Minimal macOS terminal after studying Ghostty with REA.<br><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="240" alt="AdamLinCodes/AdamTerm"><br><sub>Image: AdamLinCodes/AdamTerm ([source](https://github.com/AdamLinCodes/AdamTerm))</sub>
- [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) — **Uses rea: Yes**. Wispr Flow static teardown + 64-line local rebuild.<br><img src="https://opengraph.githubassets.com/1/az9713/wispr-flow-rea-teardown" width="240" alt="az9713/wispr-flow-rea-teardown"><br><sub>GitHub repo card for [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown), not a screenshot</sub>
- [cudanexus/vd-streamer-linux](https://github.com/cudanexus/vd-streamer-linux) — **Uses rea: Yes**. Unofficial Linux port of Virtual Desktop Streamer; Claude Code + REA.<br><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="240" alt="cudanexus/vd-streamer-linux"><br><sub>GitHub repo card for [cudanexus/vd-streamer-linux](https://github.com/cudanexus/vd-streamer-linux), not a screenshot</sub>

## プロトコル / ハードウェア

- [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) — **Uses rea: Unverified**. First-gen Siri Remote on Linux (Bluetooth protocol). MIT.<br><img src="https://opengraph.githubassets.com/1/a-funk/open-appleremote" width="240" alt="a-funk/open-appleremote"><br><sub>GitHub repo card for [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote), not a screenshot</sub>
- [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) — **Uses rea: No**. Linux Logitech G HUB replacement over HID++ 2.0. MIT.<br><img src="https://raw.githubusercontent.com/Slyvan25/OpenGHub/master/docs/screenshots/devices.png" width="240" alt="Slyvan25/OpenGHub"><br><sub>Image: Slyvan25/OpenGHub ([source](https://github.com/Slyvan25/OpenGHub))</sub>

## ファームウェア / ドライバ

- [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) — **Uses rea: Yes**. PreSonus AudioBox VSL kernel module; REA used for part of the vendor-library findings. GPL-3.0.<br><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="240" alt="grisuno/VSL-DSP"><br><sub>GitHub repo card for [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP), not a screenshot</sub>
- [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) — **Uses rea: No**. Firmware analysis/extraction tool. MIT.<br><img src="https://raw.githubusercontent.com/ReFirmLabs/binwalk/master/images/output.png" width="240" alt="ReFirmLabs/binwalk"><br><sub>Image: ReFirmLabs/binwalk ([source](https://github.com/ReFirmLabs/binwalk))</sub>

## セキュリティ / 評価

- [NullLabTests/OpenBSD_netcat_REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) — **Uses rea: Yes**. Static analysis of netcat-openbsd with REA + Ghidra. MIT.<br><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="240" alt="NullLabTests/OpenBSD_netcat_REA"><br><sub>Image: NullLabTests/OpenBSD_netcat_REA ([source](https://github.com/NullLabTests/OpenBSD_netcat_REA))</sub>
- [REA discussion #2254](https://github.com/morluto/rea/discussions/2254) — **Uses rea: Yes**. Stripped bzip2 analysed and checked against an unstripped build.<br><sub>No image.</sub>

## REA 関連ツール

- [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) — **Uses rea: Yes**. Agent skill for evidence-based reconstruction with REA. MIT.<br><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="240" alt="ShadowSwaps/REA-Reconstruction-Companion"><br><sub>GitHub repo card for [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion), not a screenshot</sub>
- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) — **Uses rea: No**. Decompiler REA can drive. Apache-2.0.<br><img src="https://opengraph.githubassets.com/1/NationalSecurityAgency/ghidra" width="240" alt="NationalSecurityAgency/ghidra"><br><sub>GitHub repo card for [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra), not a screenshot</sub>
- [skylot/jadx](https://github.com/skylot/jadx) — **Uses rea: No**. Android DEX decompiler REA can drive. Apache-2.0.<br><img src="https://user-images.githubusercontent.com/118523/142730720-839f017e-38db-423e-b53f-39f5f0a0316f.png" width="240" alt="skylot/jadx"><br><sub>Image: skylot/jadx ([source](https://github.com/skylot/jadx))</sub>

---

貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md)、ライセンスは [CC0-1.0](LICENSE)。
