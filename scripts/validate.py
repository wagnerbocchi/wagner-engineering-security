#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "wagner-engineering-security"
REMOVED = ("wazuh", "thehive", "the hive", "cortex", "shuffle", "soc-soar-stack")

errors: list[str] = []

def check_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"JSON inválido {path}: {e}")
        return {}

manifest = check_json(PLUGIN / ".codex-plugin" / "plugin.json")
marketplace = check_json(ROOT / ".agents" / "plugins" / "marketplace.json")
if manifest.get("name") != "wagner-engineering-security":
    errors.append("plugin.json: name incorreto")
if manifest.get("skills") != "./skills/":
    errors.append("plugin.json: skills deve ser ./skills/")

skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
if len(skills) != 13:
    errors.append(f"esperadas 13 skills; encontradas {len(skills)}")

for skill_md in skills:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"frontmatter ausente: {skill_md}")
        continue
    fm = m.group(1)
    nm = re.search(r"^name:\s*([^\n]+)", fm, re.M)
    if not nm or nm.group(1).strip() != skill_md.parent.name:
        errors.append(f"name/frontmatter divergente: {skill_md}")
    if not re.search(r"^description:\s*", fm, re.M):
        errors.append(f"description ausente: {skill_md}")

    low = text.lower()
    for term in REMOVED:
        if term in low:
            errors.append(f"termo legado '{term}' em {skill_md}")

    for ref in re.findall(r"references/([A-Za-z0-9._-]+\.md)", text):
        target = skill_md.parent / "references" / ref
        if not target.exists():
            errors.append(f"referência ausente: {skill_md.parent.name}/references/{ref}")

for path in PLUGIN.rglob("*.md"):
    low = path.read_text(encoding="utf-8").lower()
    for term in REMOVED:
        if term in low:
            errors.append(f"termo legado '{term}' em {path}")

entries = [p for p in marketplace.get("plugins", []) if p.get("name") == "wagner-engineering-security"]
if len(entries) != 1:
    errors.append("marketplace deve conter exatamente uma entrada do plugin")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)
print(f"VALIDATION OK: {len(skills)} skills")
