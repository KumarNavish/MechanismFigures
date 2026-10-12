# Maintain one product, not a maze

## Sources of truth

| Concern | Edit here | Generated/read-only outputs |
|---|---|---|
| Entry workflow | `SKILL.md` | Loaded only when selected. |
| Scientific case, original asset, provenance and style | `assets/calibration.json` | `references/cases/*.md`, gallery, credit documents. |
| Current selection and retired references | `assets/approved-canon.json` within the skill | Curation audit tests. `docs/curation-2026-10-08.json` preserves the change rationale. |
| Review policy | `assets/rubric.json` and `references/critique.md` | Hash-bound reviews; do not change thresholds after seeing evaluation results. |
| Host discovery routes | `tools/agent_hosts.json` | Global installer/doctor, documented scope. |
| Motion | `tools/motion.*`, `tools/build_motion.py` | `assets/motion.html`, `assets/motion-story.json`, embedded gallery section. |
| Distribution | `plugin.json` (generated-plugin metadata), `tools/package.py` | Skill ZIP, plugin ZIP and checksums. |

## Local validation

```bash
python3 -m unittest discover -s tests -v
python3 tools/check_repo.py
python3 tools/build_gallery.py
git diff --check
python3 install.py --global --agents all --dry-run
```

Use `--home` pointing to an isolated temporary directory for installer smoke tests. Never run a model-backed agent to check installation. Verify files, then separately verify host discovery with user-controlled UI if the host offers it.

## Agent context budget

Installation docs stay outside the active scientific workflow. The skill loads only the input/decision guide, review policy and two relevant cases; it does not preload twenty figure explanations. New requirements belong at the decision where they matter, not in a giant always-on prompt. [Agent navigation index](../references/INDEX.md).

## Image and scientific safety

Never generate a replacement calibration figure, relabel a different figure as an original, or confuse an author's generative-model result with a measured observation. Retain exact published source, panel number, crop/rasterization notes and file hashes. Verify each image visually, not just by signature. No uniform code license covers all source figures.

When changing the selection, record the request, explicit old/new IDs, retained image hashes and perceptual rationale. Preserve failures in the curation record without promoting a rejected image back into the current gallery. A style-score average is not evidence of scientific fidelity.

## Releases

Set the package version consistently. Build both archives, inspect their manifests and hashes, test fresh installation, run unit and rendered browser checks, then publish the exact tested commit. Confirm the remote commit, GitHub Actions result, live gallery bytes and release checksums. Do not overwrite an uncertain release mutation without reconciling its original receipt.

## Root skill standard

One source tree is installable by standard skills CLI, direct Git clone or ZIP: root `SKILL.md`, `kit/`, `references/`, `assets/`, `scripts/`, `agents/`, `evals/`. Keep only legacy website redirects under `skills/mechanism-figures`; do not add a second nested `SKILL.md`. `tools/install.py` inventories an explicit payload so private `.git`, `.work`, caches and jobs are never copied.

The gallery/motion reader retains its independent curation edition while packaging versions advance. Canon image hashes and scientific review thresholds remain unchanged by this layout migration.
