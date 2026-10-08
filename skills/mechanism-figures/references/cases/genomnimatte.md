# Generative Omnimatte — Give an object’s nonlocal effects their own visible layer.

Lee, Lu, Rumbley, Geyer, Huang, Dekel & Cole · CVPR 2025 · Figure 1; related Figure 4

[Publication](https://gen-omnimatte.github.io/) · [Original image source](https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_Generative_Omnimatte_Learning_to_Decompose_Video_into_Layers_CVPR_2025_paper.pdf)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/genomnimatte-figure.png) — SHA-256 `e90b87bb0211b3a0d5bfd6fc0b02727a39e0e76b3d36635194612e9f7c4051f6`. Actual published primary figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "genomnimatte.pdf", "page_zero_based": 0, "crop_fraction_top_left": [0.084, 0.275, 0.91, 0.579], "output": "genomnimatte-fig1.png", "width": 2601, "height": 1239, "sha256": "e90b87bb0211b3a0d5bfd6fc0b02727a39e0e76b3d36635194612e9f7c4051f6", "bytes": 3688076, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}
- [related figure](../../assets/calibration/genomnimatte-context.png) — SHA-256 `bb4d46f0cf9608edfc471246e53799ef6814a2c03258b6da0cd21ac292ded100`. Actual published related figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "genomnimatte.pdf", "page_zero_based": 3, "crop_fraction_top_left": [0.084, 0.08, 0.91, 0.332], "output": "genomnimatte-fig4.png", "width": 2601, "height": 1028, "sha256": "bb4d46f0cf9608edfc471246e53799ef6814a2c03258b6da0cd21ac292ded100", "bytes": 804255, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Replaces a node/feature mask schematic with a concrete layer decomposition, visible nonlocal effects and matched scene-level interventions.

## See the mechanism

1. For one row in Figure 1, keep the input scene fixed while following the separated transparent layers.
2. Compare the object-removal and edited results: look beyond the foreground silhouette to its associated effects.
3. In related Figure 4, trace preserve/remove/uncertain trimask regions into solo videos and the common clean background.

**Mechanism:** Video is decomposed into object-associated RGBA layers that include effects such as shadows/reflections; removal-conditioned videos and a clean background support layer reconstruction.

**Visual construction:** Give an object’s nonlocal effects their own visible layer.

**What the eye understands:** Removing an object must also account for what it changes elsewhere in the image; a silhouette mask is not the entire associated contribution.

**Why an ordinary plot is weaker:** A segmentation score hides residual shadows and incomplete objects. Exploded layers and matched removal/edit results make that distinction directly inspectable.

## Learn this visual style, then adapt it

**Observe:** Transparent, spatially aligned sheets turn a hidden decomposition into a stack the reader can inspect. Real scenes remain repeated at matched scale, and interventions make the decomposition testable by eye.

**Apply:** Make a latent decomposition spatial, then reveal its consequences through a matched edit rather than an isolated feature-importance ranking.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Replace the object with the project entity and its layer with the spatially distributed contribution supported by the model or evidence.

**Keep the relationship:** Keep scene identity, pixel correspondence and known/estimated content distinct. A generated counterfactual is not a real-world intervention.

1. Show the original scene and an exploded representation of the contributions without changing their coordinates.
2. Place a matched deletion or edit beside the decomposition so missed effects become visible.
3. Expose the inference/reconstruction operation and distinguish observed pixels from generatively completed regions.

**Acceptance test:** Does the comparison expose effects outside the object mask, and are inferred/filled pixels labeled honestly?

**Do not copy literally:** Do not equate an attention map or generative completion with causal proof; do not silently label hallucinated occluded content as observed.

**Scientific boundary:** These are published model outputs. The authors report limits for physical interactions and difficult associations; RGBA color layers do not model every shape-changing effect.

## Attribution and rights

MechanismFigures editorial reading of the cited publication. Replacement selected after the user retired the previous image on 2026-10-08; not an author endorsement or a new empirical result.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse.
