[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# REA Atlas：逆向工程项目地图（含 rea 标记）

开源逆向工程项目地图：游戏反编译、静态重编译、重实现、资源提取工具、通用逆向工具，以及应用/协议/固件逆向。每条标注是否使用 [morluto/rea](https://github.com/morluto/rea)（Reverse Engineer Anything）：**Uses rea: Yes / No / Unverified**，只有公开证据（README、官方 showcase 或仓库文档）才标 Yes。

> 非官方，与 morluto/rea 无关联。不收录、不托管破解、盗版、ROM 或版权素材。

## 目录

- [游戏](#游戏)
  - [NES / FC](#nes--fc)
  - [SFC / SNES](#sfc--snes)
  - [MD / Genesis](#md--genesis)
  - [世嘉土星](#世嘉土星)
  - [Game Boy](#game-boy)
  - [GBA](#gba)
  - [任天堂 64](#任天堂-64)
  - [GameCube](#gamecube)
  - [Wii](#wii)
  - [NDS](#nds)
  - [3DS](#3ds)
  - [PS1](#ps1)
  - [PS2](#ps2)
  - [Xbox / Xbox 360](#xbox--xbox-360)
  - [PC / DOS / PC-98](#pc--dos--pc-98)
- [应用 / Electron / 桌面](#应用--electron--桌面)
- [协议 / 硬件](#协议--硬件)
- [固件 / 驱动](#固件--驱动)
- [安全 / 评测](#安全--评测)
- [逆向工具](#逆向工具)
- [REA 官方 Showcase](#rea-官方-showcase)

## 游戏

### NES / FC

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/aldonunez/zelda1-disassembly"><img src="https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png" width="160" alt="aldonunez/zelda1-disassembly"></a></td><td><a href="https://github.com/aldonunez/zelda1-disassembly"><b>zelda1-disassembly</b></a><br><sub>aldonunez</sub></td><td>初代塞尔达传说（FC）完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/4/41/Legend_of_zelda_cover_%28with_cartridge%29_gold.png">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 资源提取与工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/SourMesen/Mesen2"><img src="https://opengraph.githubassets.com/1/SourMesen/Mesen2" width="160" alt="SourMesen/Mesen2"></a></td><td><a href="https://github.com/SourMesen/Mesen2"><b>Mesen2</b></a><br><sub>SourMesen</sub></td><td>带强大调试工具的多机种模拟器</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
</table>

### SFC / SNES

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/snesrev/zelda3"><img src="https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg" width="160" alt="snesrev/zelda3"></a></td><td><a href="https://github.com/snesrev/zelda3"><b>zelda3</b></a><br><sub>snesrev</sub></td><td>用 C 重写的众神的三角力量，支持宽屏（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/2/21/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/snesrev/sm"><img src="https://upload.wikimedia.org/wikipedia/en/e/e4/Smetroidbox.jpg" width="160" alt="snesrev/sm"></a></td><td><a href="https://github.com/snesrev/sm"><b>sm</b></a><br><sub>snesrev</sub></td><td>用 C 重写的超级银河战士（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/e/e4/Smetroidbox.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 重制 / 移植

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/snesrev/smw"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png" width="160" alt="snesrev/smw"></a></td><td><a href="https://github.com/snesrev/smw"><b>smw</b></a><br><sub>snesrev</sub></td><td>用 C 重写的超级马里奥世界（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png">维基百科（© 版权方）</a></sub></td></tr>
</table>

### MD / Genesis

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/sonicretro/s1disasm"><img src="https://upload.wikimedia.org/wikipedia/en/b/ba/Sonic_the_Hedgehog_1_Genesis_box_art.jpg" width="160" alt="sonicretro/s1disasm"></a></td><td><a href="https://github.com/sonicretro/s1disasm"><b>s1disasm</b></a><br><sub>sonicretro</sub></td><td>刺猬索尼克（MD）完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/b/ba/Sonic_the_Hedgehog_1_Genesis_box_art.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/sonicretro/s2disasm"><img src="https://upload.wikimedia.org/wikipedia/en/0/0c/Sonic_2_US_Cover.jpg" width="160" alt="sonicretro/s2disasm"></a></td><td><a href="https://github.com/sonicretro/s2disasm"><b>s2disasm</b></a><br><sub>sonicretro</sub></td><td>索尼克 2（MD）完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0c/Sonic_2_US_Cover.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/sonicretro/skdisasm"><img src="https://upload.wikimedia.org/wikipedia/en/d/d3/Sonic_%26_Knuckles_cover.jpg" width="160" alt="sonicretro/skdisasm"></a></td><td><a href="https://github.com/sonicretro/skdisasm"><b>skdisasm</b></a><br><sub>sonicretro</sub></td><td>索尼克 3 &amp; 纳克鲁斯完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/d/d3/Sonic_%26_Knuckles_cover.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 重制 / 移植

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/RSDKModding/RSDKv5-Decompilation"><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv5-Decompilation/master/header.png?raw=true" width="160" alt="RSDKModding/RSDKv5-Decompilation"></a></td><td><a href="https://github.com/RSDKModding/RSDKv5-Decompilation"><b>RSDKv5-Decompilation</b></a><br><sub>RSDKModding</sub></td><td>索尼克狂热的引擎反编译（读取你自己的数据文件）</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/RSDKModding/RSDKv4-Decompilation"><img src="https://raw.githubusercontent.com/RSDKModding/RSDKv4-Decompilation/main/header.png?raw=true" width="160" alt="RSDKModding/RSDKv4-Decompilation"></a></td><td><a href="https://github.com/RSDKModding/RSDKv4-Decompilation"><b>RSDKv4-Decompilation</b></a><br><sub>RSDKModding</sub></td><td>索尼克 1、2（2013）引擎的反编译</td><td>否</td><td><sub>项目 README</sub></td></tr>
</table>

### 世嘉土星

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/yaz0r/Azel"><img src="https://github.com/user-attachments/assets/71f6a246-24cc-4d64-9673-53b9e4c3e4df" width="160" alt="yaz0r/Azel"></a></td><td><a href="https://github.com/yaz0r/Azel"><b>Azel</b></a><br><sub>yaz0r</sub></td><td>逆向并重新实现的铁甲飞龙 Saga</td><td>否</td><td><sub>项目 README</sub></td></tr>
</table>

### Game Boy

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/pret/pokered"><img src="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp" width="160" alt="pret/pokered"></a></td><td><a href="https://github.com/pret/pokered"><b>pokered</b></a><br><sub>pret</sub></td><td>宝可梦红/蓝完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokegold"><img src="https://upload.wikimedia.org/wikipedia/en/4/4c/Pok%C3%A9mon_box_art_-_Gold_Version.png" width="160" alt="pret/pokegold"></a></td><td><a href="https://github.com/pret/pokegold"><b>pokegold</b></a><br><sub>pret</sub></td><td>宝可梦金/银完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/4/4c/Pok%C3%A9mon_box_art_-_Gold_Version.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeyellow"><img src="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp" width="160" alt="pret/pokeyellow"></a></td><td><a href="https://github.com/pret/pokeyellow"><b>pokeyellow</b></a><br><sub>pret</sub></td><td>宝可梦皮卡丘版完整反汇编</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/af/Pok%C3%A9mon_Red_and_Blue_cover_art.webp">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokecrystal"><img src="https://github.com/user-attachments/assets/c39cb860-bb9c-4204-9184-b2761ead0a74" width="160" alt="pret/pokecrystal"></a></td><td><a href="https://github.com/pret/pokecrystal"><b>pokecrystal</b></a><br><sub>pret</sub></td><td>宝可梦水晶完整反汇编</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/zladx/LADX-Disassembly"><img src="https://raw.githubusercontent.com/zladx/LADX-Disassembly/main/docs/entities.png" width="160" alt="zladx/LADX-Disassembly"></a></td><td><a href="https://github.com/zladx/LADX-Disassembly"><b>LADX-Disassembly</b></a><br><sub>zladx</sub></td><td>塞尔达：织梦岛 DX 完整反汇编</td><td>否</td><td><sub>项目 README</sub></td></tr>
</table>

### GBA

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/pret/pokeemerald"><img src="https://user-images.githubusercontent.com/35422415/226195894-bd8307ea-f6be-46cc-85ec-dd28b4f2d144.gif" width="160" alt="pret/pokeemerald"></a></td><td><a href="https://github.com/pret/pokeemerald"><b>pokeemerald</b></a><br><sub>pret</sub></td><td>宝可梦绿宝石的 C 源码，无数改版的起点</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/pret/pokefirered"><img src="https://upload.wikimedia.org/wikipedia/en/a/a7/Pokemon_LeafGreen_box.jpg" width="160" alt="pret/pokefirered"></a></td><td><a href="https://github.com/pret/pokefirered"><b>pokefirered</b></a><br><sub>pret</sub></td><td>宝可梦火红/叶绿的 C 源码</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a7/Pokemon_LeafGreen_box.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tmc"><img src="https://upload.wikimedia.org/wikipedia/en/0/0a/TLOZ-_Minish_Cap_NA_Box_art.png" width="160" alt="zeldaret/tmc"></a></td><td><a href="https://github.com/zeldaret/tmc"><b>tmc</b></a><br><sub>zeldaret</sub></td><td>塞尔达：缩小帽，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0a/TLOZ-_Minish_Cap_NA_Box_art.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeruby"><img src="https://upload.wikimedia.org/wikipedia/en/b/be/PokemonRubySapphireBox.jpg" width="160" alt="pret/pokeruby"></a></td><td><a href="https://github.com/pret/pokeruby"><b>pokeruby</b></a><br><sub>pret</sub></td><td>宝可梦红宝石/蓝宝石的 C 源码</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/b/be/PokemonRubySapphireBox.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/jiangzhengwenjz/katam"><img src="https://upload.wikimedia.org/wikipedia/en/0/0b/Kirby_%26_the_Amazing_Mirror.jpg" width="160" alt="jiangzhengwenjz/katam"></a></td><td><a href="https://github.com/jiangzhengwenjz/katam"><b>katam</b></a><br><sub>jiangzhengwenjz</sub></td><td>星之卡比：镜之大迷宫，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0b/Kirby_%26_the_Amazing_Mirror.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pmd-red"><img src="https://upload.wikimedia.org/wikipedia/en/d/d3/Pok%C3%A9mon_Mystery_Dungeon_Blue_and_Red_Rescue_Team_cover_arts.jpg" width="160" alt="pret/pmd-red"></a></td><td><a href="https://github.com/pret/pmd-red"><b>pmd-red</b></a><br><sub>pret</sub></td><td>宝可梦不可思议的迷宫 赤之救助队，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/d/d3/Pok%C3%A9mon_Mystery_Dungeon_Blue_and_Red_Rescue_Team_cover_arts.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

### 任天堂 64

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/zeldaret/oot"><img src="https://github.com/user-attachments/assets/70b4a529-9a5e-4b9c-ac45-48f9f2183eed" width="160" alt="zeldaret/oot"></a></td><td><a href="https://github.com/zeldaret/oot"><b>oot</b></a><br><sub>zeldaret</sub></td><td>时之笛完整反编译为 C（不含 ROM）</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/sm64"><img src="https://upload.wikimedia.org/wikipedia/en/e/e9/Super_Mario_64.png" width="160" alt="n64decomp/sm64"></a></td><td><a href="https://github.com/n64decomp/sm64"><b>sm64</b></a><br><sub>n64decomp</sub></td><td>可构建的超级马里奥 64 C 源码（不含 ROM）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/e/e9/Super_Mario_64.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/HarbourMasters/Starship"><img src="https://upload.wikimedia.org/wikipedia/en/6/63/StarFox64_N64_Game_Box.jpg" width="160" alt="HarbourMasters/Starship"></a></td><td><a href="https://github.com/HarbourMasters/Starship"><b>Starship</b></a><br><sub>HarbourMasters</sub></td><td>在 PC 上原生运行星际火狐 64（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/63/StarFox64_N64_Game_Box.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/mk64"><img src="https://upload.wikimedia.org/wikipedia/en/a/a1/Mario_Kart_64.jpg" width="160" alt="n64decomp/mk64"></a></td><td><a href="https://github.com/n64decomp/mk64"><b>mk64</b></a><br><sub>n64decomp</sub></td><td>马里奥赛车 64，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a1/Mario_Kart_64.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/mm"><img src="https://user-images.githubusercontent.com/12245827/191111633-e72abfd3-b53c-4d13-82d1-44e6718f1fb0.png" width="160" alt="zeldaret/mm"></a></td><td><a href="https://github.com/zeldaret/mm"><b>mm</b></a><br><sub>zeldaret</sub></td><td>塞尔达：姆吉拉的假面，反编译为 C</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/pmret/papermario"><img src="https://upload.wikimedia.org/wikipedia/en/6/61/Papermario.jpg" width="160" alt="pmret/papermario"></a></td><td><a href="https://github.com/pmret/papermario"><b>papermario</b></a><br><sub>pmret</sub></td><td>纸片马里奥（N64），反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/61/Papermario.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/N64Recomp/N64Recomp"><img src="https://opengraph.githubassets.com/1/N64Recomp/N64Recomp" width="160" alt="N64Recomp/N64Recomp"></a></td><td><a href="https://github.com/N64Recomp/N64Recomp"><b>N64Recomp</b></a><br><sub>N64Recomp</sub></td><td>把 N64 游戏直接重编译成原生代码</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/n64decomp/perfect_dark"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg" width="160" alt="n64decomp/perfect_dark"></a></td><td><a href="https://github.com/n64decomp/perfect_dark"><b>perfect_dark</b></a><br><sub>n64decomp</sub></td><td>完美黑暗（N64），反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 重制 / 移植

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/HarbourMasters/Shipwright"><img src="https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg" width="160" alt="HarbourMasters/Shipwright"></a></td><td><a href="https://github.com/HarbourMasters/Shipwright"><b>Shipwright</b></a><br><sub>HarbourMasters</sub></td><td>在 PC 上原生运行塞尔达：时之笛（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/Zelda64Recomp/Zelda64Recomp"><img src="https://raw.githubusercontent.com/Zelda64Recomp/Zelda64Recomp/dev/docs/deck_gyro_1.jpg" width="160" alt="Zelda64Recomp/Zelda64Recomp"></a></td><td><a href="https://github.com/Zelda64Recomp/Zelda64Recomp"><b>Zelda64Recomp</b></a><br><sub>Zelda64Recomp</sub></td><td>重编译到 PC 的姆吉拉的假面，支持现代操作（ROM 自备）</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/2ship2harkinian/2ship2harkinian"><img src="https://upload.wikimedia.org/wikipedia/en/6/60/The_Legend_of_Zelda_-_Majora%27s_Mask_Box_Art.jpg" width="160" alt="2ship2harkinian/2ship2harkinian"></a></td><td><a href="https://github.com/2ship2harkinian/2ship2harkinian"><b>2ship2harkinian</b></a><br><sub>2ship2harkinian</sub></td><td>在 PC 上原生运行塞尔达：姆吉拉的假面（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/6/60/The_Legend_of_Zelda_-_Majora%27s_Mask_Box_Art.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 资源提取与工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/ethteck/splat"><img src="https://opengraph.githubassets.com/1/ethteck/splat" width="160" alt="ethteck/splat"></a></td><td><a href="https://github.com/ethteck/splat"><b>splat</b></a><br><sub>ethteck</sub></td><td>把 N64、PS1 二进制切分成可反编译的工程</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/NEstelami/ZAPD"><img src="https://raw.githubusercontent.com/NEstelami/ZAPD/master/docs/zapd_warning_example.png?raw=true" width="160" alt="NEstelami/ZAPD"></a></td><td><a href="https://github.com/NEstelami/ZAPD"><b>ZAPD</b></a><br><sub>NEstelami</sub></td><td>把 Zelda 64 的资源转成可编辑的源文件</td><td>否</td><td><sub>项目 README</sub></td></tr>
</table>

### GameCube

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/zeldaret/tww"><img src="https://upload.wikimedia.org/wikipedia/en/7/79/The_Legend_of_Zelda_The_Wind_Waker.jpg" width="160" alt="zeldaret/tww"></a></td><td><a href="https://github.com/zeldaret/tww"><b>tww</b></a><br><sub>zeldaret</sub></td><td>塞尔达：风之杖，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/7/79/The_Legend_of_Zelda_The_Wind_Waker.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/doldecomp/sms"><img src="https://upload.wikimedia.org/wikipedia/en/0/05/Super_Mario_Sunshine_Box_Art.png" width="160" alt="doldecomp/sms"></a></td><td><a href="https://github.com/doldecomp/sms"><b>sms</b></a><br><sub>doldecomp</sub></td><td>超级马里奥阳光，反编译为 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/05/Super_Mario_Sunshine_Box_Art.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/doldecomp/melee"><img src="https://upload.wikimedia.org/wikipedia/en/7/75/Super_Smash_Bros_Melee_box_art.png" width="160" alt="doldecomp/melee"></a></td><td><a href="https://github.com/doldecomp/melee"><b>melee</b></a><br><sub>doldecomp</sub></td><td>任天堂明星大乱斗 DX，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/7/75/Super_Smash_Bros_Melee_box_art.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/tp"><img src="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Twilight_Princess_Game_Cover.jpg" width="160" alt="zeldaret/tp"></a></td><td><a href="https://github.com/zeldaret/tp"><b>tp</b></a><br><sub>zeldaret</sub></td><td>塞尔达：黄昏公主，反编译为 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Twilight_Princess_Game_Cover.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/projectPiki/pikmin2"><img src="https://upload.wikimedia.org/wikipedia/en/3/38/Pikmin_2_Case.jpg" width="160" alt="projectPiki/pikmin2"></a></td><td><a href="https://github.com/projectPiki/pikmin2"><b>pikmin2</b></a><br><sub>projectPiki</sub></td><td>皮克敏 2，反编译为 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/38/Pikmin_2_Case.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 资源提取与工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/encounter/decomp-toolkit"><img src="https://opengraph.githubassets.com/1/encounter/decomp-toolkit" width="160" alt="encounter/decomp-toolkit"></a></td><td><a href="https://github.com/encounter/decomp-toolkit"><b>decomp-toolkit</b></a><br><sub>encounter</sub></td><td>众多 GameCube、Wii 反编译项目背后的工具链</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/encounter/objdiff"><img src="https://raw.githubusercontent.com/encounter/objdiff/main/assets/screen-symbols.png" width="160" alt="encounter/objdiff"></a></td><td><a href="https://github.com/encounter/objdiff"><b>objdiff</b></a><br><sub>encounter</sub></td><td>一眼看出你的反编译函数还差在哪</td><td>否</td><td><sub>项目 README</sub></td></tr>
</table>

### Wii

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/zeldaret/ss"><img src="https://upload.wikimedia.org/wikipedia/en/9/99/Legend_of_Zelda_Skyward_Sword_boxart.png" width="160" alt="zeldaret/ss"></a></td><td><a href="https://github.com/zeldaret/ss"><b>ss</b></a><br><sub>zeldaret</sub></td><td>塞尔达：天空之剑，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/9/99/Legend_of_Zelda_Skyward_Sword_boxart.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/DarkRTA/rb3"><img src="https://upload.wikimedia.org/wikipedia/en/3/3b/Rock_Band_3_Game_Cover.jpg" width="160" alt="DarkRTA/rb3"></a></td><td><a href="https://github.com/DarkRTA/rb3"><b>rb3</b></a><br><sub>DarkRTA</sub></td><td>摇滚乐队 3（Wii），反编译为 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/3b/Rock_Band_3_Game_Cover.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

### NDS

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/pret/pokeplatinum"><img src="https://github.com/user-attachments/assets/157f7c15-4684-48e9-aacb-eefefbcffcec" width="160" alt="pret/pokeplatinum"></a></td><td><a href="https://github.com/pret/pokeplatinum"><b>pokeplatinum</b></a><br><sub>pret</sub></td><td>宝可梦白金的 C 源码</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/zeldaret/ph"><img src="https://upload.wikimedia.org/wikipedia/en/5/5e/The_Legend_of_Zelda_Phantom_Hourglass_Game_Cover.jpg" width="160" alt="zeldaret/ph"></a></td><td><a href="https://github.com/zeldaret/ph"><b>ph</b></a><br><sub>zeldaret</sub></td><td>塞尔达：幻影沙漏，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/5/5e/The_Legend_of_Zelda_Phantom_Hourglass_Game_Cover.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/pret/pokeheartgold"><img src="https://upload.wikimedia.org/wikipedia/en/c/cb/PokemonHGSSBox.jpg" width="160" alt="pret/pokeheartgold"></a></td><td><a href="https://github.com/pret/pokeheartgold"><b>pokeheartgold</b></a><br><sub>pret</sub></td><td>宝可梦心金/魂银，反编译为 C</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/c/cb/PokemonHGSSBox.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

### 3DS

#### 资源提取与工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/3DSGuy/Project_CTR"><img src="https://opengraph.githubassets.com/1/3DSGuy/Project_CTR" width="160" alt="3DSGuy/Project_CTR"></a></td><td><a href="https://github.com/3DSGuy/Project_CTR"><b>Project_CTR</b></a><br><sub>3DSGuy</sub></td><td>构建和查看 3DS 文件格式（ctrtool / makerom）</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
</table>

### PS1

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/Xeeynamo/sotn-decomp"><img src="https://github.com/user-attachments/assets/fff7ddb2-736f-4e7d-b0ee-3c1151649773" width="160" alt="Xeeynamo/sotn-decomp"></a></td><td><a href="https://github.com/Xeeynamo/sotn-decomp"><b>sotn-decomp</b></a><br><sub>Xeeynamo</sub></td><td>恶魔城：月下夜想曲，反编译为 C</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/shdecompilations/silent-hill-decomp"><img src="https://upload.wikimedia.org/wikipedia/en/9/96/Silent_Hill_video_game_cover.png" width="160" alt="shdecompilations/silent-hill-decomp"></a></td><td><a href="https://github.com/shdecompilations/silent-hill-decomp"><b>silent-hill-decomp</b></a><br><sub>shdecompilations</sub></td><td>寂静岭（PS1）反编译进行中</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/9/96/Silent_Hill_video_game_cover.png">维基百科（© 版权方）</a></sub></td></tr>
</table>

### PS2

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/ran-j/PS2Recomp"><img src="https://opengraph.githubassets.com/1/ran-j/PS2Recomp" width="160" alt="ran-j/PS2Recomp"></a></td><td><a href="https://github.com/ran-j/PS2Recomp"><b>PS2Recomp</b></a><br><sub>ran-j</sub></td><td>把 PS2 游戏重编译成原生 PC 程序</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/open-goal/jak-project"><img src="https://raw.githubusercontent.com/open-goal/jak-project/master/docs/img/promosmall1.png" width="160" alt="open-goal/jak-project"></a></td><td><a href="https://github.com/open-goal/jak-project"><b>jak-project</b></a><br><sub>open-goal</sub></td><td>在 PC 上原生运行杰克与达斯特（光盘自备）</td><td>否</td><td><sub>项目 README</sub></td></tr>
</table>

### Xbox / Xbox 360

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/hedge-dev/XenonRecomp"><img src="https://opengraph.githubassets.com/1/hedge-dev/XenonRecomp" width="160" alt="hedge-dev/XenonRecomp"></a></td><td><a href="https://github.com/hedge-dev/XenonRecomp"><b>XenonRecomp</b></a><br><sub>hedge-dev</sub></td><td>把 Xbox 360 游戏重编译为原生 C++</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
</table>

#### 重制 / 移植

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/hedge-dev/UnleashedRecomp"><img src="https://upload.wikimedia.org/wikipedia/en/a/a0/Sonic_unleashed_boxart.jpg" width="160" alt="hedge-dev/UnleashedRecomp"></a></td><td><a href="https://github.com/hedge-dev/UnleashedRecomp"><b>UnleashedRecomp</b></a><br><sub>hedge-dev</sub></td><td>在 PC 上原生运行索尼克：释放（游戏自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a0/Sonic_unleashed_boxart.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 资源提取与工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/xemu-project/xemu"><img src="https://user-images.githubusercontent.com/71127352/144098855-dbc7b12a-d715-4102-b45c-faeb46deabde.png" width="160" alt="xemu-project/xemu"></a></td><td><a href="https://github.com/xemu-project/xemu"><b>xemu</b></a><br><sub>xemu-project</sub></td><td>在 Windows、macOS、Linux 上玩初代 Xbox 游戏</td><td>否</td><td><sub>维护者发布</sub></td></tr>
</table>

### PC / DOS / PC-98

#### 反编译 / 重编译

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/N0zoM1z0/dx-ball"><img src="https://raw.githubusercontent.com/N0zoM1z0/dx-ball/main/resources/dxball-title.png" width="160" alt="N0zoM1z0/dx-ball"></a></td><td><a href="https://github.com/N0zoM1z0/dx-ball"><b>dx-ball</b></a><br><sub>N0zoM1z0</sub></td><td>用 C/C++ 重建 DX-Ball 1.07，并对照原版 x86 测试</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th04"><img src="https://raw.githubusercontent.com/N0zoM1z0/th04/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th04"></a></td><td><a href="https://github.com/N0zoM1z0/th04"><b>th04</b></a><br><sub>N0zoM1z0</sub></td><td>东方幻想乡（PC-98）的可读源码，对照原编译器校验</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th08"><img src="https://raw.githubusercontent.com/N0zoM1z0/th08/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th08"></a></td><td><a href="https://github.com/N0zoM1z0/th08"><b>th08</b></a><br><sub>N0zoM1z0</sub></td><td>东方永夜抄，重建为源码</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th10"><img src="https://raw.githubusercontent.com/N0zoM1z0/th10/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th10"></a></td><td><a href="https://github.com/N0zoM1z0/th10"><b>th10</b></a><br><sub>N0zoM1z0</sub></td><td>东方风神录，重建为源码</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/isledecomp/isle"><img src="https://upload.wikimedia.org/wikipedia/en/a/a1/Lego-island.jpg" width="160" alt="isledecomp/isle"></a></td><td><a href="https://github.com/isledecomp/isle"><b>isle</b></a><br><sub>isledecomp</sub></td><td>乐高岛（1997），反编译为 C++</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/a/a1/Lego-island.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/diasurgical/DevilutionX"><img src="https://github.com/user-attachments/assets/7ac73801-ef7b-4cc1-8442-a191a2a0a1ce" width="160" alt="diasurgical/DevilutionX"></a></td><td><a href="https://github.com/diasurgical/DevilutionX"><b>DevilutionX</b></a><br><sub>diasurgical</sub></td><td>在现代系统上玩暗黑破坏神（需你自己的 DIABDAT.MPQ）</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th09"><img src="https://raw.githubusercontent.com/N0zoM1z0/th09/main/resources/title-screen.png" width="160" alt="N0zoM1z0/th09"></a></td><td><a href="https://github.com/N0zoM1z0/th09"><b>th09</b></a><br><sub>N0zoM1z0</sub></td><td>东方花映冢，重建为源码</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th095"><img src="https://raw.githubusercontent.com/N0zoM1z0/th095/main/resources/title-screen.jpg" width="160" alt="N0zoM1z0/th095"></a></td><td><a href="https://github.com/N0zoM1z0/th095"><b>th095</b></a><br><sub>N0zoM1z0</sub></td><td>东方文花帖，重建为源码</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th105"><img src="https://raw.githubusercontent.com/N0zoM1z0/th105/main/resources/title-screen.jpg" width="160" alt="N0zoM1z0/th105"></a></td><td><a href="https://github.com/N0zoM1z0/th105"><b>th105</b></a><br><sub>N0zoM1z0</sub></td><td>东方绯想天，重建为源码</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/touhou-reverse-engineering"><img src="https://opengraph.githubassets.com/1/N0zoM1z0/touhou-reverse-engineering" width="160" alt="N0zoM1z0/touhou-reverse-engineering"></a></td><td><a href="https://github.com/N0zoM1z0/touhou-reverse-engineering"><b>touhou-reverse-engineering</b></a><br><sub>N0zoM1z0</sub></td><td>以证据为先的东方 IDA 笔记，附运行时补丁实验</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
</table>

#### 重制 / 移植

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><img src="https://raw.githubusercontent.com/ucodia/desktop-games-nostalgia/main/docs/demo.gif" width="160" alt="ucodia/desktop-games-nostalgia"></a></td><td><a href="https://github.com/ucodia/desktop-games-nostalgia"><b>desktop-games-nostalgia</b></a><br><sub>ucodia</sub></td><td>再砸一次桌面：Gemtree 2000 年的小玩具登上 macOS 和网页</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><img src="https://raw.githubusercontent.com/tuunanet/rea-ski-or-die-reconstruction/main/docs/snowball-war.gif" width="160" alt="tuunanet/rea-ski-or-die-reconstruction"></a></td><td><a href="https://github.com/tuunanet/rea-ski-or-die-reconstruction"><b>rea-ski-or-die-reconstruction</b></a><br><sub>tuunanet</sub></td><td>Ski or Die 的雪球大战，用 Rust + SDL2 重做（素材自备）</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><img src="https://raw.githubusercontent.com/Moxnatiy/OpenBattlefield2/master/docs/screenshots/menu-main.png" width="160" alt="Moxnatiy/OpenBattlefield2"></a></td><td><a href="https://github.com/Moxnatiy/OpenBattlefield2"><b>OpenBattlefield2</b></a><br><sub>Moxnatiy</sub></td><td>战地 2 引擎的 C++20 净室重写（读取你自己的游戏）</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenRsG/GunZRs"><img src="https://raw.githubusercontent.com/OpenRsG/GunZRs/main/docs/media/menu.jpg" width="160" alt="OpenRsG/GunZRs"></a></td><td><a href="https://github.com/OpenRsG/GunZRs"><b>GunZRs</b></a><br><sub>OpenRsG</sub></td><td>GunZ：The Duel 用 Rust + Bevy 重生</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/a-barzanti/ai-rebuilds"><img src="https://opengraph.githubassets.com/1/a-barzanti/ai-rebuilds" width="160" alt="a-barzanti/ai-rebuilds"></a></td><td><a href="https://github.com/a-barzanti/ai-rebuilds"><b>ai-rebuilds</b></a><br><sub>a-barzanti</sub></td><td>被遗弃的老游戏重回浏览器，不含任何原版文件</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/OpenRCT2/OpenRCT2"><img src="https://github.com/user-attachments/assets/fa893cc8-1484-4751-94be-4ead00a6c8f9" width="160" alt="OpenRCT2/OpenRCT2"></a></td><td><a href="https://github.com/OpenRCT2/OpenRCT2"><b>OpenRCT2</b></a><br><sub>OpenRCT2</sub></td><td>开源版过山车大亨 2，在现代系统上继续运行</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenMW/openmw"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/OpenMW_with_example_suit_2.png" width="160" alt="OpenMW/openmw"></a></td><td><a href="https://github.com/OpenMW/openmw"><b>openmw</b></a><br><sub>OpenMW</sub></td><td>在现代开源引擎上玩晨风</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/commons/9/9e/OpenMW_with_example_suit_2.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/julianxhokaxhiu/FFNx"><img src="https://raw.githubusercontent.com/julianxhokaxhiu/FFNx/master/.screens/ff7.png" width="160" alt="julianxhokaxhiu/FFNx"></a></td><td><a href="https://github.com/julianxhokaxhiu/FFNx"><b>FFNx</b></a><br><sub>julianxhokaxhiu</sub></td><td>PC 版 FF7/FF8 的现代驱动与 Mod 平台</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/Interkarma/daggerfall-unity"><img src="https://github.com/Interkarma/daggerfall-unity/assets/10426244/4f176f9d-6332-47b3-a4d7-317ed8d6b38b" width="160" alt="Interkarma/daggerfall-unity"></a></td><td><a href="https://github.com/Interkarma/daggerfall-unity"><b>daggerfall-unity</b></a><br><sub>Interkarma</sub></td><td>用 Unity 重现的匕首雨（读取你自己的游戏数据）</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenXcom/OpenXcom"><img src="https://opengraph.githubassets.com/1/OpenXcom/OpenXcom" width="160" alt="OpenXcom/OpenXcom"></a></td><td><a href="https://github.com/OpenXcom/OpenXcom"><b>OpenXcom</b></a><br><sub>OpenXcom</sub></td><td>在现代开源引擎上玩初代 UFO / X-COM</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/scummvm/scummvm"><img src="https://www.scummvm.org/data/screenshots/prince/prince/prince_win_en_1_3_full.png" width="160" alt="scummvm/scummvm"></a></td><td><a href="https://github.com/scummvm/scummvm"><b>scummvm</b></a><br><sub>scummvm</sub></td><td>在几乎任何设备上玩经典点击冒险游戏</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/fallout2-ce/fallout2-ce"><img src="https://raw.githubusercontent.com/fallout2-ce/fallout2-ce/main/docs/images/two-column-inventory.jpg" width="160" alt="fallout2-ce/fallout2-ce"></a></td><td><a href="https://github.com/fallout2-ce/fallout2-ce"><b>fallout2-ce</b></a><br><sub>fallout2-ce</sub></td><td>在现代系统上玩辐射 2（读取你自己的游戏数据）</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/OpenTTD/OpenTTD"><img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/OpenTTD-15.3-en.png" width="160" alt="OpenTTD/OpenTTD"></a></td><td><a href="https://github.com/OpenTTD/OpenTTD"><b>OpenTTD</b></a><br><sub>OpenTTD</sub></td><td>开源的运输大亨，至今仍在更新</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/commons/b/ba/OpenTTD-15.3-en.png">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/OpenRA/OpenRA"><img src="https://www.openra.net/images/news/20260222-generators.gif" width="160" alt="OpenRA/OpenRA"></a></td><td><a href="https://github.com/OpenRA/OpenRA"><b>OpenRA</b></a><br><sub>OpenRA</sub></td><td>为现代联机重建的经典命令与征服</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/perfect-dark-pc-port/perfect_dark"><img src="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg" width="160" alt="perfect-dark-pc-port/perfect_dark"></a></td><td><a href="https://github.com/perfect-dark-pc-port/perfect_dark"><b>perfect_dark</b></a><br><sub>perfect-dark-pc-port</sub></td><td>在 PC 上原生运行完美黑暗（ROM 自备）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/3/32/Perfect_dark_box.jpg">维基百科（© 版权方）</a></sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/th08-web"><img src="https://raw.githubusercontent.com/N0zoM1z0/th08-web/main/resources/th08-web-social-preview.jpg" width="160" alt="N0zoM1z0/th08-web"></a></td><td><a href="https://github.com/N0zoM1z0/th08-web"><b>th08-web</b></a><br><sub>N0zoM1z0</sub></td><td>在浏览器里玩永夜抄，基于 th08 重建</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/AsyncFinn/rook"><img src="https://opengraph.githubassets.com/1/AsyncFinn/rook" width="160" alt="AsyncFinn/rook"></a></td><td><a href="https://github.com/AsyncFinn/rook"><b>rook</b></a><br><sub>AsyncFinn</sub></td><td>Rust 写的 Roblox 兼容引擎，对照 Studio 测试</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/tallowmere/free-heroes4"><img src="https://upload.wikimedia.org/wikipedia/en/c/cc/Heroes_of_Might_and_Magic_IV_box.jpg" width="160" alt="tallowmere/free-heroes4"></a></td><td><a href="https://github.com/tallowmere/free-heroes4"><b>free-heroes4</b></a><br><sub>tallowmere</sub></td><td>英雄无敌 IV 的 C++23 新引擎（读取你的 GOG 文件）</td><td>否</td><td><sub><a href="https://upload.wikimedia.org/wikipedia/en/c/cc/Heroes_of_Might_and_Magic_IV_box.jpg">维基百科（© 版权方）</a></sub></td></tr>
</table>

#### 资源提取与工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/ata4/disunity"><img src="https://opengraph.githubassets.com/1/ata4/disunity" width="160" alt="ata4/disunity"></a></td><td><a href="https://github.com/ata4/disunity"><b>disunity</b></a><br><sub>ata4</sub></td><td>早期的 Unity 资源文件探查工具</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/Perfare/AssetStudio"><img src="https://opengraph.githubassets.com/1/Perfare/AssetStudio" width="160" alt="Perfare/AssetStudio"></a></td><td><a href="https://github.com/Perfare/AssetStudio"><b>AssetStudio</b></a><br><sub>Perfare</sub></td><td>浏览并导出 Unity 游戏资源</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/AssetRipper/AssetRipper"><img src="https://raw.githubusercontent.com/AssetRipper/AssetRipper/master/docs/articles/images/RunningOnMac/004.png" width="160" alt="AssetRipper/AssetRipper"></a></td><td><a href="https://github.com/AssetRipper/AssetRipper"><b>AssetRipper</b></a><br><sub>AssetRipper</sub></td><td>把 Unity 构建产物还原成可编辑的工程</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/ladislav-zezula/CascLib"><img src="https://opengraph.githubassets.com/1/ladislav-zezula/CascLib" width="160" alt="ladislav-zezula/CascLib"></a></td><td><a href="https://github.com/ladislav-zezula/CascLib"><b>CascLib</b></a><br><sub>ladislav-zezula</sub></td><td>读取暴雪 CASC 游戏存档格式</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/N0zoM1z0/touhou-reconstruction-factory"><img src="https://opengraph.githubassets.com/1/N0zoM1z0/touhou-reconstruction-factory" width="160" alt="N0zoM1z0/touhou-reconstruction-factory"></a></td><td><a href="https://github.com/N0zoM1z0/touhou-reconstruction-factory"><b>touhou-reconstruction-factory</b></a><br><sub>N0zoM1z0</sub></td><td>东方系列重建背后的智能体流水线</td><td>❔ 待验证</td><td><sub>仓库卡片</sub></td></tr>
</table>

## 应用 / Electron / 桌面

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/michaelshimeles/sketch"><img src="https://raw.githubusercontent.com/michaelshimeles/sketch/main/docs/screenshots/app_demo.png" width="160" alt="michaelshimeles/sketch"></a></td><td><a href="https://github.com/michaelshimeles/sketch"><b>sketch</b></a><br><sub>michaelshimeles</sub></td><td>Rust 写的无限设计画布，研究 Paper 后重建</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/rec-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/rec-rs/main/docs/screenshots/main.png" width="160" alt="michaelshimeles/rec-rs"></a></td><td><a href="https://github.com/michaelshimeles/rec-rs"><b>rec-rs</b></a><br><sub>michaelshimeles</sub></td><td>Rust 写的 macOS 快速录屏工具，参照 OBS 设计</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/iammukeshm/hexgrab"><img src="https://opengraph.githubassets.com/1/iammukeshm/hexgrab" width="160" alt="iammukeshm/hexgrab"></a></td><td><a href="https://github.com/iammukeshm/hexgrab"><b>hexgrab</b></a><br><sub>iammukeshm</sub></td><td>迷你 Windows 取色器，从 PowerToys 二进制研究而来</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/AdamLinCodes/AdamTerm"><img src="https://raw.githubusercontent.com/AdamLinCodes/AdamTerm/main/docs/adamterm.png" width="160" alt="AdamLinCodes/AdamTerm"></a></td><td><a href="https://github.com/AdamLinCodes/AdamTerm"><b>AdamTerm</b></a><br><sub>AdamLinCodes</sub></td><td>研究 Ghostty 后做出的极简 macOS 终端</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><img src="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg" width="160" alt="az9713/wispr-flow-rea-teardown"></a></td><td><a href="https://github.com/az9713/wispr-flow-rea-teardown"><b>wispr-flow-rea-teardown</b></a><br><sub>az9713</sub></td><td>拆解 Wispr Flow 语音管线，附 64 行重写版</td><td>✅ 是</td><td><sub><a href="https://img.youtube.com/vi/FnB9tHKBJXQ/maxresdefault.jpg">视频封面</a></sub></td></tr>
<tr><td><a href="https://github.com/cudanexus/vd-streamer-linux"><img src="https://opengraph.githubassets.com/1/cudanexus/vd-streamer-linux" width="160" alt="cudanexus/vd-streamer-linux"></a></td><td><a href="https://github.com/cudanexus/vd-streamer-linux"><b>vd-streamer-linux</b></a><br><sub>cudanexus</sub></td><td>把 Linux 桌面串流到 Quest、Pico 头显</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/electron/asar"><img src="images/asar-terminal.png" width="160" alt="electron/asar"></a></td><td><a href="https://github.com/electron/asar"><b>asar</b></a><br><sub>electron</sub></td><td>打包、解包 Electron 应用里的归档</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><img src="https://opengraph.githubassets.com/1/KarlssonChristoffer/DiskLens" width="160" alt="KarlssonChristoffer/DiskLens"></a></td><td><a href="https://github.com/KarlssonChristoffer/DiskLens"><b>DiskLens</b></a><br><sub>KarlssonChristoffer</sub></td><td>像 WinDirStat 一样看清 Windows 11 磁盘被什么占满</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/LilZeeCN/zee-rp"><img src="https://raw.githubusercontent.com/LilZeeCN/zee-rp/main/examples/screenshot/source.png" width="160" alt="LilZeeCN/zee-rp"></a></td><td><a href="https://github.com/LilZeeCN/zee-rp"><b>zee-rp</b></a><br><sub>LilZeeCN</sub></td><td>用命令行或 MCP 读写 Axure RP 原型文件</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/lxistired/ledger-reborn"><img src="https://raw.githubusercontent.com/lxistired/ledger-reborn/main/docs/screenshots/accounting.png" width="160" alt="lxistired/ledger-reborn"></a></td><td><a href="https://github.com/lxistired/ledger-reborn"><b>ledger-reborn</b></a><br><sub>lxistired</sub></td><td>本地优先的记账应用，参照 QuickBooks Mac 版</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/michaelshimeles/terminal-rs"><img src="https://raw.githubusercontent.com/michaelshimeles/terminal-rs/master/docs/img/overview.png" width="160" alt="michaelshimeles/terminal-rs"></a></td><td><a href="https://github.com/michaelshimeles/terminal-rs"><b>terminal-rs</b></a><br><sub>michaelshimeles</sub></td><td>Rust 写的彭博风格交易终端</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/GLinnik21/plx-native"><img src="https://raw.githubusercontent.com/GLinnik21/plx-native/main/docs/screenshots/home.jpg" width="160" alt="GLinnik21/plx-native"></a></td><td><a href="https://github.com/GLinnik21/plx-native"><b>plx-native</b></a><br><sub>GLinnik21</sub></td><td>LG 电视上更快的原生 Plex 客户端</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/storytold/photocraft"><img src="https://raw.githubusercontent.com/storytold/photocraft/main/docs/images/photocraft-demo.jpg" width="160" alt="storytold/photocraft"></a></td><td><a href="https://github.com/storytold/photocraft"><b>photocraft</b></a><br><sub>storytold</sub></td><td>从零开源重写的 Photoshop 风格编辑器</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/sickpyramid/ReaFuse"><img src="https://opengraph.githubassets.com/1/sickpyramid/ReaFuse" width="160" alt="sickpyramid/ReaFuse"></a></td><td><a href="https://github.com/sickpyramid/ReaFuse"><b>ReaFuse</b></a><br><sub>sickpyramid</sub></td><td>借助 REA 把两个 JS/TS 项目融合成一个</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/laaielichter/Reverseport"><img src="https://raw.githubusercontent.com/laaielichter/Reverseport/main/docs/assets/demo.gif" width="160" alt="laaielichter/Reverseport"></a></td><td><a href="https://github.com/laaielichter/Reverseport"><b>Reverseport</b></a><br><sub>laaielichter</sub></td><td>把逆向成果移植到 Godot、Unity、Unreal 或 three.js</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
</table>

## 协议 / 硬件

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/a-funk/open-appleremote"><img src="https://opengraph.githubassets.com/1/a-funk/open-appleremote" width="160" alt="a-funk/open-appleremote"></a></td><td><a href="https://github.com/a-funk/open-appleremote"><b>open-appleremote</b></a><br><sub>a-funk</sub></td><td>在 Linux 上用第一代 Siri 遥控器，连手势也支持</td><td>❔ 待验证</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/Slyvan25/OpenGHub"><img src="https://raw.githubusercontent.com/Slyvan25/OpenGHub/master/docs/screenshots/devices.png" width="160" alt="Slyvan25/OpenGHub"></a></td><td><a href="https://github.com/Slyvan25/OpenGHub"><b>OpenGHub</b></a><br><sub>Slyvan25</sub></td><td>在 Linux 上不用 G HUB 也能控制罗技外设</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/mitmproxy/mitmproxy"><img src="https://mitmproxy.org/screenshot.png" width="160" alt="mitmproxy/mitmproxy"></a></td><td><a href="https://github.com/mitmproxy/mitmproxy"><b>mitmproxy</b></a><br><sub>mitmproxy</sub></td><td>实时查看和修改 HTTPS 流量</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/postlund/pyatv"><img src="https://opengraph.githubassets.com/1/postlund/pyatv" width="160" alt="postlund/pyatv"></a></td><td><a href="https://github.com/postlund/pyatv"><b>pyatv</b></a><br><sub>postlund</sub></td><td>用 Python 控制 Apple TV 和 AirPlay 设备</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/wireshark/wireshark"><img src="images/wireshark-gui.png" width="160" alt="wireshark/wireshark"></a></td><td><a href="https://github.com/wireshark/wireshark"><b>wireshark</b></a><br><sub>wireshark</sub></td><td>看清网络上的每一个数据包</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
</table>

## 固件 / 驱动

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/grisuno/VSL-DSP"><img src="https://opengraph.githubassets.com/1/grisuno/VSL-DSP" width="160" alt="grisuno/VSL-DSP"></a></td><td><a href="https://github.com/grisuno/VSL-DSP"><b>VSL-DSP</b></a><br><sub>grisuno</sub></td><td>PreSonus AudioBox VSL 声卡的 Linux 内核模块</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/ReFirmLabs/binwalk"><img src="https://raw.githubusercontent.com/ReFirmLabs/binwalk/master/images/output.png" width="160" alt="ReFirmLabs/binwalk"></a></td><td><a href="https://github.com/ReFirmLabs/binwalk"><b>binwalk</b></a><br><sub>ReFirmLabs</sub></td><td>找出并提取固件镜像里藏着的东西</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/qilingframework/qiling"><img src="https://raw.githubusercontent.com/qilingframework/theme.qiling.io/master/source/img/fuzzer.jpg?raw=true" width="160" alt="qilingframework/qiling"></a></td><td><a href="https://github.com/qilingframework/qiling"><b>qiling</b></a><br><sub>qilingframework</sub></td><td>跨系统、跨 CPU 模拟并插桩二进制</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/ghidraninja/game-and-watch-backup"><img src="https://img.youtube.com/vi/-MzmoEFs0bQ/maxresdefault.jpg" width="160" alt="ghidraninja/game-and-watch-backup"></a></td><td><a href="https://github.com/ghidraninja/game-and-watch-backup"><b>game-and-watch-backup</b></a><br><sub>ghidraninja</sub></td><td>备份并恢复你自己的 Game &amp; Watch 固件</td><td>否</td><td><sub><a href="https://img.youtube.com/vi/-MzmoEFs0bQ/maxresdefault.jpg">视频封面</a></sub></td></tr>
<tr><td><a href="https://github.com/attify/firmware-analysis-toolkit"><img src="https://opengraph.githubassets.com/1/attify/firmware-analysis-toolkit" width="160" alt="attify/firmware-analysis-toolkit"></a></td><td><a href="https://github.com/attify/firmware-analysis-toolkit"><b>firmware-analysis-toolkit</b></a><br><sub>attify</sub></td><td>模拟运行物联网固件，安全地研究它</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/onekey-sec/unblob"><img src="images/unblob-terminal.png" width="160" alt="onekey-sec/unblob"></a></td><td><a href="https://github.com/onekey-sec/unblob"><b>unblob</b></a><br><sub>onekey-sec</sub></td><td>递归解包几乎所有固件和容器格式</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/travisgoodspeed/md380tools"><img src="https://opengraph.githubassets.com/1/travisgoodspeed/md380tools" width="160" alt="travisgoodspeed/md380tools"></a></td><td><a href="https://github.com/travisgoodspeed/md380tools"><b>md380tools</b></a><br><sub>travisgoodspeed</sub></td><td>TYT MD-380 对讲机的自制固件补丁</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
</table>

## 安全 / 评测

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><img src="https://raw.githubusercontent.com/NullLabTests/OpenBSD_netcat_REA/main/assets/rea-pipeline.png" width="160" alt="NullLabTests/OpenBSD_netcat_REA"></a></td><td><a href="https://github.com/NullLabTests/OpenBSD_netcat_REA"><b>OpenBSD_netcat_REA</b></a><br><sub>NullLabTests</sub></td><td>用 REA + Ghidra 静态分析 netcat-openbsd</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/morluto/rea/discussions/2254"><img src="images/rea-discussion-2254.png" width="160" alt="REA discussion #2254"></a></td><td><a href="https://github.com/morluto/rea/discussions/2254"><b>REA discussion #2254</b></a></td><td>分析去符号的 bzip2，并对照真实构建验证</td><td>✅ 是</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><img src="https://opengraph.githubassets.com/1/UnknownHacker1/rea-groundtruth" width="160" alt="UnknownHacker1/rea-groundtruth"></a></td><td><a href="https://github.com/UnknownHacker1/rea-groundtruth"><b>rea-groundtruth</b></a><br><sub>UnknownHacker1</sub></td><td>拿真实源码检验 REA 的分析报告</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/az9713/REA-demo"><img src="https://opengraph.githubassets.com/1/az9713/REA-demo" width="160" alt="az9713/REA-demo"></a></td><td><a href="https://github.com/az9713/REA-demo"><b>REA-demo</b></a><br><sub>az9713</sub></td><td>让 REA 分析它自己，附可证伪的预测</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-lab"><img src="https://opengraph.githubassets.com/1/pablodiazjorge/rea-lab" width="160" alt="pablodiazjorge/rea-lab"></a></td><td><a href="https://github.com/pablodiazjorge/rea-lab"><b>rea-lab</b></a><br><sub>pablodiazjorge</sub></td><td>Windows + Ghidra 练习题和预注册的 REA 评测</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
</table>

## 逆向工具

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><img src="https://opengraph.githubassets.com/1/ShadowSwaps/REA-Reconstruction-Companion" width="160" alt="ShadowSwaps/REA-Reconstruction-Companion"></a></td><td><a href="https://github.com/ShadowSwaps/REA-Reconstruction-Companion"><b>REA-Reconstruction-Companion</b></a><br><sub>ShadowSwaps</sub></td><td>让重建过程始终有证据可查的智能体技能</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/NationalSecurityAgency/ghidra"><img src="images/ghidra-gui.png" width="160" alt="NationalSecurityAgency/ghidra"></a></td><td><a href="https://github.com/NationalSecurityAgency/ghidra"><b>ghidra</b></a><br><sub>NationalSecurityAgency</sub></td><td>NSA 开源的免费反编译/反汇编套件</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/skylot/jadx"><img src="https://user-images.githubusercontent.com/118523/142730720-839f017e-38db-423e-b53f-39f5f0a0316f.png" width="160" alt="skylot/jadx"></a></td><td><a href="https://github.com/skylot/jadx"><b>jadx</b></a><br><sub>skylot</sub></td><td>把安卓 APK 还原成可读的 Java</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/LaurieWired/GhidraMCP"><img src="https://github.com/user-attachments/assets/4986d702-be3f-4697-acce-aea55cd79ad3" width="160" alt="LaurieWired/GhidraMCP"></a></td><td><a href="https://github.com/LaurieWired/GhidraMCP"><b>GhidraMCP</b></a><br><sub>LaurieWired</sub></td><td>让 AI 智能体通过 MCP 操作 Ghidra</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/x64dbg/x64dbg"><img src="https://raw.githubusercontent.com/x64dbg/x64dbg/development/.github/screenshots/cpu-light.png" width="160" alt="x64dbg/x64dbg"></a></td><td><a href="https://github.com/x64dbg/x64dbg"><b>x64dbg</b></a><br><sub>x64dbg</sub></td><td>Windows 程序首选的开源调试器</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/iBotPeaches/Apktool"><img src="images/apktool-terminal.png" width="160" alt="iBotPeaches/Apktool"></a></td><td><a href="https://github.com/iBotPeaches/Apktool"><b>Apktool</b></a><br><sub>iBotPeaches</sub></td><td>解包、阅读并重新打包安卓 APK</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/angr/angr"><img src="https://opengraph.githubassets.com/1/angr/angr" width="160" alt="angr/angr"></a></td><td><a href="https://github.com/angr/angr"><b>angr</b></a><br><sub>angr</sub></td><td>在 Python 里做符号执行和二进制分析</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/avast/retdec"><img src="https://user-images.githubusercontent.com/20342097/35865940-2288d66a-0b56-11e8-9a92-d154b7111053.png" width="160" alt="avast/retdec"></a></td><td><a href="https://github.com/avast/retdec"><b>retdec</b></a><br><sub>avast</sub></td><td>把多种架构的机器码反编译成 C</td><td>否</td><td><sub>维护者发布</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/cutter"><img src="https://raw.githubusercontent.com/rizinorg/cutter/dev/docs/source/images/screenshot.png" width="160" alt="rizinorg/cutter"></a></td><td><a href="https://github.com/rizinorg/cutter"><b>cutter</b></a><br><sub>rizinorg</sub></td><td>基于 Rizin 的友好逆向图形界面</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/ghidraninja/ghidra_scripts"><img src="https://raw.githubusercontent.com/ghidraninja/ghidra_scripts/master/images/binwalk.png" width="160" alt="ghidraninja/ghidra_scripts"></a></td><td><a href="https://github.com/ghidraninja/ghidra_scripts"><b>ghidra_scripts</b></a><br><sub>ghidraninja</sub></td><td>实用 Ghidra 脚本合集，从 binwalk 到 YARA</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/radareorg/radare2"><img src="https://raw.githubusercontent.com/radareorg/radare2/master/doc/images/shot.png" width="160" alt="radareorg/radare2"></a></td><td><a href="https://github.com/radareorg/radare2"><b>radare2</b></a><br><sub>radareorg</sub></td><td>可脚本化的命令行逆向框架</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/mandiant/flare-floss"><img src="images/floss-terminal.png" width="160" alt="mandiant/flare-floss"></a></td><td><a href="https://github.com/mandiant/flare-floss"><b>flare-floss</b></a><br><sub>mandiant</sub></td><td>把恶意软件里隐藏、混淆的字符串挖出来</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/WerWolv/ImHex"><img src="images/imhex-gui.png" width="160" alt="WerWolv/ImHex"></a></td><td><a href="https://github.com/WerWolv/ImHex"><b>ImHex</b></a><br><sub>WerWolv</sub></td><td>带模式语言、能帮你解析结构的十六进制编辑器</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/mandiant/capa"><img src="https://raw.githubusercontent.com/mandiant/capa/master/doc/img/capa_web_explorer.png" width="160" alt="mandiant/capa"></a></td><td><a href="https://github.com/mandiant/capa"><b>capa</b></a><br><sub>mandiant</sub></td><td>问一个程序“你能干什么”，得到映射到 ATT&amp;CK 的答案</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/frida/frida"><img src="images/frida-terminal.png" width="160" alt="frida/frida"></a></td><td><a href="https://github.com/frida/frida"><b>frida</b></a><br><sub>frida</sub></td><td>注入任意平台上运行中的程序，实时改写行为</td><td>否</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://github.com/dnSpyEx/dnSpy"><img src="https://raw.githubusercontent.com/dnSpyEx/dnSpy/master/images/debug-animated.gif" width="160" alt="dnSpyEx/dnSpy"></a></td><td><a href="https://github.com/dnSpyEx/dnSpy"><b>dnSpy</b></a><br><sub>dnSpyEx</sub></td><td>无需源码即可调试和修改 .NET 程序集</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/decompme/decomp.me"><img src="https://opengraph.githubassets.com/1/decompme/decomp.me" width="160" alt="decompme/decomp.me"></a></td><td><a href="https://github.com/decompme/decomp.me"><b>decomp.me</b></a><br><sub>decompme</sub></td><td>在浏览器里协作反编译，一起冲击完全匹配</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/mrexodia/ida-pro-mcp"><img src="https://img.youtube.com/vi/iFxNuk3kxhk/0.jpg" width="160" alt="mrexodia/ida-pro-mcp"></a></td><td><a href="https://github.com/mrexodia/ida-pro-mcp"><b>ida-pro-mcp</b></a><br><sub>mrexodia</sub></td><td>让 AI 智能体通过 MCP 操作 IDA Pro</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/jsdec"><img src="https://opengraph.githubassets.com/1/rizinorg/jsdec" width="160" alt="rizinorg/jsdec"></a></td><td><a href="https://github.com/rizinorg/jsdec"><b>jsdec</b></a><br><sub>rizinorg</sub></td><td>为 Rizin 生成可读伪 C，手写汇编也行</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/rizinorg/rizin"><img src="https://rizin.re/images/rizin_preview.png" width="160" alt="rizinorg/rizin"></a></td><td><a href="https://github.com/rizinorg/rizin"><b>rizin</b></a><br><sub>rizinorg</sub></td><td>源自 radare2 的 UNIX 风格逆向框架</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/icsharpcode/ILSpy"><img src="https://opengraph.githubassets.com/1/icsharpcode/ILSpy" width="160" alt="icsharpcode/ILSpy"></a></td><td><a href="https://github.com/icsharpcode/ILSpy"><b>ILSpy</b></a><br><sub>icsharpcode</sub></td><td>把任意 .NET 程序集还原成 C#</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/google/bindiff"><img src="https://zynamics.com/images/bindiff_scr1_s.gif" width="160" alt="google/bindiff"></a></td><td><a href="https://github.com/google/bindiff"><b>bindiff</b></a><br><sub>google</sub></td><td>找出两个版本二进制之间改了什么</td><td>否</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/0xshlomil/ida-free-mcp"><img src="https://opengraph.githubassets.com/1/0xshlomil/ida-free-mcp" width="160" alt="0xshlomil/ida-free-mcp"></a></td><td><a href="https://github.com/0xshlomil/ida-free-mcp"><b>ida-free-mcp</b></a><br><sub>0xshlomil</sub></td><td>通过 MCP 让 AI 智能体使用免费版 IDA</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/HexRaysSA/ida-mcp"><img src="https://opengraph.githubassets.com/1/HexRaysSA/ida-mcp" width="160" alt="HexRaysSA/ida-mcp"></a></td><td><a href="https://github.com/HexRaysSA/ida-mcp"><b>ida-mcp</b></a><br><sub>HexRaysSA</sub></td><td>Hex-Rays 官方的 IDA MCP 服务</td><td>否</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/Nowng/rea-mcp"><img src="https://opengraph.githubassets.com/1/Nowng/rea-mcp" width="160" alt="Nowng/rea-mcp"></a></td><td><a href="https://github.com/Nowng/rea-mcp"><b>rea-mcp</b></a><br><sub>Nowng</sub></td><td>在 LM Studio 里配合本地模型用 REA</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/alexmi256/rea-agent-docker"><img src="https://opengraph.githubassets.com/1/alexmi256/rea-agent-docker" width="160" alt="alexmi256/rea-agent-docker"></a></td><td><a href="https://github.com/alexmi256/rea-agent-docker"><b>rea-agent-docker</b></a><br><sub>alexmi256</sub></td><td>REA 的 Docker 镜像，含 Ghidra/Hopper/IDA 版本</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/cognixws/picode-rea"><img src="https://opengraph.githubassets.com/1/cognixws/picode-rea" width="160" alt="cognixws/picode-rea"></a></td><td><a href="https://github.com/cognixws/picode-rea"><b>picode-rea</b></a><br><sub>cognixws</sub></td><td>在 PiCode 里使用 REA 的静态分析工具</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/czcdr/dsh-plugin-rea"><img src="https://raw.githubusercontent.com/czcdr/dsh-plugin-rea/main/assets/screenshot-1.png" width="160" alt="czcdr/dsh-plugin-rea"></a></td><td><a href="https://github.com/czcdr/dsh-plugin-rea"><b>dsh-plugin-rea</b></a><br><sub>czcdr</sub></td><td>在 DeepSeek Harness 里用 REA，自动装好 Ghidra</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><img src="https://opengraph.githubassets.com/1/sheilacraig/dsh-rea-mcp" width="160" alt="sheilacraig/dsh-rea-mcp"></a></td><td><a href="https://github.com/sheilacraig/dsh-rea-mcp"><b>dsh-rea-mcp</b></a><br><sub>sheilacraig</sub></td><td>只靠配置就把 REA 挂进 DeepSeek Harness</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><img src="https://opengraph.githubassets.com/1/ya123-4/rea-dsh-plugin" width="160" alt="ya123-4/rea-dsh-plugin"></a></td><td><a href="https://github.com/ya123-4/rea-dsh-plugin"><b>rea-dsh-plugin</b></a><br><sub>ya123-4</sub></td><td>在 DeepSeek Harness 中注册 REA 的 MCP 工具</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/zhaofeng130/dsh-rea"><img src="https://opengraph.githubassets.com/1/zhaofeng130/dsh-rea" width="160" alt="zhaofeng130/dsh-rea"></a></td><td><a href="https://github.com/zhaofeng130/dsh-rea"><b>dsh-rea</b></a><br><sub>zhaofeng130</sub></td><td>给 DeepSeek Harness 加上 REA 技能和工具</td><td>✅ 是</td><td><sub>仓库卡片</sub></td></tr>
<tr><td><a href="https://github.com/pablodiazjorge/rea-casebook"><img src="https://raw.githubusercontent.com/pablodiazjorge/rea-casebook/main/media/session-dark.png" width="160" alt="pablodiazjorge/rea-casebook"></a></td><td><a href="https://github.com/pablodiazjorge/rea-casebook"><b>rea-casebook</b></a><br><sub>pablodiazjorge</sub></td><td>让 Claude Code 的每条结论都引用真实 REA 证据</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/jinshi666888/rea-playbook"><img src="https://raw.githubusercontent.com/jinshi666888/rea-playbook/main/docs/assets/demo.gif" width="160" alt="jinshi666888/rea-playbook"></a></td><td><a href="https://github.com/jinshi666888/rea-playbook"><b>rea-playbook</b></a><br><sub>jinshi666888</sub></td><td>带迷你 Electron 靶子的 REA 动手实验</td><td>✅ 是</td><td><sub>项目 README</sub></td></tr>
<tr><td><a href="https://github.com/dav1dngy/era-agent"><img src="https://raw.githubusercontent.com/dav1dngy/era-agent/main/docs/assets/screenshots/01-main-workspace.png" width="160" alt="dav1dngy/era-agent"></a></td><td><a href="https://github.com/dav1dngy/era-agent"><b>era-agent</b></a><br><sub>dav1dngy</sub></td><td>以证据驱动、会尝试自我改进的逆向智能体</td><td>❔ 待验证</td><td><sub>项目 README</sub></td></tr>
</table>

## REA 官方 Showcase

<table>
<tr><th width="170">图片</th><th>项目</th><th>简介</th><th>使用 rea</th><th>图片来源</th></tr>
<tr><td><a href="https://rea.tools/showcase/dx-ball/"><img src="images/showcase-dx-ball.png" width="160" alt="DX-Ball: sound-pan function"></a></td><td><a href="https://rea.tools/showcase/dx-ball/"><b>DX-Ball: sound-pan function</b></a></td><td>看 REA 把 DX-Ball 的一个音效函数还原成逐字节一致的 C</td><td>✅ 是</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/notion/"><img src="images/showcase-notion.png" width="160" alt="Notion: Electron clipboard bridge"></a></td><td><a href="https://rea.tools/showcase/notion/"><b>Notion: Electron clipboard bridge</b></a></td><td>跟着一次 Notion 复制操作，从页面一路追到 IPC 和主进程</td><td>✅ 是</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/th04/"><img src="images/showcase-th04.png" width="160" alt="TH04: PC-98 bullet-ring maths"></a></td><td><a href="https://rea.tools/showcase/th04/"><b>TH04: PC-98 bullet-ring maths</b></a></td><td>从 16 位 DOS 代码里找回东方幻想乡的弹幕角度算法</td><td>✅ 是</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/aegis/"><img src="images/showcase-aegis.png" width="160" alt="Aegis: TOTP code generation"></a></td><td><a href="https://rea.tools/showcase/aegis/"><b>Aegis: TOTP code generation</b></a></td><td>看清 Aegis 安卓应用是怎样生成两步验证码的</td><td>✅ 是</td><td><sub>本仓库截图</sub></td></tr>
<tr><td><a href="https://rea.tools/showcase/ctf/"><img src="images/showcase-ctf.png" width="160" alt="CTF: flag checker"></a></td><td><a href="https://rea.tools/showcase/ctf/"><b>CTF: flag checker</b></a></td><td>一步步解开 DownUnderCTF 2023 的逆向题</td><td>✅ 是</td><td><sub>本仓库截图</sub></td></tr>
</table>

---

另见 / 致谢：许多 REA 社区条目参考并核对了 [AIshihzong/awesome-reverse-engineer-anything](https://github.com/AIshihzong/awesome-reverse-engineer-anything)。

贡献指南见 [CONTRIBUTING.md](CONTRIBUTING.md)。许可：[CC0-1.0](LICENSE)。
