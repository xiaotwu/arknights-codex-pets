#!/usr/bin/env python3
"""Regenerate both character catalogs and SHA256SUMS from pets.json."""

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SAFE_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
GAME_TITLES = {
    "Arknights": ("Arknights", "明日方舟"),
    "Arknights: Endfield": ("Arknights: Endfield", "明日方舟·终末地"),
}


def repository_path(value, *, directory=False):
    """Accept only existing, relative repository paths without symlinks."""
    if not isinstance(value, str) or not value:
        raise ValueError("File references must be nonempty strings")
    parts = value.split("/")
    if ("\\" in value or any(part in ("", ".", "..") for part in parts)
            or any(ord(char) < 32 for char in value)):
        raise ValueError(f"Unsafe repository path: {value!r}")
    path = ROOT
    for part in parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink references are not allowed: {value}")
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Path must stay inside the repository: {value}")
    if not (path.is_dir() if directory else path.is_file()):
        raise ValueError(f"Missing {'directory' if directory else 'file'}: {value}")
    return path


def read_object(path):
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def required_text(entry, field):
    value = entry.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing or invalid {field}")
    return value


def digest(path):
    checksum = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def validate_entries():
    metadata = read_object(repository_path("pets.json"))
    if metadata.get("schemaVersion") != 1 or not isinstance(metadata.get("pets"), list):
        raise ValueError("pets.json must use schemaVersion 1 with a pets array")
    ids, website_ids, checksums = set(), set(), {}
    for pet in metadata["pets"]:
        if not isinstance(pet, dict):
            raise ValueError("Every pets entry must be an object")
        pet_id = required_text(pet, "id")
        if not SAFE_ID.fullmatch(pet_id) or pet_id in ids:
            raise ValueError(f"Invalid or duplicate pet ID: {pet_id!r}")
        ids.add(pet_id)
        required_text(pet, "displayName")
        required_text(pet, "englishName")
        game = required_text(pet, "game")
        if game == "Arknights: Endfield" and not pet_id.startswith("arknights-endfield-"):
            raise ValueError(f"Endfield IDs must start with arknights-endfield-: {pet_id}")
        full = pet.get("full")
        if not isinstance(full, dict):
            raise ValueError(f"Missing full sprite metadata: {pet_id}")
        file = required_text(full, "file")
        checksums[file] = digest(repository_path(file))
        if full.get("sha256") and full["sha256"] != checksums[file]:
            raise ValueError(f"Full sprite SHA-256 mismatch: {pet_id}")
        if pet.get("characterNotes"):
            repository_path(pet["characterNotes"])
        previews = pet.get("previews", {})
        if not isinstance(previews, dict):
            raise ValueError(f"previews must be an object: {pet_id}")
        for file in previews.values():
            repository_path(file)
        share_url = pet.get("shareUrl")
        if share_url:
            if not isinstance(share_url, str):
                raise ValueError(f"Invalid shareUrl: {pet_id}")
            url = urlsplit(share_url)
            if (url.scheme != "https" or not url.netloc or url.username or url.password
                    or any(ord(char) < 32 for char in share_url)):
                raise ValueError(f"shareUrl must be an HTTPS URL: {pet_id}")
        website = pet.get("codexPets")
        if website is not None:
            if not isinstance(website, dict):
                raise ValueError(f"codexPets must be an object: {pet_id}")
            website_id = required_text(website, "id")
            if not SAFE_ID.fullmatch(website_id) or website_id in website_ids:
                raise ValueError(f"Invalid or duplicate codex-pets.net ID: {website_id!r}")
            website_ids.add(website_id)
            if required_text(website, "url") != f"https://codex-pets.net/#/pets/{website_id}":
                raise ValueError(f"codexPets URL must match its published ID: {pet_id}")
        local = pet.get("codexLocal")
        if local is not None:
            if not isinstance(local, dict):
                raise ValueError(f"codexLocal must be an object: {pet_id}")
            package_dir = repository_path(required_text(local, "directory"), directory=True)
            manifest_file = required_text(local, "manifest")
            sprite_file = required_text(local, "spritesheet")
            manifest_path = repository_path(manifest_file)
            sprite_path = repository_path(sprite_file)
            if manifest_path.parent != package_dir or sprite_path.parent != package_dir:
                raise ValueError(f"Native package files must be inside their directory: {pet_id}")
            manifest = read_object(manifest_path)
            for field in ("id", "displayName", "description"):
                if manifest.get(field) != required_text(pet, field):
                    raise ValueError(f"Native manifest {field} differs from pets.json: {pet_id}")
            if manifest.get("spritesheetPath") != sprite_path.name:
                raise ValueError(f"Native manifest spritesheetPath differs from pets.json: {pet_id}")
            for file in (manifest_file, sprite_file):
                checksums[file] = digest(repository_path(file))
            if local.get("sha256") and local["sha256"] != checksums[sprite_file]:
                raise ValueError(f"Native sprite SHA-256 mismatch: {pet_id}")
    return sorted(metadata["pets"], key=lambda pet: pet["id"]), checksums


