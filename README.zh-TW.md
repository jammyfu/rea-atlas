[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# REA Atlas：逆向工程專案地圖（含 rea 標記）

開源逆向工程專案地圖：遊戲反編譯、靜態重編譯、重新實作、資源擷取工具、通用逆向工具，以及應用程式/協定/韌體逆向。每條標註是否使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）：**Uses rea: Yes / No / Unverified**，只有在具備公開證據（README、官方 showcase 或儲存庫文件）才標 Yes。

> 非官方，與 morluto/rea 無關聯。

## 目錄

- [已使用 REA 的專案（證據標記子集）](#已使用-rea-的專案證據標記子集)
- [遊戲](#遊戲)
  - [NES / FC](#nes--fc)
  - [SFC / SNES](#sfc--snes)
  - [MD / Genesis](#md--genesis)
  - [SEGA Saturn](#sega-saturn)
  - [Game Boy](#game-boy)
  - [GBA](#gba)
  - [Nintendo 64](#nintendo-64)
  - [GameCube](#gamecube)
  - [Wii](#wii)
  - [NDS](#nds)
  - [3DS](#3ds)
  - [PS1](#ps1)
  - [PS2](#ps2)
  - [Xbox / Xbox 360](#xbox--xbox-360)
  - [PC / DOS / PC-98](#pc--dos--pc-98)
- [應用程式 / Electron / 桌面](#應用程式--electron--桌面)
- [協定 / 硬體](#協定--硬體)
- [韌體 / 驅動](#韌體--驅動)
- [資安 / 評測](#資安--評測)
- [逆向工具](#逆向工具)
- [REA 官方 Showcase](#rea-官方-showcase)

## 已使用 REA 的專案（證據標記子集）

_可選過濾：以下有公開證據表明使用了 REA。地圖裡大部分專案是普通逆向工作，並不要求用 REA。_

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://rea.tools/showcase/dx-ball/"><img src="images/showcase-dx-ball.png" width="160" alt="DX-Ball: sound-pan function"></a></td><td><a href="https://rea.tools/showcase/dx-ball/"><b>DX-Ball: sound-pan function</b></a></td><td>看 REA 把 DX-Ball 的一個音效函式還原成逐位元組一致的 C</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/notion/"><img src="images/showcase-notion.png" width="160" alt="Notion: Electron clipboard bridge"></a></td><td><a href="https://rea.tools/showcase/notion/"><b>Notion: Electron clipboard bridge</b></a></td><td>跟著一次 Notion 複製操作，從頁面一路追進 IPC 和主行程</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/th04/"><img src="images/showcase-th04.png" width="160" alt="TH04: PC-98 bullet-ring maths"></a></td><td><a href="https://rea.tools/showcase/th04/"><b>TH04: PC-98 bullet-ring maths</b></a></td><td>從 16 位元 DOS 程式碼裡找回東方幻想鄉的彈幕角度演算法</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/aegis/"><img src="images/showcase-aegis.png" width="160" alt="Aegis: TOTP code generation"></a></td><td><a href="https://rea.tools/showcase/aegis/"><b>Aegis: TOTP code generation</b></a></td><td>看清 Aegis Android App 究竟如何產生兩步驟驗證碼</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/ctf/"><img src="images/showcase-ctf.png" width="160" alt="CTF: flag checker"></a></td><td><a href="https://rea.tools/showcase/ctf/"><b>CTF: flag checker</b></a></td><td>一步步解開 DownUnderCTF 2023 的逆向題</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/dx-ball"><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="160" alt="N0zoM1z0/dx-ball"></a></td><td><a href="https://github.com/N0zoM1z0/dx-ball"><b>dx-ball</b></a><br><sub>N0zoM1z0</sub></td><td>用 C/C++ 重建 DX-Ball 1.07，並對照原版 x86 測試</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th04"><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th04"></a></td><td><a href="https://github.com/N0zoM1z0/th04"><b>th04</b></a><br><sub>N0zoM1z0</sub></td><td>東方幻想鄉（PC-98）的可讀原始碼，並以原版編譯器驗證</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="160" alt="ucodia/desktop-games-nostalgia"></a></td><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><b>desktop-games-nostalgia</b></a><br><sub>ucodia</sub></td><td>再砸一次桌面：Gemtree 2000 年的小玩具登上 macOS 和網頁</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="160" alt="tuunanet/rea-ski-or-die-reconstruction"></a></td><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><b>rea-ski-or-die-reconstruction</b></a><br><sub>tuunanet</sub></td><td>Ski or Die 的雪球大戰，以 Rust + SDL2 重製（素材需自備）</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="160" alt="Moxnatiy/OpenBattlefield2"></a></td><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><b>OpenBattlefield2</b></a><br><sub>Moxnatiy</sub></td><td>戰地風雲 2 引擎的 C++20 淨室重寫（讀取你自己的遊戲檔案）</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenRsG/GunZRs"><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="160" alt="OpenRsG/GunZRs"></a></td><td><a href="https://github.com/OpenRsG/GunZRs"><b>GunZRs</b></a><br><sub>OpenRsG</sub></td><td>GunZ: The Duel 以 Rust + Bevy 重生</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/a-barzanti/ai-rebuilds"><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="160" alt="a-barzanti/ai-rebuilds"></a></td><td><a href="https://github.com/a-barzanti/ai-rebuilds"><b>ai-rebuilds</b></a><br><sub>a-barzanti</sub></td><td>被遺棄的老遊戲重回瀏覽器，不含任何原版檔案</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/sketch"><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="160" alt="michaelshimeles/sketch"></a></td><td><a href="https://github.com/michaelshimeles/sketch"><b>sketch</b></a><br><sub>michaelshimeles</sub></td><td>以 Rust 寫成的無限設計畫布，研究 Paper 後重建</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/rec-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="160" alt="michaelshimeles/rec-rs"></a></td><td><a href="https://github.com/michaelshimeles/rec-rs"><b>rec-rs</b></a><br><sub>michaelshimeles</sub></td><td>以 Rust 寫成的 macOS 快速螢幕錄影工具，參考 OBS 設計</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/iammukeshm/hexgrab"><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="160" alt="iammukeshm/hexgrab"></a></td><td><a href="https://github.com/iammukeshm/hexgrab"><b>hexgrab</b></a><br><sub>iammukeshm</sub></td><td>迷你 Windows 取色工具，從 PowerToys 二進位檔研究而來</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/AdamLinCodes/AdamTerm"><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="160" alt="AdamLinCodes/AdamTerm"></a></td><td><a href="https://github.com/AdamLinCodes/AdamTerm"><b>AdamTerm</b></a><br><sub>AdamLinCodes</sub></td><td>研究 Ghostty 後做出的極簡 macOS 終端機</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><img src="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg" width="160" alt="az9713/wispr-flow-rea-teardown"></a></td><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><b>wispr-flow-rea-teardown</b></a><br><sub>az9713</sub></td><td>拆解 Wispr Flow 的語音管線，附 64 行重寫版</td><td>✅ 是</td><td><sub><a href="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg">影片封面</a></sub></td></tr>
<tr><td><a href="https://github.com/cudanexus/vd-streamer-linux"><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="160" alt="cudanexus/vd-streamer-linux"></a></td><td><a href="https://github.com/cudanexus/vd-streamer-linux"><b>vd-streamer-linux</b></a><br><sub>cudanexus</sub></td><td>把 Linux 桌面串流到 Quest、Pico 頭戴裝置</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/grisuno/VSL-DSP"><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="160" alt="grisuno/VSL-DSP"></a></td><td><a href="https://github.com/grisuno/VSL-DSP"><b>VSL-DSP</b></a><br><sub>grisuno</sub></td><td>PreSonus AudioBox VSL 音效卡的 Linux 核心模組</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="160" alt="NullLabTests/OpenBSD_netcat_REA"></a></td><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><b>OpenBSD_netcat_REA</b></a><br><sub>NullLabTests</sub></td><td>以 REA + Ghidra 靜態分析 netcat-openbsd</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/morluto/rea/discussions/2254"><img src="images/rea-discussion-2254.png" width="160" alt="REA discussion #2254"></a></td><td><a href="https://github.com/morluto/rea/discussions/2254"><b>REA discussion #2254</b></a></td><td>分析去除符號的 bzip2，並與實際建置結果比對驗證</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="160" alt="ShadowSwaps/REA-Reconstruction-Companion"></a></td><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><b>REA-Reconstruction-Companion</b></a><br><sub>ShadowSwaps</sub></td><td>讓重建過程隨時有證據可查的 AI 代理技能</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><img src="https://opengraph.githubassets.com/1/KarlssonChristoffer/DiskLens" width="160" alt="KarlssonChristoffer/DiskLens"></a></td><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><b>DiskLens</b></a><br><sub>KarlssonChristoffer</sub></td><td>像 WinDirStat 一樣看清 Windows 11 磁碟被什麼佔滿</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/lxistired/ledger-reborn"><img src="https://raw.githubusercontent.com/lxistired/ledger-reborn/main/docs/screenshots/accounting.png" width="160" alt="lxistired/ledger-reborn"></a></td><td><a href="https://github.com/lxistired/ledger-reborn"><b>ledger-reborn</b></a><br><sub>lxistired</sub></td><td>本機優先的記帳 App，參考 QuickBooks Mac 版</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/terminal-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/terminal-rs/master/docs/img/overview.png" width="160" alt="michaelshimeles/terminal-rs"></a></td><td><a href="https://github.com/michaelshimeles/terminal-rs"><b>terminal-rs</b></a><br><sub>michaelshimeles</sub></td><td>以 Rust 寫成的彭博風格交易終端機</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/sickpyramid/ReaFuse"><img src="https://opengraph.githubassets.com/1/sickpyramid/ReaFuse" width="160" alt="sickpyramid/ReaFuse"></a></td><td><a href="https://github.com/sickpyramid/ReaFuse"><b>ReaFuse</b></a><br><sub>sickpyramid</sub></td><td>藉助 REA 把兩個 JS/TS 專案合併成一個</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/0xshlomil/ida-free-mcp"><img src="https://opengraph.githubassets.com/1/0xshlomil/ida-free-mcp" width="160" alt="0xshlomil/ida-free-mcp"></a></td><td><a href="https://github.com/0xshlomil/ida-free-mcp"><b>ida-free-mcp</b></a><br><sub>0xshlomil</sub></td><td>透過 MCP 讓 AI 代理使用免費版 IDA</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/Nowng/rea-mcp"><img src="https://opengraph.githubassets.com/1/Nowng/rea-mcp" width="160" alt="Nowng/rea-mcp"></a></td><td><a href="https://github.com/Nowng/rea-mcp"><b>rea-mcp</b></a><br><sub>Nowng</sub></td><td>在 LM Studio 裡搭配本機模型使用 REA</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/alexmi256/rea-agent-docker"><img src="https://opengraph.githubassets.com/1/alexmi256/rea-agent-docker" width="160" alt="alexmi256/rea-agent-docker"></a></td><td><a href="https://github.com/alexmi256/rea-agent-docker"><b>rea-agent-docker</b></a><br><sub>alexmi256</sub></td><td>REA 的 Docker 映像檔，含 Ghidra/Hopper/IDA 版本</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/cognixws/picode-rea"><img src="https://opengraph.githubassets.com/1/cognixws/picode-rea" width="160" alt="cognixws/picode-rea"></a></td><td><a href="https://github.com/cognixws/picode-rea"><b>picode-rea</b></a><br><sub>cognixws</sub></td><td>在 PiCode 裡使用 REA 的靜態分析工具</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/czcdr/dsh-plugin-rea"><img src="https://raw.githubusercontent.com/czcdr/dsh-plugin-rea/main/assets/screenshot-1.png" width="160" alt="czcdr/dsh-plugin-rea"></a></td><td><a href="https://github.com/czcdr/dsh-plugin-rea"><b>dsh-plugin-rea</b></a><br><sub>czcdr</sub></td><td>在 DeepSeek Harness 裡使用 REA，自動裝好 Ghidra</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><img src="https://opengraph.githubassets.com/1/sheilacraig/dsh-rea-mcp" width="160" alt="sheilacraig/dsh-rea-mcp"></a></td><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><b>dsh-rea-mcp</b></a><br><sub>sheilacraig</sub></td><td>只靠設定就把 REA 接進 DeepSeek Harness</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><img src="https://opengraph.githubassets.com/1/ya123-4/rea-dsh-plugin" width="160" alt="ya123-4/rea-dsh-plugin"></a></td><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><b>rea-dsh-plugin</b></a><br><sub>ya123-4</sub></td><td>在 DeepSeek Harness 中註冊 REA 的 MCP 工具</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/zhaofeng130/dsh-rea"><img src="https://opengraph.githubassets.com/1/zhaofeng130/dsh-rea" width="160" alt="zhaofeng130/dsh-rea"></a></td><td><a href="https://github.com/zhaofeng130/dsh-rea"><b>dsh-rea</b></a><br><sub>zhaofeng130</sub></td><td>給 DeepSeek Harness 加上 REA 技能和工具</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-casebook"><img src="https://raw.githubusercontent.com/pablodiazjorge/rea-casebook/main/media/session-dark.png" width="160" alt="pablodiazjorge/rea-casebook"></a></td><td><a href="https://github.com/pablodiazjorge/rea-casebook"><b>rea-casebook</b></a><br><sub>pablodiazjorge</sub></td><td>讓 Claude Code 的每項結論都引用真實的 REA 證據</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/jinshi666888/rea-playbook"><img src="https://raw.githubusercontent.com/jinshi666888/rea-playbook/main/docs/assets/demo.gif" width="160" alt="jinshi666888/rea-playbook"></a></td><td><a href="https://github.com/jinshi666888/rea-playbook"><b>rea-playbook</b></a><br><sub>jinshi666888</sub></td><td>附迷你 Electron 靶機的 REA 實作練習</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><img src="https://opengraph.githubassets.com/1/UnknownHacker1/rea-groundtruth" width="160" alt="UnknownHacker1/rea-groundtruth"></a></td><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><b>rea-groundtruth</b></a><br><sub>UnknownHacker1</sub></td><td>以真實原始碼檢驗 REA 的分析報告</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/az9713/REA-demo"><img src="https://opengraph.githubassets.com/1/az9713/REA-demo" width="160" alt="az9713/REA-demo"></a></td><td><a href="https://github.com/az9713/REA-demo"><b>REA-demo</b></a><br><sub>az9713</sub></td><td>讓 REA 分析它自己，附可證偽的預測</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-lab"><img src="https://opengraph.githubassets.com/1/pablodiazjorge/rea-lab" width="160" alt="pablodiazjorge/rea-lab"></a></td><td><a href="https://github.com/pablodiazjorge/rea-lab"><b>rea-lab</b></a><br><sub>pablodiazjorge</sub></td><td>Windows + Ghidra 練習題與預先登記的 REA 評測</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/EndLess728/MiTV-Remote"><b>MiTV-Remote</b></a><br><sub>EndLess728</sub></td><td>在 Mac、Android、iPhone 上用 Wi-Fi 遙控小米電視</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/B-Howell/soundconnect-desktop"><b>soundconnect-desktop</b></a><br><sub>B-Howell</sub></td><td>在 Windows 桌面上控制 Sony 藍牙耳機</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Xiangyu-CAS/rea-capcut"><b>rea-capcut</b></a><br><sub>Xiangyu-CAS</sub></td><td>用 REA 研究剪映後重做的開源離線剪輯軟體</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/chilliesdev/fmseasonhub-re"><b>fmseasonhub-re</b></a><br><sub>chilliesdev</sub></td><td>用 REA 拆解 FM Season Hub 應用程式的分析筆記</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/rodneypantonial/sims3-modernization"><b>sims3-modernization</b></a><br><sub>rodneypantonial</sub></td><td>讓模擬市民 3 在新電腦上少卡頓、少當機</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/nicolvus/a6000-fw-decomp"><b>a6000-fw-decomp</b></a><br><sub>nicolvus</sub></td><td>用 REA 和 Ghidra 拆 Sony A6000 相機韌體</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/tanepiper/game-frame"><b>game-frame</b></a><br><sub>tanepiper</sub></td><td>讓 AI agent 從發行檔案逆向遊戲的框架</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Caho1/open-claude-ui"><b>open-claude-ui</b></a><br><sub>Caho1</sub></td><td>用 REA 深度拆解並高保真還原 Claude 桌面端 UI 元件與互動物理</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/glauberlima/open-scrantic"><b>open-scrantic</b></a><br><sub>glauberlima</sub></td><td>用 REA 逆向並重寫的 1992 年 Johnny Castaway 螢幕保護程式（Rust）</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/aicodeking/leanrea"><b>leanrea</b></a><br><sub>aicodeking</sub></td><td>輕量 skill，替代 REA 的 MCP 層，讓 agent 直接呼叫 CLI 工具</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/cranebeaker/coop-anything"><b>coop-anything</b></a><br><sub>cranebeaker</sub></td><td>用 REA 調查入口，為單機遊戲添加合作模式的 MCP 伺服器與技能</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/MiaAI-Lab/sparkDash"><b>sparkDash</b></a><br><sub>MiaAI-Lab</sub></td><td>整合 REA 長時分析任務、按需載入結果的多裝置儀表板</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/carlhako/keen-clone"><b>keen-clone</b></a><br><sub>carlhako</sub></td><td>用 REA + Ghidra 函式級還原的 Commander Keen 1 原生 Linux/SDL2 重實現</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/NathanKanaeru/samp-client-re"><b>samp-client-re</b></a><br><sub>NathanKanaeru</sub></td><td>用 REA/Ghidra 恢復架構的 SA-MP 0.3.DL-R1 clean-room 客戶端重實現</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Stijnus/dsh-rev-eng"><b>dsh-rev-eng</b></a><br><sub>Stijnus</sub></td><td>將 REA 技能與可選 MCP 打包為 DSH 插件，用於逆向工程與 Mac 應用建構。</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/CurLeaf/dsh-command-rea"><b>dsh-command-rea</b></a><br><sub>CurLeaf</sub></td><td>DSH /rea 斜線命令，將逆向分析請求路由到 REA 技能與 MCP 工具。</td><td>✅ 是</td><td><sub>—</sub></td></tr>
</table>

## 遊戲

### NES / FC

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/aldonunez/zelda1-disassembly"><img src="https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png" width="160" alt="aldonunez/zelda1-disassembly"></a></td><td><a href="https://github.com/aldonunez/zelda1-disassembly"><b>zelda1-disassembly</b></a><br><sub>aldonunez</sub></td><td>初代薩爾達傳說（FC）完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 資源擷取與工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/SourMesen/Mesen2"><img src="https://opengraph.githubassets.com/1/SourMesen/Mesen2" width="160" alt="SourMesen/Mesen2"></a></td><td><a href="https://github.com/SourMesen/Mesen2"><b>Mesen2</b></a><br><sub>SourMesen</sub></td><td>內建強大除錯工具的多機種模擬器</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
</table>

### SFC / SNES

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/snesrev/zelda3"><img src="https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg" width="160" alt="snesrev/zelda3"></a></td><td><a href="https://github.com/snesrev/zelda3"><b>zelda3</b></a><br><sub>snesrev</sub></td><td>以 C 重寫的薩爾達傳說 眾神的三角力量，支援寬螢幕（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/snesrev/sm"><img src="https://upload.wikimedia.org/wikipedia/en/e/e4/Smetroidbox.jpg" width="160" alt="snesrev/sm"></a></td><td><a href="https://github.com/snesrev/sm"><b>sm</b></a><br><sub>snesrev</sub></td><td>以 C 重寫的超級銀河戰士（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/e/e4/Smetroidbox.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 重製 / 移植

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/snesrev/smw"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png" width="160" alt="snesrev/smw"></a></td><td><a href="https://github.com/snesrev/smw"><b>smw</b></a><br><sub>snesrev</sub></td><td>以 C 重寫的超級瑪利歐世界（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png">維基百科（© 版權方）</a></sub></td></tr>
</table>

### MD / Genesis

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/sonicretro/s1disasm"><img src="https://upload.wikimedia.org/wikipedia/en/b/ba/Sonic_the_Hedgehog_1_Genesis_box_art.jpg" width="160" alt="sonicretro/s1disasm"></a></td><td><a href="https://github.com/sonicretro/s1disasm"><b>s1disasm</b></a><br><sub>sonicretro</sub></td><td>音速小子（MD）完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/b/ba/Sonic_the_Hedgehog_1_Genesis_box_art.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/sonicretro/s2disasm"><img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Sonic_2_US_Cover.jpg" width="160" alt="sonicretro/s2disasm"></a></td><td><a href="https://github.com/sonicretro/s2disasm"><b>s2disasm</b></a><br><sub>sonicretro</sub></td><td>音速小子 2（MD）完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0c/Sonic_2_US_Cover.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/sonicretro/skdisasm"><img src="https://upload.wikimedia.org/wikipedia/en/d/d3/Sonic_%26_Knuckles_cover.jpg" width="160" alt="sonicretro/skdisasm"></a></td><td><a href="https://github.com/sonicretro/skdisasm"><b>skdisasm</b></a><br><sub>sonicretro</sub></td><td>Sonic 3 &amp; Knuckles 完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/d/d3/Sonic_%26_Knuckles_cover.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 重製 / 移植

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/RSDKModding/RSDKv5-Decompilation"><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv5-Decompilation/master/header.png?raw=true" width="160" alt="RSDKModding/RSDKv5-Decompilation"></a></td><td><a href="https://github.com/RSDKModding/RSDKv5-Decompilation"><b>RSDKv5-Decompilation</b></a><br><sub>RSDKModding</sub></td><td>Sonic Mania 的引擎反編譯（讀取你自己的資料檔）</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/RSDKModding/RSDKv4-Decompilation"><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv4-Decompilation/main/header.png?raw=true" width="160" alt="RSDKModding/RSDKv4-Decompilation"></a></td><td><a href="https://github.com/RSDKModding/RSDKv4-Decompilation"><b>RSDKv4-Decompilation</b></a><br><sub>RSDKModding</sub></td><td>音速小子 1、2（2013）引擎的反編譯</td><td>否</td><td><sub>專案 README</sub></td></tr>
</table>

### SEGA Saturn

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/yaz0r/Azel"><img src="https://github.com/user-attachments/assets/71f6a246-24cc-4d64-9673-53b9e4c3e4df" width="160" alt="yaz0r/Azel"></a></td><td><a href="https://github.com/yaz0r/Azel"><b>Azel</b></a><br><sub>yaz0r</sub></td><td>經逆向後重新實作的 Panzer Dragoon Saga</td><td>否</td><td><sub>專案 README</sub></td></tr>
</table>

### Game Boy

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/pret/pokered"><img src="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp" width="160" alt="pret/pokered"></a></td><td><a href="https://github.com/pret/pokered"><b>pokered</b></a><br><sub>pret</sub></td><td>寶可夢 紅/藍完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokegold"><img src="https://upload.wikimedia.org/wikipedia/en/4/4c/Pok%C3%A9mon_box_art_-_Gold_Version.png" width="160" alt="pret/pokegold"></a></td><td><a href="https://github.com/pret/pokegold"><b>pokegold</b></a><br><sub>pret</sub></td><td>寶可夢 金/銀完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/4/4c/Pok%C3%A9mon_box_art_-_Gold_Version.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeyellow"><img src="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp" width="160" alt="pret/pokeyellow"></a></td><td><a href="https://github.com/pret/pokeyellow"><b>pokeyellow</b></a><br><sub>pret</sub></td><td>寶可夢 皮卡丘完整反組譯</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokecrystal"><img src="https://github.com/user-attachments/assets/c39cb860-bb9c-4204-9184-b2761ead0a74" width="160" alt="pret/pokecrystal"></a></td><td><a href="https://github.com/pret/pokecrystal"><b>pokecrystal</b></a><br><sub>pret</sub></td><td>寶可夢 水晶完整反組譯</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/zladx/LADX-Disassembly"><img src="https://raw.githubusercontent.com/zladx/LADX-Disassembly/main/docs/entities.png" width="160" alt="zladx/LADX-Disassembly"></a></td><td><a href="https://github.com/zladx/LADX-Disassembly"><b>LADX-Disassembly</b></a><br><sub>zladx</sub></td><td>薩爾達傳說 織夢島 DX 完整反組譯</td><td>否</td><td><sub>專案 README</sub></td></tr>
</table>

### GBA

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/pret/pokeemerald"><img src="https://user-images.githubusercontent.com/35422415/226195894-bd8307ea-f6be-46cc-85ec-dd28b4f2d144.gif" width="160" alt="pret/pokeemerald"></a></td><td><a href="https://github.com/pret/pokeemerald"><b>pokeemerald</b></a><br><sub>pret</sub></td><td>寶可夢 綠寶石的 C 原始碼，無數改版的起點</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/pret/pokefirered"><img src="https://upload.wikimedia.org/wikipedia/en/a/a7/Pokemon_LeafGreen_box.jpg" width="160" alt="pret/pokefirered"></a></td><td><a href="https://github.com/pret/pokefirered"><b>pokefirered</b></a><br><sub>pret</sub></td><td>寶可夢 火紅/葉綠的 C 原始碼</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a7/Pokemon_LeafGreen_box.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tmc"><img src="https://upload.wikimedia.org/wikipedia/en/0/0a/TLOZ-_Minish_Cap_NA_Box_art.png" width="160" alt="zeldaret/tmc"></a></td><td><a href="https://github.com/zeldaret/tmc"><b>tmc</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 縮小帽，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0a/TLOZ-_Minish_Cap_NA_Box_art.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeruby"><img src="https://upload.wikimedia.org/wikipedia/en/b/be/PokemonRubySapphireBox.jpg" width="160" alt="pret/pokeruby"></a></td><td><a href="https://github.com/pret/pokeruby"><b>pokeruby</b></a><br><sub>pret</sub></td><td>寶可夢 紅寶石/藍寶石的 C 原始碼</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/b/be/PokemonRubySapphireBox.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/jiangzhengwenjz/katam"><img src="https://upload.wikimedia.org/wikipedia/en/0/0b/Kirby_%26_the_Amazing_Mirror.jpg" width="160" alt="jiangzhengwenjz/katam"></a></td><td><a href="https://github.com/jiangzhengwenjz/katam"><b>katam</b></a><br><sub>jiangzhengwenjz</sub></td><td>星之卡比 鏡之大迷宮，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0b/Kirby_%26_the_Amazing_Mirror.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pmd-red"><img src="https://upload.wikimedia.org/wikipedia/en/d/d3/Pok%C3%A9mon_Mystery_Dungeon_Blue_and_Red_Rescue_Team_cover_arts.jpg" width="160" alt="pret/pmd-red"></a></td><td><a href="https://github.com/pret/pmd-red"><b>pmd-red</b></a><br><sub>pret</sub></td><td>寶可夢不可思議的迷宮 紅之救助隊，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/d/d3/Pok%C3%A9mon_Mystery_Dungeon_Blue_and_Red_Rescue_Team_cover_arts.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

### Nintendo 64

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/zeldaret/oot"><img src="https://github.com/user-attachments/assets/70b4a529-9a5e-4b9c-ac45-48f9f2183eed" width="160" alt="zeldaret/oot"></a></td><td><a href="https://github.com/zeldaret/oot"><b>oot</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 時之笛完整反編譯為 C（不含 ROM）</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/sm64"><img src="https://upload.wikimedia.org/wikipedia/en/e/e9/Super_Mario_64.png" width="160" alt="n64decomp/sm64"></a></td><td><a href="https://github.com/n64decomp/sm64"><b>sm64</b></a><br><sub>n64decomp</sub></td><td>可建置的超級瑪利歐 64 C 原始碼（不含 ROM）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/e/e9/Super_Mario_64.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/HarbourMasters/Starship"><img src="https://upload.wikimedia.org/wikipedia/en/6/63/StarFox64_N64_Game_Box.jpg" width="160" alt="HarbourMasters/Starship"></a></td><td><a href="https://github.com/HarbourMasters/Starship"><b>Starship</b></a><br><sub>HarbourMasters</sub></td><td>在 PC 上原生執行星際火狐 64（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/63/StarFox64_N64_Game_Box.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/mk64"><img src="https://upload.wikimedia.org/wikipedia/en/a/a1/Mario_Kart_64.jpg" width="160" alt="n64decomp/mk64"></a></td><td><a href="https://github.com/n64decomp/mk64"><b>mk64</b></a><br><sub>n64decomp</sub></td><td>瑪利歐賽車 64，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a1/Mario_Kart_64.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/mm"><img src="https://user-images.githubusercontent.com/12245827/191111633-e72abfd3-b53c-4d13-82d1-44e6718f1fb0.png" width="160" alt="zeldaret/mm"></a></td><td><a href="https://github.com/zeldaret/mm"><b>mm</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 穆修拉的假面，反編譯為 C</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/pmret/papermario"><img src="https://upload.wikimedia.org/wikipedia/en/6/61/Papermario.jpg" width="160" alt="pmret/papermario"></a></td><td><a href="https://github.com/pmret/papermario"><b>papermario</b></a><br><sub>pmret</sub></td><td>紙片瑪利歐（N64），反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/61/Papermario.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/N64Recomp/N64Recomp"><img src="https://opengraph.githubassets.com/1/N64Recomp/N64Recomp" width="160" alt="N64Recomp/N64Recomp"></a></td><td><a href="https://github.com/N64Recomp/N64Recomp"><b>N64Recomp</b></a><br><sub>N64Recomp</sub></td><td>把 N64 遊戲直接重新編譯成原生程式碼</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/perfect_dark"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg" width="160" alt="n64decomp/perfect_dark"></a></td><td><a href="https://github.com/n64decomp/perfect_dark"><b>perfect_dark</b></a><br><sub>n64decomp</sub></td><td>Perfect Dark（N64），反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 重製 / 移植

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/HarbourMasters/Shipwright"><img src="https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg" width="160" alt="HarbourMasters/Shipwright"></a></td><td><a href="https://github.com/HarbourMasters/Shipwright"><b>Shipwright</b></a><br><sub>HarbourMasters</sub></td><td>在 PC 上原生執行薩爾達傳說 時之笛（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/Zelda64Recomp/Zelda64Recomp"><img src="https://raw.githubusercontent.com/Zelda64Recomp/Zelda64Recomp/dev/docs/deck_gyro_1.jpg" width="160" alt="Zelda64Recomp/Zelda64Recomp"></a></td><td><a href="https://github.com/Zelda64Recomp/Zelda64Recomp"><b>Zelda64Recomp</b></a><br><sub>Zelda64Recomp</sub></td><td>重新編譯到 PC 的薩爾達傳說 穆修拉的假面，支援現代操作（ROM 需自備）</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/2ship2harkinian/2ship2harkinian"><img src="https://upload.wikimedia.org/wikipedia/en/6/60/The_Legend_of_Zelda_-_Majora%27s_Mask_Box_Art.jpg" width="160" alt="2ship2harkinian/2ship2harkinian"></a></td><td><a href="https://github.com/2ship2harkinian/2ship2harkinian"><b>2ship2harkinian</b></a><br><sub>2ship2harkinian</sub></td><td>在 PC 上原生執行薩爾達傳說 穆修拉的假面（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/60/The_Legend_of_Zelda_-_Majora%27s_Mask_Box_Art.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 資源擷取與工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/ethteck/splat"><img src="https://opengraph.githubassets.com/1/ethteck/splat" width="160" alt="ethteck/splat"></a></td><td><a href="https://github.com/ethteck/splat"><b>splat</b></a><br><sub>ethteck</sub></td><td>把 N64、PS1 二進位檔切分成可反編譯的專案</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/NEstelami/ZAPD"><img src="https://raw.githubusercontent.com/NEstelami/ZAPD/master/docs/zapd_warning_example.png?raw=true" width="160" alt="NEstelami/ZAPD"></a></td><td><a href="https://github.com/NEstelami/ZAPD"><b>ZAPD</b></a><br><sub>NEstelami</sub></td><td>把 Zelda 64 的資源轉成可編輯的原始檔</td><td>否</td><td><sub>專案 README</sub></td></tr>
</table>

### GameCube

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/zeldaret/tww"><img src="https://upload.wikimedia.org/wikipedia/en/7/79/The_Legend_of_Zelda_The_Wind_Waker.jpg" width="160" alt="zeldaret/tww"></a></td><td><a href="https://github.com/zeldaret/tww"><b>tww</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 風之律動，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/7/79/The_Legend_of_Zelda_The_Wind_Waker.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/doldecomp/sms"><img src="https://upload.wikimedia.org/wikipedia/en/0/05/Super_Mario_Sunshine_Box_Art.png" width="160" alt="doldecomp/sms"></a></td><td><a href="https://github.com/doldecomp/sms"><b>sms</b></a><br><sub>doldecomp</sub></td><td>超級瑪利歐陽光，反編譯為 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/05/Super_Mario_Sunshine_Box_Art.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/doldecomp/melee"><img src="https://upload.wikimedia.org/wikipedia/en/7/75/Super_Smash_Bros_Melee_box_art.png" width="160" alt="doldecomp/melee"></a></td><td><a href="https://github.com/doldecomp/melee"><b>melee</b></a><br><sub>doldecomp</sub></td><td>任天堂明星大亂鬥 DX，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/7/75/Super_Smash_Bros_Melee_box_art.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tp"><img src="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Twilight_Princess_Game_Cover.jpg" width="160" alt="zeldaret/tp"></a></td><td><a href="https://github.com/zeldaret/tp"><b>tp</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 曙光公主，反編譯為 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Twilight_Princess_Game_Cover.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/projectPiki/pikmin2"><img src="https://upload.wikimedia.org/wikipedia/en/3/38/Pikmin_2_Case.jpg" width="160" alt="projectPiki/pikmin2"></a></td><td><a href="https://github.com/projectPiki/pikmin2"><b>pikmin2</b></a><br><sub>projectPiki</sub></td><td>皮克敏 2，反編譯為 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/38/Pikmin_2_Case.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 資源擷取與工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/encounter/decomp-toolkit"><img src="https://opengraph.githubassets.com/1/encounter/decomp-toolkit" width="160" alt="encounter/decomp-toolkit"></a></td><td><a href="https://github.com/encounter/decomp-toolkit"><b>decomp-toolkit</b></a><br><sub>encounter</sub></td><td>眾多 GameCube、Wii 反編譯專案背後的工具鏈</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/encounter/objdiff"><img src="https://raw.githubusercontent.com/encounter/objdiff/main/assets/screen-symbols.png" width="160" alt="encounter/objdiff"></a></td><td><a href="https://github.com/encounter/objdiff"><b>objdiff</b></a><br><sub>encounter</sub></td><td>一眼看出你反編譯的函式還差在哪裡</td><td>否</td><td><sub>專案 README</sub></td></tr>
</table>

### Wii

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/zeldaret/ss"><img src="https://upload.wikimedia.org/wikipedia/en/9/99/Legend_of_Zelda_Skyward_Sword_boxart.png" width="160" alt="zeldaret/ss"></a></td><td><a href="https://github.com/zeldaret/ss"><b>ss</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 禦天之劍，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/9/99/Legend_of_Zelda_Skyward_Sword_boxart.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/DarkRTA/rb3"><img src="https://upload.wikimedia.org/wikipedia/en/3/3b/Rock_Band_3_Game_Cover.jpg" width="160" alt="DarkRTA/rb3"></a></td><td><a href="https://github.com/DarkRTA/rb3"><b>rb3</b></a><br><sub>DarkRTA</sub></td><td>Rock Band 3（Wii），反編譯為 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/3b/Rock_Band_3_Game_Cover.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

### NDS

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/pret/pokeplatinum"><img src="https://github.com/user-attachments/assets/157f7c15-4684-48e9-aacb-eefefbcffcec" width="160" alt="pret/pokeplatinum"></a></td><td><a href="https://github.com/pret/pokeplatinum"><b>pokeplatinum</b></a><br><sub>pret</sub></td><td>寶可夢 白金的 C 原始碼</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/ph"><img src="https://upload.wikimedia.org/wikipedia/en/5/5e/The_Legend_of_Zelda_Phantom_Hourglass_Game_Cover.jpg" width="160" alt="zeldaret/ph"></a></td><td><a href="https://github.com/zeldaret/ph"><b>ph</b></a><br><sub>zeldaret</sub></td><td>薩爾達傳說 夢幻的砂時計，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/5/5e/The_Legend_of_Zelda_Phantom_Hourglass_Game_Cover.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeheartgold"><img src="https://upload.wikimedia.org/wikipedia/en/c/cb/PokemonHGSSBox.jpg" width="160" alt="pret/pokeheartgold"></a></td><td><a href="https://github.com/pret/pokeheartgold"><b>pokeheartgold</b></a><br><sub>pret</sub></td><td>寶可夢 心金/魂銀，反編譯為 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/c/cb/PokemonHGSSBox.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

### 3DS

#### 資源擷取與工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/3DSGuy/Project_CTR"><img src="https://opengraph.githubassets.com/1/3DSGuy/Project_CTR" width="160" alt="3DSGuy/Project_CTR"></a></td><td><a href="https://github.com/3DSGuy/Project_CTR"><b>Project_CTR</b></a><br><sub>3DSGuy</sub></td><td>建置與檢視 3DS 檔案格式（ctrtool / makerom）</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
</table>

### PS1

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/Xeeynamo/sotn-decomp"><img src="https://github.com/user-attachments/assets/fff7ddb2-736f-4e7d-b0ee-3c1151649773" width="160" alt="Xeeynamo/sotn-decomp"></a></td><td><a href="https://github.com/Xeeynamo/sotn-decomp"><b>sotn-decomp</b></a><br><sub>Xeeynamo</sub></td><td>惡魔城：月下夜想曲，反編譯為 C</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/shdecompilations/silent-hill-decomp"><img src="https://upload.wikimedia.org/wikipedia/en/9/96/Silent_Hill_video_game_cover.png" width="160" alt="shdecompilations/silent-hill-decomp"></a></td><td><a href="https://github.com/shdecompilations/silent-hill-decomp"><b>silent-hill-decomp</b></a><br><sub>shdecompilations</sub></td><td>沉默之丘（PS1）反編譯進行中</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/9/96/Silent_Hill_video_game_cover.png">維基百科（© 版權方）</a></sub></td></tr>
</table>

### PS2

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/ran-j/PS2Recomp"><img src="https://opengraph.githubassets.com/1/ran-j/PS2Recomp" width="160" alt="ran-j/PS2Recomp"></a></td><td><a href="https://github.com/ran-j/PS2Recomp"><b>PS2Recomp</b></a><br><sub>ran-j</sub></td><td>把 PS2 遊戲重新編譯成原生 PC 程式</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/open-goal/jak-project"><img src="https://raw.githubusercontent.com/open-goal/jak-project/master/docs/img/promosmall1.png" width="160" alt="open-goal/jak-project"></a></td><td><a href="https://github.com/open-goal/jak-project"><b>jak-project</b></a><br><sub>open-goal</sub></td><td>在 PC 上原生執行 Jak and Daxter（光碟需自備）</td><td>否</td><td><sub>專案 README</sub></td></tr>
</table>

### Xbox / Xbox 360

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/hedge-dev/XenonRecomp"><img src="https://opengraph.githubassets.com/1/hedge-dev/XenonRecomp" width="160" alt="hedge-dev/XenonRecomp"></a></td><td><a href="https://github.com/hedge-dev/XenonRecomp"><b>XenonRecomp</b></a><br><sub>hedge-dev</sub></td><td>把 Xbox 360 遊戲重新編譯為原生 C++</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
</table>

#### 重製 / 移植

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/hedge-dev/UnleashedRecomp"><img src="https://upload.wikimedia.org/wikipedia/en/a/a0/Sonic_unleashed_boxart.jpg" width="160" alt="hedge-dev/UnleashedRecomp"></a></td><td><a href="https://github.com/hedge-dev/UnleashedRecomp"><b>UnleashedRecomp</b></a><br><sub>hedge-dev</sub></td><td>在 PC 上原生執行 Sonic Unleashed（遊戲需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a0/Sonic_unleashed_boxart.jpg">維基百科（© 版權方）</a></sub></td></tr>
</table>

#### 資源擷取與工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/xemu-project/xemu"><img src="https://user-images.githubusercontent.com/71127352/144098855-dbc7b12a-d715-4102-b45c-faeb46deabde.png" width="160" alt="xemu-project/xemu"></a></td><td><a href="https://github.com/xemu-project/xemu"><b>xemu</b></a><br><sub>xemu-project</sub></td><td>在 Windows、macOS、Linux 上玩初代 Xbox 遊戲</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
</table>

### PC / DOS / PC-98

#### 反編譯 / 重編譯

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/N0zoM1z0/dx-ball"><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="160" alt="N0zoM1z0/dx-ball"></a></td><td><a href="https://github.com/N0zoM1z0/dx-ball"><b>dx-ball</b></a><br><sub>N0zoM1z0</sub></td><td>用 C/C++ 重建 DX-Ball 1.07，並對照原版 x86 測試</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th04"><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th04"></a></td><td><a href="https://github.com/N0zoM1z0/th04"><b>th04</b></a><br><sub>N0zoM1z0</sub></td><td>東方幻想鄉（PC-98）的可讀原始碼，並以原版編譯器驗證</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th08"><img src="https://raw.githubusercontent.com/N0zoM1z0/th08/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th08"></a></td><td><a href="https://github.com/N0zoM1z0/th08"><b>th08</b></a><br><sub>N0zoM1z0</sub></td><td>東方永夜抄，重建成原始碼</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th10"><img src="https://raw.githubusercontent.com/N0zoM1z0/th10/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th10"></a></td><td><a href="https://github.com/N0zoM1z0/th10"><b>th10</b></a><br><sub>N0zoM1z0</sub></td><td>東方風神錄，重建成原始碼</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/isledecomp/isle"><img src="https://upload.wikimedia.org/wikipedia/en/a/a1/Lego-island.jpg" width="160" alt="isledecomp/isle"></a></td><td><a href="https://github.com/isledecomp/isle"><b>isle</b></a><br><sub>isledecomp</sub></td><td>LEGO Island（1997），反編譯為 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a1/Lego-island.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/diasurgical/DevilutionX"><img src="https://github.com/user-attachments/assets/7ac73801-ef7b-4cc1-8442-a191a2a0a1ce" width="160" alt="diasurgical/DevilutionX"></a></td><td><a href="https://github.com/diasurgical/DevilutionX"><b>DevilutionX</b></a><br><sub>diasurgical</sub></td><td>在現代系統上玩暗黑破壞神（需自備 DIABDAT.MPQ）</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th09"><img src="https://raw.githubusercontent.com/N0zoM1z0/th09/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th09"></a></td><td><a href="https://github.com/N0zoM1z0/th09"><b>th09</b></a><br><sub>N0zoM1z0</sub></td><td>東方花映塚，重建成原始碼</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th095"><img src="https://raw.githubusercontent.com/N0zoM1z0/th095/main/resources/title-screen.jpg" width="160" alt="N0zoM1z0/th095"></a></td><td><a href="https://github.com/N0zoM1z0/th095"><b>th095</b></a><br><sub>N0zoM1z0</sub></td><td>東方文花帖，重建成原始碼</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th105"><img src="https://raw.githubusercontent.com/N0zoM1z0/th105/main/resources/title-screen.jpg" width="160" alt="N0zoM1z0/th105"></a></td><td><a href="https://github.com/N0zoM1z0/th105"><b>th105</b></a><br><sub>N0zoM1z0</sub></td><td>東方緋想天，重建成原始碼</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/touhou-reverse-engineering"><img src="https://opengraph.githubassets.com/1/N0zoM1z0/touhou-reverse-engineering" width="160" alt="N0zoM1z0/touhou-reverse-engineering"></a></td><td><a href="https://github.com/N0zoM1z0/touhou-reverse-engineering"><b>touhou-reverse-engineering</b></a><br><sub>N0zoM1z0</sub></td><td>證據優先的東方 IDA 筆記，附執行期修補實驗</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
</table>

#### 重製 / 移植

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="160" alt="ucodia/desktop-games-nostalgia"></a></td><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><b>desktop-games-nostalgia</b></a><br><sub>ucodia</sub></td><td>再砸一次桌面：Gemtree 2000 年的小玩具登上 macOS 和網頁</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="160" alt="tuunanet/rea-ski-or-die-reconstruction"></a></td><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><b>rea-ski-or-die-reconstruction</b></a><br><sub>tuunanet</sub></td><td>Ski or Die 的雪球大戰，以 Rust + SDL2 重製（素材需自備）</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="160" alt="Moxnatiy/OpenBattlefield2"></a></td><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><b>OpenBattlefield2</b></a><br><sub>Moxnatiy</sub></td><td>戰地風雲 2 引擎的 C++20 淨室重寫（讀取你自己的遊戲檔案）</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenRsG/GunZRs"><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="160" alt="OpenRsG/GunZRs"></a></td><td><a href="https://github.com/OpenRsG/GunZRs"><b>GunZRs</b></a><br><sub>OpenRsG</sub></td><td>GunZ: The Duel 以 Rust + Bevy 重生</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/a-barzanti/ai-rebuilds"><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="160" alt="a-barzanti/ai-rebuilds"></a></td><td><a href="https://github.com/a-barzanti/ai-rebuilds"><b>ai-rebuilds</b></a><br><sub>a-barzanti</sub></td><td>被遺棄的老遊戲重回瀏覽器，不含任何原版檔案</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/OpenRCT2/OpenRCT2"><img src="https://github.com/user-attachments/assets/fa893cc8-1484-4751-94be-4ead00a6c8f9" width="160" alt="OpenRCT2/OpenRCT2"></a></td><td><a href="https://github.com/OpenRCT2/OpenRCT2"><b>OpenRCT2</b></a><br><sub>OpenRCT2</sub></td><td>開源版 RollerCoaster Tycoon 2，在現代系統上繼續執行</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenMW/openmw"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/OpenMW_with_example_suit_2.png" width="160" alt="OpenMW/openmw"></a></td><td><a href="https://github.com/OpenMW/openmw"><b>openmw</b></a><br><sub>OpenMW</sub></td><td>在現代開源引擎上玩 Morrowind</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/commons/9/9e/OpenMW_with_example_suit_2.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/julianxhokaxhiu/FFNx"><img src="https://raw.githubusercontent.com/julianxhokaxhiu/FFNx/master/.screens/ff7.png" width="160" alt="julianxhokaxhiu/FFNx"></a></td><td><a href="https://github.com/julianxhokaxhiu/FFNx"><b>FFNx</b></a><br><sub>julianxhokaxhiu</sub></td><td>PC 版 FF7/FF8 的現代驅動程式與 Mod 平台</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/Interkarma/daggerfall-unity"><img src="https://github.com/Interkarma/daggerfall-unity/assets/10426244/4f176f9d-6332-47b3-a4d7-317ed8d6b38b" width="160" alt="Interkarma/daggerfall-unity"></a></td><td><a href="https://github.com/Interkarma/daggerfall-unity"><b>daggerfall-unity</b></a><br><sub>Interkarma</sub></td><td>以 Unity 重現的 Daggerfall（讀取你自己的遊戲資料）</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenXcom/OpenXcom"><img src="https://opengraph.githubassets.com/1/OpenXcom/OpenXcom" width="160" alt="OpenXcom/OpenXcom"></a></td><td><a href="https://github.com/OpenXcom/OpenXcom"><b>OpenXcom</b></a><br><sub>OpenXcom</sub></td><td>在現代開源引擎上玩初代 UFO / X-COM</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/scummvm/scummvm"><img src="https://www.scummvm.org/data/screenshots/prince/prince/prince_win_en_1_3_full.png" width="160" alt="scummvm/scummvm"></a></td><td><a href="https://github.com/scummvm/scummvm"><b>scummvm</b></a><br><sub>scummvm</sub></td><td>在幾乎任何裝置上玩經典點擊式冒險遊戲</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/fallout2-ce/fallout2-ce"><img src="https://raw.githubusercontent.com/fallout2-ce/fallout2-ce/main/docs/images/two-column-inventory.jpg" width="160" alt="fallout2-ce/fallout2-ce"></a></td><td><a href="https://github.com/fallout2-ce/fallout2-ce"><b>fallout2-ce</b></a><br><sub>fallout2-ce</sub></td><td>在現代系統上玩異塵餘生 2（讀取你自己的遊戲資料）</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenTTD/OpenTTD"><img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/OpenTTD-15.3-en.png" width="160" alt="OpenTTD/OpenTTD"></a></td><td><a href="https://github.com/OpenTTD/OpenTTD"><b>OpenTTD</b></a><br><sub>OpenTTD</sub></td><td>開源版 Transport Tycoon，至今仍持續更新</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/commons/b/ba/OpenTTD-15.3-en.png">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/OpenRA/OpenRA"><img src="https://www.openra.net/images/news/20260222-generators.gif" width="160" alt="OpenRA/OpenRA"></a></td><td><a href="https://github.com/OpenRA/OpenRA"><b>OpenRA</b></a><br><sub>OpenRA</sub></td><td>為現代連線對戰重建的經典終極動員令</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/perfect-dark-pc-port/perfect_dark"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg" width="160" alt="perfect-dark-pc-port/perfect_dark"></a></td><td><a href="https://github.com/perfect-dark-pc-port/perfect_dark"><b>perfect_dark</b></a><br><sub>perfect-dark-pc-port</sub></td><td>在 PC 上原生執行 Perfect Dark（ROM 需自備）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th08-web"><img src="https://raw.githubusercontent.com/N0zoM1z0/th08-web/main/resources/th08-web-social-preview.jpg" width="160" alt="N0zoM1z0/th08-web"></a></td><td><a href="https://github.com/N0zoM1z0/th08-web"><b>th08-web</b></a><br><sub>N0zoM1z0</sub></td><td>在瀏覽器裡玩永夜抄，以 th08 重建版為基礎</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/AsyncFinn/rook"><img src="https://opengraph.githubassets.com/1/AsyncFinn/rook" width="160" alt="AsyncFinn/rook"></a></td><td><a href="https://github.com/AsyncFinn/rook"><b>rook</b></a><br><sub>AsyncFinn</sub></td><td>以 Rust 寫成的 Roblox 相容引擎，對照 Studio 測試</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/tallowmere/free-heroes4"><img src="https://upload.wikimedia.org/wikipedia/en/c/cc/Heroes_of_Might_and_Magic_IV_box.jpg" width="160" alt="tallowmere/free-heroes4"></a></td><td><a href="https://github.com/tallowmere/free-heroes4"><b>free-heroes4</b></a><br><sub>tallowmere</sub></td><td>魔法門之英雄無敵 IV 的 C++23 新引擎（讀取你的 GOG 檔案）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/c/cc/Heroes_of_Might_and_Magic_IV_box.jpg">維基百科（© 版權方）</a></sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/carlhako/keen-clone"><b>keen-clone</b></a><br><sub>carlhako</sub></td><td>用 REA + Ghidra 函式級還原的 Commander Keen 1 原生 Linux/SDL2 重實現</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/NathanKanaeru/samp-client-re"><b>samp-client-re</b></a><br><sub>NathanKanaeru</sub></td><td>用 REA/Ghidra 恢復架構的 SA-MP 0.3.DL-R1 clean-room 客戶端重實現</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/openage/openage"><b>openage</b></a><br><sub>openage</sub></td><td>帝國時代 2 及其他 RTS 的開源引擎重實現</td><td>否</td><td><sub>—</sub></td></tr>
</table>

#### 資源擷取與工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/ata4/disunity"><img src="https://opengraph.githubassets.com/1/ata4/disunity" width="160" alt="ata4/disunity"></a></td><td><a href="https://github.com/ata4/disunity"><b>disunity</b></a><br><sub>ata4</sub></td><td>早期的 Unity 資源檔檢視工具</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/Perfare/AssetStudio"><img src="https://opengraph.githubassets.com/1/Perfare/AssetStudio" width="160" alt="Perfare/AssetStudio"></a></td><td><a href="https://github.com/Perfare/AssetStudio"><b>AssetStudio</b></a><br><sub>Perfare</sub></td><td>瀏覽並匯出 Unity 遊戲資源</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/AssetRipper/AssetRipper"><img src="https://raw.githubusercontent.com/AssetRipper/AssetRipper/master/docs/articles/images/RunningOnMac/004.png" width="160" alt="AssetRipper/AssetRipper"></a></td><td><a href="https://github.com/AssetRipper/AssetRipper"><b>AssetRipper</b></a><br><sub>AssetRipper</sub></td><td>把 Unity 建置產物還原成可編輯的專案</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/ladislav-zezula/CascLib"><img src="https://opengraph.githubassets.com/1/ladislav-zezula/CascLib" width="160" alt="ladislav-zezula/CascLib"></a></td><td><a href="https://github.com/ladislav-zezula/CascLib"><b>CascLib</b></a><br><sub>ladislav-zezula</sub></td><td>讀取暴雪 CASC 遊戲儲存格式</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/touhou-reconstruction-factory"><img src="https://opengraph.githubassets.com/1/N0zoM1z0/touhou-reconstruction-factory" width="160" alt="N0zoM1z0/touhou-reconstruction-factory"></a></td><td><a href="https://github.com/N0zoM1z0/touhou-reconstruction-factory"><b>touhou-reconstruction-factory</b></a><br><sub>N0zoM1z0</sub></td><td>東方系列重建背後的 AI 代理流水線</td><td>❔ 待驗證</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/rodneypantonial/sims3-modernization"><b>sims3-modernization</b></a><br><sub>rodneypantonial</sub></td><td>讓模擬市民 3 在新電腦上少卡頓、少當機</td><td>✅ 是</td><td><sub>—</sub></td></tr>
</table>

## 應用程式 / Electron / 桌面

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/michaelshimeles/sketch"><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="160" alt="michaelshimeles/sketch"></a></td><td><a href="https://github.com/michaelshimeles/sketch"><b>sketch</b></a><br><sub>michaelshimeles</sub></td><td>以 Rust 寫成的無限設計畫布，研究 Paper 後重建</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/rec-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="160" alt="michaelshimeles/rec-rs"></a></td><td><a href="https://github.com/michaelshimeles/rec-rs"><b>rec-rs</b></a><br><sub>michaelshimeles</sub></td><td>以 Rust 寫成的 macOS 快速螢幕錄影工具，參考 OBS 設計</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/iammukeshm/hexgrab"><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="160" alt="iammukeshm/hexgrab"></a></td><td><a href="https://github.com/iammukeshm/hexgrab"><b>hexgrab</b></a><br><sub>iammukeshm</sub></td><td>迷你 Windows 取色工具，從 PowerToys 二進位檔研究而來</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/AdamLinCodes/AdamTerm"><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="160" alt="AdamLinCodes/AdamTerm"></a></td><td><a href="https://github.com/AdamLinCodes/AdamTerm"><b>AdamTerm</b></a><br><sub>AdamLinCodes</sub></td><td>研究 Ghostty 後做出的極簡 macOS 終端機</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><img src="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg" width="160" alt="az9713/wispr-flow-rea-teardown"></a></td><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><b>wispr-flow-rea-teardown</b></a><br><sub>az9713</sub></td><td>拆解 Wispr Flow 的語音管線，附 64 行重寫版</td><td>✅ 是</td><td><sub><a href="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg">影片封面</a></sub></td></tr>
<tr><td><a href="https://github.com/cudanexus/vd-streamer-linux"><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="160" alt="cudanexus/vd-streamer-linux"></a></td><td><a href="https://github.com/cudanexus/vd-streamer-linux"><b>vd-streamer-linux</b></a><br><sub>cudanexus</sub></td><td>把 Linux 桌面串流到 Quest、Pico 頭戴裝置</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/electron/asar"><img src="images/asar-terminal.png" width="160" alt="electron/asar"></a></td><td><a href="https://github.com/electron/asar"><b>asar</b></a><br><sub>electron</sub></td><td>封裝、解包 Electron 應用程式裡的封存檔</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><img src="https://opengraph.githubassets.com/1/KarlssonChristoffer/DiskLens" width="160" alt="KarlssonChristoffer/DiskLens"></a></td><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><b>DiskLens</b></a><br><sub>KarlssonChristoffer</sub></td><td>像 WinDirStat 一樣看清 Windows 11 磁碟被什麼佔滿</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/LilZeeCN/zee-rp"><img src="https://raw.githubusercontent.com/LilZeeCN/zee-rp/main/examples/screenshot/source.png" width="160" alt="LilZeeCN/zee-rp"></a></td><td><a href="https://github.com/LilZeeCN/zee-rp"><b>zee-rp</b></a><br><sub>LilZeeCN</sub></td><td>以命令列或 MCP 讀寫 Axure RP 原型檔</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/lxistired/ledger-reborn"><img src="https://raw.githubusercontent.com/lxistired/ledger-reborn/main/docs/screenshots/accounting.png" width="160" alt="lxistired/ledger-reborn"></a></td><td><a href="https://github.com/lxistired/ledger-reborn"><b>ledger-reborn</b></a><br><sub>lxistired</sub></td><td>本機優先的記帳 App，參考 QuickBooks Mac 版</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/terminal-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/terminal-rs/master/docs/img/overview.png" width="160" alt="michaelshimeles/terminal-rs"></a></td><td><a href="https://github.com/michaelshimeles/terminal-rs"><b>terminal-rs</b></a><br><sub>michaelshimeles</sub></td><td>以 Rust 寫成的彭博風格交易終端機</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/GLinnik21/plx-native"><img src="https://raw.githubusercontent.com/GLinnik21/plx-native/main/docs/screenshots/home.jpg" width="160" alt="GLinnik21/plx-native"></a></td><td><a href="https://github.com/GLinnik21/plx-native"><b>plx-native</b></a><br><sub>GLinnik21</sub></td><td>LG 電視上更快的原生 Plex 用戶端</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/storytold/photocraft"><img src="https://raw.githubusercontent.com/storytold/photocraft/main/docs/images/photocraft-demo.jpg" width="160" alt="storytold/photocraft"></a></td><td><a href="https://github.com/storytold/photocraft"><b>photocraft</b></a><br><sub>storytold</sub></td><td>有人從零重寫了一個類似 Adobe Photoshop 的免費開源修圖軟體。用 Rust 寫的，支援圖層、遮色片、PSD 檔案，但完全沒用 Adobe 的程式碼。</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/sickpyramid/ReaFuse"><img src="https://opengraph.githubassets.com/1/sickpyramid/ReaFuse" width="160" alt="sickpyramid/ReaFuse"></a></td><td><a href="https://github.com/sickpyramid/ReaFuse"><b>ReaFuse</b></a><br><sub>sickpyramid</sub></td><td>藉助 REA 把兩個 JS/TS 專案合併成一個</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/laaielichter/Reverseport"><img src="https://raw.githubusercontent.com/laaielichter/Reverseport/main/docs/assets/demo.gif" width="160" alt="laaielichter/Reverseport"></a></td><td><a href="https://github.com/laaielichter/Reverseport"><b>Reverseport</b></a><br><sub>laaielichter</sub></td><td>把逆向成果移植到 Godot、Unity、Unreal 或 three.js</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Xiangyu-CAS/rea-capcut"><b>rea-capcut</b></a><br><sub>Xiangyu-CAS</sub></td><td>用 REA 研究剪映後重做的開源離線剪輯軟體</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/chilliesdev/fmseasonhub-re"><b>fmseasonhub-re</b></a><br><sub>chilliesdev</sub></td><td>用 REA 拆解 FM Season Hub 應用程式的分析筆記</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Caho1/open-claude-ui"><b>open-claude-ui</b></a><br><sub>Caho1</sub></td><td>用 REA 深度拆解並高保真還原 Claude 桌面端 UI 元件與互動物理</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/glauberlima/open-scrantic"><b>open-scrantic</b></a><br><sub>glauberlima</sub></td><td>用 REA 逆向並重寫的 1992 年 Johnny Castaway 螢幕保護程式（Rust）</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/storytold/vectorcraft"><img src="images/vectorcraft-card.jpg" width="160" alt="storytold/vectorcraft"></a></td><td><a href="https://github.com/storytold/vectorcraft"><b>vectorcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 Adobe Illustrator 的向量繪圖工具。純 Rust 實作，可以畫海報、Logo、插畫，完全沒用 Adobe 的程式碼。</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/filmcraft"><b>filmcraft</b></a><br><sub>storytold</sub></td><td>有人從零做了一個類似 Adobe Premiere Pro 的免費影片剪輯軟體。用 Rust 寫的，可以剪片子、加特效、調色，完全沒用 Adobe 的程式碼。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/storytold/lightcraft"><img src="images/lightcraft-card.jpg" width="160" alt="storytold/lightcraft"></a></td><td><a href="https://github.com/storytold/lightcraft"><b>lightcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 Adobe Lightroom 的照片管理與 RAW 沖印工具。純 Rust 實作，用來整理和編輯照片，完全沒用 Adobe 的程式碼。</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/wordcraft"><b>wordcraft</b></a><br><sub>storytold</sub></td><td>純 Rust 潔淨室文字處理器</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/pdfcraft"><b>pdfcraft</b></a><br><sub>storytold</sub></td><td>純 Rust 潔淨室 PDF 閱讀與編輯器</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/effectcraft"><b>effectcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 Adobe After Effects 的動效與視覺特效軟體。用 Rust 寫的，可以做動畫標題和合成，完全沒用 Adobe 的程式碼。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/cadcraft"><b>cadcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 AutoCAD 的 CAD 製圖軟體。純 Rust 實作。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/figcraft"><b>figcraft</b></a><br><sub>storytold</sub></td><td>有人從零做了一個類似 Figma 的免費介面設計與原型工具。用 Rust 寫的。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/designcraft"><b>designcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 Adobe InDesign 的排版出版工具。純 Rust 實作。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/deckcraft"><b>deckcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 PowerPoint 的簡報軟體。用 Rust 寫的，做投影片不用微軟的程式碼。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/soundcraft"><b>soundcraft</b></a><br><sub>storytold</sub></td><td>從零重寫的類似 Pro Tools 的數位音訊工作站。純 Rust 實作。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/gridcraft"><b>gridcraft</b></a><br><sub>storytold</sub></td><td>有人從零做了一個類似 Excel 的免費試算表軟體。用 Rust 寫的。</td><td>否</td><td><sub>—</sub></td></tr>
</table>

## 協定 / 硬體

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/a-funk/open-appleremote"><img src="https://opengraph.githubassets.com/1/a-funk/open-appleremote" width="160" alt="a-funk/open-appleremote"></a></td><td><a href="https://github.com/a-funk/open-appleremote"><b>open-appleremote</b></a><br><sub>a-funk</sub></td><td>在 Linux 上使用第一代 Siri 遙控器，連手勢都支援</td><td>❔ 待驗證</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/Slyvan25/OpenGHub"><img src="https://raw.githubusercontent.com/Slyvan25/OpenGHub/master/docs/screenshots/devices.png" width="160" alt="Slyvan25/OpenGHub"></a></td><td><a href="https://github.com/Slyvan25/OpenGHub"><b>OpenGHub</b></a><br><sub>Slyvan25</sub></td><td>在 Linux 上不用 G HUB 也能控制羅技周邊</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/mitmproxy/mitmproxy"><img src="https://mitmproxy.org/screenshot.png" width="160" alt="mitmproxy/mitmproxy"></a></td><td><a href="https://github.com/mitmproxy/mitmproxy"><b>mitmproxy</b></a><br><sub>mitmproxy</sub></td><td>即時檢視和修改 HTTPS 流量</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/postlund/pyatv"><img src="https://opengraph.githubassets.com/1/postlund/pyatv" width="160" alt="postlund/pyatv"></a></td><td><a href="https://github.com/postlund/pyatv"><b>pyatv</b></a><br><sub>postlund</sub></td><td>以 Python 控制 Apple TV 和 AirPlay 裝置</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/wireshark/wireshark"><img src="images/wireshark-gui.png" width="160" alt="wireshark/wireshark"></a></td><td><a href="https://github.com/wireshark/wireshark"><b>wireshark</b></a><br><sub>wireshark</sub></td><td>看清網路上的每一個封包</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/EndLess728/MiTV-Remote"><b>MiTV-Remote</b></a><br><sub>EndLess728</sub></td><td>在 Mac、Android、iPhone 上用 Wi-Fi 遙控小米電視</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/B-Howell/soundconnect-desktop"><b>soundconnect-desktop</b></a><br><sub>B-Howell</sub></td><td>在 Windows 桌面上控制 Sony 藍牙耳機</td><td>✅ 是</td><td><sub>—</sub></td></tr>
</table>

## 韌體 / 驅動

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/grisuno/VSL-DSP"><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="160" alt="grisuno/VSL-DSP"></a></td><td><a href="https://github.com/grisuno/VSL-DSP"><b>VSL-DSP</b></a><br><sub>grisuno</sub></td><td>PreSonus AudioBox VSL 音效卡的 Linux 核心模組</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/ReFirmLabs/binwalk"><img src="https://raw.githubusercontent.com/ReFirmLabs/binwalk/master/images/output.png" width="160" alt="ReFirmLabs/binwalk"></a></td><td><a href="https://github.com/ReFirmLabs/binwalk"><b>binwalk</b></a><br><sub>ReFirmLabs</sub></td><td>找出並擷取韌體映像檔裡藏著的東西</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/qilingframework/qiling"><img src="https://raw.githubusercontent.com/qilingframework/theme.qiling.io/master/source/img/fuzzer.jpg?raw=true" width="160" alt="qilingframework/qiling"></a></td><td><a href="https://github.com/qilingframework/qiling"><b>qiling</b></a><br><sub>qilingframework</sub></td><td>跨作業系統、跨 CPU 模擬並插樁二進位檔</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/ghidraninja/game-and-watch-backup"><img src="https://img.youtube.com/vi/-MzmoEFs0bQ/maxresdefault.jpg" width="160" alt="ghidraninja/game-and-watch-backup"></a></td><td><a href="https://github.com/ghidraninja/game-and-watch-backup"><b>game-and-watch-backup</b></a><br><sub>ghidraninja</sub></td><td>備份並還原你自己的 Game &amp; Watch 韌體</td><td>否</td><td><sub><a href="https://img.youtube.com/vi/-MzmoEFs0bQ/maxresdefault.jpg">影片封面</a></sub></td></tr>
<tr><td><a href="https://github.com/attify/firmware-analysis-toolkit"><img src="https://opengraph.githubassets.com/1/attify/firmware-analysis-toolkit" width="160" alt="attify/firmware-analysis-toolkit"></a></td><td><a href="https://github.com/attify/firmware-analysis-toolkit"><b>firmware-analysis-toolkit</b></a><br><sub>attify</sub></td><td>模擬執行物聯網韌體，安全地進行研究</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/onekey-sec/unblob"><img src="images/unblob-terminal.png" width="160" alt="onekey-sec/unblob"></a></td><td><a href="https://github.com/onekey-sec/unblob"><b>unblob</b></a><br><sub>onekey-sec</sub></td><td>遞迴解包幾乎所有韌體與容器格式</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/travisgoodspeed/md380tools"><img src="https://opengraph.githubassets.com/1/travisgoodspeed/md380tools" width="160" alt="travisgoodspeed/md380tools"></a></td><td><a href="https://github.com/travisgoodspeed/md380tools"><b>md380tools</b></a><br><sub>travisgoodspeed</sub></td><td>TYT MD-380 對講機的自製韌體修補</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/nicolvus/a6000-fw-decomp"><b>a6000-fw-decomp</b></a><br><sub>nicolvus</sub></td><td>用 REA 和 Ghidra 拆 Sony A6000 相機韌體</td><td>✅ 是</td><td><sub>—</sub></td></tr>
</table>

## 資安 / 評測

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="160" alt="NullLabTests/OpenBSD_netcat_REA"></a></td><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><b>OpenBSD_netcat_REA</b></a><br><sub>NullLabTests</sub></td><td>以 REA + Ghidra 靜態分析 netcat-openbsd</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/morluto/rea/discussions/2254"><img src="images/rea-discussion-2254.png" width="160" alt="REA discussion #2254"></a></td><td><a href="https://github.com/morluto/rea/discussions/2254"><b>REA discussion #2254</b></a></td><td>分析去除符號的 bzip2，並與實際建置結果比對驗證</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><img src="https://opengraph.githubassets.com/1/UnknownHacker1/rea-groundtruth" width="160" alt="UnknownHacker1/rea-groundtruth"></a></td><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><b>rea-groundtruth</b></a><br><sub>UnknownHacker1</sub></td><td>以真實原始碼檢驗 REA 的分析報告</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/az9713/REA-demo"><img src="https://opengraph.githubassets.com/1/az9713/REA-demo" width="160" alt="az9713/REA-demo"></a></td><td><a href="https://github.com/az9713/REA-demo"><b>REA-demo</b></a><br><sub>az9713</sub></td><td>讓 REA 分析它自己，附可證偽的預測</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-lab"><img src="https://opengraph.githubassets.com/1/pablodiazjorge/rea-lab" width="160" alt="pablodiazjorge/rea-lab"></a></td><td><a href="https://github.com/pablodiazjorge/rea-lab"><b>rea-lab</b></a><br><sub>pablodiazjorge</sub></td><td>Windows + Ghidra 練習題與預先登記的 REA 評測</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
</table>

## 逆向工具

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="160" alt="ShadowSwaps/REA-Reconstruction-Companion"></a></td><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><b>REA-Reconstruction-Companion</b></a><br><sub>ShadowSwaps</sub></td><td>讓重建過程隨時有證據可查的 AI 代理技能</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/NationalSecurityAgency/ghidra"><img src="images/ghidra-gui.png" width="160" alt="NationalSecurityAgency/ghidra"></a></td><td><a href="https://github.com/NationalSecurityAgency/ghidra"><b>ghidra</b></a><br><sub>NationalSecurityAgency</sub></td><td>NSA 開源的免費反編譯/反組譯套件</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/skylot/jadx"><img src="https://user-images.githubusercontent.com/118523/142730720-839f017e-38db-423e-b53f-39f5f0a0316f.png" width="160" alt="skylot/jadx"></a></td><td><a href="https://github.com/skylot/jadx"><b>jadx</b></a><br><sub>skylot</sub></td><td>把 Android APK 還原成可讀的 Java</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/LaurieWired/GhidraMCP"><img src="https://github.com/user-attachments/assets/4986d702-be3f-4697-acce-aea55cd79ad3" width="160" alt="LaurieWired/GhidraMCP"></a></td><td><a href="https://github.com/LaurieWired/GhidraMCP"><b>GhidraMCP</b></a><br><sub>LaurieWired</sub></td><td>一個橋接工具，讓 AI 助手（比如 Claude）能直接控制免費的逆向工具 Ghidra。AI 可以幫你反編譯程式、給函式改名、分析二進位檔案。</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/x64dbg/x64dbg"><img src="https://raw.githubusercontent.com/x64dbg/x64dbg/development/.github/screenshots/cpu-light.png" width="160" alt="x64dbg/x64dbg"></a></td><td><a href="https://github.com/x64dbg/x64dbg"><b>x64dbg</b></a><br><sub>x64dbg</sub></td><td>Windows 程式首選的開源除錯器</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/iBotPeaches/Apktool"><img src="images/apktool-terminal.png" width="160" alt="iBotPeaches/Apktool"></a></td><td><a href="https://github.com/iBotPeaches/Apktool"><b>Apktool</b></a><br><sub>iBotPeaches</sub></td><td>解包、閱讀並重新封裝 Android APK</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/angr/angr"><img src="https://opengraph.githubassets.com/1/angr/angr" width="160" alt="angr/angr"></a></td><td><a href="https://github.com/angr/angr"><b>angr</b></a><br><sub>angr</sub></td><td>在 Python 裡進行符號執行與二進位分析</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/avast/retdec"><img src="https://user-images.githubusercontent.com/20342097/35865940-2288d66a-0b56-11e8-9a92-d154b7111053.png" width="160" alt="avast/retdec"></a></td><td><a href="https://github.com/avast/retdec"><b>retdec</b></a><br><sub>avast</sub></td><td>把多種架構的機器碼反編譯成 C</td><td>否</td><td><sub>維護者貼文</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/cutter"><img src="https://raw.githubusercontent.com/rizinorg/cutter/dev/docs/source/images/screenshot.png" width="160" alt="rizinorg/cutter"></a></td><td><a href="https://github.com/rizinorg/cutter"><b>cutter</b></a><br><sub>rizinorg</sub></td><td>基於 Rizin、容易上手的逆向工程圖形介面</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/ghidraninja/ghidra_scripts"><img src="https://raw.githubusercontent.com/ghidraninja/ghidra_scripts/master/images/binwalk.png" width="160" alt="ghidraninja/ghidra_scripts"></a></td><td><a href="https://github.com/ghidraninja/ghidra_scripts"><b>ghidra_scripts</b></a><br><sub>ghidraninja</sub></td><td>實用 Ghidra 腳本合集，從 binwalk 到 YARA</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/radareorg/radare2"><img src="https://raw.githubusercontent.com/radareorg/radare2/master/doc/images/shot.png" width="160" alt="radareorg/radare2"></a></td><td><a href="https://github.com/radareorg/radare2"><b>radare2</b></a><br><sub>radareorg</sub></td><td>可用腳本操控的命令列逆向工程框架</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/mandiant/flare-floss"><img src="images/floss-terminal.png" width="160" alt="mandiant/flare-floss"></a></td><td><a href="https://github.com/mandiant/flare-floss"><b>flare-floss</b></a><br><sub>mandiant</sub></td><td>把惡意軟體裡隱藏、混淆過的字串挖出來</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/WerWolv/ImHex"><img src="images/imhex-gui.png" width="160" alt="WerWolv/ImHex"></a></td><td><a href="https://github.com/WerWolv/ImHex"><b>ImHex</b></a><br><sub>WerWolv</sub></td><td>內建模式語言、能幫你解析結構的十六進位編輯器</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/mandiant/capa"><img src="https://raw.githubusercontent.com/mandiant/capa/master/doc/img/capa_web_explorer.png" width="160" alt="mandiant/capa"></a></td><td><a href="https://github.com/mandiant/capa"><b>capa</b></a><br><sub>mandiant</sub></td><td>問程式一句「你能做什麼」，得到對應 ATT&amp;CK 的答案</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/frida/frida"><img src="images/frida-terminal.png" width="160" alt="frida/frida"></a></td><td><a href="https://github.com/frida/frida"><b>frida</b></a><br><sub>frida</sub></td><td>注入任何平台上執行中的程式，即時改寫其行為</td><td>否</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://github.com/dnSpyEx/dnSpy"><img src="https://raw.githubusercontent.com/dnSpyEx/dnSpy/master/images/debug-animated.gif" width="160" alt="dnSpyEx/dnSpy"></a></td><td><a href="https://github.com/dnSpyEx/dnSpy"><b>dnSpy</b></a><br><sub>dnSpyEx</sub></td><td>不需原始碼即可除錯和修改 .NET 組件</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/decompme/decomp.me"><img src="https://opengraph.githubassets.com/1/decompme/decomp.me" width="160" alt="decompme/decomp.me"></a></td><td><a href="https://github.com/decompme/decomp.me"><b>decomp.me</b></a><br><sub>decompme</sub></td><td>在瀏覽器裡協作反編譯，一起挑戰完全匹配</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/mrexodia/ida-pro-mcp"><img src="https://img.youtube.com/vi/iFxNuk3kxhk/0.jpg" width="160" alt="mrexodia/ida-pro-mcp"></a></td><td><a href="https://github.com/mrexodia/ida-pro-mcp"><b>ida-pro-mcp</b></a><br><sub>mrexodia</sub></td><td>讓 AI 代理透過 MCP 操作 IDA Pro</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/jsdec"><img src="https://opengraph.githubassets.com/1/rizinorg/jsdec" width="160" alt="rizinorg/jsdec"></a></td><td><a href="https://github.com/rizinorg/jsdec"><b>jsdec</b></a><br><sub>rizinorg</sub></td><td>為 Rizin 產生可讀的虛擬 C 碼，手寫組合語言也行</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/rizin"><img src="https://rizin.re/images/rizin_preview.png" width="160" alt="rizinorg/rizin"></a></td><td><a href="https://github.com/rizinorg/rizin"><b>rizin</b></a><br><sub>rizinorg</sub></td><td>源自 radare2 的 UNIX 風格逆向工程框架</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/icsharpcode/ILSpy"><img src="https://opengraph.githubassets.com/1/icsharpcode/ILSpy" width="160" alt="icsharpcode/ILSpy"></a></td><td><a href="https://github.com/icsharpcode/ILSpy"><b>ILSpy</b></a><br><sub>icsharpcode</sub></td><td>把任何 .NET 組件還原成 C#</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/google/bindiff"><img src="https://zynamics.com/images/bindiff_scr1_s.gif" width="160" alt="google/bindiff"></a></td><td><a href="https://github.com/google/bindiff"><b>bindiff</b></a><br><sub>google</sub></td><td>找出兩個版本的二進位檔之間改了什麼</td><td>否</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/0xshlomil/ida-free-mcp"><img src="https://opengraph.githubassets.com/1/0xshlomil/ida-free-mcp" width="160" alt="0xshlomil/ida-free-mcp"></a></td><td><a href="https://github.com/0xshlomil/ida-free-mcp"><b>ida-free-mcp</b></a><br><sub>0xshlomil</sub></td><td>透過 MCP 讓 AI 代理使用免費版 IDA</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/HexRaysSA/ida-mcp"><img src="https://opengraph.githubassets.com/1/HexRaysSA/ida-mcp" width="160" alt="HexRaysSA/ida-mcp"></a></td><td><a href="https://github.com/HexRaysSA/ida-mcp"><b>ida-mcp</b></a><br><sub>HexRaysSA</sub></td><td>Hex-Rays 官方的 IDA MCP 服務</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/Nowng/rea-mcp"><img src="https://opengraph.githubassets.com/1/Nowng/rea-mcp" width="160" alt="Nowng/rea-mcp"></a></td><td><a href="https://github.com/Nowng/rea-mcp"><b>rea-mcp</b></a><br><sub>Nowng</sub></td><td>在 LM Studio 裡搭配本機模型使用 REA</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/alexmi256/rea-agent-docker"><img src="https://opengraph.githubassets.com/1/alexmi256/rea-agent-docker" width="160" alt="alexmi256/rea-agent-docker"></a></td><td><a href="https://github.com/alexmi256/rea-agent-docker"><b>rea-agent-docker</b></a><br><sub>alexmi256</sub></td><td>REA 的 Docker 映像檔，含 Ghidra/Hopper/IDA 版本</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/cognixws/picode-rea"><img src="https://opengraph.githubassets.com/1/cognixws/picode-rea" width="160" alt="cognixws/picode-rea"></a></td><td><a href="https://github.com/cognixws/picode-rea"><b>picode-rea</b></a><br><sub>cognixws</sub></td><td>在 PiCode 裡使用 REA 的靜態分析工具</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/czcdr/dsh-plugin-rea"><img src="https://raw.githubusercontent.com/czcdr/dsh-plugin-rea/main/assets/screenshot-1.png" width="160" alt="czcdr/dsh-plugin-rea"></a></td><td><a href="https://github.com/czcdr/dsh-plugin-rea"><b>dsh-plugin-rea</b></a><br><sub>czcdr</sub></td><td>在 DeepSeek Harness 裡使用 REA，自動裝好 Ghidra</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><img src="https://opengraph.githubassets.com/1/sheilacraig/dsh-rea-mcp" width="160" alt="sheilacraig/dsh-rea-mcp"></a></td><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><b>dsh-rea-mcp</b></a><br><sub>sheilacraig</sub></td><td>只靠設定就把 REA 接進 DeepSeek Harness</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><img src="https://opengraph.githubassets.com/1/ya123-4/rea-dsh-plugin" width="160" alt="ya123-4/rea-dsh-plugin"></a></td><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><b>rea-dsh-plugin</b></a><br><sub>ya123-4</sub></td><td>在 DeepSeek Harness 中註冊 REA 的 MCP 工具</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/zhaofeng130/dsh-rea"><img src="https://opengraph.githubassets.com/1/zhaofeng130/dsh-rea" width="160" alt="zhaofeng130/dsh-rea"></a></td><td><a href="https://github.com/zhaofeng130/dsh-rea"><b>dsh-rea</b></a><br><sub>zhaofeng130</sub></td><td>給 DeepSeek Harness 加上 REA 技能和工具</td><td>✅ 是</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-casebook"><img src="https://raw.githubusercontent.com/pablodiazjorge/rea-casebook/main/media/session-dark.png" width="160" alt="pablodiazjorge/rea-casebook"></a></td><td><a href="https://github.com/pablodiazjorge/rea-casebook"><b>rea-casebook</b></a><br><sub>pablodiazjorge</sub></td><td>讓 Claude Code 的每項結論都引用真實的 REA 證據</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/jinshi666888/rea-playbook"><img src="https://raw.githubusercontent.com/jinshi666888/rea-playbook/main/docs/assets/demo.gif" width="160" alt="jinshi666888/rea-playbook"></a></td><td><a href="https://github.com/jinshi666888/rea-playbook"><b>rea-playbook</b></a><br><sub>jinshi666888</sub></td><td>附迷你 Electron 靶機的 REA 實作練習</td><td>✅ 是</td><td><sub>專案 README</sub></td></tr>
<tr><td><a href="https://github.com/dav1dngy/era-agent"><img src="https://raw.githubusercontent.com/dav1dngy/era-agent/main/docs/assets/screenshots/01-main-workspace.png" width="160" alt="dav1dngy/era-agent"></a></td><td><a href="https://github.com/dav1dngy/era-agent"><b>era-agent</b></a><br><sub>dav1dngy</sub></td><td>證據驅動、會嘗試自我改進的逆向工程 AI 代理</td><td>❔ 待驗證</td><td><sub>專案 README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/tanepiper/game-frame"><b>game-frame</b></a><br><sub>tanepiper</sub></td><td>讓 AI agent 從發行檔案逆向遊戲的框架</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/agioracle/rea-unity-game"><b>rea-unity-game</b></a><br><sub>agioracle</sub></td><td>用 agent 逆向 Unity 遊戲的工作流程</td><td>❔ 待驗證</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/aicodeking/leanrea"><b>leanrea</b></a><br><sub>aicodeking</sub></td><td>輕量 skill，替代 REA 的 MCP 層，讓 agent 直接呼叫 CLI 工具</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/cranebeaker/coop-anything"><b>coop-anything</b></a><br><sub>cranebeaker</sub></td><td>用 REA 調查入口，為單機遊戲添加合作模式的 MCP 伺服器與技能</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/MiaAI-Lab/sparkDash"><b>sparkDash</b></a><br><sub>MiaAI-Lab</sub></td><td>整合 REA 長時分析任務、按需載入結果的多裝置儀表板</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/orikami048/gea"><img src="images/gea-card.png" width="160" alt="orikami048/gea"></a></td><td><a href="https://github.com/orikami048/gea"><b>gea</b></a><br><sub>orikami048</sub></td><td>遊戲逆向、資源提取與 Cocos/Three.js 重現的 MCP 與 CLI；受 morluto/rea 啟發。</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Stijnus/dsh-rev-eng"><b>dsh-rev-eng</b></a><br><sub>Stijnus</sub></td><td>將 REA 技能與可選 MCP 打包為 DSH 插件，用於逆向工程與 Mac 應用建構。</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/CurLeaf/dsh-command-rea"><b>dsh-command-rea</b></a><br><sub>CurLeaf</sub></td><td>DSH /rea 斜線命令，將逆向分析請求路由到 REA 技能與 MCP 工具。</td><td>✅ 是</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/alexgaoth/awesome-reverse-engineered"><b>awesome-reverse-engineered</b></a><br><sub>alexgaoth</sub></td><td>一個很大的可搜尋目錄，收錄了超過 1.7 萬個開源專案。這些專案存在是因為有人把閉源的應用、遊戲、API 或裝置逆向了。它還有自己的搜尋網站和 MCP，方便 AI 查詢。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/SubmitGame/awesome-decomp-games"><b>awesome-decomp-games</b></a><br><sub>SubmitGame</sub></td><td>評級並自動刷新的遊戲反編譯、靜態重編譯、源碼移植與引擎重製列表</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/wtsxdev/reverse-engineering"><b>reverse-engineering</b></a><br><sub>wtsxDev</sub></td><td>經典的逆向工程資源、工具與學習資料精選列表</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/cyberkaida/reverse-engineering-assistant"><img src="images/reva-card.jpg" width="160" alt="cyberkaida/reverse-engineering-assistant"></a></td><td><a href="https://github.com/cyberkaida/reverse-engineering-assistant"><b>reverse-engineering-assistant</b></a><br><sub>cyberkaida</sub></td><td>另一種讓 AI 控制 Ghidra（NSA 出的免費逆向工具）的方法。它給 AI 很多小而專注的工具，這樣分析大程式時不容易暈。</td><td>否</td><td><sub>儲存庫卡片</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/radareorg/radare2-mcp"><b>radare2-mcp</b></a><br><sub>radareorg</sub></td><td>radare2 官方 MCP stdio 伺服器</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/radareorg/r2ai"><b>r2ai</b></a><br><sub>radareorg</sub></td><td>radare2 的基於 LLM 的逆向工具與插件</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/fosdickio/binary_ninja_mcp"><b>binary_ninja_mcp</b></a><br><sub>fosdickio</sub></td><td>讓 LLM Agent 驅動 Binary Ninja 的 MCP 伺服器（反編譯、交叉參照、重新命名、註解）。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/zinja-coder/jadx-ai-mcp"><b>jadx-ai-mcp</b></a><br><sub>zinja-coder</sub></td><td>JADX 的 MCP 外掛，讓 AI Agent 反編譯並瀏覽 Android APK / DEX。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/JusticeRage/Gepetto"><b>Gepetto</b></a><br><sub>JusticeRage</sub></td><td>IDA Pro 外掛，用語言模型在逆向過程中解釋、重新命名與註解函式。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/symgraph/GhidrAssist"><b>GhidrAssist</b></a><br><sub>symgraph</sub></td><td>Ghidra 的 LLM 擴充，輔助重新命名、解釋與分析反編譯程式碼。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/albertan017/LLM4Decompile"><b>LLM4Decompile</b></a><br><sub>albertan017</sub></td><td>基於 LLM 的二進位反編譯研究模型與工具（開源權重）。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/alphaSeclab/awesome-reverse-engineering"><b>awesome-reverse-engineering</b></a><br><sub>alphaSeclab</sub></td><td>涵蓋主流平台與領域的大型逆向工程工具與資源精選列表。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/morluto/awesome-reverse-engineering"><b>awesome-reverse-engineering</b></a><br><sub>morluto</sub></td><td>逆向工具與學習資源的精選入門列表（二進位、應用、韌體、格式、協定）。由 REA 作者維護。</td><td>否</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/nforest/awesome-decompilation"><b>awesome-decompilation</b></a><br><sub>nforest</sub></td><td>反編譯相關資源、論文、中間表示與專案的精選列表。</td><td>否</td><td><sub>—</sub></td></tr>
</table>

## REA 官方 Showcase

<table>
<tr><th width="170">圖片</th><th>專案</th><th>簡介</th><th>使用 rea</th><th>圖片來源</th></tr>
<tr><td><a href="https://rea.tools/showcase/dx-ball/"><img src="images/showcase-dx-ball.png" width="160" alt="DX-Ball: sound-pan function"></a></td><td><a href="https://rea.tools/showcase/dx-ball/"><b>DX-Ball: sound-pan function</b></a></td><td>看 REA 把 DX-Ball 的一個音效函式還原成逐位元組一致的 C</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/notion/"><img src="images/showcase-notion.png" width="160" alt="Notion: Electron clipboard bridge"></a></td><td><a href="https://rea.tools/showcase/notion/"><b>Notion: Electron clipboard bridge</b></a></td><td>跟著一次 Notion 複製操作，從頁面一路追進 IPC 和主行程</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/th04/"><img src="images/showcase-th04.png" width="160" alt="TH04: PC-98 bullet-ring maths"></a></td><td><a href="https://rea.tools/showcase/th04/"><b>TH04: PC-98 bullet-ring maths</b></a></td><td>從 16 位元 DOS 程式碼裡找回東方幻想鄉的彈幕角度演算法</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/aegis/"><img src="images/showcase-aegis.png" width="160" alt="Aegis: TOTP code generation"></a></td><td><a href="https://rea.tools/showcase/aegis/"><b>Aegis: TOTP code generation</b></a></td><td>看清 Aegis Android App 究竟如何產生兩步驟驗證碼</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/ctf/"><img src="images/showcase-ctf.png" width="160" alt="CTF: flag checker"></a></td><td><a href="https://rea.tools/showcase/ctf/"><b>CTF: flag checker</b></a></td><td>一步步解開 DownUnderCTF 2023 的逆向題</td><td>✅ 是</td><td><sub>本儲存庫截圖</sub></td></tr>
</table>

---

另見 / 致謝：許多 REA 社群條目參考並比對了 [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)。

貢獻指南見 [CONTRIBUTING.md](CONTRIBUTING.md)。授權：[CC0-1.0](LICENSE)。
