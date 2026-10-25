#!/usr/bin/env python3
"""Structural integrity check for GeoGeekLab VIS sources."""
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, msg):
    if not ok:
        errors.append(msg)

for folder, count in [("logos", 48), ("family/ref-fox", 21), ("new-mascots", 9)]:
    files = list((ROOT / folder).rglob("*.svg"))
    check(len(files) == count, f"{folder}: expected {count} SVGs, found {len(files)}")
    for file in files:
        try:
            root = ET.parse(file).getroot()
            check(root.tag.endswith("svg"), f"{file}: root is not SVG")
        except ET.ParseError as exc:
            errors.append(f"{file}: invalid XML: {exc}")

sheets = list((ROOT / "identity-sheets").glob("*.md"))
check(len(sheets) == 26, f"expected 26 identity sheets, found {len(sheets)}")
try:
    manifest = json.loads((ROOT / "manifests/registry.json").read_text(encoding="utf-8"))
    check(len(manifest.get("records", [])) == 26, "expected 26 manifest records")
except (ValueError, OSError) as exc:
    errors.append(f"invalid manifest: {exc}")

for filename in ["README.md", "GALLERY.md", "GUIDE.zh-CN.md", "ARTWORK-NOTICE.md"]:
    check((ROOT / filename).is_file(), f"missing {filename}")

if errors:
    print("\n".join("ERROR: " + x for x in errors))
    sys.exit(1)
print(f"OK: {len(sheets)} identity sheets; 78 SVGs; 26 manifest records.")
