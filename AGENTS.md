# MechanismFigures: routes for an agent

**To make a figure:** read `SKILL.md`. It gives the loop, the moves and the stage. Do not read all case files.

**To install or update for this user:** read `docs/INSTALL.md`. Run `python3 install.py --global --agents all --dry-run`, then the same command with `--update` in place of `--dry-run`. Do not start a model to test discovery.

**To maintain this repository:** read `docs/MAINTAINING.md`. The source of truth for the atlas is `assets/references.json`. Run `python3 tools/build.py` after each change to it, then `python3 -m unittest discover -s tests`.

Rules:

- All atlas images are published figures or crops of them. Do not add a generated image to the atlas.
- Do not bring back a retired reference. The retired IDs are in `assets/references.json`.
- Twelve references were retained by the user on 2026-10-08. Do not remove them or change their image bytes without an instruction from the user.
- A new reference needs a verified licence, a source URL, a treatment note and a look at the real image. Record who selected it in `approval`.
- The installer does not call a model, change account settings or write outside its declared paths.
