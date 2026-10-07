# mip-NeRF: Make the support visible

Barron et al. · ICCV 2021 · Figure 1

[Publication](https://openaccess.thecvf.com/content/ICCV2021/html/Barron_Mip-NeRF_A_Multiscale_Representation_for_Anti-Aliasing_Neural_Radiance_Fields_ICCV_2021_paper.html) · [Original asset](https://arxiv.org/pdf/2103.13415)

**Use when:** Scale, uncertainty, receptive fields, spatial averaging or integration are being lost in point representations.

## Look in this order

1. Find the isolated points on the left ray: none has a size.
2. Look at the middle cone: one pixel covers a growing region of space.
3. Compare the Gaussian on the right: the encoded quantity now includes that region, not just its center.

## Mechanism → construction → immediate insight

**Mechanism:** Pixel footprints change with viewing scale; point samples discard the spatial extent being averaged.

**Construction:** Widen the ray into a cone. Give every sample a volume, then show how that volume is encoded.

**The eye sees:** Two samples at one position can represent different measurements because their footprints differ.

**Why not an ordinary plot:** An anti-aliasing score shows improvement. The cone shows which missing information the representation restores.

## Recreate the explanatory operation

**Replace the objects:** Ray sample → your local query; cone → its actual support; integrated encoding → the operation that depends on that support.

**Preserve:** Keep the same center and orientation when comparing supports. Extent must encode a defined physical or statistical quantity.

1. Draw two measurements sharing a center but having different supports.
2. Place the approximation or aggregation directly on each support.
3. Attach the consequence that differs only because the supports differ.

**Acceptance test:** Can the reader explain why identical centers do not imply identical measurements? Check support units, normalization and the approximation.

**Do not copy literally:** Do not use a fuzzy blob as an undefined symbol for uncertainty.

**Transfer example (proposal, not a finding):** For uncertain sensor readings, show each sensor's measured footprint and the field it averages—not identical dots with different labels.

**Scientific boundary:** The Gaussian is an approximation to a conical frustum. This schematic explains the representation, not its empirical advantage.

## Actual images and rights

Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.

Status: source-link-only. No broadly redistributable figure license verified; the paper and original asset are linked, not bundled.

License: not verified for redistribution. [Permission basis](https://openaccess.thecvf.com/content/ICCV2021/html/Barron_Mip-NeRF_A_Multiscale_Representation_for_Anti-Aliasing_Neural_Radiance_Fields_ICCV_2021_paper.html).

MechanismFigures design interpretation; not a quotation or endorsement by the paper authors.
