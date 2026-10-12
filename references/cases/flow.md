# Multisample Flow Matching — Put the intermediate work beside its computational cost

Pooladian et al. · ICML 2023 · Figure 2

[Publication](https://proceedings.mlr.press/v202/pooladian23a.html) · [Original image source](https://proceedings.mlr.press/v202/pooladian23a/pooladian23a.pdf)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/e65934cc-flow.jpg) — SHA-256 `2c8c92f836499cfd098c981a3ec0ba7a7f011081cc4ad4a515d6722f6e29cd7e`. Actual Figure 2 rasterized from the PMLR proceedings PDF.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Methods reach similar endpoints through different intermediate states or demand different solver budgets.

## See the mechanism

1. Read density evolution from left to right using the common time columns.
2. Compare when the checkerboard structure begins forming in different rows.
3. Move to the right-hand solver outputs: inspect what survives at a small number of function evaluations.

**Mechanism:** The coupling changes the intermediate probability path and how well a coarse numerical solver reaches the target.

**Visual construction:** Align whole density evolutions across methods. Attach matched low-budget outputs to the same rows.

**What the eye understands:** Some paths acquire checkerboard structure early; others leave difficult rearrangement until late.

**Why an ordinary plot is weaker:** An endpoint score hides when the work happens. The sequence ties intermediate structure to a visible computational consequence.

## Learn this visual style, then adapt it

**Observe:** All methods share the same time columns and spatial domain; budget-limited outputs are attached to the corresponding row.

**Apply:** Use rigorously matched small multiples so the moment structure appears can be compared by eye. Keep time, normalization and solver budgets aligned; distinguish density snapshots from particle trajectories.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Density → your evolving state distribution; time columns → matched stages; solver columns → matched compute budgets.

**Keep the relationship:** Use consistent time, domain and display scale across methods. Do not confuse distribution snapshots with particle trajectories.

1. Align a small set of informative intermediate stages across methods.
2. Place the budget-limited output beside each corresponding evolution.
3. Connect the observed difference to a measured numerical or computational consequence.

**Acceptance test:** Is the claimed mechanism visible before the endpoint? Match compute and inspect whether the intermediate difference predicts the result.

**Do not copy literally:** Do not choose different favorable timesteps for different methods.

**Scientific boundary:** These are density snapshots, not individual trajectories. The 2D example does not establish universal low-step performance.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
