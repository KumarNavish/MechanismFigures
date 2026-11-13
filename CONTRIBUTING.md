# Contributing

An instruction earns its place when it prevents a real defect in a figure. Keep `SKILL.md` below 220 lines. Put depth in one file in `references/`.

To add a reference, follow `docs/MAINTAINING.md`. A reference must be a published figure with a verified licence. Generated images do not go into the atlas.

Run `python3 tools/build.py` and `python3 -m unittest discover -s tests` before you send a change. If you change the stage, render `kit/template.mjs` and look at the images.

Do not add a model API, analytics, network access at run time, or a dependency that needs an install step.
