# Changelog

## 1.0.1 — 2026-11-13

- **No grey.** The palette context colours are pale cool blues. The contact shadow has a blue tint (`shadowColor`). The default cap of a cut is darker and more saturated, not greyer. The guides tell the agent not to use grey.
- **`unlit` option.** `unlit: true` draws a part in its exact colour with no shading and no shadow on it. Use it when the reader must read a value from a colour.
- Source of the change: the first use of version 1.0.0 on a paper, where shaded low values and grey context looked grey.

## 1.0.0 — 2026-11-13

A rewrite with a strong bias for 3D.

- **Skill.** `SKILL.md` is a six-step loop: mechanism sentence, cast, look, move, build, repair. It tells the agent to propose a 3D construction first.
- **Atlas.** 42 references and 55 images, up from 20 and 29. 37 references use 3D. The 20 earlier references keep their image bytes. 22 CC BY 4.0 references are new curator selections that the user has not reviewed.
- **Moves.** Fifteen named visual moves, each with its construction, stage calls, failures and references.
- **Stage.** A three.js r170 studio (`kit/stage.mjs`) and a renderer (`scripts/render.mjs`): orthographic camera, contact shadows, outlines, capped cuts and quarter cuts, exploded parts, field surfaces, vector labels, a label audit, detail tiles and a grayscale copy.
- **Beats.** A figure module can export beats. The renderer makes one frame for each beat with a fixed camera, and a scroll page.
- **Guides.** New: clarity and cinematic flow, truth, critique with a defect table, craft for 3D.
- **Gallery.** A new page with claim titles, a filter by move and a full-size viewer.
- **Removed.** The JSON contract, the hash-bound review gate and the rubric; the benchmark and evaluation folders; the motion walkthrough; the 2D Python kit; the plugin package; the publication-verification workflow. The git history keeps them.
- **Install.** The payload is the working skill only: `SKILL.md`, `references`, `assets`, `kit`, `scripts`, the licence files and `VERSION`.

## 0.5.0 — 2026-10-12

Adopt the supplied Anatomy repository standard: one root skill, standard skills-CLI/Git/ZIP routes, image-led README, original geometry/SVG and model-driven motion helpers, 1×/4× rendered capture, craft/verification guides and evaluation cases. Preserve all current reference image bytes and scientific thresholds. Legacy gallery/motion URLs redirect without introducing duplicate skill discovery. The conservative Python installer uses an explicit payload and remains available for existing managed installations.

## 0.4.0 — 2026-10-08

Retired the eight references explicitly rejected by the user and replaced them with visually inspected published constructions. The other twelve references and their image hashes are unchanged; the active set remains twenty references and twenty-nine assets. Added a shared user-global installer, documented host adapters, conflict detection, version backups, interruption recovery, and a read-only doctor. Reorganized entry points for install/use/maintenance, added a portable plugin manifest and local catalog, and documented the boundary between local scope, activation and cloud-account installation. No model runner or account setting is invoked.

## 0.3.0 — 2026-10-07

Added an authored 60-second walkthrough on the gallery and a shareable motion.html: question, reference inspection, visible mechanism, critique, delivery, and reference-quality possibilities. Uses only unchanged approved scientific images; no generated showcase or simulated agent result. Includes playback/seek/replay/chapter controls, reduced-motion mode, text transcript, and visibility-aware suspension. The 20-reference / 29-image canon and scientific review thresholds are unchanged.

## 0.2.0 — 2026-10-07

Restore every approved real published figure: 20 references, 29 image assets, no text-only replacements. Present the original six anchors first, including full AlphaFold and CellRank figures. Remove self-generated demonstrations from the current public tree. Require two actual reference-image inspections with registered hashes, concrete composition/encoding/style observations, and output-to-reference comparisons. Preserve source-specific attribution and rights rather than applying the repository MIT license to images.

## 0.1.0 — 2026-10-07

Initial public skill: mechanism-to-figure workflow; twenty calibration case guides; rights-aware image bundle; standard-library contract/preflight/review helpers; offline atomic installer; ten-dimensional anchored rubric; independent-review distinction; analytical examples; diagnostic task packets and matched-evaluation protocol.

The public calibration rebuild repairs a transparency rendering defect found in the earlier Gaussian-splatting figure raster. Original paper content is preserved; source and renderer treatment are documented.

No claim of cross-agent empirical efficacy or universal reference-level output is made in this release.
