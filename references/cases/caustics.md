# Computational Caustics

**Make the desired image become a physical ray map.**

Schwartzburg, Testuz, Tagliasacchi & Pauly. *High-contrast Computational Caustic Design*. SIGGRAPH / ACM TOG 2014, Figures 1 and 2. [Publication](https://www.epfl.ch/labs/gcm/research-projects/computational-caustics/)

**View:** 3D · **Moves:** Target to consequence, Ray trace

## Open the image

- [`assets/calibration/caustics-context.png`](../../assets/calibration/caustics-context.png): related. Actual published related figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "caustics.pdf", "page_zero_based": 0, "crop_fraction_top_left": [0.086, 0.148, 0.925, 0.304], "output": "caustics-fig1.png", "width": 2601, "height": 627, "sha256": "563e05b724676af6bb845a3458e8893d82328c1004a2bb0a6e8df6ea267cdf4f", "bytes": 2694464, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}
- [`assets/calibration/caustics-figure.png`](../../assets/calibration/caustics-figure.png): focused. Actual published primary figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "caustics.pdf", "page_zero_based": 1, "crop_fraction_top_left": [0.08, 0.05, 0.93, 0.264], "output": "caustics-fig2.png", "width": 2601, "height": 849, "sha256": "1025c741106269f1003c831d178c8c2e31d3fc2faa2a4e55e3f671120c0a46f5", "bytes": 335071, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"} Figure 2 photographic target: Philippe Halsman © Philippe Halsman Archive; source credit retained here.

Look at the image file. This text does not replace the look.

## Mechanism

A transport map from source to target irradiance specifies surface normals; surface optimization produces a refractor whose light distribution approximates the target.

## Where to look

1. Locate the light source, transparent surface and receiving screen; keep their roles distinct.
2. Follow the target irradiance backwards into the transport assignment and the corresponding surface-normal field.
3. Use related Figure 1 to connect the optimized physical acrylic surface with the projected caustic as it rotates.

## Why it works

The same receiver plane makes source and target distributions comparable; ray direction, normal direction and physical surface remain attached, not split into abstract module names.

## Take this

Expose the inverse map from a desired field to local controls, then return to a measured physical consequence.

## Test your figure

Can the reader explain how changing one local surface region changes a particular part of the received pattern?

## Do not copy

Do not borrow ray geometry for a process with no defensible transport mapping, or imply exact image recovery from an illustrative example.

## Limit

The surface is an optimized approximation under an optical model. Target imagery and physical photographs have their own rights and are not new evidence for another project.

## Rights

Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse. Status: `reference-excerpt`.
Selection: curator selection of 2026-10-08.
