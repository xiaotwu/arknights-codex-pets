# Character publication

- The user requests Public share links for every character by default. Include this step when publishing future characters unless the user explicitly restricts sharing.
- Resolve the owned custom pet by its stable ID and use the Pets sharing tool. Store its actual returned public URL in `pets.json` as `shareUrl`; reuse an existing valid link. Never invent a share URL.
- If sharing is unavailable or restricted, report and document the exception.
- Run `python3 scripts/update_catalog.py` and `git diff --check` after catalog metadata changes. Keep both character catalogs and both README languages current; English remains the default README.
- Group the generated catalogs by `game`, keeping Arknights and Arknights: Endfield separate.
- For Endfield characters, use `arknights-endfield-<english-name>` consistently for repository ID, filenames, local package directory, and website ID; set `game` to `Arknights: Endfield`. Preserve existing Arknights IDs.

## Persistent workflow

- This repository is the canonical local home for published pet assets, manifests, previews, character notes, checksums and import documentation. Start each task by reading this file, `pets.json` and the current Git status; do not rely on an old chat or a fixed character count.
- Use the applicable Pets creation/update skill. Distinguish character facts supported by sources from visual observations and creative interpretation. If a referenced site is inaccessible, say what could not be read and use the supplied material without inventing missing facts.
- Preserve recognizable character details and colors. Do not add an unrequested purple border or background. For human-like running, both arms must move from their shoulders through their elbows and wrists, with each arm opposing its same-side leg; follow the actual hip/knee/ankle chain. Bracelet movement alone is not proof of arm movement.
- Inspect complete loops and ordered frames from the final encoded sheet, including both running directions. Validate the exact final bytes, show the resulting motion, and preserve useful source/QA artifacts in the pet's ChatGPT Library before upload. Structural checks do not substitute for visual motion review.
- Update an existing custom ChatGPT pet by its stable pet ID. Preserve its name, description and active selection unless the user requests a change. Verify stored image pixels after replacement. Do not create duplicate pets to repair one character.
- Publish to GitHub and codex-pets.net as part of a requested character publication, then update both language catalogs and import documentation. Use stable site IDs without the owner's GitHub username. Keep game groups separate and make the catalog extensible.
- Before replacing an existing site entry, inspect the current UI. If replacement requires irreversible deletion, prepare and validate the replacement first and obtain the required action-time confirmation for that exact entry. An earlier deletion approval for another character does not apply.
- Verify actual stored/downloaded assets, the pushed GitHub commit and catalog/checksum results. Report source checks, stored-file verification and actual client playback as separate evidence. Do not describe an unobserved client refresh/playback as tested.

## Mandatory completion cleanup

- The user requests this cleanup after every completed generation or repair. Keep locally only the canonical repository's maintained assets/documentation, pet packages actually installed for Codex/ChatGPT, and small persistent rule/state records. The useful process archive belongs in ChatGPT Library.
- Treat downloaded references copied for the task, generated alternatives, rejected revisions, strips, extracted frames, scratch scripts, temporary QA/previews/screenshots, local upload ZIPs, duplicate delivery folders and smoke-install directories as temporary. Once publication/verification and Library persistence are complete, remove these task-owned local copies. Do not keep a second local archive or silently retain temporary files in Trash as a substitute for cleanup.
- Inventory exact paths and sizes first. Protect active work, original user-owned inputs, other projects, shared runtimes/plugins, credentials and browser profiles. A task's broad scratch directory is removable only after checking for unrelated or active contents. Follow the user's deletion-confirmation rules for irreversible removal; report cleanup as pending if confirmation or another concrete blocker remains.
- Prefer links to the canonical repository or persistent Library artifacts in final delivery. Before removing a local duplicate, update any maintained project-status pointers that would otherwise refer to the removed path.
- Track browser tabs, windows, native apps and background jobs opened by this task. Close/stop them promptly when their work is finished, including tabs previously marked as deliverables, unless the user explicitly asks to keep them open. Do not close the user's pre-existing tabs/apps, another task's resources, or the Codex session hosting the work. Quit an app only when it was launched solely for this task and has no unrelated activity.
- Finish with a short receipt: publication links/commit, validation scope, local files retained, temporary bytes removed, task resources closed, and any actual pending cleanup. Keep the receipt concise and do not leave bulky local logs just to prove cleanup.
