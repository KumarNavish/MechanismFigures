# CellRank — Connect a local rule to a global future

Lange et al. · Nature Methods 2022 · Figure 1

[Publication](https://www.nature.com/articles/s41592-021-01346-6/figures/1) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41592-021-01346-6/MediaObjects/41592_2021_1346_Fig1_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/ff87748f-cellrank.png) — SHA-256 `7eeca7a6a75679185c4f307cc1c2e362ee7a52cb52c062bcd4ed06b945ab02d7`. Publisher figure; panels a–b cropped together. Full figure continues through coarse-graining and fate probabilities.
- [full figure](../../assets/calibration/e3277e8e-cellrank.png) — SHA-256 `9b0011799630e4e71d5a9088c0c58ce14b4cfead6a0a9c47ab10c3f8756a4e81`. Full published figure

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Local transition estimates accumulate into macrostates, commitment or long-run behavior.

## See the mechanism

1. Find the highlighted cell and its velocity in a–b.
2. Watch alignment with neighboring states become weighted transitions.
3. In the full figure, follow the transition matrix into macrostates and fate probabilities on the same population.

**Mechanism:** A cell's inferred expression velocity biases transitions toward compatible neighboring expression states.

**Visual construction:** Magnify one cell from the population. Turn angular agreement with its velocity into outgoing edge weights.

**What the eye understands:** Neighbors ahead of the motion become more likely next states; proximity alone is insufficient.

**Why an ordinary plot is weaker:** A colored cell map shows groups. This enlargement shows the local rule from which directed fate estimates are built.

## Learn this visual style, then adapt it

**Observe:** A highlighted cell connects the population view to a magnified neighborhood, transition structure and fate map. The same scientific state persists across scales.

**Apply:** Compose the local rule and global consequence as one readable progression. Use repeated state identity and anchored enlargements; keep uncertainty and inferred transitions distinct from observations.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Cell → your state; neighborhood → admissible next states; edge weight → transition probability; terminal fate → long-run outcome.

**Keep the relationship:** Preserve state identity through local graph, transition matrix and global map. Distinguish inferred transitions from observed histories.

1. Enlarge one state and label its possible next steps.
2. Show how the update defines their relative probabilities.
3. Compress the same transition system into macrostates and show the resulting outcome distribution.

**Acceptance test:** Can the reader trace a global claim back to its local update? Check probability normalization and model assumptions.

**Do not copy literally:** Do not treat distances in a 2D embedding as the high-dimensional transition rule.

**Scientific boundary:** Transitions use high-dimensional expression information, not distances in the displayed embedding. Inferred fates are not directly observed lineages.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Article Rights and permissions states CC BY 4.0; reviewed figure credit lines contain no separate restriction. Original and focused assets are separately labeled.

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
