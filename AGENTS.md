# Character publication

- The user requests Public share links for every character by default. Include this step when publishing future characters unless the user explicitly restricts sharing.
- Resolve the owned custom pet by its stable ID and use the Pets sharing tool. Store its actual returned public URL in `pets.json` as `shareUrl`; reuse an existing valid link. Never invent a share URL.
- If sharing is unavailable or restricted, report and document the exception.
- Run `python3 scripts/update_catalog.py` and `git diff --check` after catalog metadata changes. Keep both character catalogs and both README languages current; English remains the default README.
- Group the generated catalogs by `game`, keeping Arknights and Arknights: Endfield separate.
- For Endfield characters, use `arknights-endfield-<english-name>` consistently for repository ID, filenames, local package directory, and website ID; set `game` to `Arknights: Endfield`. Preserve existing Arknights IDs.
