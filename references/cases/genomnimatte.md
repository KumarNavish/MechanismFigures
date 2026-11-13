# Generative Omnimatte

**Give an object’s nonlocal effects their own visible layer.**

Lee, Lu, Rumbley, Geyer, Huang, Dekel & Cole. *Generative Omnimatte: Learning to Decompose Video into Layers*. CVPR 2025, Figure 1; related Figure 4. [Publication](https://gen-omnimatte.github.io/)

**View:** 3D and flat · **Moves:** Layer stack, Matched counterfactual

## Open the image

- [`assets/calibration/genomnimatte-figure.png`](../../assets/calibration/genomnimatte-figure.png): focused. Actual published primary figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "genomnimatte.pdf", "page_zero_based": 0, "crop_fraction_top_left": [0.084, 0.275, 0.91, 0.579], "output": "genomnimatte-fig1.png", "width": 2601, "height": 1239, "sha256": "e90b87bb0211b3a0d5bfd6fc0b02727a39e0e76b3d36635194612e9f7c4051f6", "bytes": 3688076, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}
- [`assets/calibration/genomnimatte-context.png`](../../assets/calibration/genomnimatte-context.png): related. Actual published related figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "genomnimatte.pdf", "page_zero_based": 3, "crop_fraction_top_left": [0.084, 0.08, 0.91, 0.332], "output": "genomnimatte-fig4.png", "width": 2601, "height": 1028, "sha256": "bb4d46f0cf9608edfc471246e53799ef6814a2c03258b6da0cd21ac292ded100", "bytes": 804255, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}

Look at the image file. This text does not replace the look.

## Mechanism

Video is decomposed into object-associated RGBA layers that include effects such as shadows/reflections; removal-conditioned videos and a clean background support layer reconstruction.

## Where to look

1. For one row in Figure 1, keep the input scene fixed while following the separated transparent layers.
2. Compare the object-removal and edited results: look beyond the foreground silhouette to its associated effects.
3. In related Figure 4, trace preserve/remove/uncertain trimask regions into solo videos and the common clean background.

## Why it works

Transparent, spatially aligned sheets turn a hidden decomposition into a stack the reader can inspect. Real scenes remain repeated at matched scale, and interventions make the decomposition testable by eye.

## Take this

Make a latent decomposition spatial, then reveal its consequences through a matched edit rather than an isolated feature-importance ranking.

## Test your figure

Does the comparison expose effects outside the object mask, and are inferred/filled pixels labeled honestly?

## Do not copy

Do not equate an attention map or generative completion with causal proof; do not silently label hallucinated occluded content as observed.

## Limit

These are published model outputs. The authors report limits for physical interactions and difficult associations; RGBA color layers do not model every shape-changing effect.

## Rights

Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse. Status: `reference-excerpt`.
Selection: curator selection of 2026-10-08.
