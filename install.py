#!/usr/bin/env python3
"""Install the bundled native Codex v1 pets without replacing existing pets."""

import argparse
import json
import os
from pathlib import Path
import shutil
import sys


PACKAGE_ROOT = Path(__file__).resolve().parent / "codex"
PACKAGE_FILES = ("pet.json", "spritesheet.webp")


def discover_packages():
    if PACKAGE_ROOT.is_symlink() or not PACKAGE_ROOT.is_dir():
        raise ValueError(f"Missing regular package directory: {PACKAGE_ROOT}")
    packages = sorted(
        path.name for path in PACKAGE_ROOT.iterdir()
        if path.is_dir() and not path.is_symlink()
    )
    if not packages:
        raise ValueError(f"No pet packages found under: {PACKAGE_ROOT}")
    return packages


def validate_package(slug):
    source = PACKAGE_ROOT / slug
    for filename in PACKAGE_FILES:
        path = source / filename
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing regular package file: {path}")
    with (source / "pet.json").open(encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise ValueError(f"Invalid pet.json object: {source}")
    for field in ("id", "displayName", "description", "spritesheetPath"):
        value = manifest.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Invalid or missing {field}: {source / 'pet.json'}")
    if manifest["id"] != slug:
        raise ValueError(f"Pet ID must match package name {slug!r}: {source}")
    if manifest["spritesheetPath"] != "spritesheet.webp":
        raise ValueError(f"spritesheetPath must be spritesheet.webp: {source}")
    return source, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pets", nargs="*", metavar="PET",
        help="pet IDs to install; installs all available pets when omitted",
    )
    parser.add_argument(
        "--list", action="store_true",
        help="list available pet IDs and display names without installing",
    )
    parser.add_argument(
        "--dest", type=Path,
        default=Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "pets",
        help="alternate pets root (default: $CODEX_HOME/pets or ~/.codex/pets)",
    )
    args = parser.parse_args()
    if args.list and args.pets:
        parser.error("--list cannot be combined with pet IDs")
    destination = args.dest.expanduser().absolute()
    created = []
    try:
        available = discover_packages()
        unknown = [slug for slug in args.pets if slug not in available]
        if unknown:
            parser.error(f"unknown pet ID(s): {', '.join(unknown)}; use --list to see available pets")
        selected = list(dict.fromkeys(args.pets or available))
        packages = [(slug, *validate_package(slug)) for slug in selected]
        if args.list:
            print("ID\tNAME")
            for slug, _, manifest in packages:
                print(f"{slug}\t{manifest['displayName']}")
            return 0
        for slug, _, _ in packages:
            target = destination / slug
            if target.exists() or target.is_symlink():
                raise FileExistsError(f"Refusing to replace existing target: {target}")
        destination.mkdir(parents=True, exist_ok=True)
        for slug, source, _ in packages:
            target = destination / slug
            target.mkdir()
            created.append(target)
            for filename in PACKAGE_FILES:
                shutil.copy2(source / filename, target / filename)
    except (OSError, ValueError) as error:
        for target in reversed(created):
            shutil.rmtree(target)
        print(f"Error: {error}", file=sys.stderr)
        return 1
    for target in created:
        print(f"Installed: {target}")
    print("Open Settings > Pets > Refresh, then choose your pet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
