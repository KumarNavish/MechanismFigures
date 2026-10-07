# mip-NeRF — Make the support visible

Barron et al. · ICCV 2021 · Figure 1

[Publication](https://openaccess.thecvf.com/content/ICCV2021/html/Barron_Mip-NeRF_A_Multiscale_Representation_for_Anti-Aliasing_Neural_Radiance_Fields_ICCV_2021_paper.html) · [Original image source](https://arxiv.org/pdf/2103.13415)

## Inspect the actual images before designing

- [focused figure](../../assets/calibration/5ea69e05-mipnerf.png) — SHA-256 `67582f35eefc5ee510b03d78eb08783580984f9c861fe19f82db6dd50b8459f9`. Actual figure rasterized from the authors' arXiv manuscript. The alternate view is Figure 3, not an uncropped Figure 1.
- [related figure](../../assets/calibration/f19aa5fb-mip-footprint.png) — SHA-256 `94dca5761a321b2eada79ee0b9ffa70b43a5a036c5cfb4bb7b80fef2a170d717`. Figure 3 · unequal pixel footprints

Reading a caption or this guide is not image inspection. Open at least two approved reference images at readable size and record their hashes.

**Use when:** Scale, uncertainty, receptive fields, spatial averaging or integration are being lost in point representations.

## See the mechanism

1. Find the isolated points on the left ray: none has a size.
2. Look at the middle cone: one pixel covers a growing region of space.
3. Compare the Gaussian on the right: the encoded quantity now includes that region, not just its center.

**Mechanism:** Pixel footprints change with viewing scale; point samples discard the spatial extent being averaged.

**Visual construction:** Widen the ray into a cone. Give every sample a volume, then show how that volume is encoded.

**What the eye understands:** Two samples at one position can represent different measurements because their footprints differ.

**Why an ordinary plot is weaker:** An anti-aliasing score shows improvement. The cone shows which missing information the representation restores.

## Learn this visual style, then adapt it

**Observe:** One camera geometry contrasts point samples, finite conical support and its Gaussian approximation. Similar positions make the missing extent visible.

**Apply:** Use the same origin, orientation and measurement center across alternatives. Give the support a defined spatial body; transparent layers should expose overlap, not merely soften the styling.

Record `composition_observation`, `encoding_observation`, `style_observation`, and `planned_application` for this image. Specify visible layout, persistent geometry, selective emphasis, annotation placement, color roles and whitespace—not just “clean” or “beautiful”.

## Transfer into the project

**Replace the objects:** Ray sample → your local query; cone → its actual support; integrated encoding → the operation that depends on that support.

**Keep the relationship:** Keep the same center and orientation when comparing supports. Extent must encode a defined physical or statistical quantity.

1. Draw two measurements sharing a center but having different supports.
2. Place the approximation or aggregation directly on each support.
3. Attach the consequence that differs only because the supports differ.

**Acceptance test:** Can the reader explain why identical centers do not imply identical measurements? Check support units, normalization and the approximation.

**Do not copy literally:** Do not use a fuzzy blob as an undefined symbol for uncertainty.

**Scientific boundary:** The Gaussian is an approximation to a conical frustum. This schematic explains the representation, not its empirical advantage.

## Attribution and rights

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.

Original authors/publishers retain image rights. The repository MIT license covers code/commentary, not the figures. Approved published figure included for source-specific critical visual study. Original author/publisher rights remain; the repository MIT license does not license this image or grant further republication rights. A broadly reusable image license has not been established.
