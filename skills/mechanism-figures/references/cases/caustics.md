# Computational Caustics — Make the desired image become a physical ray map.

Schwartzburg, Testuz, Tagliasacchi & Pauly · SIGGRAPH / ACM TOG 2014 · Figures 1 and 2

[Publication](https://www.epfl.ch/labs/gcm/research-projects/computational-caustics/) · [Original image source](https://theialab.ca/pubs/schwartzburg2014caustics.pdf)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/caustics-figure.png) — SHA-256 `1025c741106269f1003c831d178c8c2e31d3fc2faa2a4e55e3f671120c0a46f5`. Actual published primary figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "caustics.pdf", "page_zero_based": 1, "crop_fraction_top_left": [0.08, 0.05, 0.93, 0.264], "output": "caustics-fig2.png", "width": 2601, "height": 849, "sha256": "1025c741106269f1003c831d178c8c2e31d3fc2faa2a4e55e3f671120c0a46f5", "bytes": 335071, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"} Figure 2 photographic target: Philippe Halsman © Philippe Halsman Archive; source credit retained here.
- [related figure](../../assets/calibration/caustics-context.png) — SHA-256 `563e05b724676af6bb845a3458e8893d82328c1004a2bb0a6e8df6ea267cdf4f`. Actual published related figure, rasterized from the author/proceedings PDF with MuPDF 1.26.0. Extraction: {"source": "caustics.pdf", "page_zero_based": 0, "crop_fraction_top_left": [0.086, 0.148, 0.925, 0.304], "output": "caustics-fig1.png", "width": 2601, "height": 627, "sha256": "563e05b724676af6bb845a3458e8893d82328c1004a2bb0a6e8df6ea267cdf4f", "bytes": 2694464, "renderer": "MuPDF 1.26.0; actual published figure rasterization, no redraw"}

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Replaces a sparse footprint schematic with an inverse-design construction joining transport, geometry, fabrication and a visible optical result.

## See the mechanism

1. Locate the light source, transparent surface and receiving screen; keep their roles distinct.
2. Follow the target irradiance backwards into the transport assignment and the corresponding surface-normal field.
3. Use related Figure 1 to connect the optimized physical acrylic surface with the projected caustic as it rotates.

**Mechanism:** A transport map from source to target irradiance specifies surface normals; surface optimization produces a refractor whose light distribution approximates the target.

**Visual construction:** Make the desired image become a physical ray map.

**What the eye understands:** Moving light on the receiver requires changing where the surface sends each ray—not painting the surface with the target picture.

**Why an ordinary plot is weaker:** An image-error score hides the inverse-design dependency. The linked receiver, transport map, normals and refractor make the dependency inspectable.

## Learn this visual style, then adapt it

**Observe:** The same receiver plane makes source and target distributions comparable; ray direction, normal direction and physical surface remain attached, not split into abstract module names.

**Apply:** Expose the inverse map from a desired field to local controls, then return to a measured physical consequence.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Replace light with the conserved or transported quantity, the receiver with the target domain, and surface normals with the real controllable field.

**Keep the relationship:** Preserve source/target domains, flux accounting and the mapping between a local control and its downstream effect.

1. Show both where the quantity starts and where it must arrive.
2. Draw the correspondence that turns the desired outcome into local control parameters.
3. Place the implemented structure and its measured consequence beside that mapping; label model and experiment separately.

**Acceptance test:** Can the reader explain how changing one local surface region changes a particular part of the received pattern?

**Do not copy literally:** Do not borrow ray geometry for a process with no defensible transport mapping, or imply exact image recovery from an illustrative example.

**Scientific boundary:** The surface is an optimized approximation under an optical model. Target imagery and physical photographs have their own rights and are not new evidence for another project.

## Attribution and rights

MechanismFigures editorial reading of the cited publication. Replacement selected after the user retired the previous image on 2026-10-08; not an author endorsement or a new empirical result.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Actual published figure excerpt included with source-specific critical study. No general redistribution license is asserted by this repository. Original authors/publishers retain rights; inspect the source terms and any third-party image credits before further reuse.
