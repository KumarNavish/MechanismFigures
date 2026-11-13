# Maintain

## Sources of truth

| Concern | Edit | Generated from it |
|---|---|---|
| The workflow | `SKILL.md` | none |
| Moves, craft, truth, critique, story, stage | `references/*.md` | none |
| The atlas: references, images, rights | `assets/references.json` and `assets/calibration/` | `references/atlas.md`, `references/cases/*.md`, `assets/gallery.html`, `THIRD_PARTY.md` |
| The 3D stage | `kit/stage.mjs`, `scripts/render.mjs` | none |
| Install routes | `tools/agent_hosts.json`, `tools/install.py`, `tools/global_install.py` | none |

Do not edit a generated file. Run `python3 tools/build.py`.

## Checks

```bash
python3 tools/build.py
```

```bash
python3 -m unittest discover -s tests
```

The tests include one real render of `kit/template.mjs`. That test needs Node 22 or later and Chrome. It is skipped when they are absent.

## Add a reference

1. Find a published figure that shows an operation and its consequence, not only a structure. Prefer 3D.
2. Verify the licence on the article page. Use `bundled` only for a Creative Commons Attribution licence.
3. Put the image in `assets/calibration/`. Do not redraw it. A crop is permitted, and the treatment note must say so.
4. Open the image and write the entry in `assets/references.json`: the claim title, the mechanism, three places to look, why it works, what to take, a test, the limit, the moves and the view.
5. Record the SHA-256 and the selection in `approval`.
6. Run the build and the tests. Look at the new card in `assets/gallery.html`.

## Release

Change `VERSION` and the version in the `SKILL.md` front matter. Add an entry to `CHANGELOG.md`. Run the checks. Commit, tag and push. GitHub Pages serves `assets/gallery.html` from the `main` branch.

## The stage

three.js r170 and its line addons are in `kit/vendor` with their MIT licence. To change the version, replace the files and run the render test. Look at the output images: a test that passes does not prove that the render is good.
