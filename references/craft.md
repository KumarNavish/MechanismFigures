# Craft: make the mechanism survive close inspection

Anatomy's useful discipline is not “add an isometric look.” It is to decide the explanatory object before drawing, build its parts consistently, and inspect the result where a reader will find faults. The following rules adapt that discipline to scientific figures; they do not impose its machine vocabulary or minimum part count.

## 1. Choose the visual world

Write: **entity → operation → consequence**, and identify what the reader must predict. Choose a world where that operation is visible: a physical domain, an indexed graph, a valid state space, a deformation, a correspondence, or a matched sequence. Do not invent mechanical furniture around an abstract relationship merely to resemble a reference.

The [construction guide](choose.md) selects by evidence and insight. A perspective view is justified only when depth reveals a real interface, layer, occlusion or transformation. A plane is stronger when exact alignment or distance is the claim.

## 2. Inventory meaning before primitives

For each visible part name its scientific identity, evidence status, attachment/interface and visual role. Include the unchanged context necessary to interpret the operation. Exclude screws, gradients, frames and repeated blocks that do not contribute to the claim. There is no minimum number of parts; missing a necessary relation is a defect, and adding irrelevant complexity is also a defect.

For each connection name the source, target and operation. Its endpoints must attach to those objects. A narrative arrow is not a measured trajectory, causal proof or quantitative flow. Distinguish inferred, measured and schematic marks directly.

## 3. Construct once, transform explicitly

Keep model state separate from geometry, labels and controls. A number in the readout, a color, and a moving part must derive from the same state—not three independently authored approximations. Preserve object IDs across panels and time. Use the same origin, scale, camera and visibility convention for matched comparisons.

Use `kit/geometry.py` for declared coordinate transforms, not to confer meaning on arbitrary coordinates. Uniform fitting preserves projected proportions. Orthographic projection does not preserve every 3D distance and does not solve occlusion; state what the view encodes.

## 4. Interfaces are where errors hide

Inspect every decisive join: where a line touches a state; where a mask meets an object; where two layers correspond; where a trajectory crosses a boundary; where a local rule becomes a global outcome. At that join, can the eye follow the operation without guessing?

For physical structures, check support, contact, clearances and depth ordering with a suitable geometry engine. The included 2D bounds/anchor helper is not a 3D collision checker. For mathematical structures, check orientation, index convention, projection distortion, invariants and boundary cases from equations or data.

## 5. Two scales, one argument

At intended size, the main relation must read without legend hunting. At 4×, inspect labels, line terminations, ordering, boundaries, crops and correspondence. Detail should remain accurate—not merely more numerous. Whitespace is allowed and often essential; an empty region is not a defect by itself.

Use a quiet unchanged context, a clear active operation, and local annotations. Color must have a recorded role and essential distinctions must survive without it. Physical text dimensions and comparison scales stay fixed during refinement. Never hide a collision by shrinking labels below the output requirement.

## 6. Repair in causal order

False implication → missing mechanism → broken correspondence → unreadable construction → annotation → finish. Record the mistaken reading, its visible cause, the change and the expected improvement. Re-render and inspect. Do not “repair” a scientific error by changing a score, camera crop or caption while leaving the misleading picture intact.
