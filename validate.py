"""Offline integrity checks for the atlas and its skill technology map."""

import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


def check(condition, message):
    if not condition:
        raise ValueError(message)


def https_url(value):
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main():
    entries = json.loads(Path("data.json").read_text(encoding="utf-8"))
    descriptions = json.loads(Path("descriptions.json").read_text(encoding="utf-8"))
    skill_map = json.loads(Path("skill-map.json").read_text(encoding="utf-8"))
    languages = {"en", "zh-CN", "zh-TW", "ja", "ko"}
    names = [entry[2] for entry in entries]
    check(len(names) == len(set(names)), "Duplicate catalog project names")
    urls = [entry[3].rstrip("/").lower() for entry in entries]
    duplicates = [url for url, count in Counter(urls).items() if count > 1]
    check(not duplicates, f"Duplicate catalog URLs: {duplicates}")
    for entry in entries:
        check(len(entry) == 6, f"Expected six columns: {entry}")
        check(https_url(entry[3]), f"Invalid project URL: {entry[2]}")
        check(entry[4] in {"Yes", "No", "Unverified"}, f"Invalid REA tag: {entry[2]}")
        check(entry[2] in descriptions, f"Missing descriptions: {entry[2]}")
        check(set(descriptions[entry[2]]) == languages, f"Missing language: {entry[2]}")
        check(all(descriptions[entry[2]].values()), f"Empty description: {entry[2]}")
    check(skill_map["schema_version"] == 1, "Unsupported skill-map schema")
    skills = skill_map["skills"]
    check(len(skills) == 10, "The requested map must contain exactly ten skills")
    check(len({skill["id"] for skill in skills}) == 10, "Duplicate skill ids")
    mapped = set()
    for skill in skills:
        check(skill["repo"] in names, f"Skill source absent from catalog: {skill['repo']}")
        check(https_url(skill["source"]), f"Invalid skill source: {skill['id']}")
        check(set(skill["summary"]) == {"en", "zh-CN"}, f"Missing skill summary: {skill['id']}")
        check(set(skill["limitations"]) == {"en", "zh-CN"}, f"Missing limitations: {skill['id']}")
        check(skill["license"]["label"], f"Missing license status: {skill['id']}")
        check(https_url(skill["license"]["source"]), f"Invalid license source: {skill['id']}")
        check(len(skill["related"]) == len(set(skill["related"])), f"Duplicate mapped project: {skill['id']}")
        check(bool(skill["related"]), f"Empty technique mapping: {skill['id']}")
        for name in skill["related"]:
            check(name in names, f"Mapped project absent from catalog: {name}")
            mapped.add(name)
    evidence = skill_map["project_evidence"]
    for name in mapped | {skill["repo"] for skill in skills}:
        check(name in evidence, f"Missing project evidence: {name}")
        check(https_url(evidence[name]["source"]), f"Invalid evidence URL: {name}")
        check(evidence[name]["checked_on"] == skill_map["checked_on"], f"Evidence date mismatch: {name}")
        check(bool(evidence[name]["note"]), f"Empty evidence note: {name}")
    for filename in ["README.md", "README.zh-CN.md", "README.zh-TW.md", "README.ja.md", "README.ko.md"]:
        rendered = Path(filename).read_text(encoding="utf-8")
        check("SKILL_MAP" in rendered, f"Missing skill map navigation: {filename}")
        check("REA Atlas" not in rendered and "jammyfu/rea-atlas" not in rendered, f"Old atlas branding: {filename}")
        check("Reverse Engineering Atlas" in rendered, f"Missing atlas brand: {filename}")
        for entry in entries:
            check(f'href="{entry[3]}"' in rendered, f"Catalog entry omitted from {filename}: {entry[2]}")
        for anchor in ["atlas-start", "atlas-skills", "atlas-policy", "atlas-games", "atlas-app", "atlas-protocol", "atlas-firmware", "atlas-security", "atlas-tooling", "atlas-rea", "atlas-data"]:
            check(f'<a id="{anchor}"></a>' in rendered, f"Missing navigation target in {filename}: {anchor}")
        check(rendered.index('id="atlas-games"') < rendered.index('id="atlas-rea"'), f"REA subset dominates the catalog: {filename}")
        check(rendered.count("<details>") == rendered.count("</details>") == 1, f"Invalid optional-view markup: {filename}")
        heading_ids = set(re.findall(r'<a id="([^"]+)"></a>', rendered))
        seen = Counter()
        for heading in re.findall(r'^#{1,6} (.+)$', rendered, re.M):
            slug = re.sub(r'[^\w\- ]', '', heading.strip().lower()).replace(' ', '-')
            heading_ids.add(slug if seen[slug] == 0 else f'{slug}-{seen[slug]}')
            seen[slug] += 1
        for target in re.findall(r'\]\(#([^)]*)\)', rendered):
            check(target in heading_ids, f"Broken in-page link in {filename}: #{target}")
        for skill in skills:
            check(skill["repo"] in rendered, f"Missing skill in {filename}: {skill['repo']}")
    print(f"OK: {len(entries)} catalog entries, 5 languages, 10 skill mappings, {len(mapped)} related projects")


if __name__ == "__main__":
    main()
