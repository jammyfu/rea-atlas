[English](SKILL_MAP.md) · [简体中文](SKILL_MAP.zh-CN.md)

# 十类 Skill 技术与项目地图

核验日期：2026-11-07。

本索引区分 skill 原项目、同技术方向的工具以及验证练习。相关项目由技术用途关联，不意味着 skill 实际依赖、维护者背书或使用了 REA。

核验范围：官方仓库元数据、README 和列出的文档；未安装或执行任何项目，未独立复现性能、兼容性或安全声明。公开可访问不等于已获开源许可，许可证和附加条款以各上游为准。

仅用于自有或明确授权的程序、协议与实验环境。遵守软件许可、隐私和当地法律；不收录破解、DRM 绕过或版权资产分发。第三方网站、账号和数据另需授权。

维护源：[skill-map.json](skill-map.json)，执行 `python render.py` 同步生成本文件及五语 README。

- [REA](#rea)
- [reverse-skill](#reverse-skill)
- [android-reverse-engineering-skill](#android-reverse-engineering-skill)
- [replica-skill](#replica-skill)
- [leanrea](#leanrea)
- [ctf-skills](#ctf-skills)
- [reverse-skills](#reverse-skills)
- [hello_js_reverse_skill](#hello-js-reverse-skill)
- [Open-ReverseLab](#open-reverselab)
- [js-reverse-automation--skill](#js-reverse-automation-skill)

<a id="rea"></a>

## REA

[morluto/rea](https://github.com/morluto/rea) · [README](https://github.com/morluto/rea/blob/main/README.md)

把 Agent 接到原生二进制、Android、JS/Electron、.NET、网站、固件和运行时观察工具，返回反编译、引用、结构与证据局限。CLI 与 MCP 共用工作流。

**补充依据:** [1](https://github.com/morluto/rea/blob/main/docs/reverse-engineering-tools.md) · [2](https://github.com/morluto/rea/blob/main/THIRD_PARTY_NOTICES.md) · [3](https://github.com/morluto/rea/blob/main/docs/javascript-application-workflows.md) · [4](https://github.com/morluto/rea/blob/main/docs/browser-observation.md)

**技术:** CLI / MCP, decompilation, cross-references, evidence

**许可:** [MIT](https://github.com/morluto/rea/blob/main/README.md)

**局限与注意事项:** 不是从任意程序恢复完整原始源码。深度原生分析需要 Hopper/Ghidra/IDA/Kuna，Android 需要 JADX/JDK，能力与平台及发行版本有关。分析在本地，但结果仍会进入所用 Agent/模型供应商的数据流程。 MIT 仅覆盖 REA 自有代码；第三方独立许可证，IDA/Hopper/JEB 等商业引擎另需合法许可证。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 反汇编、反编译、图形与脚本分析，支持 GUI 和自动化。 | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | DEX/APK 到 Java 的 GUI/CLI 反编译，含交叉引用、资源和 smali 调试。 | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [electron/asar](https://github.com/electron/asar) | 列出、单文件提取、整包解出ASAR；作为Electron静态分析入口。 | [README / docs](https://github.com/electron/asar/blob/main/README.md) |
| [frida/frida](https://github.com/frida/frida) | 跨平台动态插桩工具，适合在授权应用运行时观察和验证行为。 | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Ghidra 插件和 MCP 服务，暴露反编译、符号/数据重命名、导入导出信息，含 PyGhidra headless 模式。 | [README / docs](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md) |
| [cyberkaida/reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | Ghidra MCP 扩展，支持交互和 headless、类型/名称编辑、脚本及项目分析。 | [README / docs](https://github.com/cyberkaida/reverse-engineering-assistant/blob/main/README.md) |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | 面向网站、桌面应用与游戏的 Rust 逆向分析和 AI 重建工作台，含原生二进制分析、反汇编/伪 C、调用图、文件格式解析、证据管理与 CLI/MCP，可接 Ghidra 和编码代理。 | [README / docs](https://github.com/storytold/craft-anything/blob/main/README.md) |

<a id="reverse-skill"></a>

## reverse-skill

[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) · [README](https://github.com/zhaoxuya520/reverse-skill/blob/main/README.md)

按 APK、原生二进制、JS、CTF、固件等输入选择技能与工具，包含环境探测、授权范围门禁、案例目录、证据链和报告流程。

**补充依据:** [1](https://github.com/zhaoxuya520/reverse-skill/blob/main/SECURITY.md) · [2](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/UV-AND-DOWNLOAD-SECURITY.md) · [3](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/SECURITY-REVIEW-2026-09-03.md)

**技术:** target routing, tool discovery, evidence workflows

**许可:** [MIT (root); GPLv3 submodule and separately licensed dependencies](https://github.com/zhaoxuya520/reverse-skill/blob/main/README.md)

**局限与注意事项:** 路由包不是逆向引擎。外部工具、MCP 与脚本仍需安装配置，自动安装和联网操作应先核查来源、范围和版本。README 不同小节的模块/规则计数存在不一致，不建议写死数量。 主项目 MIT；CTF-Sandbox-Orchestrator/ 为 GPLv3；被调用的 Pentest Swarm AI 为 AGPL-3.0；其余工具各自许可。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 反汇编、反编译、图形与脚本分析，支持 GUI 和自动化。 | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | 命令行原生二进制分析框架，适合可脚本化探测与批量处理。 | [README / docs](https://github.com/radareorg/radare2/blob/master/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | DEX/APK 到 Java 的 GUI/CLI 反编译，含交叉引用、资源和 smali 调试。 | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 解码 Android 资源与 smali，支持修改后的 APK 重建。 | [README / docs](https://github.com/iBotPeaches/Apktool/blob/main/README.md) |
| [frida/frida](https://github.com/frida/frida) | 跨平台动态插桩工具，适合在授权应用运行时观察和验证行为。 | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [angr/angr](https://github.com/angr/angr) | 程序分析平台，适合自动探索原生二进制执行路径和约束分析。 | [README / docs](https://github.com/angr/angr/blob/master/README.md) |

<a id="android-reverse-engineering-skill"></a>

## android-reverse-engineering-skill

[SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) · [README](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md)

先识别 APK/XAPK 框架，再用 JADX 和可选 Java 反编译器分析 APK/XAPK/JAR/AAR；梳理 Manifest、网络调用与调用链，尝试利用 Kotlin 元数据恢复混淆类名。

**补充依据:** [1](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/THIRD_PARTY_NOTICES.md) · [2](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/PRIVACY.md)

**技术:** APK / DEX, Kotlin metadata, HTTP API analysis

**许可:** [Apache-2.0](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md)

**局限与注意事项:** 需 JDK 17+、JADX；可选 Vineflower/Fernflower/dex2jar。Windows PowerShell 支持仍标注 experimental。Kotlin 名称恢复依赖目标实际保留的元数据，不能把 README 的高恢复率宣传写成保证；加固、JNI/SO 与运行时验证要另用工具。 Apache-2.0；第三方反编译器及运行时工具不随插件捆绑，按各自许可证。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [skylot/jadx](https://github.com/skylot/jadx) | DEX/APK 到 Java 的 GUI/CLI 反编译，含交叉引用、资源和 smali 调试。 | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 解码 Android 资源与 smali，支持修改后的 APK 重建。 | [README / docs](https://github.com/iBotPeaches/Apktool/blob/main/README.md) |
| [androguard/androguard](https://github.com/androguard/androguard) | Android APK/DEX、引用和程序结构分析，仓库 v5 还含 Agent/MCP 接口和可选 ARM64 分析。 | [README / docs](https://github.com/androguard/androguard/blob/master/README.md) |
| [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | JADX GUI 插件，将当前反编译上下文接入 Agent。 | [README / docs](https://github.com/zinja-coder/jadx-ai-mcp/blob/jadx-ai/README.md) |
| [zinja-coder/jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server) | Python MCP 服务器，通过 JADX-AI-MCP 插件访问 Android 反编译上下文。 | [README / docs](https://github.com/zinja-coder/jadx-mcp-server/blob/main/README.md) |
| [sensepost/objection](https://github.com/sensepost/objection) | 基于 Frida 的 Android/iOS 运行时探索和移动安全评估。 | [README / docs](https://github.com/sensepost/objection/blob/master/README.md) |
| [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | 自动化移动应用静态/动态安全评估框架，覆盖 Android/iOS/Windows。 | [README / docs](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md) |

<a id="replica-skill"></a>

## replica-skill

[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) · [README](https://github.com/Jakeschincariol/replica-skill/blob/main/README.md)

公开页面、截图、商店介绍及获准使用的自有账号研究；生成页面/流程/数据模型；架构、设计、测试、差异评分、用户评价分析、重新品牌化及部署检查。六个 Python 工具自身不联网。

**补充依据:** [1](https://github.com/Jakeschincariol/replica-skill/blob/main/replica-recon/SKILL.md)

**技术:** black-box observation, clean-room specs, behavior tests

**许可:** [MIT](https://github.com/Jakeschincariol/replica-skill/blob/main/README.md)

**局限与注意事项:** “clone any app”指功能和流程，不含原代码、品牌、素材、内容库、私有 API 或商业网络；界面不能证明后台架构。自动评分不是等价性证明，复杂产品仍需工程实现与人工验证。 MIT；不授予目标产品的代码、品牌、素材或数据权利。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 以无障碍树驱动页面探索、交互、快照和测试；可使用隔离会话或持久profile。 | [README / docs](https://github.com/microsoft/playwright-mcp/blob/main/README.md) |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 浏览器会话、点击、快照、截图、选择器检查和代码生成；适合已有shell能力的coding agent。 | [README / docs](https://github.com/microsoft/playwright-cli/blob/main/README.md) |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 网络、控制台、source-mapped堆栈、截图和性能trace；Puppeteer驱动交互。 | [README / docs](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) |
| [webrecorder/browsertrix-crawler](https://github.com/webrecorder/browsertrix-crawler) | 用真实浏览器捕获动态站点，以Docker运行，适合公开页面证据留存/可复查归档。 | [README / docs](https://github.com/webrecorder/browsertrix-crawler/blob/main/README.md) |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | 面向网站、桌面应用与游戏的 Rust 逆向分析和 AI 重建工作台，含原生二进制分析、反汇编/伪 C、调用图、文件格式解析、证据管理与 CLI/MCP，可接 Ghidra 和编码代理。 | [README / docs](https://github.com/storytold/craft-anything/blob/main/README.md) |

<a id="leanrea"></a>

## leanrea

[aicodeking/leanrea](https://github.com/aicodeking/leanrea) · [README](https://github.com/aicodeking/leanrea/blob/main/README.md)

用小型 SKILL.md 指导 Agent 直接运行本机 CLI，按文件类型路由 Electron、原生、Go/Rust、Android、WASM、抓包和固件分析，并区分观察、推断和未知。

**补充依据:** [1](https://github.com/aicodeking/leanrea/blob/main/bench/BENCHMARK.md)

**技术:** CLI orchestration, target triage, evidence

**许可:** [MIT](https://github.com/aicodeking/leanrea/blob/main/README.md)

**局限与注意事项:** 不提供独立分析引擎或 MCP 服务；依赖 Agent 的 shell 能力与现有工具。性能数字是作者在 REA 6.5.0、单模型、单台 macOS、4 任务×3 次下的基准，不可推广成普遍速度或准确率结论。 MIT。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 反汇编、反编译、图形与脚本分析，支持 GUI 和自动化。 | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | 命令行原生二进制分析框架，适合可脚本化探测与批量处理。 | [README / docs](https://github.com/radareorg/radare2/blob/master/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | DEX/APK 到 Java 的 GUI/CLI 反编译，含交叉引用、资源和 smali 调试。 | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [electron/asar](https://github.com/electron/asar) | 列出、单文件提取、整包解出ASAR；作为Electron静态分析入口。 | [README / docs](https://github.com/electron/asar/blob/main/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | wasm2wat、wasm-objdump、wasm-validate、wasm2c等，适合检查JS调用的WASM模块。 | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 浏览器会话、点击、快照、截图、选择器检查和代码生成；适合已有shell能力的coding agent。 | [README / docs](https://github.com/microsoft/playwright-cli/blob/main/README.md) |

<a id="ctf-skills"></a>

## ctf-skills

[ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills) · [README](https://github.com/ljagiello/ctf-skills/blob/main/README.md)

按 reverse、pwn、crypto、web、forensics 等题型组织技能，并提供 solve-challenge 调度与 writeup 流程。逆向部分覆盖原生、VM、WASM、Android/JNI、模拟执行和工具集成。

**补充依据:** [1](https://github.com/ljagiello/ctf-skills/blob/main/ctf-reverse/SKILL.md)

**技术:** CTF reversing, symbolic execution, emulation

**许可:** [MIT](https://github.com/ljagiello/ctf-skills/blob/main/README.md)

**局限与注意事项:** 技能不等同于已安装工具；有按需和批量安装脚本，批量环境依赖较多。类似题搜索依赖 Tavily API；应避免未经许可上传私有样本或题目内容。 MIT；安装工具与引用资料仍各自许可。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [angr/angr](https://github.com/angr/angr) | 程序分析平台，适合自动探索原生二进制执行路径和约束分析。 | [README / docs](https://github.com/angr/angr/blob/master/README.md) |
| [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | 多架构 CPU 模拟框架，适合函数/代码片段模拟与细粒度插桩。 | [README / docs](https://github.com/unicorn-engine/unicorn/blob/master/README.md) |
| [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) | Python CTF 框架和二进制实验原型工具集。 | [README / docs](https://github.com/Gallopsled/pwntools/blob/dev/README.md) |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | 增强 GDB/LLDB 的调试和低级程序分析体验。 | [README / docs](https://github.com/pwndbg/pwndbg/blob/dev/README.md) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | 命令行原生二进制分析框架，适合可脚本化探测与批量处理。 | [README / docs](https://github.com/radareorg/radare2/blob/master/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | wasm2wat、wasm-objdump、wasm-validate、wasm2c等，适合检查JS调用的WASM模块。 | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |

<a id="reverse-skills"></a>

## reverse-skills

[P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) · [README](https://github.com/P4nda0s/reverse-skills/blob/main/README.md)

围绕 IDA 导出的反编译结果分析函数符号和重建数据结构，另提供 Frida、Unicorn、DEX、IL2CPP、IDAPython 与 iOS 分析技能。README 明确为 IDA-NO-MCP 配套设计。

**补充依据:** [1](https://api.github.com/repos/P4nda0s/reverse-skills/contents)

**技术:** decompiler exports, type reconstruction, instrumentation

**许可:** [MIT claimed in README; no independent LICENSE found](https://github.com/P4nda0s/reverse-skills/blob/main/README.md)

**局限与注意事项:** 不是独立反编译器；IDA、Frida、Unicorn 等依赖及设备权限另行满足。DEX/iOS dump、进程插桩会触及实际目标，需授权和隔离测试设备。 README 声明 MIT，但根目录只有 .gitignore、README.md、README_EN.md、skills，没有独立 LICENSE，GitHub API license=null。应标记“MIT（README 声明；无独立许可证文件）”，不能当作已完成许可证审计。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [P4nda0s/IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | 将 IDA 反编译与调用关系导出为适合代码 Agent 读取的文件；有 Python 插件和 Rust CLI。 | [README / docs](https://github.com/P4nda0s/IDA-NO-MCP/blob/main/README.md) |
| [HexRaysSA/ida-mcp](https://github.com/HexRaysSA/ida-mcp) | Hex-Rays 官方 IDA MCP，基于 IDA Nexus 支持 GUI 和 headless、多客户端会话。 | [README / docs](https://github.com/HexRaysSA/ida-mcp/blob/main/README.md) |
| [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | 把 IDA Pro 反编译与分析操作提供给 Agent。 | [README / docs](https://github.com/mrexodia/ida-pro-mcp/blob/main/README.md) |
| [frida/frida](https://github.com/frida/frida) | 跨平台动态插桩工具，适合在授权应用运行时观察和验证行为。 | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [dnakov/frida-mcp](https://github.com/dnakov/frida-mcp) | 通过 MCP 提供 Frida 设备/进程管理、JavaScript 会话、脚本加载与运行时观察。 | [README / docs](https://github.com/dnakov/frida-mcp/blob/main/README.md) |
| [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | 多架构 CPU 模拟框架，适合函数/代码片段模拟与细粒度插桩。 | [README / docs](https://github.com/unicorn-engine/unicorn/blob/master/README.md) |

<a id="hello-js-reverse-skill"></a>

## hello_js_reverse_skill

[WhiteNightShadow/hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) · [README](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/README.md)

签名来源隔离、状态/新鲜度对照、混淆和JSVMP调查策略、WASM加载、Set-Cookie与JS写入归因、Node/Python实现模板、版本回归。以 camoufox-reverse-mcp 提供实际浏览器能力。

**补充依据:** [1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/references/browser-evidence-contract.md) · [2](https://api.github.com/repos/WhiteNightShadow/hello_js_reverse_skill/git/trees/main?recursive=1) · [3](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/scripts/real_cases/LICENSE)

**技术:** JavaScript AST, deobfuscation, runtime analysis

**许可:** [Project-wide license unclear; CC0 limited to scripts/real_cases](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/README.md)

**局限与注意事项:** 方法和模板不保证还原任意算法或VM；Hook可能改变目标行为。GitHub license=null，树中仅 scripts/real_cases/LICENSE，未发现覆盖主项目的根许可证，不能默认自由复制或商业复用。 主项目许可未明确；scripts/real_cases/LICENSE 为 CC0-1.0，仅覆盖该目录原创材料，不含上游源码/依赖/生成bundle。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [WhiteNightShadow/camoufox-reverse-mcp](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) | 支撑hello_js_reverse_skill的浏览器层；主世界/Frame Hook、脚本搜索、网络证据、离线验签，可选定制Gecko属性追踪。 | [README / docs](https://github.com/WhiteNightShadow/camoufox-reverse-mcp/blob/main/README.md) |
| [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack) | 识别并还原支持的obfuscator.io模式、去压缩、转写以及Webpack/Browserify拆包。 | [README / docs](https://github.com/j4k0xb/webcrack/blob/master/README.md) |
| [pionxzh/wakaru](https://github.com/pionxzh/wakaru) | AST重写、转译helper恢复和支持的bundle拆分；可结合source map恢复原文件/名称。 | [README / docs](https://github.com/pionxzh/wakaru/blob/main/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | wasm2wat、wasm-objdump、wasm-validate、wasm2c等，适合检查JS调用的WASM模块。 | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |
| [RyanDFIR/hindsight](https://github.com/RyanDFIR/hindsight) | 离线浏览器历史、缓存、书签、Cookie、LocalStorage等时间线；支持部分Firefox profile数据库。 | [README / docs](https://github.com/RyanDFIR/hindsight/blob/main/README.md) |

<a id="open-reverselab"></a>

## Open-ReverseLab

[LING71671/open-reverselab](https://github.com/LING71671/open-reverselab) · [README](https://github.com/LING71671/open-reverselab/blob/main/README.md)

将 Ghidra、Frida、x64dbg、Rizin 等工具包装为 MCP，按 Android、PE、CTF 和通用分析组织可执行知识库与 samples/exports/reports 工作区。

**补充依据:** [1](https://github.com/LING71671/open-reverselab/blob/main/DISCLAIMER.md) · [2](https://github.com/LING71671/open-reverselab/blob/main/LICENSE)

**技术:** MCP workbench, native / Android, case reports

**许可:** [GPL-3.0-only (README); additional disclaimer needs review](https://github.com/LING71671/open-reverselab/blob/main/README.md)

**局限与注意事项:** 部署比单个 skill 更重；Windows GUI/PE 工具不等同跨平台可用。README 提到主机级环境缓存，应检查收集范围。不要照抄其防病毒排除建议；应在隔离环境评估安全工具及样本。知识库篇数在仓库描述与 README 不完全一致，不建议写死。 README 明确 GPL-3.0-only，另有声明对所有使用者及衍生品有约束力的 DISCLAIMER；其与开源许可的关系需另行审阅，不宜只标无条件 GPL。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 反汇编、反编译、图形与脚本分析，支持 GUI 和自动化。 | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [frida/frida](https://github.com/frida/frida) | 跨平台动态插桩工具，适合在授权应用运行时观察和验证行为。 | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [rizinorg/rizin](https://github.com/rizinorg/rizin) | 二进制分析、反汇编、调试、十六进制与格式处理，支持 rzpipe 脚本。 | [README / docs](https://github.com/rizinorg/rizin/blob/dev/README.md) |
| [rizinorg/cutter](https://github.com/rizinorg/cutter) | Rizin 的图形化逆向平台，支持插件及 Ghidra 反编译集成。 | [README / docs](https://github.com/rizinorg/cutter/blob/dev/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | DEX/APK 到 Java 的 GUI/CLI 反编译，含交叉引用、资源和 smali 调试。 | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | 解码 Android 资源与 smali，支持修改后的 APK 重建。 | [README / docs](https://github.com/iBotPeaches/Apktool/blob/main/README.md) |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | 面向网站、桌面应用与游戏的 Rust 逆向分析和 AI 重建工作台，含原生二进制分析、反汇编/伪 C、调用图、文件格式解析、证据管理与 CLI/MCP，可接 Ghidra 和编码代理。 | [README / docs](https://github.com/storytold/craft-anything/blob/main/README.md) |

<a id="js-reverse-automation-skill"></a>

## js-reverse-automation--skill

[Fausto-404/js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) · [README](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/README.md)

运行时加密/签名入口候选发现、Webpack模块观测、差分验证、动作级请求与业务响应证据、生成JSRPC注入/Flask代理/Burp autoDecoder配置。

**补充依据:** [1](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/js-reverse-automation/references/capability-boundaries.md)

**技术:** CDP, AST, browser runtime, WASM

**许可:** [Apache-2.0](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/README.md)

**局限与注意事项:** 能力边界明确不支持通用VMP静态还原、未导出的WASM内部函数、Service Worker内部闭包、跨域iframe、CSP WebSocket绕过等；README宽泛JSVMP宣传不能当完整支持。需要受控测试账号和隔离环境。 Apache-2.0；JSRPC、autoDecoder、Burp及浏览器组件分别适用其许可。

| 相关项目 | 用途 | 核验来源 |
| --- | --- | --- |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 网络、控制台、source-mapped堆栈、截图和性能trace；Puppeteer驱动交互。 | [README / docs](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) |
| [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack) | 识别并还原支持的obfuscator.io模式、去压缩、转写以及Webpack/Browserify拆包。 | [README / docs](https://github.com/j4k0xb/webcrack/blob/master/README.md) |
| [pionxzh/wakaru](https://github.com/pionxzh/wakaru) | AST重写、转译helper恢复和支持的bundle拆分；可结合source map恢复原文件/名称。 | [README / docs](https://github.com/pionxzh/wakaru/blob/main/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | wasm2wat、wasm-objdump、wasm-validate、wasm2c等，适合检查JS调用的WASM模块。 | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |
| [electron/asar](https://github.com/electron/asar) | 列出、单文件提取、整包解出ASAR；作为Electron静态分析入口。 | [README / docs](https://github.com/electron/asar/blob/main/README.md) |
| [doyensec/electronegativity](https://github.com/doyensec/electronegativity) | AST/DOM扫描Electron安全设置，支持JS/HTML/ASAR和CSV/SARIF结果。 | [README / docs](https://github.com/doyensec/electronegativity/blob/master/README.md) |
| [doyensec/ElectroNG](https://github.com/doyensec/ElectroNG) | Electron桌面扫描应用，核心逻辑位于ElectroNG-core。 | [README / docs](https://github.com/doyensec/ElectroNG/blob/main/README.md) |

## 来源与维护

以下记录为技术索引内项目的检查依据；日期是本次资料检查日期，不是项目发布日期。所有用途简介为编辑性概述，不构成安装或安全背书。

- [aicodeking/leanrea](https://github.com/aicodeking/leanrea/blob/main/README.md) (2026-11-07): 不提供独立分析引擎或 MCP 服务；依赖 Agent 的 shell 能力与现有工具。性能数字是作者在 REA 6.5.0、单模型、单台 macOS、4 任务×3 次下的基准，不可推广成普遍速度或准确率结论。 MIT。
  [补充依据 1](https://github.com/aicodeking/leanrea/blob/main/bench/BENCHMARK.md)
- [androguard/androguard](https://github.com/androguard/androguard/blob/master/README.md) (2026-11-07): 当前主分支 v5 与 PyPI v4.1.4 不一致；不能默认 pip 安装得到 README 全部新能力。
- [angr/angr](https://github.com/angr/angr/blob/master/README.md) (2026-11-07): 复杂程序需建模环境，不能保证全路径覆盖或自动求解。
- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) (2026-11-07): 客户端能读取并修改浏览器数据，应使用隔离profile；正式支持Chrome/Chrome for Testing。默认使用统计开启，性能功能可能发送trace URL到CrUX。 Apache-2.0
- [cyberkaida/reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant/blob/main/README.md) (2026-11-07): PyGhidra 脚本接口有执行权限，官方建议公开监听时启用 API key 或禁用脚本工具；匹配 Ghidra 与 Java 版本。
- [dnakov/frida-mcp](https://github.com/dnakov/frida-mcp/blob/main/README.md) (2026-11-07): 社区桥接，不是 Frida 官方项目；最近 push 为 2025-05-12，README 存在 yourusername 占位，使用前应检查维护与 Frida 版本兼容。
- [doyensec/electronegativity](https://github.com/doyensec/electronegativity/blob/master/README.md) (2026-11-07): 官方已归档并指向ElectroNG；只作为历史/补充条目，不推荐为当前主工具。结果需人工确认。 Apache-2.0
- [doyensec/ElectroNG](https://github.com/doyensec/ElectroNG/blob/main/README.md) (2026-11-07): README警告2024年后仅小修，针对现代Electron可能不完整/效果下降；不能因为未归档就标为活跃成熟推荐。 Apache-2.0
- [electron/asar](https://github.com/electron/asar/blob/main/README.md) (2026-11-07): 解包器而非反编译器；ASAR并不等同加密，提取不自动授予源代码复用权。 MIT
- [Fausto-404/js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/README.md) (2026-11-07): 能力边界明确不支持通用VMP静态还原、未导出的WASM内部函数、Service Worker内部闭包、跨域iframe、CSP WebSocket绕过等；README宽泛JSVMP宣传不能当完整支持。需要受控测试账号和隔离环境。 Apache-2.0；JSRPC、autoDecoder、Burp及浏览器组件分别适用其许可。
  [补充依据 1](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/js-reverse-automation/references/capability-boundaries.md)
- [frida/frida](https://github.com/frida/frida/blob/main/README.md) (2026-11-07): 根 COPYING 为 wxWindows Library Licence 3.1，并非简单 MIT；不同组件单独核验。插桩具有代码执行与进程控制权限。
  [补充依据 1](https://github.com/frida/frida/blob/main/COPYING)
- [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools/blob/dev/README.md) (2026-11-07): 主要 MIT，少量 GPL/BSD-2-Clause，特别检查 pwnlib/constants 与 pwnlib/data。
  [补充依据 1](https://github.com/Gallopsled/pwntools/blob/dev/LICENSE-pwntools.txt)
- [HexRaysSA/ida-mcp](https://github.com/HexRaysSA/ida-mcp/blob/main/README.md) (2026-11-07): 需 IDA 9.4+、idalib、Python 3.11+；MIT 只覆盖桥接代码，不授予 IDA 商业许可。
- [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool/blob/main/README.md) (2026-11-07): 资源/字节码工作流，不等同恢复原始 Java/Kotlin 源码；修改重签影响签名与行为。
- [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack/blob/master/README.md) (2026-11-07): 不是任意JSVMP解密器，也无法恢复编译中丢失的信息；依赖isolated-vm与兼容Node版本，处理不可信输入应隔离。 MIT
- [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill/blob/main/README.md) (2026-11-07): “clone any app”指功能和流程，不含原代码、品牌、素材、内容库、私有 API 或商业网络；界面不能证明后台架构。自动评分不是等价性证明，复杂产品仍需工程实现与人工验证。 MIT；不授予目标产品的代码、品牌、素材或数据权利。
  [补充依据 1](https://github.com/Jakeschincariol/replica-skill/blob/main/replica-recon/SKILL.md)
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md) (2026-11-07): 匹配 Ghidra/扩展版本；重命名和脚本调用会改变分析数据库，服务不要无保护公开。
- [LING71671/open-reverselab](https://github.com/LING71671/open-reverselab/blob/main/README.md) (2026-11-07): 部署比单个 skill 更重；Windows GUI/PE 工具不等同跨平台可用。README 提到主机级环境缓存，应检查收集范围。不要照抄其防病毒排除建议；应在隔离环境评估安全工具及样本。知识库篇数在仓库描述与 README 不完全一致，不建议写死。 README 明确 GPL-3.0-only，另有声明对所有使用者及衍生品有约束力的 DISCLAIMER；其与开源许可的关系需另行审阅，不宜只标无条件 GPL。
  [补充依据 1](https://github.com/LING71671/open-reverselab/blob/main/DISCLAIMER.md) · [补充依据 2](https://github.com/LING71671/open-reverselab/blob/main/LICENSE)
- [ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills/blob/main/README.md) (2026-11-07): 技能不等同于已安装工具；有按需和批量安装脚本，批量环境依赖较多。类似题搜索依赖 Tavily API；应避免未经许可上传私有样本或题目内容。 MIT；安装工具与引用资料仍各自许可。
  [补充依据 1](https://github.com/ljagiello/ctf-skills/blob/main/ctf-reverse/SKILL.md)
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/blob/main/README.md) (2026-11-07): 与MCP是交互方式取舍，不代表任务更安全或天然更准确；默认内存profile，需按任务管理会话/证据留存。 Apache-2.0
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp/blob/main/README.md) (2026-11-07): 通用浏览器执行层，不是反混淆器；受浏览器会话/页面权限约束。origin allow/block配置明确不构成安全边界。 Apache-2.0
- [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md) (2026-11-07): 更偏安全评估工作台；动态环境和平台支持需另配，不是通用源码重建工具。
- [morluto/rea](https://github.com/morluto/rea/blob/main/README.md) (2026-11-07): 不是从任意程序恢复完整原始源码。深度原生分析需要 Hopper/Ghidra/IDA/Kuna，Android 需要 JADX/JDK，能力与平台及发行版本有关。分析在本地，但结果仍会进入所用 Agent/模型供应商的数据流程。 MIT 仅覆盖 REA 自有代码；第三方独立许可证，IDA/Hopper/JEB 等商业引擎另需合法许可证。
  [补充依据 1](https://github.com/morluto/rea/blob/main/docs/reverse-engineering-tools.md) · [补充依据 2](https://github.com/morluto/rea/blob/main/THIRD_PARTY_NOTICES.md) · [补充依据 3](https://github.com/morluto/rea/blob/main/docs/javascript-application-workflows.md) · [补充依据 4](https://github.com/morluto/rea/blob/main/docs/browser-observation.md)
- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp/blob/main/README.md) (2026-11-07): 当前 README 首段推荐改用 Hex-Rays 官方 ida-mcp；IDA Free 不支持，IDA Pro/idalib 许可另需满足。
- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) (2026-11-07): 插件与 JDK 版本需匹配；注意官方安全公告；反编译结果不是原始源码。
- [P4nda0s/IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP/blob/main/README.md) (2026-11-07): 根目录无 LICENSE，GitHub license=null；不得默认是明确开源许可。Rust 版依赖合法 IDA Pro 9.x/idalib，版本和平台需匹配。建议放相关但许可未核实区。
  [补充依据 1](https://api.github.com/repos/P4nda0s/IDA-NO-MCP/contents)
- [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills/blob/main/README.md) (2026-11-07): 不是独立反编译器；IDA、Frida、Unicorn 等依赖及设备权限另行满足。DEX/iOS dump、进程插桩会触及实际目标，需授权和隔离测试设备。 README 声明 MIT，但根目录只有 .gitignore、README.md、README_EN.md、skills，没有独立 LICENSE，GitHub API license=null。应标记“MIT（README 声明；无独立许可证文件）”，不能当作已完成许可证审计。
  [补充依据 1](https://api.github.com/repos/P4nda0s/reverse-skills/contents)
- [pionxzh/wakaru](https://github.com/pionxzh/wakaru/blob/main/README.md) (2026-11-07): 不是混淆破解器；重型控制流/VM需专项方法，未保留的原始变量名不能凭空恢复。包版本inventory仍在开发，不是已发布能力。 Apache-2.0
  [补充依据 1](https://github.com/pionxzh/wakaru/blob/main/skills/wakaru/SKILL.md)
- [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg/blob/dev/README.md) (2026-11-07): LLDB 支持仍标注 early-stage；需按文档匹配 Python/调试器版本。
- [radareorg/radare2](https://github.com/radareorg/radare2/blob/master/README.md) (2026-11-07): 主要 LGPLv3，部分组件 GPL/其他许可，分发时按构建核验。
  [补充依据 1](https://github.com/radareorg/radare2/blob/master/COPYING.md)
- [rizinorg/cutter](https://github.com/rizinorg/cutter/blob/dev/README.md) (2026-11-07): 依赖 Rizin 和插件兼容性；不是 radare2 当前官方 GUI。
- [rizinorg/rizin](https://github.com/rizinorg/rizin/blob/dev/README.md) (2026-11-07): 从 radare2 分支发展，命令/API 不应默认与 radare2 完全兼容。
- [RyanDFIR/hindsight](https://github.com/RyanDFIR/hindsight/blob/main/README.md) (2026-11-07): 属于本地profile取证，不是live JS追踪；必须仅处理获授权的profile，报告可能含凭据和私人数据，解析支持取决于浏览器版本。 Apache-2.0
- [sensepost/objection](https://github.com/sensepost/objection/blob/master/README.md) (2026-11-07): 设备/应用加载方式与平台支持需核验；运行时操作可能改变目标状态。
- [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md) (2026-11-07): 需 JDK 17+、JADX；可选 Vineflower/Fernflower/dex2jar。Windows PowerShell 支持仍标注 experimental。Kotlin 名称恢复依赖目标实际保留的元数据，不能把 README 的高恢复率宣传写成保证；加固、JNI/SO 与运行时验证要另用工具。 Apache-2.0；第三方反编译器及运行时工具不随插件捆绑，按各自许可证。
  [补充依据 1](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/THIRD_PARTY_NOTICES.md) · [补充依据 2](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/PRIVACY.md)
- [skylot/jadx](https://github.com/skylot/jadx/blob/master/README.md) (2026-11-07): 官方明确不能保证 100% 反编译成功；复杂/混淆代码需字节码核对。
- [storytold/craft-anything](https://github.com/storytold/craft-anything/blob/main/README.md) (2026-11-07): README 与 Cargo.toml 标明 MIT OR Apache-2.0。项目处于早期 Alpha：部分 Frida 会话为模拟实现，Codex 集成未做真实账号构建验证，应用/游戏行为验证有限。README 与生成文档工具数量不一致，因此不固定工具数。品牌素材另有商标限制。
  [补充依据 1](https://github.com/storytold/craft-anything/blob/main/Cargo.toml) · [补充依据 2](https://github.com/storytold/craft-anything/blob/main/docs/tools.md) · [补充依据 3](https://github.com/storytold/craft-anything/blob/main/docs/tool-status.md) · [补充依据 4](https://github.com/storytold/craft-anything/blob/main/docs/STATUS.md)
- [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn/blob/master/README.md) (2026-11-07): 不是完整操作系统模拟；调用者需提供内存和外部调用环境。GPLv2。
- [WebAssembly/wabt](https://github.com/WebAssembly/wabt/blob/main/README.md) (2026-11-07): WAT/C输出不等于原始C/C++/Rust源码恢复；扩展proposal支持不同，解释执行与纯静态读取应分开。 Apache-2.0
- [webrecorder/browsertrix-crawler](https://github.com/webrecorder/browsertrix-crawler/blob/main/README.md) (2026-11-07): 网页归档不等于完整后端复制或司法证据认证；抓取范围、个人数据、站点条款与证据完整性需要额外管理。 AGPL-3.0-or-later（README），GitHub元数据显示AGPL-3.0。
- [WhiteNightShadow/camoufox-reverse-mcp](https://github.com/WhiteNightShadow/camoufox-reverse-mcp/blob/main/README.md) (2026-11-07): 反指纹不等于不可检测；客户端可访问Cookie/存储；引擎追踪enable_trace=True会临时关闭Firefox content sandbox，不能作为默认低风险模式。 MIT
- [WhiteNightShadow/hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/README.md) (2026-11-07): 方法和模板不保证还原任意算法或VM；Hook可能改变目标行为。GitHub license=null，树中仅 scripts/real_cases/LICENSE，未发现覆盖主项目的根许可证，不能默认自由复制或商业复用。 主项目许可未明确；scripts/real_cases/LICENSE 为 CC0-1.0，仅覆盖该目录原创材料，不含上游源码/依赖/生成bundle。
  [补充依据 1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/references/browser-evidence-contract.md) · [补充依据 2](https://api.github.com/repos/WhiteNightShadow/hello_js_reverse_skill/git/trees/main?recursive=1) · [补充依据 3](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/scripts/real_cases/LICENSE)
- [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill/blob/main/README.md) (2026-11-07): 路由包不是逆向引擎。外部工具、MCP 与脚本仍需安装配置，自动安装和联网操作应先核查来源、范围和版本。README 不同小节的模块/规则计数存在不一致，不建议写死数量。 主项目 MIT；CTF-Sandbox-Orchestrator/ 为 GPLv3；被调用的 Pentest Swarm AI 为 AGPL-3.0；其余工具各自许可。
  [补充依据 1](https://github.com/zhaoxuya520/reverse-skill/blob/main/SECURITY.md) · [补充依据 2](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/UV-AND-DOWNLOAD-SECURITY.md) · [补充依据 3](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/SECURITY-REVIEW-2026-09-03.md)
- [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp/blob/jadx-ai/README.md) (2026-11-07): 与同作者 jadx-mcp-server 配套，区分插件和服务器，避免把两个仓库算成两个独立分析引擎。
- [zinja-coder/jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server/blob/main/README.md) (2026-11-07): 需要配套 JADX 插件和合适的 Java/Python 环境；这是桥接层，不替代 JADX。

[REA Atlas](README.zh-CN.md)
