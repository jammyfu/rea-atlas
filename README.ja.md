[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# REA Atlas：リバースエンジニアリング・プロジェクトマップ（rea タグ付き）

オープンなリバースエンジニアリング・プロジェクトのマップです。ゲームの逆コンパイル、静的再コンパイル、再実装、アセット抽出ツール、汎用 RE ツール、アプリ／プロトコル／ファームウェア解析を収録し、各項目に [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）の使用有無 **Uses rea: Yes / No / Unverified** を付けています。Yes は公開された根拠がある場合のみです。

> 非公式であり、morluto/rea とは無関係です。

## 目次

- [REA を使用したプロジェクト（証拠付きサブセット）](#rea-を使用したプロジェクト証拠付きサブセット)
- [ゲーム](#ゲーム)
  - [ファミコン / NES](#ファミコン--nes)
  - [スーパーファミコン / SNES](#スーパーファミコン--snes)
  - [メガドライブ / Genesis](#メガドライブ--genesis)
  - [セガサターン](#セガサターン)
  - [ゲームボーイ](#ゲームボーイ)
  - [ゲームボーイアドバンス](#ゲームボーイアドバンス)
  - [NINTENDO64](#nintendo64)
  - [ゲームキューブ](#ゲームキューブ)
  - [Wii](#wii)
  - [ニンテンドーDS](#ニンテンドーds)
  - [ニンテンドー3DS](#ニンテンドー3ds)
  - [PlayStation](#playstation)
  - [PlayStation 2](#playstation-2)
  - [Xbox / Xbox 360](#xbox--xbox-360)
  - [PC / DOS / PC-98](#pc--dos--pc-98)
- [アプリ / Electron / デスクトップ](#アプリ--electron--デスクトップ)
- [プロトコル / ハードウェア](#プロトコル--ハードウェア)
- [ファームウェア / ドライバ](#ファームウェア--ドライバ)
- [セキュリティ / 評価](#セキュリティ--評価)
- [リバースエンジニアリングツール](#リバースエンジニアリングツール)
- [REA 公式ショーケース](#rea-公式ショーケース)

## REA を使用したプロジェクト（証拠付きサブセット）

_任意のフィルタ：以下は REA を使用した公開証拠があるプロジェクトです。マップの大半は通常の逆解析プロジェクトで、REA は必須ではありません。_

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/morluto/rea/discussions/2254"><img src="images/rea-discussion-2254.png" width="160" alt="REA discussion #2254"></a></td><td><a href="https://github.com/morluto/rea/discussions/2254"><b>REA discussion #2254</b></a></td><td>シンボルなし bzip2 を解析し、元のビルドと照合</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/aicodeking/leanrea"><b>leanrea</b></a><br><sub>aicodeking</sub></td><td>REA の MCP 層を置き換える軽量スキル。エージェントが CLI ツールを直接駆動</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/cranebeaker/coop-anything"><b>coop-anything</b></a><br><sub>cranebeaker</sub></td><td>REA でエントリポイントを調査し、シングルプレイゲームに協力モードを追加する MCP サーバー</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Caho1/open-claude-ui"><b>open-claude-ui</b></a><br><sub>Caho1</sub></td><td>REA で Claude Desktop の UI とインタラクション物理を抽出した高忠実度リビルド</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/MiaAI-Lab/sparkDash"><b>sparkDash</b></a><br><sub>MiaAI-Lab</sub></td><td>長時間の REA 分析ジョブを統合し、結果をオンデマンドで読み込むマルチデバイスダッシュボード</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/terminal-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/terminal-rs/master/docs/img/overview.png" width="160" alt="michaelshimeles/terminal-rs"></a></td><td><a href="https://github.com/michaelshimeles/terminal-rs"><b>terminal-rs</b></a><br><sub>michaelshimeles</sub></td><td>Rust 製の Bloomberg 風トレーディング端末</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="160" alt="ShadowSwaps/REA-Reconstruction-Companion"></a></td><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><b>REA-Reconstruction-Companion</b></a><br><sub>ShadowSwaps</sub></td><td>再構築を常に証拠と結びつけるエージェントスキル</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/rec-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="160" alt="michaelshimeles/rec-rs"></a></td><td><a href="https://github.com/michaelshimeles/rec-rs"><b>rec-rs</b></a><br><sub>michaelshimeles</sub></td><td>OBS を参考にした Rust 製の高速 macOS 録画ツール</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Xiangyu-CAS/rea-capcut"><b>rea-capcut</b></a><br><sub>Xiangyu-CAS</sub></td><td>REA で CapCut を調べて作り直したオープンソースのオフライン動画編集</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/dx-ball"><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="160" alt="N0zoM1z0/dx-ball"></a></td><td><a href="https://github.com/N0zoM1z0/dx-ball"><b>dx-ball</b></a><br><sub>N0zoM1z0</sub></td><td>DX-Ball 1.07 を C/C++ で再構築、元の x86 と照合テスト</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/sketch"><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="160" alt="michaelshimeles/sketch"></a></td><td><a href="https://github.com/michaelshimeles/sketch"><b>sketch</b></a><br><sub>michaelshimeles</sub></td><td>Paper を研究して作った Rust 製の無限デザインキャンバス</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/giveen/decomp.anything"><b>decomp.anything</b></a><br><sub>giveen</sub></td><td>更新停止したマッチング型デコンパイラ decomp.wtf の継続フォーク。Windows/Linux バイナリ対応と REA 連携を追加し、ゲーム以外のプログラムもエージェントが解析できるようにした。</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="160" alt="Moxnatiy/OpenBattlefield2"></a></td><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><b>OpenBattlefield2</b></a><br><sub>Moxnatiy</sub></td><td>バトルフィールド 2 のエンジンを C++20 でクリーンルーム再実装（手持ちの製品版を使用）</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/czcdr/dsh-plugin-rea"><img src="https://raw.githubusercontent.com/czcdr/dsh-plugin-rea/main/assets/screenshot-1.png" width="160" alt="czcdr/dsh-plugin-rea"></a></td><td><a href="https://github.com/czcdr/dsh-plugin-rea"><b>dsh-plugin-rea</b></a><br><sub>czcdr</sub></td><td>DeepSeek Harness で REA を、Ghidra も自動導入</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/0xshlomil/ida-free-mcp"><img src="https://opengraph.githubassets.com/1/0xshlomil/ida-free-mcp" width="160" alt="0xshlomil/ida-free-mcp"></a></td><td><a href="https://github.com/0xshlomil/ida-free-mcp"><b>ida-free-mcp</b></a><br><sub>0xshlomil</sub></td><td>MCP 経由で AI エージェントから IDA Free を使う</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/lxistired/ledger-reborn"><img src="https://raw.githubusercontent.com/lxistired/ledger-reborn/main/docs/screenshots/accounting.png" width="160" alt="lxistired/ledger-reborn"></a></td><td><a href="https://github.com/lxistired/ledger-reborn"><b>ledger-reborn</b></a><br><sub>lxistired</sub></td><td>QuickBooks for Mac を参考にしたローカル優先の会計アプリ</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/glauberlima/open-scrantic"><b>open-scrantic</b></a><br><sub>glauberlima</sub></td><td>REA で逆解析した 1992 年 Johnny Castaway スクリーンセーバーの Rust 再実装</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th04"><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th04"></a></td><td><a href="https://github.com/N0zoM1z0/th04"><b>th04</b></a><br><sub>N0zoM1z0</sub></td><td>東方幻想郷（PC-98）を読めるソースに、当時のコンパイラで検証</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/rodneypantonial/sims3-modernization"><b>sims3-modernization</b></a><br><sub>rodneypantonial</sub></td><td>最新 PC でシムズ3 のカクつきとクラッシュを減らす</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/tanepiper/game-frame"><b>game-frame</b></a><br><sub>tanepiper</sub></td><td>配布ファイルからエージェントがゲームを解析するフレームワーク</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/alexmi256/rea-agent-docker"><img src="https://opengraph.githubassets.com/1/alexmi256/rea-agent-docker" width="160" alt="alexmi256/rea-agent-docker"></a></td><td><a href="https://github.com/alexmi256/rea-agent-docker"><b>rea-agent-docker</b></a><br><sub>alexmi256</sub></td><td>Ghidra・Hopper・IDA 版がある REA の Docker イメージ</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/EndLess728/MiTV-Remote"><b>MiTV-Remote</b></a><br><sub>EndLess728</sub></td><td>Mac・Android・iPhone から Wi-Fi で Xiaomi テレビを操作</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/nicolvus/a6000-fw-decomp"><b>a6000-fw-decomp</b></a><br><sub>nicolvus</sub></td><td>REA と Ghidra で Sony A6000 のファームウェアを解析</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="160" alt="ucodia/desktop-games-nostalgia"></a></td><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><b>desktop-games-nostalgia</b></a><br><sub>ucodia</sub></td><td>デスクトップをまた壊そう：Gemtree の 2000 年作を macOS とブラウザへ</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/sickpyramid/ReaFuse"><img src="https://opengraph.githubassets.com/1/sickpyramid/ReaFuse" width="160" alt="sickpyramid/ReaFuse"></a></td><td><a href="https://github.com/sickpyramid/ReaFuse"><b>ReaFuse</b></a><br><sub>sickpyramid</sub></td><td>REA を使って 2 つの JS/TS プロジェクトを融合</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-lab"><img src="https://opengraph.githubassets.com/1/pablodiazjorge/rea-lab" width="160" alt="pablodiazjorge/rea-lab"></a></td><td><a href="https://github.com/pablodiazjorge/rea-lab"><b>rea-lab</b></a><br><sub>pablodiazjorge</sub></td><td>Windows + Ghidra の演習と事前登録した REA 評価</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/grisuno/VSL-DSP"><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="160" alt="grisuno/VSL-DSP"></a></td><td><a href="https://github.com/grisuno/VSL-DSP"><b>VSL-DSP</b></a><br><sub>grisuno</sub></td><td>PreSonus AudioBox VSL 用の Linux カーネルモジュール</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="160" alt="NullLabTests/OpenBSD_netcat_REA"></a></td><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><b>OpenBSD_netcat_REA</b></a><br><sub>NullLabTests</sub></td><td>REA と Ghidra で netcat-openbsd を静的解析</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/iammukeshm/hexgrab"><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="160" alt="iammukeshm/hexgrab"></a></td><td><a href="https://github.com/iammukeshm/hexgrab"><b>hexgrab</b></a><br><sub>iammukeshm</sub></td><td>PowerToys のバイナリを調べて作った小さな Windows カラーピッカー</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/cudanexus/vd-streamer-linux"><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="160" alt="cudanexus/vd-streamer-linux"></a></td><td><a href="https://github.com/cudanexus/vd-streamer-linux"><b>vd-streamer-linux</b></a><br><sub>cudanexus</sub></td><td>Linux デスクトップを Quest・Pico へストリーミング</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/zhaofeng130/dsh-rea"><img src="https://opengraph.githubassets.com/1/zhaofeng130/dsh-rea" width="160" alt="zhaofeng130/dsh-rea"></a></td><td><a href="https://github.com/zhaofeng130/dsh-rea"><b>dsh-rea</b></a><br><sub>zhaofeng130</sub></td><td>DeepSeek Harness に REA のスキルとツールを追加</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-casebook"><img src="https://raw.githubusercontent.com/pablodiazjorge/rea-casebook/main/media/session-dark.png" width="160" alt="pablodiazjorge/rea-casebook"></a></td><td><a href="https://github.com/pablodiazjorge/rea-casebook"><b>rea-casebook</b></a><br><sub>pablodiazjorge</sub></td><td>Claude Code の結論すべてに実際の REA 証拠を引用させる</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/B-Howell/soundconnect-desktop"><b>soundconnect-desktop</b></a><br><sub>B-Howell</sub></td><td>Windows デスクトップから Sony の Bluetooth ヘッドホンを操作</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="160" alt="tuunanet/rea-ski-or-die-reconstruction"></a></td><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><b>rea-ski-or-die-reconstruction</b></a><br><sub>tuunanet</sub></td><td>Ski or Die の雪合戦を Rust + SDL2 で再現（素材は各自用意）</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/OpenRsG/GunZRs"><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="160" alt="OpenRsG/GunZRs"></a></td><td><a href="https://github.com/OpenRsG/GunZRs"><b>GunZRs</b></a><br><sub>OpenRsG</sub></td><td>GunZ: The Duel を Rust + Bevy で復活</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><img src="https://opengraph.githubassets.com/1/sheilacraig/dsh-rea-mcp" width="160" alt="sheilacraig/dsh-rea-mcp"></a></td><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><b>dsh-rea-mcp</b></a><br><sub>sheilacraig</sub></td><td>設定だけで DeepSeek Harness に REA を組み込む</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/a-barzanti/ai-rebuilds"><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="160" alt="a-barzanti/ai-rebuilds"></a></td><td><a href="https://github.com/a-barzanti/ai-rebuilds"><b>ai-rebuilds</b></a><br><sub>a-barzanti</sub></td><td>見捨てられたゲームをブラウザで復活、元ファイルは含まない</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/Nowng/rea-mcp"><img src="https://opengraph.githubassets.com/1/Nowng/rea-mcp" width="160" alt="Nowng/rea-mcp"></a></td><td><a href="https://github.com/Nowng/rea-mcp"><b>rea-mcp</b></a><br><sub>Nowng</sub></td><td>LM Studio のローカルモデルで REA を使う</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><img src="https://opengraph.githubassets.com/1/ya123-4/rea-dsh-plugin" width="160" alt="ya123-4/rea-dsh-plugin"></a></td><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><b>rea-dsh-plugin</b></a><br><sub>ya123-4</sub></td><td>DeepSeek Harness に REA の MCP ツールを登録</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><img src="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg" width="160" alt="az9713/wispr-flow-rea-teardown"></a></td><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><b>wispr-flow-rea-teardown</b></a><br><sub>az9713</sub></td><td>Wispr Flow の音声パイプラインを分解、64 行の再実装付き</td><td>✅ はい</td><td><sub><a href="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg">動画サムネイル</a></sub></td></tr>
<tr><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><img src="https://opengraph.githubassets.com/1/KarlssonChristoffer/DiskLens" width="160" alt="KarlssonChristoffer/DiskLens"></a></td><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><b>DiskLens</b></a><br><sub>KarlssonChristoffer</sub></td><td>WinDirStat 風に Windows 11 のディスク使用量を可視化</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/cognixws/picode-rea"><img src="https://opengraph.githubassets.com/1/cognixws/picode-rea" width="160" alt="cognixws/picode-rea"></a></td><td><a href="https://github.com/cognixws/picode-rea"><b>picode-rea</b></a><br><sub>cognixws</sub></td><td>PiCode から REA の静的解析ツールを使う</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/jinshi666888/rea-playbook"><img src="https://raw.githubusercontent.com/jinshi666888/rea-playbook/main/docs/assets/demo.gif" width="160" alt="jinshi666888/rea-playbook"></a></td><td><a href="https://github.com/jinshi666888/rea-playbook"><b>rea-playbook</b></a><br><sub>jinshi666888</sub></td><td>小さな Electron ターゲット付きの REA ハンズオン</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><img src="https://opengraph.githubassets.com/1/UnknownHacker1/rea-groundtruth" width="160" alt="UnknownHacker1/rea-groundtruth"></a></td><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><b>rea-groundtruth</b></a><br><sub>UnknownHacker1</sub></td><td>REA のレポートを実際のソースと突き合わせる</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/dx-ball/"><img src="images/showcase-dx-ball.png" width="160" alt="DX-Ball: sound-pan function"></a></td><td><a href="https://rea.tools/showcase/dx-ball/"><b>DX-Ball: sound-pan function</b></a></td><td>REA が DX-Ball の音響関数をバイト単位で一致する C に戻す過程</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/notion/"><img src="images/showcase-notion.png" width="160" alt="Notion: Electron clipboard bridge"></a></td><td><a href="https://rea.tools/showcase/notion/"><b>Notion: Electron clipboard bridge</b></a></td><td>Notion のコピー操作をページから IPC、メインプロセスまで追跡</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/th04/"><img src="images/showcase-th04.png" width="160" alt="TH04: PC-98 bullet-ring maths"></a></td><td><a href="https://rea.tools/showcase/th04/"><b>TH04: PC-98 bullet-ring maths</b></a></td><td>16 ビット DOS コードから東方幻想郷の弾幕角度計算を復元</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/aegis/"><img src="images/showcase-aegis.png" width="160" alt="Aegis: TOTP code generation"></a></td><td><a href="https://rea.tools/showcase/aegis/"><b>Aegis: TOTP code generation</b></a></td><td>Aegis（Android）が二段階認証コードを生成する仕組みを解明</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/ctf/"><img src="images/showcase-ctf.png" width="160" alt="CTF: flag checker"></a></td><td><a href="https://rea.tools/showcase/ctf/"><b>CTF: flag checker</b></a></td><td>DownUnderCTF 2023 のリバーシング問題を順に解く</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/AdamLinCodes/AdamTerm"><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="160" alt="AdamLinCodes/AdamTerm"></a></td><td><a href="https://github.com/AdamLinCodes/AdamTerm"><b>AdamTerm</b></a><br><sub>AdamLinCodes</sub></td><td>Ghostty を調べて作ったミニマルな macOS ターミナル</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/az9713/REA-demo"><img src="https://opengraph.githubassets.com/1/az9713/REA-demo" width="160" alt="az9713/REA-demo"></a></td><td><a href="https://github.com/az9713/REA-demo"><b>REA-demo</b></a><br><sub>az9713</sub></td><td>REA が自分自身を解析、反証可能な予測付き</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/chilliesdev/fmseasonhub-re"><b>fmseasonhub-re</b></a><br><sub>chilliesdev</sub></td><td>REA で FM Season Hub アプリを解析したノート</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/carlhako/keen-clone"><b>keen-clone</b></a><br><sub>carlhako</sub></td><td>REA + Ghidra で関数単位に復元した Commander Keen 1 のネイティブ Linux/SDL2 再実装</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/NathanKanaeru/samp-client-re"><b>samp-client-re</b></a><br><sub>NathanKanaeru</sub></td><td>REA/Ghidra でアーキテクチャを復元した SA-MP 0.3.DL-R1 のクリーンルームクライアント再実装</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Stijnus/dsh-rev-eng"><b>dsh-rev-eng</b></a><br><sub>Stijnus</sub></td><td>REA スキルとオプションの MCP をパッケージした DSH プラグイン。リバースエンジニアリングと Mac アプリ構築用。</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/CurLeaf/dsh-command-rea"><b>dsh-command-rea</b></a><br><sub>CurLeaf</sub></td><td>DSH の /rea スラッシュコマンド。リクエストを REA スキルと MCP ツールにルーティング。</td><td>✅ はい</td><td><sub>—</sub></td></tr>
</table>

## ゲーム

### ファミコン / NES

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/aldonunez/zelda1-disassembly"><img src="https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png" width="160" alt="aldonunez/zelda1-disassembly"></a></td><td><a href="https://github.com/aldonunez/zelda1-disassembly"><b>zelda1-disassembly</b></a><br><sub>aldonunez</sub></td><td>初代ゼルダの伝説（FC）を完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

#### アセット抽出・ツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/SourMesen/Mesen2"><img src="https://opengraph.githubassets.com/1/SourMesen/Mesen2" width="160" alt="SourMesen/Mesen2"></a></td><td><a href="https://github.com/SourMesen/Mesen2"><b>Mesen2</b></a><br><sub>SourMesen</sub></td><td>強力なデバッグ機能付きのマルチシステムエミュレータ</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

### スーパーファミコン / SNES

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/snesrev/zelda3"><img src="https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg" width="160" alt="snesrev/zelda3"></a></td><td><a href="https://github.com/snesrev/zelda3"><b>zelda3</b></a><br><sub>snesrev</sub></td><td>神々のトライフォースを C で再実装、ワイド対応（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/snesrev/sm"><img src="https://upload.wikimedia.org/wikipedia/en/e/e4/Smetroidbox.jpg" width="160" alt="snesrev/sm"></a></td><td><a href="https://github.com/snesrev/sm"><b>sm</b></a><br><sub>snesrev</sub></td><td>スーパーメトロイドを C で再実装（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/e/e4/Smetroidbox.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/snesrev/smw"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png" width="160" alt="snesrev/smw"></a></td><td><a href="https://github.com/snesrev/smw"><b>smw</b></a><br><sub>snesrev</sub></td><td>スーパーマリオワールドを C で再実装（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

### メガドライブ / Genesis

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/sonicretro/s1disasm"><img src="https://upload.wikimedia.org/wikipedia/en/b/ba/Sonic_the_Hedgehog_1_Genesis_box_art.jpg" width="160" alt="sonicretro/s1disasm"></a></td><td><a href="https://github.com/sonicretro/s1disasm"><b>s1disasm</b></a><br><sub>sonicretro</sub></td><td>ソニック・ザ・ヘッジホッグ（メガドライブ）を完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/b/ba/Sonic_the_Hedgehog_1_Genesis_box_art.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/sonicretro/s2disasm"><img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Sonic_2_US_Cover.jpg" width="160" alt="sonicretro/s2disasm"></a></td><td><a href="https://github.com/sonicretro/s2disasm"><b>s2disasm</b></a><br><sub>sonicretro</sub></td><td>ソニック 2（メガドライブ）を完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0c/Sonic_2_US_Cover.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/sonicretro/skdisasm"><img src="https://upload.wikimedia.org/wikipedia/en/d/d3/Sonic_%26_Knuckles_cover.jpg" width="160" alt="sonicretro/skdisasm"></a></td><td><a href="https://github.com/sonicretro/skdisasm"><b>skdisasm</b></a><br><sub>sonicretro</sub></td><td>ソニック 3 &amp; ナックルズを完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/d/d3/Sonic_%26_Knuckles_cover.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/RSDKModding/RSDKv4-Decompilation"><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv4-Decompilation/main/header.png?raw=true" width="160" alt="RSDKModding/RSDKv4-Decompilation"></a></td><td><a href="https://github.com/RSDKModding/RSDKv4-Decompilation"><b>RSDKv4-Decompilation</b></a><br><sub>RSDKModding</sub></td><td>ソニック 1・2（2013）のエンジンを逆コンパイル</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/RSDKModding/RSDKv5-Decompilation"><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv5-Decompilation/master/header.png?raw=true" width="160" alt="RSDKModding/RSDKv5-Decompilation"></a></td><td><a href="https://github.com/RSDKModding/RSDKv5-Decompilation"><b>RSDKv5-Decompilation</b></a><br><sub>RSDKModding</sub></td><td>ソニックマニアのエンジンを逆コンパイル（手持ちのデータを使用）</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
</table>

### セガサターン

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/yaz0r/Azel"><img src="https://github.com/user-attachments/assets/71f6a246-24cc-4d64-9673-53b9e4c3e4df" width="160" alt="yaz0r/Azel"></a></td><td><a href="https://github.com/yaz0r/Azel"><b>Azel</b></a><br><sub>yaz0r</sub></td><td>アゼル -パンツァードラグーン RPG- を解析・再実装</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
</table>

### ゲームボーイ

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/pret/pokered"><img src="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp" width="160" alt="pret/pokered"></a></td><td><a href="https://github.com/pret/pokered"><b>pokered</b></a><br><sub>pret</sub></td><td>ポケモン 赤・緑（Red/Blue）を完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokecrystal"><img src="https://github.com/user-attachments/assets/c39cb860-bb9c-4204-9184-b2761ead0a74" width="160" alt="pret/pokecrystal"></a></td><td><a href="https://github.com/pret/pokecrystal"><b>pokecrystal</b></a><br><sub>pret</sub></td><td>ポケモン クリスタルを完全逆アセンブル</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td><a href="https://github.com/zladx/LADX-Disassembly"><img src="https://raw.githubusercontent.com/zladx/LADX-Disassembly/main/docs/entities.png" width="160" alt="zladx/LADX-Disassembly"></a></td><td><a href="https://github.com/zladx/LADX-Disassembly"><b>LADX-Disassembly</b></a><br><sub>zladx</sub></td><td>ゼルダの伝説 夢をみる島 DX を完全逆アセンブル</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeyellow"><img src="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp" width="160" alt="pret/pokeyellow"></a></td><td><a href="https://github.com/pret/pokeyellow"><b>pokeyellow</b></a><br><sub>pret</sub></td><td>ポケモン ピカチュウ（Yellow）を完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokegold"><img src="https://upload.wikimedia.org/wikipedia/en/4/4c/Pok%C3%A9mon_box_art_-_Gold_Version.png" width="160" alt="pret/pokegold"></a></td><td><a href="https://github.com/pret/pokegold"><b>pokegold</b></a><br><sub>pret</sub></td><td>ポケモン 金・銀を完全逆アセンブル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/4/4c/Pok%C3%A9mon_box_art_-_Gold_Version.png">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

### ゲームボーイアドバンス

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/pret/pokeemerald"><img src="https://user-images.githubusercontent.com/35422415/226195894-bd8307ea-f6be-46cc-85ec-dd28b4f2d144.gif" width="160" alt="pret/pokeemerald"></a></td><td><a href="https://github.com/pret/pokeemerald"><b>pokeemerald</b></a><br><sub>pret</sub></td><td>ポケモン エメラルドの C ソース、数多の改造の土台</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td><a href="https://github.com/pret/pokefirered"><img src="https://upload.wikimedia.org/wikipedia/en/a/a7/Pokemon_LeafGreen_box.jpg" width="160" alt="pret/pokefirered"></a></td><td><a href="https://github.com/pret/pokefirered"><b>pokefirered</b></a><br><sub>pret</sub></td><td>ポケモン ファイアレッド・リーフグリーンの C ソース</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a7/Pokemon_LeafGreen_box.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeruby"><img src="https://upload.wikimedia.org/wikipedia/en/b/be/PokemonRubySapphireBox.jpg" width="160" alt="pret/pokeruby"></a></td><td><a href="https://github.com/pret/pokeruby"><b>pokeruby</b></a><br><sub>pret</sub></td><td>ポケモン ルビー・サファイアの C ソース</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/b/be/PokemonRubySapphireBox.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tmc"><img src="https://upload.wikimedia.org/wikipedia/en/0/0a/TLOZ-_Minish_Cap_NA_Box_art.png" width="160" alt="zeldaret/tmc"></a></td><td><a href="https://github.com/zeldaret/tmc"><b>tmc</b></a><br><sub>zeldaret</sub></td><td>ゼルダの伝説 ふしぎのぼうしを C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0a/TLOZ-_Minish_Cap_NA_Box_art.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pmd-red"><img src="https://upload.wikimedia.org/wikipedia/en/d/d3/Pok%C3%A9mon_Mystery_Dungeon_Blue_and_Red_Rescue_Team_cover_arts.jpg" width="160" alt="pret/pmd-red"></a></td><td><a href="https://github.com/pret/pmd-red"><b>pmd-red</b></a><br><sub>pret</sub></td><td>ポケモン不思議のダンジョン 赤の救助隊を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/d/d3/Pok%C3%A9mon_Mystery_Dungeon_Blue_and_Red_Rescue_Team_cover_arts.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/jiangzhengwenjz/katam"><img src="https://upload.wikimedia.org/wikipedia/en/0/0b/Kirby_%26_the_Amazing_Mirror.jpg" width="160" alt="jiangzhengwenjz/katam"></a></td><td><a href="https://github.com/jiangzhengwenjz/katam"><b>katam</b></a><br><sub>jiangzhengwenjz</sub></td><td>星のカービィ 鏡の大迷宮を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0b/Kirby_%26_the_Amazing_Mirror.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

### NINTENDO64

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/n64decomp/sm64"><img src="https://upload.wikimedia.org/wikipedia/en/e/e9/Super_Mario_64.png" width="160" alt="n64decomp/sm64"></a></td><td><a href="https://github.com/n64decomp/sm64"><b>sm64</b></a><br><sub>n64decomp</sub></td><td>ビルド可能なスーパーマリオ 64 の C ソース（ROM は含まない）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/e/e9/Super_Mario_64.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/N64Recomp/N64Recomp"><img src="https://opengraph.githubassets.com/1/N64Recomp/N64Recomp" width="160" alt="N64Recomp/N64Recomp"></a></td><td><a href="https://github.com/N64Recomp/N64Recomp"><b>N64Recomp</b></a><br><sub>N64Recomp</sub></td><td>N64 ゲームをそのままネイティブコードへ再コンパイル</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/oot"><img src="https://github.com/user-attachments/assets/70b4a529-9a5e-4b9c-ac45-48f9f2183eed" width="160" alt="zeldaret/oot"></a></td><td><a href="https://github.com/zeldaret/oot"><b>oot</b></a><br><sub>zeldaret</sub></td><td>時のオカリナを C へ完全逆コンパイル（ROM は含まない）</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td><a href="https://github.com/HarbourMasters/Starship"><img src="https://upload.wikimedia.org/wikipedia/en/6/63/StarFox64_N64_Game_Box.jpg" width="160" alt="HarbourMasters/Starship"></a></td><td><a href="https://github.com/HarbourMasters/Starship"><b>Starship</b></a><br><sub>HarbourMasters</sub></td><td>スターフォックス 64 を PC でネイティブに（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/63/StarFox64_N64_Game_Box.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/mm"><img src="https://user-images.githubusercontent.com/12245827/191111633-e72abfd3-b53c-4d13-82d1-44e6718f1fb0.png" width="160" alt="zeldaret/mm"></a></td><td><a href="https://github.com/zeldaret/mm"><b>mm</b></a><br><sub>zeldaret</sub></td><td>ゼルダの伝説 ムジュラの仮面を C へ逆コンパイル</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td><a href="https://github.com/pmret/papermario"><img src="https://upload.wikimedia.org/wikipedia/en/6/61/Papermario.jpg" width="160" alt="pmret/papermario"></a></td><td><a href="https://github.com/pmret/papermario"><b>papermario</b></a><br><sub>pmret</sub></td><td>マリオストーリー（N64）を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/61/Papermario.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/mk64"><img src="https://upload.wikimedia.org/wikipedia/en/a/a1/Mario_Kart_64.jpg" width="160" alt="n64decomp/mk64"></a></td><td><a href="https://github.com/n64decomp/mk64"><b>mk64</b></a><br><sub>n64decomp</sub></td><td>マリオカート 64 を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a1/Mario_Kart_64.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/perfect_dark"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg" width="160" alt="n64decomp/perfect_dark"></a></td><td><a href="https://github.com/n64decomp/perfect_dark"><b>perfect_dark</b></a><br><sub>n64decomp</sub></td><td>パーフェクトダーク（N64）を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/DinosaurPlanetRecomp/dino-recomp"><img src="images/dino-recomp-card.png" width="160" alt="DinosaurPlanetRecomp/dino-recomp"></a></td><td><a href="https://github.com/DinosaurPlanetRecomp/dino-recomp"><b>dino-recomp</b></a><br><sub>DinosaurPlanetRecomp</sub></td><td>N64 プロトタイプの Dinosaur Planet を静的再コンパイルでネイティブ PC ポートに。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/bryantmh/rush2recompiled"><img src="images/rush2recompiled-card.png" width="160" alt="bryantmh/rush2recompiled"></a></td><td><a href="https://github.com/bryantmh/rush2recompiled"><b>rush2recompiled</b></a><br><sub>bryantmh</sub></td><td>N64 の Rush 2 を事前に翻訳して、ネイティブ PC で動かすプロジェクト。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/Zelda64Recomp/Zelda64Recomp"><img src="https://raw.githubusercontent.com/Zelda64Recomp/Zelda64Recomp/dev/docs/deck_gyro_1.jpg" width="160" alt="Zelda64Recomp/Zelda64Recomp"></a></td><td><a href="https://github.com/Zelda64Recomp/Zelda64Recomp"><b>Zelda64Recomp</b></a><br><sub>Zelda64Recomp</sub></td><td>ムジュラの仮面を PC 向けに再コンパイル、現代的な操作に（ROM は各自）</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/HarbourMasters/Shipwright"><img src="https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg" width="160" alt="HarbourMasters/Shipwright"></a></td><td><a href="https://github.com/HarbourMasters/Shipwright"><b>Shipwright</b></a><br><sub>HarbourMasters</sub></td><td>ゼルダの伝説 時のオカリナを PC でネイティブに（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/2ship2harkinian/2ship2harkinian"><img src="https://upload.wikimedia.org/wikipedia/en/6/60/The_Legend_of_Zelda_-_Majora%27s_Mask_Box_Art.jpg" width="160" alt="2ship2harkinian/2ship2harkinian"></a></td><td><a href="https://github.com/2ship2harkinian/2ship2harkinian"><b>2ship2harkinian</b></a><br><sub>2ship2harkinian</sub></td><td>ムジュラの仮面を PC でネイティブに（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/60/The_Legend_of_Zelda_-_Majora%27s_Mask_Box_Art.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

#### アセット抽出・ツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/ethteck/splat"><img src="https://opengraph.githubassets.com/1/ethteck/splat" width="160" alt="ethteck/splat"></a></td><td><a href="https://github.com/ethteck/splat"><b>splat</b></a><br><sub>ethteck</sub></td><td>N64・PS1 のバイナリを逆コンパイル用プロジェクトに分割</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/NEstelami/ZAPD"><img src="https://raw.githubusercontent.com/NEstelami/ZAPD/master/docs/zapd_warning_example.png?raw=true" width="160" alt="NEstelami/ZAPD"></a></td><td><a href="https://github.com/NEstelami/ZAPD"><b>ZAPD</b></a><br><sub>NEstelami</sub></td><td>ゼルダ 64 のアセットを編集可能なソースへ変換</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
</table>

### ゲームキューブ

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/doldecomp/melee"><img src="https://upload.wikimedia.org/wikipedia/en/7/75/Super_Smash_Bros_Melee_box_art.png" width="160" alt="doldecomp/melee"></a></td><td><a href="https://github.com/doldecomp/melee"><b>melee</b></a><br><sub>doldecomp</sub></td><td>大乱闘スマッシュブラザーズ DX を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/7/75/Super_Smash_Bros_Melee_box_art.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tp"><img src="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Twilight_Princess_Game_Cover.jpg" width="160" alt="zeldaret/tp"></a></td><td><a href="https://github.com/zeldaret/tp"><b>tp</b></a><br><sub>zeldaret</sub></td><td>ゼルダの伝説 トワイライトプリンセスを C++ へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Twilight_Princess_Game_Cover.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tww"><img src="https://upload.wikimedia.org/wikipedia/en/7/79/The_Legend_of_Zelda_The_Wind_Waker.jpg" width="160" alt="zeldaret/tww"></a></td><td><a href="https://github.com/zeldaret/tww"><b>tww</b></a><br><sub>zeldaret</sub></td><td>ゼルダの伝説 風のタクトを C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/7/79/The_Legend_of_Zelda_The_Wind_Waker.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/projectPiki/pikmin2"><img src="https://upload.wikimedia.org/wikipedia/en/3/38/Pikmin_2_Case.jpg" width="160" alt="projectPiki/pikmin2"></a></td><td><a href="https://github.com/projectPiki/pikmin2"><b>pikmin2</b></a><br><sub>projectPiki</sub></td><td>ピクミン 2 を C++ へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/38/Pikmin_2_Case.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/doldecomp/sms"><img src="https://upload.wikimedia.org/wikipedia/en/0/05/Super_Mario_Sunshine_Box_Art.png" width="160" alt="doldecomp/sms"></a></td><td><a href="https://github.com/doldecomp/sms"><b>sms</b></a><br><sub>doldecomp</sub></td><td>スーパーマリオサンシャインを C++ へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/05/Super_Mario_Sunshine_Box_Art.png">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/Hero88go/melee-unlocked"><img src="images/melee-unlocked-card.png" width="160" alt="Hero88go/melee-unlocked"></a></td><td><a href="https://github.com/Hero88go/melee-unlocked"><b>melee-unlocked</b></a><br><sub>Hero88go</sub></td><td>Super Smash Bros. Melee のデコンパイルソースからネイティブ Windows ビルドを作り、フレームレートを解除。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

#### アセット抽出・ツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/encounter/objdiff"><img src="https://raw.githubusercontent.com/encounter/objdiff/main/assets/screen-symbols.png" width="160" alt="encounter/objdiff"></a></td><td><a href="https://github.com/encounter/objdiff"><b>objdiff</b></a><br><sub>encounter</sub></td><td>逆コンパイルした関数のどこが違うか一目で分かる</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/encounter/decomp-toolkit"><img src="https://opengraph.githubassets.com/1/encounter/decomp-toolkit" width="160" alt="encounter/decomp-toolkit"></a></td><td><a href="https://github.com/encounter/decomp-toolkit"><b>decomp-toolkit</b></a><br><sub>encounter</sub></td><td>多くの GameCube・Wii 逆コンパイルを支えるツールキット</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

### Wii

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/zeldaret/ss"><img src="https://upload.wikimedia.org/wikipedia/en/9/99/Legend_of_Zelda_Skyward_Sword_boxart.png" width="160" alt="zeldaret/ss"></a></td><td><a href="https://github.com/zeldaret/ss"><b>ss</b></a><br><sub>zeldaret</sub></td><td>ゼルダの伝説 スカイウォードソードを C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/9/99/Legend_of_Zelda_Skyward_Sword_boxart.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/DarkRTA/rb3"><img src="https://upload.wikimedia.org/wikipedia/en/3/3b/Rock_Band_3_Game_Cover.jpg" width="160" alt="DarkRTA/rb3"></a></td><td><a href="https://github.com/DarkRTA/rb3"><b>rb3</b></a><br><sub>DarkRTA</sub></td><td>ロックバンド 3（Wii）を C++ へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/3b/Rock_Band_3_Game_Cover.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

### ニンテンドーDS

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/pret/pokeheartgold"><img src="https://upload.wikimedia.org/wikipedia/en/c/cb/PokemonHGSSBox.jpg" width="160" alt="pret/pokeheartgold"></a></td><td><a href="https://github.com/pret/pokeheartgold"><b>pokeheartgold</b></a><br><sub>pret</sub></td><td>ポケモン ハートゴールド・ソウルシルバーを C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/c/cb/PokemonHGSSBox.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeplatinum"><img src="https://github.com/user-attachments/assets/157f7c15-4684-48e9-aacb-eefefbcffcec" width="160" alt="pret/pokeplatinum"></a></td><td><a href="https://github.com/pret/pokeplatinum"><b>pokeplatinum</b></a><br><sub>pret</sub></td><td>ポケモン プラチナの C ソース</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td><a href="https://github.com/tangosdev/sm64ds-decomp"><img src="images/sm64ds-decomp-card.png" width="160" alt="tangosdev/sm64ds-decomp"></a></td><td><a href="https://github.com/tangosdev/sm64ds-decomp"><b>sm64ds-decomp</b></a><br><sub>tangosdev</sub></td><td>『スーパーマリオ64 DS』をゼロからバイト単位で一致させる逆コンパイルプロジェクト。元のDS版を読みやすいC/C++ソースに復元。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/ph"><img src="https://upload.wikimedia.org/wikipedia/en/5/5e/The_Legend_of_Zelda_Phantom_Hourglass_Game_Cover.jpg" width="160" alt="zeldaret/ph"></a></td><td><a href="https://github.com/zeldaret/ph"><b>ph</b></a><br><sub>zeldaret</sub></td><td>ゼルダの伝説 夢幻の砂時計を C へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/5/5e/The_Legend_of_Zelda_Phantom_Hourglass_Game_Cover.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
</table>

### ニンテンドー3DS

#### アセット抽出・ツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/3DSGuy/Project_CTR"><img src="https://opengraph.githubassets.com/1/3DSGuy/Project_CTR" width="160" alt="3DSGuy/Project_CTR"></a></td><td><a href="https://github.com/3DSGuy/Project_CTR"><b>Project_CTR</b></a><br><sub>3DSGuy</sub></td><td>3DS のファイル形式を作成・解析（ctrtool / makerom）</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

### PlayStation

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/Xeeynamo/sotn-decomp"><img src="https://github.com/user-attachments/assets/fff7ddb2-736f-4e7d-b0ee-3c1151649773" width="160" alt="Xeeynamo/sotn-decomp"></a></td><td><a href="https://github.com/Xeeynamo/sotn-decomp"><b>sotn-decomp</b></a><br><sub>Xeeynamo</sub></td><td>悪魔城ドラキュラX 月下の夜想曲を C へ逆コンパイル</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td><a href="https://github.com/shdecompilations/silent-hill-decomp"><img src="https://upload.wikimedia.org/wikipedia/en/9/96/Silent_Hill_video_game_cover.png" width="160" alt="shdecompilations/silent-hill-decomp"></a></td><td><a href="https://github.com/shdecompilations/silent-hill-decomp"><b>silent-hill-decomp</b></a><br><sub>shdecompilations</sub></td><td>サイレントヒル（PS1）を C へ逆コンパイル中</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/9/96/Silent_Hill_video_game_cover.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/SlickAmogus/silent-hill-decomp"><img src="images/silent-hill-decomp-card.png" width="160" alt="SlickAmogus/silent-hill-decomp"></a></td><td><a href="https://github.com/SlickAmogus/silent-hill-decomp"><b>silent-hill-decomp</b></a><br><sub>SlickAmogus</sub></td><td>オリジナルの『サイレントヒル1』（PS1版）を逆コンパイルして作った、現代のPCで遊べるオープンソース移植版。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

### PlayStation 2

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/ran-j/PS2Recomp"><img src="https://opengraph.githubassets.com/1/ran-j/PS2Recomp" width="160" alt="ran-j/PS2Recomp"></a></td><td><a href="https://github.com/ran-j/PS2Recomp"><b>PS2Recomp</b></a><br><sub>ran-j</sub></td><td>PS2 ゲームをネイティブ PC 実行ファイルへ再コンパイル</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/open-goal/jak-project"><img src="https://raw.githubusercontent.com/open-goal/jak-project/master/docs/img/promosmall1.png" width="160" alt="open-goal/jak-project"></a></td><td><a href="https://github.com/open-goal/jak-project"><b>jak-project</b></a><br><sub>open-goal</sub></td><td>ジャック×ダクスターを PC でネイティブに（ディスクは各自）</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/TheRealestNwah/sotc-decomp"><img src="images/sotc-decomp-card.png" width="160" alt="TheRealestNwah/sotc-decomp"></a></td><td><a href="https://github.com/TheRealestNwah/sotc-decomp"><b>sotc-decomp</b></a><br><sub>TheRealestNwah</sub></td><td>『ワンダと巨像』（PS2版）のマッチング逆コンパイル。オリジナルのゲームコードを復元し、ネイティブPC移植を目指す。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td>—</td><td><a href="https://github.com/gothamor/gta-vcs-recomp"><b>gta-vcs-recomp</b></a><br><sub>gothamor</sub></td><td>元の PS2 ゲーム『グランド・セフト・オート：バイスシティ・ストーリーズ』の実行ファイルを再コンパイルして、ネイティブの Windows / Linux 版を作ります。ディスクイメージは自分で用意。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/thiagordsfx/urban-reign-recomp"><img src="images/urban-reign-recomp-card.png" width="160" alt="thiagordsfx/urban-reign-recomp"></a></td><td><a href="https://github.com/thiagordsfx/urban-reign-recomp"><b>urban-reign-recomp</b></a><br><sub>thiagordsfx</sub></td><td>PS2の格闘ゲーム『Urban Reign』を静的リコンパイルしてネイティブPC移植版に。60FPS・高解像度・HDテクスチャ対応。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

### Xbox / Xbox 360

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/hedge-dev/XenonRecomp"><img src="https://opengraph.githubassets.com/1/hedge-dev/XenonRecomp" width="160" alt="hedge-dev/XenonRecomp"></a></td><td><a href="https://github.com/hedge-dev/XenonRecomp"><b>XenonRecomp</b></a><br><sub>hedge-dev</sub></td><td>Xbox 360 ゲームをネイティブ C++ へ再コンパイル</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/hedge-dev/UnleashedRecomp"><img src="https://upload.wikimedia.org/wikipedia/en/a/a0/Sonic_unleashed_boxart.jpg" width="160" alt="hedge-dev/UnleashedRecomp"></a></td><td><a href="https://github.com/hedge-dev/UnleashedRecomp"><b>UnleashedRecomp</b></a><br><sub>hedge-dev</sub></td><td>ソニック ワールドアドベンチャーを PC でネイティブに（製品は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a0/Sonic_unleashed_boxart.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/MysteriousAeon/rayman3-hd-recompiled"><b>rayman3-hd-recompiled</b></a><br><sub>MysteriousAeon</sub></td><td>クローズドソースの Xbox 360『レイマン3 HD』を静的再コンパイルして Windows でネイティブに動くプログラムにしたもの。自分のゲームパッケージが必要。</td><td>いいえ</td><td><sub>—</sub></td></tr>
</table>

#### アセット抽出・ツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/xemu-project/xemu"><img src="https://user-images.githubusercontent.com/71127352/144098855-dbc7b12a-d715-4102-b45c-faeb46deabde.png" width="160" alt="xemu-project/xemu"></a></td><td><a href="https://github.com/xemu-project/xemu"><b>xemu</b></a><br><sub>xemu-project</sub></td><td>初代 Xbox のゲームを Windows・macOS・Linux で</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
</table>

### PC / DOS / PC-98

#### 逆コンパイル / 再コンパイル

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/diasurgical/DevilutionX"><img src="https://github.com/user-attachments/assets/7ac73801-ef7b-4cc1-8442-a191a2a0a1ce" width="160" alt="diasurgical/DevilutionX"></a></td><td><a href="https://github.com/diasurgical/DevilutionX"><b>DevilutionX</b></a><br><sub>diasurgical</sub></td><td>ディアブロを現行 OS で（手持ちの DIABDAT.MPQ を使用）</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/isledecomp/isle"><img src="https://upload.wikimedia.org/wikipedia/en/a/a1/Lego-island.jpg" width="160" alt="isledecomp/isle"></a></td><td><a href="https://github.com/isledecomp/isle"><b>isle</b></a><br><sub>isledecomp</sub></td><td>レゴアイランド（1997）を C++ へ逆コンパイル</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a1/Lego-island.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/openblack/bw1-decomp"><img src="images/bw1-decomp-card.png" width="160" alt="openblack/bw1-decomp"></a></td><td><a href="https://github.com/openblack/bw1-decomp"><b>bw1-decomp</b></a><br><sub>openblack</sub></td><td>クラシックPC神ゲーム『Black &amp; White 1』の逆コンパイル。元のクローズドソースをオープンソースに再構築。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/dx-ball"><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="160" alt="N0zoM1z0/dx-ball"></a></td><td><a href="https://github.com/N0zoM1z0/dx-ball"><b>dx-ball</b></a><br><sub>N0zoM1z0</sub></td><td>DX-Ball 1.07 を C/C++ で再構築、元の x86 と照合テスト</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th08"><img src="https://raw.githubusercontent.com/N0zoM1z0/th08/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th08"></a></td><td><a href="https://github.com/N0zoM1z0/th08"><b>th08</b></a><br><sub>N0zoM1z0</sub></td><td>東方永夜抄をソースコードとして再構築</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th04"><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th04"></a></td><td><a href="https://github.com/N0zoM1z0/th04"><b>th04</b></a><br><sub>N0zoM1z0</sub></td><td>東方幻想郷（PC-98）を読めるソースに、当時のコンパイラで検証</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th105"><img src="https://raw.githubusercontent.com/N0zoM1z0/th105/main/resources/title-screen.jpg" width="160" alt="N0zoM1z0/th105"></a></td><td><a href="https://github.com/N0zoM1z0/th105"><b>th105</b></a><br><sub>N0zoM1z0</sub></td><td>東方緋想天をソースコードとして再構築</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th095"><img src="https://raw.githubusercontent.com/N0zoM1z0/th095/main/resources/title-screen.jpg" width="160" alt="N0zoM1z0/th095"></a></td><td><a href="https://github.com/N0zoM1z0/th095"><b>th095</b></a><br><sub>N0zoM1z0</sub></td><td>東方文花帖をソースコードとして再構築</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th10"><img src="https://raw.githubusercontent.com/N0zoM1z0/th10/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th10"></a></td><td><a href="https://github.com/N0zoM1z0/th10"><b>th10</b></a><br><sub>N0zoM1z0</sub></td><td>東方風神録をソースコードとして再構築</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th09"><img src="https://raw.githubusercontent.com/N0zoM1z0/th09/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th09"></a></td><td><a href="https://github.com/N0zoM1z0/th09"><b>th09</b></a><br><sub>N0zoM1z0</sub></td><td>東方花映塚をソースコードとして再構築</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/touhou-reverse-engineering"><img src="https://opengraph.githubassets.com/1/N0zoM1z0/touhou-reverse-engineering" width="160" alt="N0zoM1z0/touhou-reverse-engineering"></a></td><td><a href="https://github.com/N0zoM1z0/touhou-reverse-engineering"><b>touhou-reverse-engineering</b></a><br><sub>N0zoM1z0</sub></td><td>証拠重視の東方 IDA ノート、実行時パッチ実験付き</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/yamahuser/mhfz-decomp"><b>mhfz-decomp</b></a><br><sub>yamahuser</sub></td><td>『モンスターハンター フロンティアZ』オンラインクライアントのリバースエンジニアリング：関数名、仕様、補助ツール。カプコンのオリジナルコードは含みません。</td><td>いいえ</td><td><sub>—</sub></td></tr>
</table>

#### リメイク / 移植

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/OpenRA/OpenRA"><img src="https://www.openra.net/images/news/20260222-generators.gif" width="160" alt="OpenRA/OpenRA"></a></td><td><a href="https://github.com/OpenRA/OpenRA"><b>OpenRA</b></a><br><sub>OpenRA</sub></td><td>名作コマンド＆コンカーを現代のオンライン対戦向けに再構築</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/OpenRCT2/OpenRCT2"><img src="https://github.com/user-attachments/assets/fa893cc8-1484-4751-94be-4ead00a6c8f9" width="160" alt="OpenRCT2/OpenRCT2"></a></td><td><a href="https://github.com/OpenRCT2/OpenRCT2"><b>OpenRCT2</b></a><br><sub>OpenRCT2</sub></td><td>ローラーコースタータイクーン 2 をオープンソースで現行 OS に</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/OpenTTD/OpenTTD"><img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/OpenTTD-15.3-en.png" width="160" alt="OpenTTD/OpenTTD"></a></td><td><a href="https://github.com/OpenTTD/OpenTTD"><b>OpenTTD</b></a><br><sub>OpenTTD</sub></td><td>トランスポートタイクーン デラックスをオープンソースで、今も進化中</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/commons/b/ba/OpenTTD-15.3-en.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/OpenMW/openmw"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/OpenMW_with_example_suit_2.png" width="160" alt="OpenMW/openmw"></a></td><td><a href="https://github.com/OpenMW/openmw"><b>openmw</b></a><br><sub>OpenMW</sub></td><td>モロウウィンドを最新のオープンソースエンジンで</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/commons/9/9e/OpenMW_with_example_suit_2.png">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/Interkarma/daggerfall-unity"><img src="https://github.com/Interkarma/daggerfall-unity/assets/10426244/4f176f9d-6332-47b3-a4d7-317ed8d6b38b" width="160" alt="Interkarma/daggerfall-unity"></a></td><td><a href="https://github.com/Interkarma/daggerfall-unity"><b>daggerfall-unity</b></a><br><sub>Interkarma</sub></td><td>ダガーフォールを Unity で再現（手持ちのゲームデータを使用）</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/scummvm/scummvm"><img src="https://www.scummvm.org/data/screenshots/prince/prince/prince_win_en_1_3_full.png" width="160" alt="scummvm/scummvm"></a></td><td><a href="https://github.com/scummvm/scummvm"><b>scummvm</b></a><br><sub>scummvm</sub></td><td>名作ポイント＆クリック ADV をほぼ何でも動かす</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/OpenXcom/OpenXcom"><img src="https://opengraph.githubassets.com/1/OpenXcom/OpenXcom" width="160" alt="OpenXcom/OpenXcom"></a></td><td><a href="https://github.com/OpenXcom/OpenXcom"><b>OpenXcom</b></a><br><sub>OpenXcom</sub></td><td>初代 UFO / X-COM を最新のオープンソースエンジンで</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/perfect-dark-pc-port/perfect_dark"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg" width="160" alt="perfect-dark-pc-port/perfect_dark"></a></td><td><a href="https://github.com/perfect-dark-pc-port/perfect_dark"><b>perfect_dark</b></a><br><sub>perfect-dark-pc-port</sub></td><td>パーフェクトダークを PC でネイティブに（ROM は各自）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td><a href="https://github.com/valentderah/totk-pc-recomp"><img src="images/totk-pc-recomp-card.png" width="160" alt="valentderah/totk-pc-recomp"></a></td><td><a href="https://github.com/valentderah/totk-pc-recomp"><b>totk-pc-recomp</b></a><br><sub>valentderah</sub></td><td>Nintendo Switch 版『ゼルダの伝説 ティアーズ オブ ザ キングダム』を、エミュレータなしで動くネイティブ Windows プログラムに静的再コンパイルします。ゲームファイルは自分で用意。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/julianxhokaxhiu/FFNx"><img src="https://raw.githubusercontent.com/julianxhokaxhiu/FFNx/master/.screens/ff7.png" width="160" alt="julianxhokaxhiu/FFNx"></a></td><td><a href="https://github.com/julianxhokaxhiu/FFNx"><b>FFNx</b></a><br><sub>julianxhokaxhiu</sub></td><td>PC 版 FF7/FF8 向けの最新ドライバー兼 Mod 基盤</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/smm2recomp/smm2recomp"><b>smm2recomp</b></a><br><sub>smm2recomp</sub></td><td>クローズドソースの Switch『スーパーマリオメーカー2』を静的再コンパイルして PC・Mac・Linux などでネイティブに動くアプリにしたもの。自分のダンプが必要。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/fallout2-ce/fallout2-ce"><img src="https://raw.githubusercontent.com/fallout2-ce/fallout2-ce/main/docs/images/two-column-inventory.jpg" width="160" alt="fallout2-ce/fallout2-ce"></a></td><td><a href="https://github.com/fallout2-ce/fallout2-ce"><b>fallout2-ce</b></a><br><sub>fallout2-ce</sub></td><td>Fallout 2 を現行 OS で（手持ちのゲームデータを使用）</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/tmcleroy/cps2recomp"><img src="images/cps2recomp-card.png" width="160" alt="tmcleroy/cps2recomp"></a></td><td><a href="https://github.com/tmcleroy/cps2recomp"><b>cps2recomp</b></a><br><sub>tmcleroy</sub></td><td>カプコンCPS-2アーケードゲーム（ストリートファイターα2など）を静的リコンパイルで作った非公式ネイティブPC移植版。ROMは自分で用意。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="160" alt="Moxnatiy/OpenBattlefield2"></a></td><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><b>OpenBattlefield2</b></a><br><sub>Moxnatiy</sub></td><td>バトルフィールド 2 のエンジンを C++20 でクリーンルーム再実装（手持ちの製品版を使用）</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th08-web"><img src="https://raw.githubusercontent.com/N0zoM1z0/th08-web/main/resources/th08-web-social-preview.jpg" width="160" alt="N0zoM1z0/th08-web"></a></td><td><a href="https://github.com/N0zoM1z0/th08-web"><b>th08-web</b></a><br><sub>N0zoM1z0</sub></td><td>th08 の再構築をもとにブラウザで遊べる永夜抄</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/AsyncFinn/rook"><img src="https://opengraph.githubassets.com/1/AsyncFinn/rook" width="160" alt="AsyncFinn/rook"></a></td><td><a href="https://github.com/AsyncFinn/rook"><b>rook</b></a><br><sub>AsyncFinn</sub></td><td>Studio と照合してテストする Rust 製 Roblox 互換エンジン</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="160" alt="ucodia/desktop-games-nostalgia"></a></td><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><b>desktop-games-nostalgia</b></a><br><sub>ucodia</sub></td><td>デスクトップをまた壊そう：Gemtree の 2000 年作を macOS とブラウザへ</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/tallowmere/free-heroes4"><img src="https://upload.wikimedia.org/wikipedia/en/c/cc/Heroes_of_Might_and_Magic_IV_box.jpg" width="160" alt="tallowmere/free-heroes4"></a></td><td><a href="https://github.com/tallowmere/free-heroes4"><b>free-heroes4</b></a><br><sub>tallowmere</sub></td><td>マイト・アンド・マジック ヒーローズ IV を C++23 の新エンジンで（GOG 版を使用）</td><td>いいえ</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/c/cc/Heroes_of_Might_and_Magic_IV_box.jpg">Wikipedia（© 権利者）</a></sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/cheviman/outrunners-port"><b>outrunners-port</b></a><br><sub>cheviman</sub></td><td>1992年セガアーケードゲーム『OutRunners』を、一致する C デコンパイルを基に PC とコンソール向けネイティブ移植。ROM は自分で用意。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="160" alt="tuunanet/rea-ski-or-die-reconstruction"></a></td><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><b>rea-ski-or-die-reconstruction</b></a><br><sub>tuunanet</sub></td><td>Ski or Die の雪合戦を Rust + SDL2 で再現（素材は各自用意）</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/OpenRsG/GunZRs"><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="160" alt="OpenRsG/GunZRs"></a></td><td><a href="https://github.com/OpenRsG/GunZRs"><b>GunZRs</b></a><br><sub>OpenRsG</sub></td><td>GunZ: The Duel を Rust + Bevy で復活</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/a-barzanti/ai-rebuilds"><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="160" alt="a-barzanti/ai-rebuilds"></a></td><td><a href="https://github.com/a-barzanti/ai-rebuilds"><b>ai-rebuilds</b></a><br><sub>a-barzanti</sub></td><td>見捨てられたゲームをブラウザで復活、元ファイルは含まない</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/carlhako/keen-clone"><b>keen-clone</b></a><br><sub>carlhako</sub></td><td>REA + Ghidra で関数単位に復元した Commander Keen 1 のネイティブ Linux/SDL2 再実装</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/NathanKanaeru/samp-client-re"><b>samp-client-re</b></a><br><sub>NathanKanaeru</sub></td><td>REA/Ghidra でアーキテクチャを復元した SA-MP 0.3.DL-R1 のクリーンルームクライアント再実装</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/openage/openage"><b>openage</b></a><br><sub>openage</sub></td><td>Age of Empires II など RTS のオープンソースエンジン再実装</td><td>いいえ</td><td><sub>—</sub></td></tr>
</table>

#### アセット抽出・ツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/Perfare/AssetStudio"><img src="https://opengraph.githubassets.com/1/Perfare/AssetStudio" width="160" alt="Perfare/AssetStudio"></a></td><td><a href="https://github.com/Perfare/AssetStudio"><b>AssetStudio</b></a><br><sub>Perfare</sub></td><td>Unity ゲームのアセットを閲覧・書き出し</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/AssetRipper/AssetRipper"><img src="https://raw.githubusercontent.com/AssetRipper/AssetRipper/master/docs/articles/images/RunningOnMac/004.png" width="160" alt="AssetRipper/AssetRipper"></a></td><td><a href="https://github.com/AssetRipper/AssetRipper"><b>AssetRipper</b></a><br><sub>AssetRipper</sub></td><td>Unity のビルドを編集可能なプロジェクトに戻す</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/ata4/disunity"><img src="https://opengraph.githubassets.com/1/ata4/disunity" width="160" alt="ata4/disunity"></a></td><td><a href="https://github.com/ata4/disunity"><b>disunity</b></a><br><sub>ata4</sub></td><td>Unity アセットファイルを調べる初期のツール群</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/ladislav-zezula/CascLib"><img src="https://opengraph.githubassets.com/1/ladislav-zezula/CascLib" width="160" alt="ladislav-zezula/CascLib"></a></td><td><a href="https://github.com/ladislav-zezula/CascLib"><b>CascLib</b></a><br><sub>ladislav-zezula</sub></td><td>Blizzard の CASC アーカイブを読み込む</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/rodneypantonial/sims3-modernization"><b>sims3-modernization</b></a><br><sub>rodneypantonial</sub></td><td>最新 PC でシムズ3 のカクつきとクラッシュを減らす</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/touhou-reconstruction-factory"><img src="https://opengraph.githubassets.com/1/N0zoM1z0/touhou-reconstruction-factory" width="160" alt="N0zoM1z0/touhou-reconstruction-factory"></a></td><td><a href="https://github.com/N0zoM1z0/touhou-reconstruction-factory"><b>touhou-reconstruction-factory</b></a><br><sub>N0zoM1z0</sub></td><td>東方シリーズ再構築を支えるエージェントパイプライン</td><td>❔ 未確認</td><td><sub>リポジトリカード</sub></td></tr>
</table>

## アプリ / Electron / デスクトップ

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/storytold/photocraft"><img src="https://raw.githubusercontent.com/storytold/photocraft/main/docs/images/photocraft-demo.jpg" width="160" alt="storytold/photocraft"></a></td><td><a href="https://github.com/storytold/photocraft"><b>photocraft</b></a><br><sub>storytold</sub></td><td>Adobe Photoshop のような写真編集ソフトをゼロから書き直した無料のオープンソース版。Rust 製でレイヤー・マスク・PSD に対応するが、Adobe のコードは一切使っていない。</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/pdfcraft"><b>pdfcraft</b></a><br><sub>storytold</sub></td><td>純 Rust のクリーンルーム PDF リーダー/エディタ</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/filmcraft"><b>filmcraft</b></a><br><sub>storytold</sub></td><td>Adobe Premiere Pro のような動画編集ソフトをゼロから作った無料のオープンソース版。Rust 製で、Adobe のコードは使っていない。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/wordcraft"><b>wordcraft</b></a><br><sub>storytold</sub></td><td>純 Rust のクリーンルームワードプロセッサ</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/storytold/lightcraft"><img src="images/lightcraft-card.jpg" width="160" alt="storytold/lightcraft"></a></td><td><a href="https://github.com/storytold/lightcraft"><b>lightcraft</b></a><br><sub>storytold</sub></td><td>Adobe Lightroom のような写真管理・RAW 現像ツールをゼロから書き直したオープンソース版。純 Rust 製。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/storytold/vectorcraft"><img src="images/vectorcraft-card.jpg" width="160" alt="storytold/vectorcraft"></a></td><td><a href="https://github.com/storytold/vectorcraft"><b>vectorcraft</b></a><br><sub>storytold</sub></td><td>Adobe Illustrator のようなベクター描画ツールをゼロから書き直したオープンソース版。純 Rust 製で、Adobe のコードは使っていない。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/effectcraft"><b>effectcraft</b></a><br><sub>storytold</sub></td><td>Adobe After Effects のようなモーショングラフィックスと VFX ソフトをゼロから書き直したオープンソース版。Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/cadcraft"><b>cadcraft</b></a><br><sub>storytold</sub></td><td>AutoCAD のような CAD・製図ソフトをゼロから書き直したオープンソース版。純 Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/gridcraft"><b>gridcraft</b></a><br><sub>storytold</sub></td><td>Excel のようなスプレッドシートをゼロから作った無料のオープンソース版。Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/designcraft"><b>designcraft</b></a><br><sub>storytold</sub></td><td>Adobe InDesign のようなページレイアウト・出版エディタをゼロから書き直したオープンソース版。Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/deckcraft"><b>deckcraft</b></a><br><sub>storytold</sub></td><td>PowerPoint のようなプレゼンソフトをゼロから書き直したオープンソース版。Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/soundcraft"><b>soundcraft</b></a><br><sub>storytold</sub></td><td>Pro Tools のような DAW をゼロから書き直したオープンソース版。Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/storytold/figcraft"><b>figcraft</b></a><br><sub>storytold</sub></td><td>Figma のような UI デザインとプロトタイピングツールをゼロから作った無料のオープンソース版。Rust 製。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/electron/asar"><img src="images/asar-terminal.png" width="160" alt="electron/asar"></a></td><td><a href="https://github.com/electron/asar"><b>asar</b></a><br><sub>electron</sub></td><td>Electron アプリ内のアーカイブを作成・展開</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Caho1/open-claude-ui"><b>open-claude-ui</b></a><br><sub>Caho1</sub></td><td>REA で Claude Desktop の UI とインタラクション物理を抽出した高忠実度リビルド</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/GLinnik21/plx-native"><img src="https://raw.githubusercontent.com/GLinnik21/plx-native/main/docs/screenshots/home.jpg" width="160" alt="GLinnik21/plx-native"></a></td><td><a href="https://github.com/GLinnik21/plx-native"><b>plx-native</b></a><br><sub>GLinnik21</sub></td><td>LG テレビ向けの高速なネイティブ Plex クライアント</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/terminal-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/terminal-rs/master/docs/img/overview.png" width="160" alt="michaelshimeles/terminal-rs"></a></td><td><a href="https://github.com/michaelshimeles/terminal-rs"><b>terminal-rs</b></a><br><sub>michaelshimeles</sub></td><td>Rust 製の Bloomberg 風トレーディング端末</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/rec-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="160" alt="michaelshimeles/rec-rs"></a></td><td><a href="https://github.com/michaelshimeles/rec-rs"><b>rec-rs</b></a><br><sub>michaelshimeles</sub></td><td>OBS を参考にした Rust 製の高速 macOS 録画ツール</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Xiangyu-CAS/rea-capcut"><b>rea-capcut</b></a><br><sub>Xiangyu-CAS</sub></td><td>REA で CapCut を調べて作り直したオープンソースのオフライン動画編集</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/sketch"><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="160" alt="michaelshimeles/sketch"></a></td><td><a href="https://github.com/michaelshimeles/sketch"><b>sketch</b></a><br><sub>michaelshimeles</sub></td><td>Paper を研究して作った Rust 製の無限デザインキャンバス</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/lxistired/ledger-reborn"><img src="https://raw.githubusercontent.com/lxistired/ledger-reborn/main/docs/screenshots/accounting.png" width="160" alt="lxistired/ledger-reborn"></a></td><td><a href="https://github.com/lxistired/ledger-reborn"><b>ledger-reborn</b></a><br><sub>lxistired</sub></td><td>QuickBooks for Mac を参考にしたローカル優先の会計アプリ</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/glauberlima/open-scrantic"><b>open-scrantic</b></a><br><sub>glauberlima</sub></td><td>REA で逆解析した 1992 年 Johnny Castaway スクリーンセーバーの Rust 再実装</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/LilZeeCN/zee-rp"><img src="https://raw.githubusercontent.com/LilZeeCN/zee-rp/main/examples/screenshot/source.png" width="160" alt="LilZeeCN/zee-rp"></a></td><td><a href="https://github.com/LilZeeCN/zee-rp"><b>zee-rp</b></a><br><sub>LilZeeCN</sub></td><td>CLI や MCP から Axure RP のプロトタイプを読み書き</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/sickpyramid/ReaFuse"><img src="https://opengraph.githubassets.com/1/sickpyramid/ReaFuse" width="160" alt="sickpyramid/ReaFuse"></a></td><td><a href="https://github.com/sickpyramid/ReaFuse"><b>ReaFuse</b></a><br><sub>sickpyramid</sub></td><td>REA を使って 2 つの JS/TS プロジェクトを融合</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/laaielichter/Reverseport"><img src="https://raw.githubusercontent.com/laaielichter/Reverseport/main/docs/assets/demo.gif" width="160" alt="laaielichter/Reverseport"></a></td><td><a href="https://github.com/laaielichter/Reverseport"><b>Reverseport</b></a><br><sub>laaielichter</sub></td><td>解析結果を Godot・Unity・Unreal・three.js へ移植</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/iammukeshm/hexgrab"><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="160" alt="iammukeshm/hexgrab"></a></td><td><a href="https://github.com/iammukeshm/hexgrab"><b>hexgrab</b></a><br><sub>iammukeshm</sub></td><td>PowerToys のバイナリを調べて作った小さな Windows カラーピッカー</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/cudanexus/vd-streamer-linux"><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="160" alt="cudanexus/vd-streamer-linux"></a></td><td><a href="https://github.com/cudanexus/vd-streamer-linux"><b>vd-streamer-linux</b></a><br><sub>cudanexus</sub></td><td>Linux デスクトップを Quest・Pico へストリーミング</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/monatis/okur"><img src="images/okur-card.png" width="160" alt="monatis/okur"></a></td><td><a href="https://github.com/monatis/okur"><b>okur</b></a><br><sub>monatis</sub></td><td>JAWS のように動くオープンソースのスクリーンリーダー。JAWS の発話を観察してゼロから再実装。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><img src="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg" width="160" alt="az9713/wispr-flow-rea-teardown"></a></td><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><b>wispr-flow-rea-teardown</b></a><br><sub>az9713</sub></td><td>Wispr Flow の音声パイプラインを分解、64 行の再実装付き</td><td>✅ はい</td><td><sub><a href="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg">動画サムネイル</a></sub></td></tr>
<tr><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><img src="https://opengraph.githubassets.com/1/KarlssonChristoffer/DiskLens" width="160" alt="KarlssonChristoffer/DiskLens"></a></td><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><b>DiskLens</b></a><br><sub>KarlssonChristoffer</sub></td><td>WinDirStat 風に Windows 11 のディスク使用量を可視化</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/AdamLinCodes/AdamTerm"><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="160" alt="AdamLinCodes/AdamTerm"></a></td><td><a href="https://github.com/AdamLinCodes/AdamTerm"><b>AdamTerm</b></a><br><sub>AdamLinCodes</sub></td><td>Ghostty を調べて作ったミニマルな macOS ターミナル</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/chilliesdev/fmseasonhub-re"><b>fmseasonhub-re</b></a><br><sub>chilliesdev</sub></td><td>REA で FM Season Hub アプリを解析したノート</td><td>✅ はい</td><td><sub>—</sub></td></tr>
</table>

## プロトコル / ハードウェア

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/mitmproxy/mitmproxy"><img src="https://mitmproxy.org/screenshot.png" width="160" alt="mitmproxy/mitmproxy"></a></td><td><a href="https://github.com/mitmproxy/mitmproxy"><b>mitmproxy</b></a><br><sub>mitmproxy</sub></td><td>HTTPS 通信をその場で見て書き換える</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/wireshark/wireshark"><img src="images/wireshark-gui.png" width="160" alt="wireshark/wireshark"></a></td><td><a href="https://github.com/wireshark/wireshark"><b>wireshark</b></a><br><sub>wireshark</sub></td><td>ネットワーク上のパケットをすべてデコードして見る</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/postlund/pyatv"><img src="https://opengraph.githubassets.com/1/postlund/pyatv" width="160" alt="postlund/pyatv"></a></td><td><a href="https://github.com/postlund/pyatv"><b>pyatv</b></a><br><sub>postlund</sub></td><td>Python から Apple TV や AirPlay 機器を操作</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/a-funk/open-appleremote"><img src="https://opengraph.githubassets.com/1/a-funk/open-appleremote" width="160" alt="a-funk/open-appleremote"></a></td><td><a href="https://github.com/a-funk/open-appleremote"><b>open-appleremote</b></a><br><sub>a-funk</sub></td><td>初代 Siri Remote を Linux で、ジェスチャーまで対応</td><td>❔ 未確認</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/Slyvan25/OpenGHub"><img src="https://raw.githubusercontent.com/Slyvan25/OpenGHub/master/docs/screenshots/devices.png" width="160" alt="Slyvan25/OpenGHub"></a></td><td><a href="https://github.com/Slyvan25/OpenGHub"><b>OpenGHub</b></a><br><sub>Slyvan25</sub></td><td>G HUB なしで Linux から Logitech 機器を操作</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/EndLess728/MiTV-Remote"><b>MiTV-Remote</b></a><br><sub>EndLess728</sub></td><td>Mac・Android・iPhone から Wi-Fi で Xiaomi テレビを操作</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/B-Howell/soundconnect-desktop"><b>soundconnect-desktop</b></a><br><sub>B-Howell</sub></td><td>Windows デスクトップから Sony の Bluetooth ヘッドホンを操作</td><td>✅ はい</td><td><sub>—</sub></td></tr>
</table>

## ファームウェア / ドライバ

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/ReFirmLabs/binwalk"><img src="https://raw.githubusercontent.com/ReFirmLabs/binwalk/master/images/output.png" width="160" alt="ReFirmLabs/binwalk"></a></td><td><a href="https://github.com/ReFirmLabs/binwalk"><b>binwalk</b></a><br><sub>ReFirmLabs</sub></td><td>ファームウェアイメージの中身を見つけて取り出す</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/qilingframework/qiling"><img src="https://raw.githubusercontent.com/qilingframework/theme.qiling.io/master/source/img/fuzzer.jpg?raw=true" width="160" alt="qilingframework/qiling"></a></td><td><a href="https://github.com/qilingframework/qiling"><b>qiling</b></a><br><sub>qilingframework</sub></td><td>OS や CPU をまたいでバイナリをエミュレート・計測</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/onekey-sec/unblob"><img src="images/unblob-terminal.png" width="160" alt="onekey-sec/unblob"></a></td><td><a href="https://github.com/onekey-sec/unblob"><b>unblob</b></a><br><sub>onekey-sec</sub></td><td>ほぼあらゆるファームやコンテナ形式を再帰的に展開</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/attify/firmware-analysis-toolkit"><img src="https://opengraph.githubassets.com/1/attify/firmware-analysis-toolkit" width="160" alt="attify/firmware-analysis-toolkit"></a></td><td><a href="https://github.com/attify/firmware-analysis-toolkit"><b>firmware-analysis-toolkit</b></a><br><sub>attify</sub></td><td>IoT ファームをエミュレートして安全に調べる</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/travisgoodspeed/md380tools"><img src="https://opengraph.githubassets.com/1/travisgoodspeed/md380tools" width="160" alt="travisgoodspeed/md380tools"></a></td><td><a href="https://github.com/travisgoodspeed/md380tools"><b>md380tools</b></a><br><sub>travisgoodspeed</sub></td><td>TYT MD-380 無線機用のカスタムファームパッチ</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/ghidraninja/game-and-watch-backup"><img src="https://img.youtube.com/vi/-MzmoEFs0bQ/maxresdefault.jpg" width="160" alt="ghidraninja/game-and-watch-backup"></a></td><td><a href="https://github.com/ghidraninja/game-and-watch-backup"><b>game-and-watch-backup</b></a><br><sub>ghidraninja</sub></td><td>手持ちの Game &amp; Watch のファームをバックアップ・復元</td><td>いいえ</td><td><sub><a href="https://img.youtube.com/vi/-MzmoEFs0bQ/maxresdefault.jpg">動画サムネイル</a></sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/nicolvus/a6000-fw-decomp"><b>a6000-fw-decomp</b></a><br><sub>nicolvus</sub></td><td>REA と Ghidra で Sony A6000 のファームウェアを解析</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/grisuno/VSL-DSP"><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="160" alt="grisuno/VSL-DSP"></a></td><td><a href="https://github.com/grisuno/VSL-DSP"><b>VSL-DSP</b></a><br><sub>grisuno</sub></td><td>PreSonus AudioBox VSL 用の Linux カーネルモジュール</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
</table>

## セキュリティ / 評価

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/morluto/rea/discussions/2254"><img src="images/rea-discussion-2254.png" width="160" alt="REA discussion #2254"></a></td><td><a href="https://github.com/morluto/rea/discussions/2254"><b>REA discussion #2254</b></a></td><td>シンボルなし bzip2 を解析し、元のビルドと照合</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-lab"><img src="https://opengraph.githubassets.com/1/pablodiazjorge/rea-lab" width="160" alt="pablodiazjorge/rea-lab"></a></td><td><a href="https://github.com/pablodiazjorge/rea-lab"><b>rea-lab</b></a><br><sub>pablodiazjorge</sub></td><td>Windows + Ghidra の演習と事前登録した REA 評価</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="160" alt="NullLabTests/OpenBSD_netcat_REA"></a></td><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><b>OpenBSD_netcat_REA</b></a><br><sub>NullLabTests</sub></td><td>REA と Ghidra で netcat-openbsd を静的解析</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><img src="https://opengraph.githubassets.com/1/UnknownHacker1/rea-groundtruth" width="160" alt="UnknownHacker1/rea-groundtruth"></a></td><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><b>rea-groundtruth</b></a><br><sub>UnknownHacker1</sub></td><td>REA のレポートを実際のソースと突き合わせる</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/az9713/REA-demo"><img src="https://opengraph.githubassets.com/1/az9713/REA-demo" width="160" alt="az9713/REA-demo"></a></td><td><a href="https://github.com/az9713/REA-demo"><b>REA-demo</b></a><br><sub>az9713</sub></td><td>REA が自分自身を解析、反証可能な予測付き</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
</table>

## リバースエンジニアリングツール

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://github.com/NationalSecurityAgency/ghidra"><img src="images/ghidra-gui.png" width="160" alt="NationalSecurityAgency/ghidra"></a></td><td><a href="https://github.com/NationalSecurityAgency/ghidra"><b>ghidra</b></a><br><sub>NationalSecurityAgency</sub></td><td>NSA が公開する無料の逆コンパイラ・逆アセンブラ</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/WerWolv/ImHex"><img src="images/imhex-gui.png" width="160" alt="WerWolv/ImHex"></a></td><td><a href="https://github.com/WerWolv/ImHex"><b>ImHex</b></a><br><sub>WerWolv</sub></td><td>構造を自動で読み解くパターン言語付きの HEX エディタ</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/skylot/jadx"><img src="https://user-images.githubusercontent.com/118523/142730720-839f017e-38db-423e-b53f-39f5f0a0316f.png" width="160" alt="skylot/jadx"></a></td><td><a href="https://github.com/skylot/jadx"><b>jadx</b></a><br><sub>skylot</sub></td><td>Android APK を読める Java に戻す</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/x64dbg/x64dbg"><img src="https://raw.githubusercontent.com/x64dbg/x64dbg/development/.github/screenshots/cpu-light.png" width="160" alt="x64dbg/x64dbg"></a></td><td><a href="https://github.com/x64dbg/x64dbg"><b>x64dbg</b></a><br><sub>x64dbg</sub></td><td>Windows バイナリ定番のオープンソースデバッガ</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/icsharpcode/ILSpy"><img src="https://opengraph.githubassets.com/1/icsharpcode/ILSpy" width="160" alt="icsharpcode/ILSpy"></a></td><td><a href="https://github.com/icsharpcode/ILSpy"><b>ILSpy</b></a><br><sub>icsharpcode</sub></td><td>どんな .NET アセンブリも C# に戻す</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/iBotPeaches/Apktool"><img src="images/apktool-terminal.png" width="160" alt="iBotPeaches/Apktool"></a></td><td><a href="https://github.com/iBotPeaches/Apktool"><b>Apktool</b></a><br><sub>iBotPeaches</sub></td><td>Android APK を展開・解析・再ビルド</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/radareorg/radare2"><img src="https://raw.githubusercontent.com/radareorg/radare2/master/doc/images/shot.png" width="160" alt="radareorg/radare2"></a></td><td><a href="https://github.com/radareorg/radare2"><b>radare2</b></a><br><sub>radareorg</sub></td><td>スクリプト可能なコマンドラインのリバースエンジニアリング基盤</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/frida/frida"><img src="images/frida-terminal.png" width="160" alt="frida/frida"></a></td><td><a href="https://github.com/frida/frida"><b>frida</b></a><br><sub>frida</sub></td><td>実行中のアプリにフックし、その場で挙動を書き換える</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/cutter"><img src="https://raw.githubusercontent.com/rizinorg/cutter/dev/docs/source/images/screenshot.png" width="160" alt="rizinorg/cutter"></a></td><td><a href="https://github.com/rizinorg/cutter"><b>cutter</b></a><br><sub>rizinorg</sub></td><td>Rizin ベースの使いやすいリバースエンジニアリング GUI</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/mrexodia/ida-pro-mcp"><img src="https://img.youtube.com/vi/iFxNuk3kxhk/0.jpg" width="160" alt="mrexodia/ida-pro-mcp"></a></td><td><a href="https://github.com/mrexodia/ida-pro-mcp"><b>ida-pro-mcp</b></a><br><sub>mrexodia</sub></td><td>MCP 経由で AI エージェントに IDA Pro を操作させる</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/LaurieWired/GhidraMCP"><img src="https://github.com/user-attachments/assets/4986d702-be3f-4697-acce-aea55cd79ad3" width="160" alt="LaurieWired/GhidraMCP"></a></td><td><a href="https://github.com/LaurieWired/GhidraMCP"><b>GhidraMCP</b></a><br><sub>LaurieWired</sub></td><td>AI アシスタント（Claude など）が無料のリバースエンジニアリングツール Ghidra を直接操作できるようにする橋。AI がデコンパイルや関数リネームを代行できる。</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/dnSpyEx/dnSpy"><img src="https://raw.githubusercontent.com/dnSpyEx/dnSpy/master/images/debug-animated.gif" width="160" alt="dnSpyEx/dnSpy"></a></td><td><a href="https://github.com/dnSpyEx/dnSpy"><b>dnSpy</b></a><br><sub>dnSpyEx</sub></td><td>ソースなしで .NET アセンブリをデバッグ・編集</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/wtsxdev/reverse-engineering"><b>reverse-engineering</b></a><br><sub>wtsxDev</sub></td><td>クラシックなリバースエンジニアリングのリソース・ツール・学習資料リスト</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/angr/angr"><img src="https://opengraph.githubassets.com/1/angr/angr" width="160" alt="angr/angr"></a></td><td><a href="https://github.com/angr/angr"><b>angr</b></a><br><sub>angr</sub></td><td>Python でシンボリック実行とバイナリ解析</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/avast/retdec"><img src="https://user-images.githubusercontent.com/20342097/35865940-2288d66a-0b56-11e8-9a92-d154b7111053.png" width="160" alt="avast/retdec"></a></td><td><a href="https://github.com/avast/retdec"><b>retdec</b></a><br><sub>avast</sub></td><td>多様なアーキテクチャの機械語を C へ逆コンパイル</td><td>いいえ</td><td><sub>メンテナー投稿</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/albertan017/LLM4Decompile"><b>LLM4Decompile</b></a><br><sub>albertan017</sub></td><td>LLM ベースのバイナリデコンパイル向け研究モデルとツール（オープンウェイト）。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/mandiant/capa"><img src="https://raw.githubusercontent.com/mandiant/capa/master/doc/img/capa_web_explorer.png" width="160" alt="mandiant/capa"></a></td><td><a href="https://github.com/mandiant/capa"><b>capa</b></a><br><sub>mandiant</sub></td><td>実行ファイルに「何ができるか」を聞き、ATT&amp;CK 付きで答えを得る</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/alphaSeclab/awesome-reverse-engineering"><b>awesome-reverse-engineering</b></a><br><sub>alphaSeclab</sub></td><td>主要プラットフォームと領域をカバーする大規模なリバースエンジニアリングツール/リソース集。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/mandiant/flare-floss"><img src="images/floss-terminal.png" width="160" alt="mandiant/flare-floss"></a></td><td><a href="https://github.com/mandiant/flare-floss"><b>flare-floss</b></a><br><sub>mandiant</sub></td><td>マルウェアに隠された難読化文字列を取り出す</td><td>いいえ</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/rizin"><img src="https://rizin.re/images/rizin_preview.png" width="160" alt="rizinorg/rizin"></a></td><td><a href="https://github.com/rizinorg/rizin"><b>rizin</b></a><br><sub>rizinorg</sub></td><td>radare2 から派生した UNIX 流のリバースエンジニアリング基盤</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/aicodeking/leanrea"><b>leanrea</b></a><br><sub>aicodeking</sub></td><td>REA の MCP 層を置き換える軽量スキル。エージェントが CLI ツールを直接駆動</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/JusticeRage/Gepetto"><b>Gepetto</b></a><br><sub>JusticeRage</sub></td><td>IDA Pro プラグイン。言語モデルで関数の説明・リネーム・コメントを支援。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/google/bindiff"><img src="https://zynamics.com/images/bindiff_scr1_s.gif" width="160" alt="google/bindiff"></a></td><td><a href="https://github.com/google/bindiff"><b>bindiff</b></a><br><sub>google</sub></td><td>2 つのバイナリ間の違いを見つける</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/zinja-coder/jadx-ai-mcp"><b>jadx-ai-mcp</b></a><br><sub>zinja-coder</sub></td><td>JADX 用 MCP プラグイン。AI エージェントが Android APK/DEX をデコンパイル・ナビゲート可能。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/SubmitGame/awesome-decomp-games"><b>awesome-decomp-games</b></a><br><sub>SubmitGame</sub></td><td>評価付き・自動更新のゲーム decomp / recomp / ソースポート / エンジンリメイク一覧</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/cranebeaker/coop-anything"><b>coop-anything</b></a><br><sub>cranebeaker</sub></td><td>REA でエントリポイントを調査し、シングルプレイゲームに協力モードを追加する MCP サーバー</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/HexRaysSA/ida-mcp"><img src="https://opengraph.githubassets.com/1/HexRaysSA/ida-mcp" width="160" alt="HexRaysSA/ida-mcp"></a></td><td><a href="https://github.com/HexRaysSA/ida-mcp"><b>ida-mcp</b></a><br><sub>HexRaysSA</sub></td><td>Hex-Rays 公式の IDA 用 MCP サーバー</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/morluto/awesome-reverse-engineering"><b>awesome-reverse-engineering</b></a><br><sub>morluto</sub></td><td>RE ツールと学習リソースの厳選入門リスト（バイナリ、アプリ、ファームウェア、フォーマット、プロトコル）。REA 作者による。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/ghidraninja/ghidra_scripts"><img src="https://raw.githubusercontent.com/ghidraninja/ghidra_scripts/master/images/binwalk.png" width="160" alt="ghidraninja/ghidra_scripts"></a></td><td><a href="https://github.com/ghidraninja/ghidra_scripts"><b>ghidra_scripts</b></a><br><sub>ghidraninja</sub></td><td>binwalk 連携から YARA まで、便利な Ghidra スクリプト集</td><td>いいえ</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/alexgaoth/awesome-reverse-engineered"><b>awesome-reverse-engineered</b></a><br><sub>alexgaoth</sub></td><td>誰かがクローズドなアプリ・ゲーム・API・デバイスをリバースエンジニアリングした結果生まれたオープンソースプロジェクトを 1.7 万以上集めた検索可能なカタログ。検索サイトと MCP サーバー付き。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/cyberkaida/reverse-engineering-assistant"><img src="images/reva-card.jpg" width="160" alt="cyberkaida/reverse-engineering-assistant"></a></td><td><a href="https://github.com/cyberkaida/reverse-engineering-assistant"><b>reverse-engineering-assistant</b></a><br><sub>cyberkaida</sub></td><td>AI が Ghidra（NSA の無料リバースエンジニアリングツール）を操作するもう一つの方法。AI に小さく集中したツールを与え、大きなプログラムでも混乱しにくくする。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/MiaAI-Lab/sparkDash"><b>sparkDash</b></a><br><sub>MiaAI-Lab</sub></td><td>長時間の REA 分析ジョブを統合し、結果をオンデマンドで読み込むマルチデバイスダッシュボード</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/symgraph/GhidrAssist"><b>GhidrAssist</b></a><br><sub>symgraph</sub></td><td>Ghidra 用 LLM 拡張。デコンパイル結果のリネーム・説明・解析を支援。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/nforest/awesome-decompilation"><b>awesome-decompilation</b></a><br><sub>nforest</sub></td><td>デコンパイル関連リソース、論文、中間表現、プロジェクトの厳選リスト。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/decompme/decomp.me"><img src="https://opengraph.githubassets.com/1/decompme/decomp.me" width="160" alt="decompme/decomp.me"></a></td><td><a href="https://github.com/decompme/decomp.me"><b>decomp.me</b></a><br><sub>decompme</sub></td><td>ブラウザで共同逆コンパイル、一致ビルドを目指す</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/radareorg/r2ai"><b>r2ai</b></a><br><sub>radareorg</sub></td><td>radare2 用の LLM ベースのリバースツールとプラグイン</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/fosdickio/binary_ninja_mcp"><b>binary_ninja_mcp</b></a><br><sub>fosdickio</sub></td><td>LLM エージェントが Binary Ninja を操作できる MCP サーバー（デコンパイル、xref、リネームなど）。</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/radareorg/radare2-mcp"><b>radare2-mcp</b></a><br><sub>radareorg</sub></td><td>radare2 公式 MCP stdio サーバー</td><td>いいえ</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="160" alt="ShadowSwaps/REA-Reconstruction-Companion"></a></td><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><b>REA-Reconstruction-Companion</b></a><br><sub>ShadowSwaps</sub></td><td>再構築を常に証拠と結びつけるエージェントスキル</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/jsdec"><img src="https://opengraph.githubassets.com/1/rizinorg/jsdec" width="160" alt="rizinorg/jsdec"></a></td><td><a href="https://github.com/rizinorg/jsdec"><b>jsdec</b></a><br><sub>rizinorg</sub></td><td>手書きアセンブリからも読みやすい疑似 C を出す Rizin 用デコンパイラ</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/giveen/decomp.anything"><b>decomp.anything</b></a><br><sub>giveen</sub></td><td>更新停止したマッチング型デコンパイラ decomp.wtf の継続フォーク。Windows/Linux バイナリ対応と REA 連携を追加し、ゲーム以外のプログラムもエージェントが解析できるようにした。</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/czcdr/dsh-plugin-rea"><img src="https://raw.githubusercontent.com/czcdr/dsh-plugin-rea/main/assets/screenshot-1.png" width="160" alt="czcdr/dsh-plugin-rea"></a></td><td><a href="https://github.com/czcdr/dsh-plugin-rea"><b>dsh-plugin-rea</b></a><br><sub>czcdr</sub></td><td>DeepSeek Harness で REA を、Ghidra も自動導入</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/0xshlomil/ida-free-mcp"><img src="https://opengraph.githubassets.com/1/0xshlomil/ida-free-mcp" width="160" alt="0xshlomil/ida-free-mcp"></a></td><td><a href="https://github.com/0xshlomil/ida-free-mcp"><b>ida-free-mcp</b></a><br><sub>0xshlomil</sub></td><td>MCP 経由で AI エージェントから IDA Free を使う</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/dav1dngy/era-agent"><img src="https://raw.githubusercontent.com/dav1dngy/era-agent/main/docs/assets/screenshots/01-main-workspace.png" width="160" alt="dav1dngy/era-agent"></a></td><td><a href="https://github.com/dav1dngy/era-agent"><b>era-agent</b></a><br><sub>dav1dngy</sub></td><td>証拠駆動で自己改善を試みるリバースエンジニアリング用エージェント</td><td>❔ 未確認</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/tanepiper/game-frame"><b>game-frame</b></a><br><sub>tanepiper</sub></td><td>配布ファイルからエージェントがゲームを解析するフレームワーク</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/alexmi256/rea-agent-docker"><img src="https://opengraph.githubassets.com/1/alexmi256/rea-agent-docker" width="160" alt="alexmi256/rea-agent-docker"></a></td><td><a href="https://github.com/alexmi256/rea-agent-docker"><b>rea-agent-docker</b></a><br><sub>alexmi256</sub></td><td>Ghidra・Hopper・IDA 版がある REA の Docker イメージ</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/DatanoiseTV/revenant"><img src="images/revenant-card.png" width="160" alt="DatanoiseTV/revenant"></a></td><td><a href="https://github.com/DatanoiseTV/revenant"><b>revenant</b></a><br><sub>DatanoiseTV</sub></td><td>放棄されたファームウェアやバイナリを LLM で自動解析し、ピンマップや再実装を生成。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/zhaofeng130/dsh-rea"><img src="https://opengraph.githubassets.com/1/zhaofeng130/dsh-rea" width="160" alt="zhaofeng130/dsh-rea"></a></td><td><a href="https://github.com/zhaofeng130/dsh-rea"><b>dsh-rea</b></a><br><sub>zhaofeng130</sub></td><td>DeepSeek Harness に REA のスキルとツールを追加</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-casebook"><img src="https://raw.githubusercontent.com/pablodiazjorge/rea-casebook/main/media/session-dark.png" width="160" alt="pablodiazjorge/rea-casebook"></a></td><td><a href="https://github.com/pablodiazjorge/rea-casebook"><b>rea-casebook</b></a><br><sub>pablodiazjorge</sub></td><td>Claude Code の結論すべてに実際の REA 証拠を引用させる</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><img src="https://opengraph.githubassets.com/1/sheilacraig/dsh-rea-mcp" width="160" alt="sheilacraig/dsh-rea-mcp"></a></td><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><b>dsh-rea-mcp</b></a><br><sub>sheilacraig</sub></td><td>設定だけで DeepSeek Harness に REA を組み込む</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/Nowng/rea-mcp"><img src="https://opengraph.githubassets.com/1/Nowng/rea-mcp" width="160" alt="Nowng/rea-mcp"></a></td><td><a href="https://github.com/Nowng/rea-mcp"><b>rea-mcp</b></a><br><sub>Nowng</sub></td><td>LM Studio のローカルモデルで REA を使う</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><img src="https://opengraph.githubassets.com/1/ya123-4/rea-dsh-plugin" width="160" alt="ya123-4/rea-dsh-plugin"></a></td><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><b>rea-dsh-plugin</b></a><br><sub>ya123-4</sub></td><td>DeepSeek Harness に REA の MCP ツールを登録</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/Sage-is/CleanRoom"><img src="images/cleanroom-card.png" width="160" alt="Sage-is/CleanRoom"></a></td><td><a href="https://github.com/Sage-is/CleanRoom"><b>CleanRoom</b></a><br><sub>Sage-is</sub></td><td>REA のローカル版を Python でシンプルに再実装した MCP サーバーと CLI。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/cognixws/picode-rea"><img src="https://opengraph.githubassets.com/1/cognixws/picode-rea" width="160" alt="cognixws/picode-rea"></a></td><td><a href="https://github.com/cognixws/picode-rea"><b>picode-rea</b></a><br><sub>cognixws</sub></td><td>PiCode から REA の静的解析ツールを使う</td><td>✅ はい</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td><a href="https://github.com/jinshi666888/rea-playbook"><img src="https://raw.githubusercontent.com/jinshi666888/rea-playbook/main/docs/assets/demo.gif" width="160" alt="jinshi666888/rea-playbook"></a></td><td><a href="https://github.com/jinshi666888/rea-playbook"><b>rea-playbook</b></a><br><sub>jinshi666888</sub></td><td>小さな Electron ターゲット付きの REA ハンズオン</td><td>✅ はい</td><td><sub>プロジェクト README</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/agioracle/rea-unity-game"><b>rea-unity-game</b></a><br><sub>agioracle</sub></td><td>エージェントで Unity ゲームを解析するワークフロー</td><td>❔ 未確認</td><td><sub>—</sub></td></tr>
<tr><td><a href="https://github.com/orikami048/gea"><img src="images/gea-card.png" width="160" alt="orikami048/gea"></a></td><td><a href="https://github.com/orikami048/gea"><b>gea</b></a><br><sub>orikami048</sub></td><td>ゲームのリバースエンジニアリング、アセット抽出、Cocos/Three.js 再現のための MCP と CLI。morluto/rea に着想。</td><td>いいえ</td><td><sub>リポジトリカード</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/Stijnus/dsh-rev-eng"><b>dsh-rev-eng</b></a><br><sub>Stijnus</sub></td><td>REA スキルとオプションの MCP をパッケージした DSH プラグイン。リバースエンジニアリングと Mac アプリ構築用。</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/CurLeaf/dsh-command-rea"><b>dsh-command-rea</b></a><br><sub>CurLeaf</sub></td><td>DSH の /rea スラッシュコマンド。リクエストを REA スキルと MCP ツールにルーティング。</td><td>✅ はい</td><td><sub>—</sub></td></tr>
<tr><td>—</td><td><a href="https://github.com/LostArtefacts/decomp-tools"><b>decomp-tools</b></a><br><sub>LostArtefacts</sub></td><td>Windows 版トゥームレイダー2～5の一致するデコンパイルを支援するツール。Wine 上でオリジナルの MSVC 5/6 コンパイラを使用。</td><td>いいえ</td><td><sub>—</sub></td></tr>
</table>

## REA 公式ショーケース

<table>
<tr><th width="170">画像</th><th>プロジェクト</th><th>概要</th><th>rea 使用</th><th>画像の出典</th></tr>
<tr><td><a href="https://rea.tools/showcase/dx-ball/"><img src="images/showcase-dx-ball.png" width="160" alt="DX-Ball: sound-pan function"></a></td><td><a href="https://rea.tools/showcase/dx-ball/"><b>DX-Ball: sound-pan function</b></a></td><td>REA が DX-Ball の音響関数をバイト単位で一致する C に戻す過程</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/notion/"><img src="images/showcase-notion.png" width="160" alt="Notion: Electron clipboard bridge"></a></td><td><a href="https://rea.tools/showcase/notion/"><b>Notion: Electron clipboard bridge</b></a></td><td>Notion のコピー操作をページから IPC、メインプロセスまで追跡</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/th04/"><img src="images/showcase-th04.png" width="160" alt="TH04: PC-98 bullet-ring maths"></a></td><td><a href="https://rea.tools/showcase/th04/"><b>TH04: PC-98 bullet-ring maths</b></a></td><td>16 ビット DOS コードから東方幻想郷の弾幕角度計算を復元</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/aegis/"><img src="images/showcase-aegis.png" width="160" alt="Aegis: TOTP code generation"></a></td><td><a href="https://rea.tools/showcase/aegis/"><b>Aegis: TOTP code generation</b></a></td><td>Aegis（Android）が二段階認証コードを生成する仕組みを解明</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/ctf/"><img src="images/showcase-ctf.png" width="160" alt="CTF: flag checker"></a></td><td><a href="https://rea.tools/showcase/ctf/"><b>CTF: flag checker</b></a></td><td>DownUnderCTF 2023 のリバーシング問題を順に解く</td><td>✅ はい</td><td><sub>当リポジトリの撮影</sub></td></tr>
</table>

---

関連リスト／謝辞：REA コミュニティの多くの項目は [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything) を参照・照合しました。

貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md)、ライセンスは [CC0-1.0](LICENSE)。
