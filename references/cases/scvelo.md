# RNA velocity / scVelo — Turn lag into an oriented shape

Bergen et al. · Nature Biotechnology 2020 · Figure 1

[Publication](https://www.nature.com/articles/s41587-020-0591-3) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41587-020-0591-3/MediaObjects/41587_2020_591_Fig1_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/17c20634-scvelo.png) — SHA-256 `1dd26713ab1d2ca06c30b89d10170fb0504fcfd32d3042d1a34b1cd9a69139c0`. Full publisher figure, raster-resized without changing its content.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Two coupled quantities distinguish increasing and decreasing states that one variable conflates.

## See the mechanism

1. Read the transcription–splicing–degradation chain.
2. Trace the induction and repression arms in unspliced–spliced coordinates.
3. Notice that equal spliced abundance need not imply the same direction of change.

**Mechanism:** Unspliced and spliced RNA respond with a lag as a gene switches on and off.

**Visual construction:** Plot the two molecular quantities against each other. Fit an oriented trajectory through their joint states.

**What the eye understands:** The same spliced abundance can sit on different arms: rising and falling states need not look alike.

**Why an ordinary plot is weaker:** One expression curve or cluster map hides the ambiguity. The phase portrait makes the missing direction geometric.

## Learn this visual style, then adapt it

**Observe:** A molecular processing chain sits above the joint phase portrait. Oriented trajectory arms and time/state color separate induction from repression.

**Apply:** Make the coupled state variables the coordinates, and directly connect the physical processing rule to the inferred trajectory. Preserve a clear separation between observed points and model-fitted paths.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Unspliced/spliced RNA → your coupled quantities; trajectory arm → regime; orientation → update direction.

**Keep the relationship:** Keep the axes physically defined. Distinguish observed points from fitted trajectory and inferred time.

1. Plot the paired state variables rather than each separately against an arbitrary index.
2. Add the fitted or known dynamical direction and the regime switch.
3. Mark two states sharing one coordinate but having different futures.

**Acceptance test:** Does the second coordinate really disambiguate direction? Check the fitted equations and label inferred ordering.

**Do not copy literally:** Do not infer a closed cycle merely because a projected cloud looks curved.

**Scientific boundary:** This is model-based reconstruction from snapshots, not a movie of the same cells. Kinetic assumptions matter.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
