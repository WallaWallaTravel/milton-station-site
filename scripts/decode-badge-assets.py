#!/usr/bin/env python3
"""Decode assets/images.b64.json into PNG files for GitHub Pages."""
import base64
import json
from pathlib import Path

src = Path("assets/images.b64.json")
data = json.loads(src.read_text())
for name, b64 in data.items():
    if Path(name).name != name:
        raise SystemExit(f"invalid asset name: {name}")
    path = Path("assets") / name
    path.write_bytes(base64.standard_b64decode(b64))
    print(f"wrote {path} ({path.stat().st_size} bytes)")
src.unlink()