def text(value):
    return re.sub(r"([\\`*_{}\[\]()#+.!|<>])", r"\\\1", str(value).replace("\n", " "))


def link(label, path, *, external=False):
    return f"[{text(label)}]({quote(path, safe='/:?=&%#' if external else '/')})"


def catalog(pets, *, chinese=False):
    title = "角色目录" if chinese else "Character catalog"
    intro = ("本目录按作品分组，由 [pets.json](pets.json) 自动生成。导入步骤请参阅 [中文说明](README.zh-CN.md)。"
             if chinese else
             "Grouped by game and generated from [pets.json](pets.json). See the [README](README.md) for import instructions.")
    headers = ("角色 | ID | 完整 PNG | Codex 本地包 | 角色设定 | 预览 | codex-pets.net | 公开分享"
               if chinese else
               "Character | ID | Full PNG | Codex package | Character notes | Previews | codex-pets.net | Public share")
    lines = ["<!-- Generated by scripts/update_catalog.py; edit pets.json instead. -->",
             "", f"# {title}", "", "[English](CATALOG.md) | [简体中文](CATALOG.zh-CN.md)",
             "", intro]
    preview_labels = ({"idle": "待机", "animations": "动作", "look": "视线", "contactSheet": "总览"}
                      if chinese else
                      {"idle": "Idle", "animations": "Animations", "look": "Gaze", "contactSheet": "Contact sheet"})
    game_order = {game: index for index, game in enumerate(GAME_TITLES)}
    ordered = sorted(pets, key=lambda pet: (
        game_order.get(pet["game"], len(game_order)), pet["game"], pet["id"]))
    current_game = None
    for pet in ordered:
        if pet["game"] != current_game:
            current_game = pet["game"]
            game_title = GAME_TITLES.get(current_game, (current_game, current_game))[int(chinese)]
            lines.extend(["", f"## {text(game_title)}", "", f"| {headers} |",
                          "| --- | --- | --- | --- | --- | --- | --- | --- |"])
        names = ((pet["displayName"], pet["englishName"]) if chinese else
                 (pet["englishName"], pet["displayName"]))
        local = pet.get("codexLocal")
        notes = pet.get("characterNotes")
        share = pet.get("shareUrl")
        website = pet.get("codexPets")
        row = [text(f"{names[0]} / {names[1]}"), f"`{pet['id']}`",
               link("PNG", pet["full"]["file"]),
               link("本地包" if chinese else "Package", local["directory"] + "/") if local else "—",
               link("设定" if chinese else "Notes", notes) if notes else "—",
               " · ".join(link(preview_labels.get(key, key), path)
                          for key, path in pet.get("previews", {}).items()) or "—",
               (link("网站导入" if chinese else "Website import", website["url"], external=True)
                + f" · `{website['id']}`") if website else "—",
               link("导入链接" if chinese else "Import link", share, external=True) if share else "—"]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def main():
    try:
        pets, checksums = validate_entries()
        outputs = {
            "CATALOG.md": catalog(pets),
            "CATALOG.zh-CN.md": catalog(pets, chinese=True),
            "SHA256SUMS": "".join(f"{checksums[path]}  {path}\n" for path in sorted(checksums)),
        }
        for filename, content in outputs.items():
            target = ROOT / filename
            if target.is_symlink():
                raise ValueError(f"Refusing to overwrite symlink: {filename}")
        for filename, content in outputs.items():
            (ROOT / filename).write_text(content, encoding="utf-8")
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"Updated catalogs and SHA256SUMS for {len(pets)} characters.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
