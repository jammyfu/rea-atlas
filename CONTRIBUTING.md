# Contributing to Reverse Engineering Atlas

1. Add one canonical entry per project to `data.json`: `[section, subsection, name, url, uses_rea, note]`, and matching five-language keys in `descriptions.json`. Use a factual one-sentence summary; do not add duplicate entries just to place a project in another workflow.
2. **Uses rea: Yes** needs public evidence (README, repo docs, official rea.tools showcase). Link it in the PR.
3. Put entries under the right platform and type (Decompilation / Recomp, Remake / Port, Asset extraction & tools) or the non-game sections.
4. Not accepted: cracks, DRM bypass, piracy, projects that ship ROMs, game files or other copyrighted assets.
5. Links must return HTTP 200 (or a valid redirect).
6. Update the source data and regenerate all five READMEs (en, zh-CN, zh-TW, ja, ko) in the same PR. Every description needs all five language keys; an English summary in each key is an acceptable fallback until reviewed translations are available. Shared navigation and guidance live in `readme_content.py` and are localized in all five languages.
7. Images: only redistributable images, with source and license credited.

## Skill technology map

- Keep `skill-map.json` as the source of truth for the ten skill entry points, technique mappings, official documentation, license caveats and check dates.
- Related projects are editorial technology matches. Do not present them as upstream dependencies, endorsements or proof of REA usage without evidence.
- Every mapped repository must also exist in `data.json` / `descriptions.json`. Add a `project_evidence` record with its checked README, metadata URL, license status and limitations.
- Keep unclear licenses explicit. A license for one subdirectory is not a license for the whole repository. Mark archived or maintenance-limited projects visibly.
- `Uses rea` concerns the analysis runtime/workflow. Merely comparing against REA in a benchmark does not make an independent alternative an REA-based project.
- Run `python render.py` and `python validate.py`; commit both generated `SKILL_MAP` guides and all five READMEs with the data change. Regeneration should produce no further changes.

Validation checks local structure and references, not live link availability or project execution. Check new external links against their official repositories separately, and distinguish documentation review from runtime verification.

By contributing you dedicate your contribution under CC0-1.0.
