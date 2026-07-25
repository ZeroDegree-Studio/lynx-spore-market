"""Generate index.json for the lynx-spore-market repository.

Scans spores/<spore_id>/spore.lynx and produces index.json with metadata for
each spore. Run by GitHub Actions on every push to main, or locally with:

    python tools/generate_index.py

Output format matches LocalMarketAdapter.index.json so the client can use the
same parser for both local and GitHub markets:

    {
      "version": "1",
      "updated_at": "<ISO 8601 UTC>",
      "spores": [
        {
          "spore_id": "...",
          "name": "...",
          "author": "...",
          "version": "...",
          "category": "...",
          "description": "...",
          "tags": [...],
          "price": 0,
          "currency": "USD",
          "official": true,
          "license": "MIT",
          "preview_url": "spores/<spore_id>/preview.png",
          "download_url": "spores/<spore_id>/spore.lynx"
        }
      ]
    }
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OFFICIAL_AUTHORS = ("lynx",)
VALID_CATEGORIES = ("style", "preference", "skill", "knowledge", "behavior")
INDEX_VERSION = "1"


def extract_metadata(spore_path: Path) -> dict[str, Any] | None:
    """Parse one spore.lynx and return its index entry, or None on failure."""
    try:
        with open(spore_path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"  ! ERROR reading {spore_path}: {e}", file=sys.stderr)
        return None

    spore_id = data.get("spore_id", "")
    name = data.get("name", "")
    author = data.get("author", "")
    category = data.get("category", "")
    version = data.get("version", "1.0.0")

    if not spore_id or not name or not author:
        print(f"  ! SKIP {spore_path}: missing required field "
              f"(spore_id/name/author)", file=sys.stderr)
        return None

    if category not in VALID_CATEGORIES:
        print(f"  ! SKIP {spore_path}: invalid category '{category}'", file=sys.stderr)
        return None

    spore_dir = spore_path.parent
    has_preview = (spore_dir / "preview.png").exists()

    return {
        "spore_id": spore_id,
        "name": name,
        "author": author,
        "version": version,
        "category": category,
        "description": data.get("description", ""),
        "tags": data.get("tags", []),
        "price": data.get("price", 0),
        "currency": data.get("currency", "USD"),
        "official": author.lower() in OFFICIAL_AUTHORS,
        "license": data.get("license", "MIT"),
        "preview_url": f"spores/{spore_id}/preview.png" if has_preview else "",
        "download_url": f"spores/{spore_id}/spore.lynx",
    }


def generate_index(repo_root: Path) -> dict[str, Any]:
    """Scan <repo_root>/spores/ and build the index structure."""
    spores_dir = repo_root / "spores"
    if not spores_dir.exists():
        print(f"  ! spores/ directory not found at {spores_dir}", file=sys.stderr)
        return {
            "version": INDEX_VERSION,
            "updated_at": _now_iso(),
            "spores": [],
        }

    entries: list[dict[str, Any]] = []
    for spore_dir in sorted(spores_dir.iterdir()):
        if not spore_dir.is_dir():
            continue
        if spore_dir.name.startswith("_"):
            # Skip draft directories (spores/_drafts/, etc.)
            continue
        spore_file = spore_dir / "spore.lynx"
        if not spore_file.exists():
            continue
        print(f"  + {spore_dir.name}/spore.lynx")
        entry = extract_metadata(spore_file)
        if entry is not None:
            entries.append(entry)

    return {
        "version": INDEX_VERSION,
        "updated_at": _now_iso(),
        "spores": entries,
    }


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    print(f"Scanning {repo_root / 'spores'} ...")
    index = generate_index(repo_root)
    out_path = repo_root / "index.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {out_path}")
    print(f"  spores indexed: {len(index['spores'])}")
    print(f"  updated_at: {index['updated_at']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
