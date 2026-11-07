"""Render the evidence-backed technology index without duplicating catalog data."""

import json
from pathlib import Path


LABELS = {
    "en": ("Skill technology map", "Ten skill entry points and related projects, grouped by technique. A technical match does not imply an upstream dependency or use of REA.", "Skill / source", "Techniques", "Related projects", "Evidence, licenses and limits"),
    "zh-CN": ("Skill 技术索引", "按技术整理十个 skill 入口及相关项目。技术相关不代表上游依赖，也不代表使用了 REA。", "Skill / 来源", "技术方向", "相关项目", "证据、许可与局限"),
    "zh-TW": ("Skill 技術索引", "依技術整理十個 skill 入口及相關專案。技術相關不代表上游相依，也不代表使用了 REA。", "Skill / 來源", "技術方向", "相關專案", "證據、授權與限制"),
    "ja": ("Skill 技術インデックス", "10 個の skill と関連プロジェクトを技術別に整理しています。技術的な関連は、依存関係や REA の使用を意味しません。", "Skill / 出典", "技術分野", "関連プロジェクト", "根拠・ライセンス・制限"),
    "ko": ("Skill 기술 색인", "10개 skill과 관련 프로젝트를 기술별로 정리했습니다. 기술적 연관성이 의존 관계나 REA 사용을 의미하지는 않습니다.", "Skill / 출처", "기술 분야", "관련 프로젝트", "근거, 라이선스 및 제한"),
}


def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")


def overview(language, skill_map):
    title, note, skill_label, techniques, related, details = LABELS[language]
    filename = "SKILL_MAP.zh-CN.md" if language in {"zh-CN", "zh-TW"} else "SKILL_MAP.md"
    lines = [note, "", f"[{details}]({filename}) · [JSON](skill-map.json)", "", f"| {skill_label} | {techniques} | {related} |", "| --- | --- | --- |"]
    for skill in skill_map["skills"]:
        lines.append(f"| [{skill['name']}](https://github.com/{skill['repo']}) | {cell(', '.join(skill['techniques']))} | [{len(skill['related'])}]({filename}#{skill['id']}) |")
    return title, lines + [""]


def render_details(skill_map, entries, descriptions):
    by_name = {entry[2]: entry for entry in entries}
    evidence = skill_map["project_evidence"]
    for language, filename in [("en", "SKILL_MAP.md"), ("zh-CN", "SKILL_MAP.zh-CN.md")]:
        chinese = language == "zh-CN"
        lines = ["[English](SKILL_MAP.md) · [简体中文](SKILL_MAP.zh-CN.md)", "", "# " + ("十类 Skill 技术与项目地图" if chinese else "Ten-skill technology and project map"), ""]
        lines += [
            (f"核验日期：{skill_map['checked_on']}。" if chinese else f"Checked on: {skill_map['checked_on']}."), "",
            ("本索引区分 skill 原项目、同技术方向的工具以及验证练习。相关项目由技术用途关联，不意味着 skill 实际依赖、维护者背书或使用了 REA。" if chinese else "This index separates the original skills, tools in the same technical area, and practice targets. Related projects are editorial technology matches, not a claim of upstream dependency, maintainer endorsement, or REA usage."), "",
            ("核验范围：官方仓库元数据、README 和列出的文档；未安装或执行任何项目，未独立复现性能、兼容性或安全声明。公开可访问不等于已获开源许可，许可证和附加条款以各上游为准。" if chinese else "Verification covers official repository metadata, READMEs and the listed documents. No project was installed or executed, and performance, compatibility and security claims were not independently reproduced. Public availability is not an open-source license; upstream licenses and any additional terms apply."), "",
            ("仅用于自有或明确授权的程序、协议与实验环境。遵守软件许可、隐私和当地法律；不收录破解、DRM 绕过或版权资产分发。第三方网站、账号和数据另需授权。" if chinese else "Use only with software, protocols and lab environments you own or are explicitly authorized to analyze. Respect licenses, privacy and local law. Cracks, DRM bypass and copyrighted-asset distribution are out of scope. Third-party websites, accounts and data require separate authorization."), "",
            ("维护源：[skill-map.json](skill-map.json)，执行 `python render.py` 同步生成本文件及五语 README。" if chinese else "Source of truth: [skill-map.json](skill-map.json). Run `python render.py` to regenerate this guide and all five READMEs."), "",
        ]
        for skill in skill_map["skills"]:
            lines.append(f"- [{skill['name']}](#{skill['id']})")
        for skill in skill_map["skills"]:
            lines += ["", f'<a id="{skill["id"]}"></a>', "", f"## {skill['name']}", "", f"[{skill['repo']}](https://github.com/{skill['repo']}) · [README]({skill['source']})", "", skill["summary"][language], ""]
            extra = evidence[skill["repo"]].get("additional_sources", [])
            if extra:
                label = "补充依据" if chinese else "Additional references"
                lines += [f"**{label}:** " + " · ".join(f"[{index}]({url})" for index, url in enumerate(extra, 1)), ""]
            lines += [f"**{'技术' if chinese else 'Techniques'}:** {', '.join(skill['techniques'])}", "", f"**{'许可' if chinese else 'License'}:** [{skill['license']['label']}]({skill['license']['source']})", "", f"**{'局限与注意事项' if chinese else 'Limits and caveats'}:** {skill['limitations'][language]}", ""]
            lines += [("| 相关项目 | 用途 | 核验来源 |" if chinese else "| Related project | Purpose | Verification source |"), "| --- | --- | --- |"]
            for name in skill["related"]:
                entry = by_name[name]
                item = evidence[name]
                purpose = item.get("purpose_zh", descriptions[name][language]) if chinese else descriptions[name][language]
                lines.append(f"| [{name}]({entry[3]}) | {cell(purpose)} | [README / docs]({item['source']}) |")
        lines += ["", "## " + ("来源与维护" if chinese else "Sources and maintenance"), "", ("以下记录为技术索引内项目的检查依据；日期是本次资料检查日期，不是项目发布日期。所有用途简介为编辑性概述，不构成安装或安全背书。" if chinese else "The following records identify the basis for projects in this technology index. The date is a documentation-check date, not a release date. Summaries are editorial and do not endorse installation or security."), ""]
        for name, item in sorted(evidence.items(), key=lambda pair: pair[0].lower()):
            note = item.get("note_zh", item["note"]) if chinese else item["note"]
            lines.append(f"- [{name}]({item['source']}) ({item['checked_on']}): {note}")
            if item.get("additional_sources"):
                lines.append("  " + " · ".join(f"[{'补充依据' if chinese else 'Reference'} {index}]({url})" for index, url in enumerate(item["additional_sources"], 1)))
        lines += ["", "[REA Atlas](README.zh-CN.md)" if chinese else "[REA Atlas](README.md)", ""]
        Path(filename).write_text("\n".join(lines), encoding="utf-8")


def load_map():
    return json.loads(Path("skill-map.json").read_text(encoding="utf-8"))
