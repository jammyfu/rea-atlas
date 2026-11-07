[English](SKILL_MAP.md) · [简体中文](SKILL_MAP.zh-CN.md)

# Ten-skill technology and project map

Checked on: 2026-11-07.

This index separates the original skills, tools in the same technical area, and practice targets. Related projects are editorial technology matches, not a claim of upstream dependency, maintainer endorsement, or REA usage.

Verification covers official repository metadata, READMEs and the listed documents. No project was installed or executed, and performance, compatibility and security claims were not independently reproduced. Public availability is not an open-source license; upstream licenses and any additional terms apply.

Use only with software, protocols and lab environments you own or are explicitly authorized to analyze. Respect licenses, privacy and local law. Cracks, DRM bypass and copyrighted-asset distribution are out of scope. Third-party websites, accounts and data require separate authorization.

Source of truth: [skill-map.json](skill-map.json). Run `python render.py` to regenerate this guide and all five READMEs.

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

Evidence-oriented CLI and MCP toolkit for native, Android, JavaScript/Electron and firmware analysis; third-party engines are separate.

**Additional references:** [1](https://github.com/morluto/rea/blob/main/docs/reverse-engineering-tools.md) · [2](https://github.com/morluto/rea/blob/main/THIRD_PARTY_NOTICES.md) · [3](https://github.com/morluto/rea/blob/main/docs/javascript-application-workflows.md) · [4](https://github.com/morluto/rea/blob/main/docs/browser-observation.md)

**Techniques:** CLI / MCP, decompilation, cross-references, evidence

**License:** [MIT](https://github.com/morluto/rea/blob/main/README.md)

**Limits and caveats:** Third-party engines and licenses are separate. Decompilation does not recover arbitrary original source. Its CDP workflow is passive observation, not general browser control. Local analysis results can still enter the chosen agent/model provider data flow.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | The NSA's free decompiler and disassembler suite | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | Turn Android APKs back into readable Java | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [electron/asar](https://github.com/electron/asar) | Pack and unpack the archives inside Electron apps | [README / docs](https://github.com/electron/asar/blob/main/README.md) |
| [frida/frida](https://github.com/frida/frida) | Hook into running apps on any platform and rewrite them live | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | A bridge that lets AI assistants (like Claude) control the free reverse-engineering tool Ghidra. The AI can decompile programs, rename functions and analyze binaries for you. | [README / docs](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md) |
| [cyberkaida/reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant) | Another way to let AI control Ghidra (the free reverse-engineering tool from the NSA). It gives the AI small, focused tools so it can analyze big programs without getting confused. | [README / docs](https://github.com/cyberkaida/reverse-engineering-assistant/blob/main/README.md) |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | Early-alpha Rust reverse-engineering and AI reconstruction workbench for web, apps and games, with CLI/MCP; some runtime and agent integrations remain unvalidated. | [README / docs](https://github.com/storytold/craft-anything/blob/main/README.md) |

<a id="reverse-skill"></a>

## reverse-skill

[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) · [README](https://github.com/zhaoxuya520/reverse-skill/blob/main/README.md)

Agent skill router and playbooks for Android, native binaries, JavaScript, CTF and firmware, with evidence and reporting workflows.

**Additional references:** [1](https://github.com/zhaoxuya520/reverse-skill/blob/main/SECURITY.md) · [2](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/UV-AND-DOWNLOAD-SECURITY.md) · [3](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/SECURITY-REVIEW-2026-09-03.md)

**Techniques:** target routing, tool discovery, evidence workflows

**License:** [MIT (root); GPLv3 submodule and separately licensed dependencies](https://github.com/zhaoxuya520/reverse-skill/blob/main/README.md)

**Limits and caveats:** A router, not an analysis engine. External tools still require installation and authorization. The root is MIT, CTF-Sandbox-Orchestrator is GPLv3 and other dependencies have their own terms.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | The NSA's free decompiler and disassembler suite | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | A scriptable command-line reverse-engineering framework | [README / docs](https://github.com/radareorg/radare2/blob/master/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | Turn Android APKs back into readable Java | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | Unpack, read and rebuild Android APKs | [README / docs](https://github.com/iBotPeaches/Apktool/blob/main/README.md) |
| [frida/frida](https://github.com/frida/frida) | Hook into running apps on any platform and rewrite them live | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [angr/angr](https://github.com/angr/angr) | Symbolic execution and binary analysis from Python | [README / docs](https://github.com/angr/angr/blob/master/README.md) |

<a id="android-reverse-engineering-skill"></a>

## android-reverse-engineering-skill

[SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) · [README](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md)

Android static-analysis skill for APK/XAPK/JAR/AAR inspection, Kotlin metadata recovery and HTTP API documentation.

**Additional references:** [1](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/THIRD_PARTY_NOTICES.md) · [2](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/PRIVACY.md)

**Techniques:** APK / DEX, Kotlin metadata, HTTP API analysis

**License:** [Apache-2.0](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md)

**Limits and caveats:** Requires JDK/JADX and optional decompilers. Kotlin recovery depends on retained metadata; success rates are not guarantees. Windows PowerShell support is experimental. Native code and runtime validation need other tools.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [skylot/jadx](https://github.com/skylot/jadx) | Turn Android APKs back into readable Java | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | Unpack, read and rebuild Android APKs | [README / docs](https://github.com/iBotPeaches/Apktool/blob/main/README.md) |
| [androguard/androguard](https://github.com/androguard/androguard) | Python framework for APK/DEX structure and cross-reference analysis; development-branch capabilities may differ from PyPI releases. | [README / docs](https://github.com/androguard/androguard/blob/master/README.md) |
| [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | MCP plugin for JADX that enables AI agents to decompile and navigate Android APKs/DEX. | [README / docs](https://github.com/zinja-coder/jadx-ai-mcp/blob/jadx-ai/README.md) |
| [zinja-coder/jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server) | MCP server that exposes Android decompilation context through the companion JADX-AI-MCP plugin. | [README / docs](https://github.com/zinja-coder/jadx-mcp-server/blob/main/README.md) |
| [sensepost/objection](https://github.com/sensepost/objection) | Frida-based runtime exploration and security assessment toolkit for authorized Android and iOS applications. | [README / docs](https://github.com/sensepost/objection/blob/master/README.md) |
| [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Automated mobile application security assessment workbench with static and dynamic analysis; not a source-reconstruction engine. | [README / docs](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md) |

<a id="replica-skill"></a>

## replica-skill

[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) · [README](https://github.com/Jakeschincariol/replica-skill/blob/main/README.md)

A clean-room product-reconstruction skill suite for researching public interfaces, planning original implementations and checking functional and visual parity.

**Additional references:** [1](https://github.com/Jakeschincariol/replica-skill/blob/main/replica-recon/SKILL.md)

**Techniques:** black-box observation, clean-room specs, behavior tests

**License:** [MIT](https://github.com/Jakeschincariol/replica-skill/blob/main/README.md)

**Limits and caveats:** Functional and workflow reconstruction does not include target source, branding, assets, private APIs or data. Interfaces do not prove backend architecture. Scoring is not proof of equivalence and implementations need independent testing.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Official Playwright MCP server for structured accessibility-based browser interaction and exploratory testing. | [README / docs](https://github.com/microsoft/playwright-mcp/blob/main/README.md) |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Playwright command-line browser actions and reusable agent skills for screenshots, selectors, recordings and testing. | [README / docs](https://github.com/microsoft/playwright-cli/blob/main/README.md) |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Official Chrome DevTools integration for agent-driven browser inspection, network debugging, performance traces and automation. | [README / docs](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) |
| [webrecorder/browsertrix-crawler](https://github.com/webrecorder/browsertrix-crawler) | High-fidelity browser-based crawler that captures web content through CDP inside a standalone container. | [README / docs](https://github.com/webrecorder/browsertrix-crawler/blob/main/README.md) |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | Early-alpha Rust reverse-engineering and AI reconstruction workbench for web, apps and games, with CLI/MCP; some runtime and agent integrations remain unvalidated. | [README / docs](https://github.com/storytold/craft-anything/blob/main/README.md) |

<a id="leanrea"></a>

## leanrea

[aicodeking/leanrea](https://github.com/aicodeking/leanrea) · [README](https://github.com/aicodeking/leanrea/blob/main/README.md)

A compact reverse-engineering skill that routes agents directly to existing command-line tools instead of adding an MCP server.

**Additional references:** [1](https://github.com/aicodeking/leanrea/blob/main/bench/BENCHMARK.md)

**Techniques:** CLI orchestration, target triage, evidence

**License:** [MIT](https://github.com/aicodeking/leanrea/blob/main/README.md)

**Limits and caveats:** CLI-only alternative rather than an REA analysis client; the benchmark uses REA as a comparator. Author performance numbers cover one model, one macOS machine, four tasks with three runs and REA 6.5.0, not general performance guarantees.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | The NSA's free decompiler and disassembler suite | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | A scriptable command-line reverse-engineering framework | [README / docs](https://github.com/radareorg/radare2/blob/master/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | Turn Android APKs back into readable Java | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [electron/asar](https://github.com/electron/asar) | Pack and unpack the archives inside Electron apps | [README / docs](https://github.com/electron/asar/blob/main/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | WebAssembly toolkit for binary/text conversion, validation, disassembly, interpretation and C translation. | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Playwright command-line browser actions and reusable agent skills for screenshots, selectors, recordings and testing. | [README / docs](https://github.com/microsoft/playwright-cli/blob/main/README.md) |

<a id="ctf-skills"></a>

## ctf-skills

[ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills) · [README](https://github.com/ljagiello/ctf-skills/blob/main/README.md)

CTF agent skills for reversing and related challenge categories, with challenge routing and reproducible writeups.

**Additional references:** [1](https://github.com/ljagiello/ctf-skills/blob/main/ctf-reverse/SKILL.md)

**Techniques:** CTF reversing, symbolic execution, emulation

**License:** [MIT](https://github.com/ljagiello/ctf-skills/blob/main/README.md)

**Limits and caveats:** Skills do not install all tools by themselves. Optional bulk setup has many dependencies; related-challenge search uses Tavily. Do not upload private samples or challenge content without authorization.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [angr/angr](https://github.com/angr/angr) | Symbolic execution and binary analysis from Python | [README / docs](https://github.com/angr/angr/blob/master/README.md) |
| [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | Multi-architecture CPU emulation framework for isolated code execution, instrumentation and reverse-engineering experiments. | [README / docs](https://github.com/unicorn-engine/unicorn/blob/master/README.md) |
| [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools) | Python framework for CTF experiments and binary-analysis automation; component licenses vary. | [README / docs](https://github.com/Gallopsled/pwntools/blob/dev/README.md) |
| [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg) | GDB and LLDB extension for low-level debugging and reverse engineering; LLDB support is still early-stage. | [README / docs](https://github.com/pwndbg/pwndbg/blob/dev/README.md) |
| [radareorg/radare2](https://github.com/radareorg/radare2) | A scriptable command-line reverse-engineering framework | [README / docs](https://github.com/radareorg/radare2/blob/master/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | WebAssembly toolkit for binary/text conversion, validation, disassembly, interpretation and C translation. | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |

<a id="reverse-skills"></a>

## reverse-skills

[P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) · [README](https://github.com/P4nda0s/reverse-skills/blob/main/README.md)

Skills for interpreting IDA exports, recovering symbols and structures, and Frida/Unicorn-assisted analysis; MIT is claimed only in the README.

**Additional references:** [1](https://api.github.com/repos/P4nda0s/reverse-skills/contents)

**Techniques:** decompiler exports, type reconstruction, instrumentation

**License:** [MIT claimed in README; no independent LICENSE found](https://github.com/P4nda0s/reverse-skills/blob/main/README.md)

**Limits and caveats:** Designed around IDA-NO-MCP exports, not a standalone decompiler. Device/process operations need authorization. README says MIT but there is no independent root LICENSE file, so licensing remains incompletely documented.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [P4nda0s/IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP) | Exports IDA decompilation and call relationships into agent-readable files; no explicit root license file was found. | [README / docs](https://github.com/P4nda0s/IDA-NO-MCP/blob/main/README.md) |
| [HexRaysSA/ida-mcp](https://github.com/HexRaysSA/ida-mcp) | Hex-Rays' official MCP server for IDA | [README / docs](https://github.com/HexRaysSA/ida-mcp/blob/main/README.md) |
| [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) | IDA Pro MCP bridge; upstream now recommends the official HexRaysSA/ida-mcp successor. | [README / docs](https://github.com/mrexodia/ida-pro-mcp/blob/main/README.md) |
| [frida/frida](https://github.com/frida/frida) | Hook into running apps on any platform and rewrite them live | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [dnakov/frida-mcp](https://github.com/dnakov/frida-mcp) | Community MCP bridge for Frida devices, processes and JavaScript sessions; check maintenance and version compatibility. | [README / docs](https://github.com/dnakov/frida-mcp/blob/main/README.md) |
| [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn) | Multi-architecture CPU emulation framework for isolated code execution, instrumentation and reverse-engineering experiments. | [README / docs](https://github.com/unicorn-engine/unicorn/blob/master/README.md) |

<a id="hello-js-reverse-skill"></a>

## hello_js_reverse_skill

[WhiteNightShadow/hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill) · [README](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/README.md)

A JavaScript-analysis skill that routes signature, obfuscation, cookie and WASM investigations through controlled experiments and browser evidence.

**Additional references:** [1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/references/browser-evidence-contract.md) · [2](https://api.github.com/repos/WhiteNightShadow/hello_js_reverse_skill/git/trees/main?recursive=1) · [3](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/scripts/real_cases/LICENSE)

**Techniques:** JavaScript AST, deobfuscation, runtime analysis

**License:** [Project-wide license unclear; CC0 limited to scripts/real_cases](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/README.md)

**Limits and caveats:** Methods and templates do not recover arbitrary algorithms or VMs. Hooks can alter behavior. No project-wide root license was found; CC0 applies only to original scripts/real_cases material, not the whole repository.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [WhiteNightShadow/camoufox-reverse-mcp](https://github.com/WhiteNightShadow/camoufox-reverse-mcp) | Camoufox-based MCP server for JavaScript runtime inspection, script search, network capture, hooks and offline signer verification. | [README / docs](https://github.com/WhiteNightShadow/camoufox-reverse-mcp/blob/main/README.md) |
| [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack) | JavaScript deobfuscation and bundle-unpacking tool for supported obfuscator.io, webpack and Browserify patterns. | [README / docs](https://github.com/j4k0xb/webcrack/blob/master/README.md) |
| [pionxzh/wakaru](https://github.com/pionxzh/wakaru) | JavaScript decompiler and bundle unpacker that recovers readable modules and modern syntax from minified or transpiled production builds. | [README / docs](https://github.com/pionxzh/wakaru/blob/main/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | WebAssembly toolkit for binary/text conversion, validation, disassembly, interpretation and C translation. | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |
| [RyanDFIR/hindsight](https://github.com/RyanDFIR/hindsight) | Browser-forensics parser that correlates Chromium and Firefox profile artifacts into timelines and exportable reports. | [README / docs](https://github.com/RyanDFIR/hindsight/blob/main/README.md) |

<a id="open-reverselab"></a>

## Open-ReverseLab

[LING71671/open-reverselab](https://github.com/LING71671/open-reverselab) · [README](https://github.com/LING71671/open-reverselab/blob/main/README.md)

Agent-oriented reverse-engineering workbench combining MCP tools, a knowledge base and evidence workspaces; review the license and disclaimer.

**Additional references:** [1](https://github.com/LING71671/open-reverselab/blob/main/DISCLAIMER.md) · [2](https://github.com/LING71671/open-reverselab/blob/main/LICENSE)

**Techniques:** MCP workbench, native / Android, case reports

**License:** [GPL-3.0-only (README); additional disclaimer needs review](https://github.com/LING71671/open-reverselab/blob/main/README.md)

**Limits and caveats:** Heavier deployment and platform-specific GUI tools. Review host-environment caching and isolate untrusted samples; do not disable antivirus protections. README says GPL-3.0-only and also presents a mandatory disclaimer whose relationship to the license needs review.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | The NSA's free decompiler and disassembler suite | [README / docs](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) |
| [frida/frida](https://github.com/frida/frida) | Hook into running apps on any platform and rewrite them live | [README / docs](https://github.com/frida/frida/blob/main/README.md) |
| [rizinorg/rizin](https://github.com/rizinorg/rizin) | A UNIX-style reverse-engineering framework, forked from radare2 | [README / docs](https://github.com/rizinorg/rizin/blob/dev/README.md) |
| [rizinorg/cutter](https://github.com/rizinorg/cutter) | A friendly GUI for reverse engineering, powered by Rizin | [README / docs](https://github.com/rizinorg/cutter/blob/dev/README.md) |
| [skylot/jadx](https://github.com/skylot/jadx) | Turn Android APKs back into readable Java | [README / docs](https://github.com/skylot/jadx/blob/master/README.md) |
| [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | Unpack, read and rebuild Android APKs | [README / docs](https://github.com/iBotPeaches/Apktool/blob/main/README.md) |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | Early-alpha Rust reverse-engineering and AI reconstruction workbench for web, apps and games, with CLI/MCP; some runtime and agent integrations remain unvalidated. | [README / docs](https://github.com/storytold/craft-anything/blob/main/README.md) |

<a id="js-reverse-automation-skill"></a>

## js-reverse-automation--skill

[Fausto-404/js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill) · [README](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/README.md)

An evidence-driven JavaScript workflow that combines Chrome DevTools MCP with runtime probes and JSRPC, Flask and Burp artifact generation.

**Additional references:** [1](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/js-reverse-automation/references/capability-boundaries.md)

**Techniques:** CDP, AST, browser runtime, WASM

**License:** [Apache-2.0](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/README.md)

**Limits and caveats:** Documented limits exclude general VMP static recovery, unexported WASM internals, Service Worker closures, cross-origin iframes and CSP WebSocket bypass. Use isolated authorized test accounts; broad README claims are not universal support.

| Related project | Purpose | Verification source |
| --- | --- | --- |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Official Chrome DevTools integration for agent-driven browser inspection, network debugging, performance traces and automation. | [README / docs](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) |
| [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack) | JavaScript deobfuscation and bundle-unpacking tool for supported obfuscator.io, webpack and Browserify patterns. | [README / docs](https://github.com/j4k0xb/webcrack/blob/master/README.md) |
| [pionxzh/wakaru](https://github.com/pionxzh/wakaru) | JavaScript decompiler and bundle unpacker that recovers readable modules and modern syntax from minified or transpiled production builds. | [README / docs](https://github.com/pionxzh/wakaru/blob/main/README.md) |
| [WebAssembly/wabt](https://github.com/WebAssembly/wabt) | WebAssembly toolkit for binary/text conversion, validation, disassembly, interpretation and C translation. | [README / docs](https://github.com/WebAssembly/wabt/blob/main/README.md) |
| [electron/asar](https://github.com/electron/asar) | Pack and unpack the archives inside Electron apps | [README / docs](https://github.com/electron/asar/blob/main/README.md) |
| [doyensec/electronegativity](https://github.com/doyensec/electronegativity) | Archived Electron static-analysis scanner for security misconfigurations and anti-patterns. | [README / docs](https://github.com/doyensec/electronegativity/blob/master/README.md) |
| [doyensec/ElectroNG](https://github.com/doyensec/ElectroNG) | Open-source successor to Electronegativity for auditing Electron security configurations and implementation patterns. | [README / docs](https://github.com/doyensec/ElectroNG/blob/main/README.md) |

## Sources and maintenance

The following records identify the basis for projects in this technology index. The date is a documentation-check date, not a release date. Summaries are editorial and do not endorse installation or security.

- [aicodeking/leanrea](https://github.com/aicodeking/leanrea/blob/main/README.md) (2026-11-07): MIT. CLI-only alternative rather than an REA analysis client; the benchmark uses REA as a comparator. Author performance numbers cover one model, one macOS machine, four tasks with three runs and REA 6.5.0, not general performance guarantees.
  [Reference 1](https://github.com/aicodeking/leanrea/blob/main/bench/BENCHMARK.md)
- [androguard/androguard](https://github.com/androguard/androguard/blob/master/README.md) (2026-11-07): Apache-2.0. The v5 development branch differs from PyPI v4.1.4; pip installation may not expose all README features.
- [angr/angr](https://github.com/angr/angr/blob/master/README.md) (2026-11-07): BSD-2-Clause. Complex programs require environment modeling; full path coverage or automatic solving is not guaranteed.
- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) (2026-11-07): Apache-2.0. Can read and modify browser data. Use an isolated profile. Usage statistics are enabled by default, and performance features may send trace URLs to CrUX.
- [cyberkaida/reverse-engineering-assistant](https://github.com/cyberkaida/reverse-engineering-assistant/blob/main/README.md) (2026-11-07): Apache-2.0. PyGhidra scripts can execute code. Use access controls and consider disabling scripting on exposed services.
- [dnakov/frida-mcp](https://github.com/dnakov/frida-mcp/blob/main/README.md) (2026-11-07): MIT. Community bridge, not Frida official. Last recorded push is 2025-05-12; README has a placeholder, so recheck maintenance and compatibility.
- [doyensec/electronegativity](https://github.com/doyensec/electronegativity/blob/master/README.md) (2026-11-07): Apache-2.0. Archived; upstream points to ElectroNG. Historical reference, not a current default recommendation. Findings require manual review.
- [doyensec/ElectroNG](https://github.com/doyensec/ElectroNG/blob/main/README.md) (2026-11-07): Apache-2.0. README warns only minor fixes since 2024 and reduced coverage for modern Electron; non-archived status does not imply active comprehensive support.
- [electron/asar](https://github.com/electron/asar/blob/main/README.md) (2026-11-07): MIT. Archive utility, not a decompiler. Extraction does not grant code reuse rights.
- [Fausto-404/js-reverse-automation--skill](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/README.md) (2026-11-07): Apache-2.0. Documented limits exclude general VMP static recovery, unexported WASM internals, Service Worker closures, cross-origin iframes and CSP WebSocket bypass. Use isolated authorized test accounts; broad README claims are not universal support.
  [Reference 1](https://github.com/Fausto-404/js-reverse-automation--skill/blob/main/js-reverse-automation/references/capability-boundaries.md)
- [frida/frida](https://github.com/frida/frida/blob/main/README.md) (2026-11-07): Mixed or component-specific licenses; see upstream notices. Instrumentation has code-execution and process-control privileges. Root COPYING is wxWindows Library Licence 3.1; check individual components.
  [Reference 1](https://github.com/frida/frida/blob/main/COPYING)
- [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools/blob/dev/README.md) (2026-11-07): Mixed or component-specific licenses; see upstream notices. Mainly MIT with some GPL and BSD-2-Clause components, notably constants and data.
  [Reference 1](https://github.com/Gallopsled/pwntools/blob/dev/LICENSE-pwntools.txt)
- [HexRaysSA/ida-mcp](https://github.com/HexRaysSA/ida-mcp/blob/main/README.md) (2026-11-07): MIT. Requires IDA 9.4+, idalib and Python 3.11+. MIT covers the bridge, not an IDA commercial license.
- [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool/blob/main/README.md) (2026-11-07): Apache-2.0. Decodes resources and smali, not original Java/Kotlin source. Rebuilding and resigning change signatures and may change behavior.
- [j4k0xb/webcrack](https://github.com/j4k0xb/webcrack/blob/master/README.md) (2026-11-07): MIT. Supports specific patterns, not arbitrary JavaScript VMs, and cannot recover discarded information. Isolate untrusted input and match Node/isolated-vm versions.
- [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill/blob/main/README.md) (2026-11-07): MIT. Functional and workflow reconstruction does not include target source, branding, assets, private APIs or data. Interfaces do not prove backend architecture. Scoring is not proof of equivalence and implementations need independent testing.
  [Reference 1](https://github.com/Jakeschincariol/replica-skill/blob/main/replica-recon/SKILL.md)
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md) (2026-11-07): Apache-2.0. Match Ghidra/extension versions; mutation and scripting can alter analysis state. Do not expose the service unprotected.
- [LING71671/open-reverselab](https://github.com/LING71671/open-reverselab/blob/main/README.md) (2026-11-07): GPL-3.0-only (README); additional disclaimer needs review. Heavier deployment and platform-specific GUI tools. Review host-environment caching and isolate untrusted samples; do not disable antivirus protections. README says GPL-3.0-only and also presents a mandatory disclaimer whose relationship to the license needs review.
  [Reference 1](https://github.com/LING71671/open-reverselab/blob/main/DISCLAIMER.md) · [Reference 2](https://github.com/LING71671/open-reverselab/blob/main/LICENSE)
- [ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills/blob/main/README.md) (2026-11-07): MIT. Skills do not install all tools by themselves. Optional bulk setup has many dependencies; related-challenge search uses Tavily. Do not upload private samples or challenge content without authorization.
  [Reference 1](https://github.com/ljagiello/ctf-skills/blob/main/ctf-reverse/SKILL.md)
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/blob/main/README.md) (2026-11-07): Apache-2.0. CLI versus MCP is a workflow tradeoff, not a security or correctness guarantee; manage browser sessions and evidence retention.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp/blob/main/README.md) (2026-11-07): Apache-2.0. General browser execution layer, not a deobfuscator. Origin allow/block options are explicitly not a security boundary.
- [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md) (2026-11-07): GPL-3.0. Security-assessment workbench; dynamic environments require separate setup and are platform-dependent.
- [morluto/rea](https://github.com/morluto/rea/blob/main/README.md) (2026-11-07): MIT. Third-party engines and licenses are separate. Decompilation does not recover arbitrary original source. Its CDP workflow is passive observation, not general browser control. Local analysis results can still enter the chosen agent/model provider data flow.
  [Reference 1](https://github.com/morluto/rea/blob/main/docs/reverse-engineering-tools.md) · [Reference 2](https://github.com/morluto/rea/blob/main/THIRD_PARTY_NOTICES.md) · [Reference 3](https://github.com/morluto/rea/blob/main/docs/javascript-application-workflows.md) · [Reference 4](https://github.com/morluto/rea/blob/main/docs/browser-observation.md)
- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp/blob/main/README.md) (2026-11-07): MIT. README now recommends official HexRaysSA/ida-mcp. IDA Free is unsupported; IDA Pro/idalib licensing is separate.
- [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) (2026-11-07): Apache-2.0. Match extension and JDK versions. Decompiled code is not original source.
- [P4nda0s/IDA-NO-MCP](https://github.com/P4nda0s/IDA-NO-MCP/blob/main/README.md) (2026-11-07): No project-wide license established. No root LICENSE found and GitHub reports no license. Rust CLI needs licensed IDA Pro 9.x/idalib; do not assume redistribution permission.
  [Reference 1](https://api.github.com/repos/P4nda0s/IDA-NO-MCP/contents)
- [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills/blob/main/README.md) (2026-11-07): MIT claimed in README; no independent LICENSE found. Designed around IDA-NO-MCP exports, not a standalone decompiler. Device/process operations need authorization. README says MIT but there is no independent root LICENSE file, so licensing remains incompletely documented.
  [Reference 1](https://api.github.com/repos/P4nda0s/reverse-skills/contents)
- [pionxzh/wakaru](https://github.com/pionxzh/wakaru/blob/main/README.md) (2026-11-07): Apache-2.0. Not a heavy-obfuscation or VM breaker. Original names require retained metadata/source maps. Package-version inventory remains in development.
  [Reference 1](https://github.com/pionxzh/wakaru/blob/main/skills/wakaru/SKILL.md)
- [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg/blob/dev/README.md) (2026-11-07): MIT. LLDB support is early-stage; match the debugger and Python versions.
- [radareorg/radare2](https://github.com/radareorg/radare2/blob/master/README.md) (2026-11-07): Mixed or component-specific licenses; see upstream notices. Mainly LGPLv3, with GPL and other component licenses; inspect the build before redistribution.
  [Reference 1](https://github.com/radareorg/radare2/blob/master/COPYING.md)
- [rizinorg/cutter](https://github.com/rizinorg/cutter/blob/dev/README.md) (2026-11-07): GPL-3.0. Rizin-based GUI; plugin compatibility matters and it is not the current radare2 GUI.
- [rizinorg/rizin](https://github.com/rizinorg/rizin/blob/dev/README.md) (2026-11-07): LGPL-3.0. Commands and APIs are not assumed compatible with current radare2.
- [RyanDFIR/hindsight](https://github.com/RyanDFIR/hindsight/blob/main/README.md) (2026-11-07): Apache-2.0. Offline browser-profile forensics, not live JavaScript tracing. Authorized profiles only; exports can contain credentials and private data. Format support depends on browser versions.
- [sensepost/objection](https://github.com/sensepost/objection/blob/master/README.md) (2026-11-07): GPL-3.0. Check device and application-loading support. Runtime operations can change target state.
- [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/README.md) (2026-11-07): Apache-2.0. Requires JDK/JADX and optional decompilers. Kotlin recovery depends on retained metadata; success rates are not guarantees. Windows PowerShell support is experimental. Native code and runtime validation need other tools.
  [Reference 1](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/THIRD_PARTY_NOTICES.md) · [Reference 2](https://github.com/SimoneAvogadro/android-reverse-engineering-skill/blob/master/PRIVACY.md)
- [skylot/jadx](https://github.com/skylot/jadx/blob/master/README.md) (2026-11-07): Apache-2.0. Upstream explicitly does not guarantee complete decompilation; verify difficult code against bytecode.
- [storytold/craft-anything](https://github.com/storytold/craft-anything/blob/main/README.md) (2026-11-07): MIT OR Apache-2.0 (README and Cargo.toml). Early alpha: some Frida sessions are simulated, Codex integration has not been validated with a real account build, and app/game behavior checks are limited. README and generated tool counts differ, so no exact tool count is asserted. Brand assets have separate trademark restrictions.
  [Reference 1](https://github.com/storytold/craft-anything/blob/main/Cargo.toml) · [Reference 2](https://github.com/storytold/craft-anything/blob/main/docs/tools.md) · [Reference 3](https://github.com/storytold/craft-anything/blob/main/docs/tool-status.md) · [Reference 4](https://github.com/storytold/craft-anything/blob/main/docs/STATUS.md)
- [unicorn-engine/unicorn](https://github.com/unicorn-engine/unicorn/blob/master/README.md) (2026-11-07): GPL-2.0. Not a full operating-system emulator; callers must model memory and external calls.
- [WebAssembly/wabt](https://github.com/WebAssembly/wabt/blob/main/README.md) (2026-11-07): Apache-2.0. WAT/C output is not original C/C++/Rust source recovery. Proposal support varies; distinguish static inspection from executing an interpreter.
- [webrecorder/browsertrix-crawler](https://github.com/webrecorder/browsertrix-crawler/blob/main/README.md) (2026-11-07): AGPL-3.0. Archiving is not full backend replication or forensic certification. Manage collection scope, personal data, site terms and evidence integrity.
- [WhiteNightShadow/camoufox-reverse-mcp](https://github.com/WhiteNightShadow/camoufox-reverse-mcp/blob/main/README.md) (2026-11-07): MIT. Browser tools can access cookies/storage. Anti-fingerprinting is not undetectability. Optional engine tracing disables the Firefox content sandbox temporarily; do not treat it as a safe default.
- [WhiteNightShadow/hello_js_reverse_skill](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/README.md) (2026-11-07): Project-wide license unclear; CC0 limited to scripts/real_cases. Methods and templates do not recover arbitrary algorithms or VMs. Hooks can alter behavior. No project-wide root license was found; CC0 applies only to original scripts/real_cases material, not the whole repository.
  [Reference 1](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/references/browser-evidence-contract.md) · [Reference 2](https://api.github.com/repos/WhiteNightShadow/hello_js_reverse_skill/git/trees/main?recursive=1) · [Reference 3](https://github.com/WhiteNightShadow/hello_js_reverse_skill/blob/main/scripts/real_cases/LICENSE)
- [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill/blob/main/README.md) (2026-11-07): MIT (root); GPLv3 submodule and separately licensed dependencies. A router, not an analysis engine. External tools still require installation and authorization. The root is MIT, CTF-Sandbox-Orchestrator is GPLv3 and other dependencies have their own terms.
  [Reference 1](https://github.com/zhaoxuya520/reverse-skill/blob/main/SECURITY.md) · [Reference 2](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/UV-AND-DOWNLOAD-SECURITY.md) · [Reference 3](https://github.com/zhaoxuya520/reverse-skill/blob/main/docs/SECURITY-REVIEW-2026-09-03.md)
- [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp/blob/jadx-ai/README.md) (2026-11-07): Apache-2.0. JADX GUI plugin; requires its companion MCP server and is not a separate decompiler.
- [zinja-coder/jadx-mcp-server](https://github.com/zinja-coder/jadx-mcp-server/blob/main/README.md) (2026-11-07): Apache-2.0. Requires the companion JADX plugin and compatible Java/Python; a bridge rather than a decompiler.

[Reverse Engineering Atlas](README.md)
