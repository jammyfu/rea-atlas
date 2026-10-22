[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# REA Atlas（REA 图谱）

收录用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）做逆向的项目，以及同类反编译/重实现项目。每条标注 **Uses rea: Yes / No / Unverified**，只有公开证据（README、官方 showcase 或仓库文档）才标 Yes。

> 非官方，与 morluto/rea 无关联。不收录、不托管破解、盗版、ROM 或版权素材。为保证各语言列表一致，条目简介统一保留英文。

<img src="https://raw.githubusercontent.com/morluto/rea/main/docs/assets/rea-showcases.png" alt="REA showcases" width="720" />

<sub>图片：REA showcase 插图，来自 [morluto/rea](https://github.com/morluto/rea/blob/main/docs/assets/rea-showcases.png)（MIT），直接引用，未转存。</sub>

## REA 官方 Showcase

- [DX-Ball: sound-pan function](https://rea.tools/showcase/dx-ball/) — **Uses rea: Yes**. Official showcase; C reconstruction matching 3,205 x86 cases.
- [Notion: Electron clipboard bridge](https://rea.tools/showcase/notion/) — **Uses rea: Yes**. Official showcase; renderer → preload → IPC trace.
- [TH04: PC-98 bullet-ring maths](https://rea.tools/showcase/th04/) — **Uses rea: Yes**. Official showcase; 16-bit angle helpers.
- [Aegis: TOTP code generation](https://rea.tools/showcase/aegis/) — **Uses rea: Yes**. Official showcase; Android app.
- [CTF: flag checker](https://rea.tools/showcase/ctf/) — **Uses rea: Yes**. Official showcase; DownUnderCTF 2023 challenge.

## 游戏

### PC / DOS / PC-98

#### 反编译 / 重编译

- [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) — **Uses rea: Yes**. DX-Ball 1.07 reconstruction; README states REA. MIT.
- [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) — **Uses rea: Yes**. Touhou 4 (PC-98) source reconstruction; REA via official showcase. MIT.
- [N0zoM1z0/th08](https://github.com/N0zoM1z0/th08) — **Uses rea: Unverified**. Touhou 8 reconstruction (agent + IDA/Ghidra); README does not mention REA. MIT.
- [N0zoM1z0/th10](https://github.com/N0zoM1z0/th10) — **Uses rea: Unverified**. Touhou 10 reconstruction; README does not mention REA. MIT.

#### 重制 / 移植

- [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) — **Uses rea: Yes**. Gemtree Desktop Games (2000) ported to macOS/browser; README cites REA + Ghidra.
- [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) — **Uses rea: Yes**. Ski or Die (DOS) minigame rebuilt in Rust + SDL2; uses your own assets.
- [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) — **Uses rea: Yes**. Clean-room Refractor 2 engine; REA documented in CLAUDE.md / tools/rea.sh. Needs your own copy.
- [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) — **Uses rea: Yes**. GunZ: The Duel in Rust + Bevy; README mentions REA. Apache-2.0.
- [a-barzanti/ai-rebuilds](https://github.com/a-barzanti/ai-rebuilds) — **Uses rea: Yes**. Abandoned games rebuilt for the web from REA-written specs; no original files committed.
- [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) — **Uses rea: No**. RollerCoaster Tycoon 2 re-implementation (pre-REA). GPL-3.0.
- [OpenMW/openmw](https://github.com/OpenMW/openmw) — **Uses rea: No**. Morrowind engine re-implementation. GPL-3.0.

### 任天堂 64

#### 反编译 / 重编译

- [zeldaret/oot](https://github.com/zeldaret/oot) — **Uses rea: No**. Ocarina of Time decompilation; ROM not included.
- [n64decomp/sm64](https://github.com/n64decomp/sm64) — **Uses rea: No**. Super Mario 64 decompilation; ROM not included. CC0-1.0.

#### 重制 / 移植

- [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) — **Uses rea: No**. Ship of Harkinian PC port of OoT; requires your own ROM.

#### 资源提取与工具

- [ethteck/splat](https://github.com/ethteck/splat) — **Uses rea: No**. Binary splitting tool for N64/PSX decomp projects. MIT.
- [NEstelami/ZAPD](https://github.com/NEstelami/ZAPD) — **Uses rea: No**. Zelda asset processor used by decomp projects. MIT.

### MD / Genesis

#### 反编译 / 重编译

- [sonicretro/s1disasm](https://github.com/sonicretro/s1disasm) — **Uses rea: No**. Sonic the Hedgehog (Mega Drive) disassembly.
- [sonicretro/s2disasm](https://github.com/sonicretro/s2disasm) — **Uses rea: No**. Sonic 2 (Mega Drive) disassembly.

### SFC / SNES

#### 反编译 / 重编译

- [snesrev/zelda3](https://github.com/snesrev/zelda3) — **Uses rea: No**. A Link to the Past C reimplementation; asset extraction from your own ROM.
- [snesrev/sm](https://github.com/snesrev/sm) — **Uses rea: No**. Super Metroid C reimplementation; needs your own ROM.

### NES / FC

_暂无已验证条目，欢迎补充。_

### GBA

#### 反编译 / 重编译

- [pret/pokeemerald](https://github.com/pret/pokeemerald) — **Uses rea: No**. Pokémon Emerald decompilation.
- [pret/pokefirered](https://github.com/pret/pokefirered) — **Uses rea: No**. Pokémon FireRed/LeafGreen decompilation.
- [zeldaret/tmc](https://github.com/zeldaret/tmc) — **Uses rea: No**. The Minish Cap decompilation.

### Game Boy

#### 反编译 / 重编译

- [pret/pokered](https://github.com/pret/pokered) — **Uses rea: No**. Pokémon Red/Blue disassembly.
- [pret/pokegold](https://github.com/pret/pokegold) — **Uses rea: No**. Pokémon Gold/Silver disassembly.

### PlayStation

#### 反编译 / 重编译

- [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp) — **Uses rea: No**. Castlevania: Symphony of the Night decompilation. AGPL-3.0.

## 应用 / Electron / 桌面

- [michaelshimeles/sketch](https://github.com/michaelshimeles/sketch) — **Uses rea: Yes**. Rust infinite-canvas design app, clean-room from Paper; README mentions REA (formerly paper-rs).
- [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) — **Uses rea: Yes**. Rust macOS recorder modelled on OBS Studio; README mentions REA.
- [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) — **Uses rea: Yes**. .NET 10 colour picker from a REA study of PowerToys. MIT.
- [AdamLinCodes/AdamTerm](https://github.com/AdamLinCodes/AdamTerm) — **Uses rea: Yes**. Minimal macOS terminal after studying Ghostty with REA.
- [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) — **Uses rea: Yes**. Wispr Flow static teardown + 64-line local rebuild.
- [cudanexus/vd-streamer-linux](https://github.com/cudanexus/vd-streamer-linux) — **Uses rea: Yes**. Unofficial Linux port of Virtual Desktop Streamer; Claude Code + REA.

## 协议 / 硬件

- [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) — **Uses rea: Unverified**. First-gen Siri Remote on Linux (Bluetooth protocol). MIT.
- [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) — **Uses rea: No**. Linux Logitech G HUB replacement over HID++ 2.0. MIT.

## 固件 / 驱动

- [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) — **Uses rea: Yes**. PreSonus AudioBox VSL kernel module; REA used for part of the vendor-library findings. GPL-3.0.
- [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) — **Uses rea: No**. Firmware analysis/extraction tool. MIT.

## 安全 / 评测

- [NullLabTests/OpenBSD_netcat_REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) — **Uses rea: Yes**. Static analysis of netcat-openbsd with REA + Ghidra. MIT.
- [REA discussion #2254](https://github.com/morluto/rea/discussions/2254) — **Uses rea: Yes**. Stripped bzip2 analysed and checked against an unstripped build.

## REA 周边工具

- [ShadowSwaps/REA-Reconstruction-Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) — **Uses rea: Yes**. Agent skill for evidence-based reconstruction with REA. MIT.
- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) — **Uses rea: No**. Decompiler REA can drive. Apache-2.0.
- [skylot/jadx](https://github.com/skylot/jadx) — **Uses rea: No**. Android DEX decompiler REA can drive. Apache-2.0.

---

贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可：[CC0-1.0](LICENSE)。
