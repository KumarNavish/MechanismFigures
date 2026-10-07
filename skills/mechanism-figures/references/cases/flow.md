# Multisample Flow Matching: Put the intermediate work beside its computational cost

Pooladian et al. · ICML 2023 · Figure 2

[Publication](https://proceedings.mlr.press/v202/pooladian23a.html) · [Original asset](https://proceedings.mlr.press/v202/pooladian23a/pooladian23a.pdf)

**Use when:** Methods reach similar endpoints through different intermediate states or demand different solver budgets.

## Look in this order

1. Read density evolution from left to right using the common time columns.
2. Compare when the checkerboard structure begins forming in different rows.
3. Move to the right-hand solver outputs: inspect what survives at a small number of function evaluations.

## Mechanism → construction → immediate insight

**Mechanism:** The coupling changes the intermediate probability path and how well a coarse numerical solver reaches the target.

**Construction:** Align whole density evolutions across methods. Attach matched low-budget outputs to the same rows.

**The eye sees:** Some paths acquire checkerboard structure early; others leave difficult rearrangement until late.

**Why not an ordinary plot:** An endpoint score hides when the work happens. The sequence ties intermediate structure to a visible computational consequence.

## Recreate the explanatory operation

**Replace the objects:** Density → your evolving state distribution; time columns → matched stages; solver columns → matched compute budgets.

**Preserve:** Use consistent time, domain and display scale across methods. Do not confuse distribution snapshots with particle trajectories.

1. Align a small set of informative intermediate stages across methods.
2. Place the budget-limited output beside each corresponding evolution.
3. Connect the observed difference to a measured numerical or computational consequence.

**Acceptance test:** Is the claimed mechanism visible before the endpoint? Match compute and inspect whether the intermediate difference predicts the result.

**Do not copy literally:** Do not choose different favorable timesteps for different methods.

**Transfer example (proposal, not a finding):** For iterative reconstruction, align intermediate reconstructions and show the result when every method is stopped at the same budget.

**Scientific boundary:** These are density snapshots, not individual trajectories. The 2D example does not establish universal low-step performance.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://proceedings.mlr.press/v202/pooladian23a.html).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
