# RFdiffusion — Keep the constraint visible while structure emerges.

Watson et al. · Nature 2023 · Figure 1

[Publication](https://www.nature.com/articles/s41586-023-06415-8) · [Original image source](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41586-023-06415-8/MediaObjects/41586_2023_6415_Fig1_HTML.png)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/rfdiffusion-figure.png) — SHA-256 `4fb2ab597652f9378eff4c283e1c929104fc114067c7cc2d45c6e683bad92411`. Unmodified publisher-hosted Figure 1.

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Replaces a two-row blob-repair cartoon with a scientifically denser geometric trajectory, multiple explicit conditions, and a visible invariant.

## See the mechanism

1. Read the noising/reverse-generative sequence in a, then identify the fixed conditioning object in each row of b.
2. Follow each row’s persistent motif or symmetry through the intermediate structures into the final backbone.
3. Compare the noisy input row with the clean-structure prediction row at matched denoising steps in c.

**Mechanism:** Iterative denoising constructs protein backbones; conditioning supplies symmetry, a binding target or a fixed motif that constrains what the trajectory can become.

**Visual construction:** Keep the constraint visible while structure emerges.

**What the eye understands:** Different design conditions change the space of possible outcomes; a fixed motif remains visible while its surrounding scaffold forms.

**Why an ordinary plot is weaker:** A designability curve reports success. Aligned intermediate structures reveal what is held fixed, what changes, and how a candidate is progressively organized.

## Learn this visual style, then adapt it

**Observe:** Rows are organized by a visible conditioning object; restrained, persistent colors distinguish fixed motifs from evolving structure. Matched temporal columns turn a complicated model into an inspectable transformation.

**Apply:** Use aligned state sequences in which the protected or conditioning object remains recognizable throughout the update.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Replace the protein with the project’s evolving state and the fixed motif with the actual constraint, target or protected substructure.

**Keep the relationship:** Preserve the time-step alignment, conditioning identity, and distinction between current noisy state and predicted clean state.

1. Anchor each row with its actual constraint, shown as a tangible object rather than a text-only condition.
2. Show matched intermediate states with stable object identities and a common viewing convention.
3. Place the final candidate and its independent validity evidence beside the trajectory, without treating a plausible shape as functional proof.

**Acceptance test:** Can a reader identify the unchanged constraint and distinguish the current state from its clean-state prediction?

**Do not copy literally:** Do not copy protein imagery for a non-structural problem or imply that a smooth denoising sequence alone validates a designed function.

**Scientific boundary:** The figure describes model construction and examples. Structural plausibility and predicted designability are not equivalent to experimental confirmation of binding or activity.

## Attribution and rights

MechanismFigures editorial reading of the cited publication. Replacement selected after the user retired the previous image on 2026-10-08; not an author endorsement or a new empirical result.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse.
