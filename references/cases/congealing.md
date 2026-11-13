# Neural Congealing

**Use an edit as a probe of correspondence.**

Ofri-Amar et al.. *Neural Congealing: Aligning Images to a Joint Semantic Atlas*. CVPR 2023, Figure 1. [Publication](https://openaccess.thecvf.com/content/CVPR2023/html/Ofri-Amar_Neural_Congealing_Aligning_Images_to_a_Joint_Semantic_Atlas_CVPR_2023_paper.html)

**View:** Flat · **Moves:** Matched counterfactual

## Open the image

- [`assets/calibration/afe52f89-congealing.jpg`](../../assets/calibration/afe52f89-congealing.jpg): focused. Actual Figure 1 from the authors' March 2023 arXiv manuscript; butterfly examples retained in their original order.

Look at the image file. This text does not replace the look.

## Mechanism

A shared atlas maps corresponding semantic parts into common coordinates despite pose and appearance changes.

## Where to look

1. Read one column from original butterfly to aligned butterfly.
2. Read across the aligned row: corresponding parts occupy common coordinates.
3. Inspect the transferred edit below: it follows the corresponding part back into each original pose.

## Why it works

Original, aligned and edited images form consistent rows with each specimen in the same column. A localized edit visibly follows the corresponding semantic part.

## Take this

To show invariance, carry a concrete, localized probe through the transformation and back.

## Test your figure

Does the probe remain attached to the intended feature? Include failures and cases outside the fitted regime.

## Do not copy

Consistent coloring alone is not proof of a correct correspondence.

## Limit

Selected successes demonstrate correspondence qualitatively; they do not establish reliability over all inputs.

## Rights

Author manuscript license link is CC BY 4.0. Actual paper figure crop, not a reconstruction; figure-specific treatment is recorded below. Status: `bundled`, [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Selection: retained by the user on 2026-10-08.
