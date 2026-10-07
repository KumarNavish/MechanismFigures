# 3D Gaussian Splatting: Give each error its own repair

Kerbl et al. · SIGGRAPH / ACM TOG 2023 · Figure 4

[Publication](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [Original asset](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf)

**Use when:** One scalar loss combines qualitatively different spatial or structural failures.

## Look in this order

1. Keep the black target outline fixed in both rows.
2. Above, the small splat leaves geometry uncovered: cloning adds coverage.
3. Below, one splat is too large for the geometry: splitting gives smaller adjustable pieces.

## Mechanism → construction → immediate insight

**Mechanism:** Insufficient coverage and oversized primitives call for different density-control operations.

**Construction:** Hold the target shape fixed. Show cloning versus splitting, followed by continued optimization, in matched rows.

**The eye sees:** One error needs another primitive; the other needs a large primitive broken into smaller ones.

**Why not an ordinary plot:** One loss value collapses both failures. Spatial overlap makes the reason for each repair visible.

## Recreate the explanatory operation

**Replace the objects:** Outline → your target; splat → model primitive; mismatch type → diagnostic; clone/split → distinct interventions.

**Preserve:** The target, coordinates and comparison scale must stay fixed across repairs.

1. Show the two failure configurations in matched rows.
2. Apply only the corresponding local repair in each row.
3. Show the post-repair state in the same coordinate system.

**Acceptance test:** Can the reader select the appropriate repair from the error's shape alone? Validate that the intervention resolves that error rather than another confounder.

**Do not copy literally:** Do not show improvement by silently moving or simplifying the target.

**Transfer example (proposal, not a finding):** For adaptive meshing, contrast an uncovered feature with an element spanning too much curvature, then show their different refinements.

**Scientific boundary:** The cartoon idealizes densification. The full method also uses optimization signals and thresholds not visible here.

## Actual images and rights

- [focused figure](../../assets/calibration/gaussian-fig4.png) — Actual Figure 4 cropped from the author paper, page 6 (zero-based page 5). Re-rendered with MuPDF 1.26.0 at 1842+ px width to repair transparency artifacts in the earlier Quartz rasterization. Crop is [0.087,0.099,0.463,0.278] in normalized page coordinates; no scientific content redrawn.

Status: bundled. Author manuscript license link is CC BY 4.0. Actual paper figure crop, not a reconstruction; figure-specific treatment is recorded below.

License: CC-BY-4.0. [Permission basis](https://arxiv.org/abs/2308.04079).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
