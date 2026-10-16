# Arknights Codex Pets

**English** | [简体中文](README.zh-CN.md)

A growing collection of fan-made *Arknights* animated companions for ChatGPT and Codex. Each character has a stable ID, importable sprite sheets, previews, and character notes.

**[Browse the character catalog](CATALOG.md)** to choose a character and download its files. The catalog is generated from [pets.json](pets.json), so new characters can be added without rewriting this guide.

## Choose an import method

| Environment | Method | File or package |
| --- | --- | --- |
| ChatGPT Work / Codex chat with the Pets plugin | Upload the full sprite sheet and ask the assistant to validate, create, and select the pet | `<character-id>.png` |
| Desktop client / Codex CLI using local custom pets | Install the local compatibility package | `codex/<character-id>/` |
| ChatGPT web with an Upload pet setting | Upload the v1 compatibility sprite sheet | `codex/<character-id>/spritesheet.webp` |

Choose files from the catalog; available Pets features depend on your account, workspace, and client version.

## Import through the Pets plugin

1. Open the [catalog](CATALOG.md) and download the character's **Full PNG** at its original size and transparency.
2. Upload it to a chat that can call the **Pets** plugin. A local Codex task can also read a repository file you have authorized it to access.
3. Replace `CHARACTER_NAME` in this prompt:

```text
Use the Pets plugin to import the attached complete transparent sprite sheet
as a pet named CHARACTER_NAME. Validate it first, then create and select the pet.
Use the existing sprite sheet without redrawing it.
```

Character notes linked in the catalog can supply the name, description, and creative context. Full v2 sheets use 1536 × 2288 pixels, nine animation states, and sixteen look directions. Check each entry in `pets.json` for its exact format.

If a catalog entry includes a **Public share** link, you can instead send that link to a Pets-enabled assistant and ask it to import and select the pet. This creates your own copy. The sprite sheet remains available if a share link expires or is withdrawn.

## Install a local compatibility package

Clone this repository, or use **Code → Download ZIP** on GitHub and extract it:

```bash
git clone https://github.com/xiaotwu/arknights-codex-pets.git
cd arknights-codex-pets
python3 install.py --list
```

Select an ID from the list, then replace `CHARACTER_ID` below:

```bash
python3 install.py CHARACTER_ID
```

You can pass multiple IDs. To install **all available packages**, omit the IDs:

```bash
python3 install.py
```

On Windows, use `py -3` instead of `python3` if needed. Use `--dest /path/to/pets` to choose a different pets directory.

The installer discovers packages in `codex/` automatically. It copies them to `$CODEX_HOME/pets/`, or `~/.codex/pets/` when `CODEX_HOME` is unset, and refuses to replace existing character directories.

```text
<CODEX_HOME>/pets/
└── <character-id>/
    ├── pet.json
    └── spritesheet.webp
```

After installation, use **Settings → Pets → Refresh** in a desktop client that provides these controls, or `/pets` in a compatible Codex CLI session. Local pets and web pets are managed separately. See the [official Pets documentation](https://learn.chatgpt.com/docs/pets).

The local package layout follows OpenAI's [hatch-pet skill](https://github.com/openai/skills/blob/main/skills/.curated/hatch-pet/SKILL.md). Its v1 sheet preserves the first nine animation rows at 1536 × 1872 pixels; the additional sixteen look directions are in the full v2 PNG.

## Upload through ChatGPT web settings

If available, open **Settings → Personalization → Pet → Select pet → Upload pet** and upload the character's v1 `spritesheet.webp` from the catalog's local package. As of October 15, 2026, [the official upload specification](https://learn.chatgpt.com/docs/pets) requires a transparent PNG or WebP, 1536 × 1872 pixels, at most 20 MiB.

## Repository layout

```text
<character-id>.png                  Full sprite sheet
codex/<character-id>/pet.json       Local package manifest
codex/<character-id>/spritesheet.webp
previews/<character-id>-*.gif       Animation previews
docs/<character-id>.md              Character notes and sources
pets.json                          Character catalog metadata
CATALOG.md / CATALOG.zh-CN.md       Generated character catalogs
scripts/update_catalog.py          Catalog and checksum generator
SHA256SUMS                         Download integrity checks
```

GIFs are previews; use PNG or WebP sprite sheets for import. Preserve the original dimensions, transparency, and cell layout.

## Add a character

1. Choose a unique lowercase English ID, using hyphens between words when needed. Use it consistently in filenames, the package directory, and the manifest's `id`.
2. Add the full sprite sheet, local compatibility package, previews, and character notes using the layout above. Follow the existing package manifest format.
3. Add an entry to `pets.json` with the character's names, description, provided file formats, relative paths, and correct SHA-256 values. Add a public share URL only when one is available. Keep game facts, cited sources, and creative interpretation distinct in the character notes.
4. Validate the sprite sheets, then regenerate both catalogs and download checksums:

```bash
python3 scripts/update_catalog.py
python3 install.py --list
```

The generator checks referenced files, metadata, and declared checksums. Character-specific content belongs in the catalog and character notes; these English and Chinese import guides can stay the same as the collection grows.

## Credits

This is an unofficial fan project with no official affiliation with Hypergryph, Yostar, or OpenAI. *Arknights* characters and original game material belong to their respective rights holders. See each character's notes for references and adaptation details.
