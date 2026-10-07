# 3D Gaussian Splatting — Give each error its own repair

Kerbl et al. · SIGGRAPH / ACM TOG 2023 · Figure 4

[Publication](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [Original image source](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/gaussian-fig4.png) — SHA-256 `95cf85419380887abe7961150ad6a787f46b74cb0a775eae829c4a482145023a`. Published Figure 4, page 6 of the author paper, normalized crop [0.087,0.099,0.463,0.278]. MuPDF rasterization preserves the transparent primitives; no scientific content redrawn.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** One scalar loss combines qualitatively different spatial or structural failures.

## See the mechanism

1. Keep the black target outline fixed in both rows.
2. Above, the small splat leaves geometry uncovered: cloning adds coverage.
3. Below, one splat is too large for the geometry: splitting gives smaller adjustable pieces.

**Mechanism:** Insufficient coverage and oversized primitives call for different density-control operations.

**Visual construction:** Hold the target shape fixed. Show cloning versus splitting, followed by continued optimization, in matched rows.

**What the eye understands:** One error needs another primitive; the other needs a large primitive broken into smaller ones.

**Why an ordinary plot is weaker:** One loss value collapses both failures. Spatial overlap makes the reason for each repair visible.

## Learn this visual style, then adapt it

**Observe:** The target outline stays fixed across two matched rows. Changes in primitive coverage are visible before the clone/split labels explain the repair.

**Apply:** Keep the target and scale fixed; show error, local repair and resulting fit in aligned positions. Represent the primitive itself, not a box naming the operation.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Outline → your target; splat → model primitive; mismatch type → diagnostic; clone/split → distinct interventions.

**Keep the relationship:** The target, coordinates and comparison scale must stay fixed across repairs.

1. Show the two failure configurations in matched rows.
2. Apply only the corresponding local repair in each row.
3. Show the post-repair state in the same coordinate system.

**Acceptance test:** Can the reader select the appropriate repair from the error's shape alone? Validate that the intervention resolves that error rather than another confounder.

**Do not copy literally:** Do not show improvement by silently moving or simplifying the target.

**Scientific boundary:** The cartoon idealizes densification. The full method also uses optimization signals and thresholds not visible here.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Author manuscript license link is CC BY 4.0. Actual paper figure crop, not a reconstruction; figure-specific treatment is recorded below.

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
