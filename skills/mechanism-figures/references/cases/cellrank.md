# CellRank: Connect a local rule to a global future

Lange et al. · Nature Methods 2022 · Figure 1a–b

[Publication](https://www.nature.com/articles/s41592-021-01346-6/figures/1) · [Original asset](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41592-021-01346-6/MediaObjects/41592_2021_1346_Fig1_HTML.png)

**Use when:** Local transition estimates accumulate into macrostates, commitment or long-run behavior.

## Look in this order

1. Find the highlighted cell and its velocity in a–b.
2. Watch alignment with neighboring states become weighted transitions.
3. In the full figure, follow the transition matrix into macrostates and fate probabilities on the same population.

## Mechanism → construction → immediate insight

**Mechanism:** A cell's inferred expression velocity biases transitions toward compatible neighboring expression states.

**Construction:** Magnify one cell from the population. Turn angular agreement with its velocity into outgoing edge weights.

**The eye sees:** Neighbors ahead of the motion become more likely next states; proximity alone is insufficient.

**Why not an ordinary plot:** A colored cell map shows groups. This enlargement shows the local rule from which directed fate estimates are built.

## Recreate the explanatory operation

**Replace the objects:** Cell → your state; neighborhood → admissible next states; edge weight → transition probability; terminal fate → long-run outcome.

**Preserve:** Preserve state identity through local graph, transition matrix and global map. Distinguish inferred transitions from observed histories.

1. Enlarge one state and label its possible next steps.
2. Show how the update defines their relative probabilities.
3. Compress the same transition system into macrostates and show the resulting outcome distribution.

**Acceptance test:** Can the reader trace a global claim back to its local update? Check probability normalization and model assumptions.

**Do not copy literally:** Do not treat distances in a 2D embedding as the high-dimensional transition rule.

**Transfer example (proposal, not a finding):** For a reliability model, connect one component's failure/repair transitions to system-level absorbing failure probabilities.

**Scientific boundary:** Transitions use high-dimensional expression information, not distances in the displayed embedding. Inferred fates are not directly observed lineages.

## Actual images and rights

- [focused figure](../../assets/calibration/ff87748f-cellrank.png) — Publisher figure; panels a–b cropped together. Full figure continues through coarse-graining and fate probabilities.
- [full figure](../../assets/calibration/e3277e8e-cellrank.png) — Full published figure

Status: bundled. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

License: CC-BY-4.0. [Permission basis](https://www.nature.com/articles/s41592-021-01346-6).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
