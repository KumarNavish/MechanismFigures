# Atlas

42 published figures, 55 image files. 37 of the figures use 3D. Open the image files and look at them. Each ID has a case file in `cases/`.

`python3 scripts/refs.py <words>` searches this atlas and prints absolute image paths.

## By move

- **Cutaway**: An operation inside a closed body. [`flagellar-stator`](cases/flagellar-stator.md), [`scutoids`](cases/scutoids.md), [`kent-hopfion`](cases/kent-hopfion.md), [`t3ss-needle`](cases/t3ss-needle.md), [`tokamak`](cases/tokamak.md), [`piezo-dome`](cases/piezo-dome.md)
- **Exploded view**: How parts join. [`photonic-braids`](cases/photonic-braids.md), [`alphatensor`](cases/alphatensor.md)
- **Layer stack**: A sequence of layers. [`photonic-braids`](cases/photonic-braids.md), [`graphcast`](cases/graphcast.md), [`kent-hopfion`](cases/kent-hopfion.md), [`kplanes`](cases/kplanes.md), [`genomnimatte`](cases/genomnimatte.md)
- **Ghost and focus**: One active part in a large assembly. [`loterie-vam`](cases/loterie-vam.md), [`rfdiffusion`](cases/rfdiffusion.md), [`myosin-stroke`](cases/myosin-stroke.md), [`frenzel-chiral`](cases/frenzel-chiral.md), [`birch-skyrmion`](cases/birch-skyrmion.md), [`mechanical`](cases/mechanical.md), [`piezo-dome`](cases/piezo-dome.md), [`hulse-compass`](cases/hulse-compass.md)
- **Fixed-camera sequence**: A change of state, shape or time. [`graphcast`](cases/graphcast.md), [`bioprint4d`](cases/bioprint4d.md), [`christoffersen-lake`](cases/christoffersen-lake.md), [`rfdiffusion`](cases/rfdiffusion.md), [`myosin-stroke`](cases/myosin-stroke.md), [`cohesin-ratchet`](cases/cohesin-ratchet.md), [`kennaway-growth`](cases/kennaway-growth.md), [`kirigami`](cases/kirigami.md), [`diffusive-machines`](cases/diffusive-machines.md), [`cohen-untangling`](cases/cohen-untangling.md), [`flow`](cases/flow.md)
- **Unroll pair**: The logic of a curved surface. [`weiler-gauge`](cases/weiler-gauge.md), [`torus`](cases/torus.md), [`hulse-compass`](cases/hulse-compass.md)
- **Ray trace**: Sampling, projection or transport through a volume. [`plenoxels`](cases/plenoxels.md), [`loterie-vam`](cases/loterie-vam.md), [`wolf-tomography`](cases/wolf-tomography.md), [`caustics`](cases/caustics.md), [`nerf`](cases/nerf.md), [`kplanes`](cases/kplanes.md), [`dreamfusion`](cases/dreamfusion.md)
- **Field on geometry**: A quantity on a surface or in a volume. [`weiler-gauge`](cases/weiler-gauge.md), [`graphcast`](cases/graphcast.md), [`kent-hopfion`](cases/kent-hopfion.md), [`wolf-tomography`](cases/wolf-tomography.md), [`bioprint4d`](cases/bioprint4d.md), [`frenzel-chiral`](cases/frenzel-chiral.md), [`zheng-hopfion`](cases/zheng-hopfion.md), [`birch-skyrmion`](cases/birch-skyrmion.md), [`kennaway-growth`](cases/kennaway-growth.md)
- **Linked zoom**: A local rule that gives a global result. [`photonic-braids`](cases/photonic-braids.md), [`plenoxels`](cases/plenoxels.md), [`flagellar-stator`](cases/flagellar-stator.md), [`scutoids`](cases/scutoids.md), [`t3ss-needle`](cases/t3ss-needle.md), [`tokamak`](cases/tokamak.md), [`frenzel-chiral`](cases/frenzel-chiral.md), [`birch-skyrmion`](cases/birch-skyrmion.md), [`diffusive-machines`](cases/diffusive-machines.md), [`piezo-dome`](cases/piezo-dome.md), [`cellrank`](cases/cellrank.md)
- **State-space geometry**: Dynamics, optimisation or invariance. [`torus`](cases/torus.md), [`safaie-dynamics`](cases/safaie-dynamics.md), [`cohen-untangling`](cases/cohen-untangling.md), [`fip`](cases/fip.md), [`cellrank`](cases/cellrank.md), [`scvelo`](cases/scvelo.md)
- **Index to geometry**: What an index or tensor refers to. [`photonic-braids`](cases/photonic-braids.md), [`kplanes`](cases/kplanes.md), [`alphatensor`](cases/alphatensor.md), [`hulse-compass`](cases/hulse-compass.md), [`alphafold`](cases/alphafold.md)
- **Target to consequence**: An inverse design. [`bioprint4d`](cases/bioprint4d.md), [`caustics`](cases/caustics.md), [`kirigami`](cases/kirigami.md), [`mechanical`](cases/mechanical.md)
- **Matched counterfactual**: The effect of one intervention. [`flagellar-stator`](cases/flagellar-stator.md), [`weiler-gauge`](cases/weiler-gauge.md), [`kent-hopfion`](cases/kent-hopfion.md), [`kennaway-growth`](cases/kennaway-growth.md), [`safaie-dynamics`](cases/safaie-dynamics.md), [`genomnimatte`](cases/genomnimatte.md), [`flow`](cases/flow.md), [`congealing`](cases/congealing.md), [`aardvark`](cases/aardvark.md)
- **Loop through one object**: A feedback or training cycle. [`nerf`](cases/nerf.md), [`cohesin-ratchet`](cases/cohesin-ratchet.md), [`dreamfusion`](cases/dreamfusion.md)
- **Block diagram**: A process in a landscape or a medium. [`azores-dike`](cases/azores-dike.md), [`graphcast`](cases/graphcast.md), [`christoffersen-lake`](cases/christoffersen-lake.md)

## All references

| ID | The figure shows | View | Moves | First image |
|---|---|---|---|---|
| [`photonic-braids`](cases/photonic-braids.md) | Give an algebraic operation a traversable physical route. | 3D | layers, exploded, zoom, index | `assets/calibration/photonic-braids-figure.png` |
| [`plenoxels`](cases/plenoxels.md) | A ray crosses a voxel grid, and each sample blends the eight corners of its voxel. | 3D | rays, zoom | `assets/calibration/plenoxels.png` |
| [`flagellar-stator`](cases/flagellar-stator.md) | With the stator in place, protons flow and the stator grips the rotor ring. | 3D | counterfactual, cutaway, zoom | `assets/calibration/flagellar-stator.jpg` |
| [`azores-dike`](cases/azores-dike.md) | Magma rises from the mantle along an old fault and stalls below the island. | 3D | block | `assets/calibration/azores-dike.png` |
| [`loterie-vam`](cases/loterie-vam.md) | Light patterns from many angles add up to a solid part inside a rotating vial. | 3D | rays, ghost | `assets/calibration/loterie-vam.png` |
| [`weiler-gauge`](cases/weiler-gauge.md) | Move a kernel along two paths: on a plane it agrees, on a sphere it rotates, on a Möbius strip it flips. | 3D | counterfactual, unroll, field | `assets/calibration/weiler-gauge-paths.png` |
| [`scutoids`](cases/scutoids.md) | Let a change of neighbors become a three-dimensional shape. | 3D | cutaway, zoom | `assets/calibration/scutoids-figure.png` |
| [`graphcast`](cases/graphcast.md) | The world stays visible while the representation changes. | 3D | block, field, sequence, layers | `assets/calibration/7b9f9e1b-graphcast.png` |
| [`kent-hopfion`](cases/kent-hopfion.md) | A quarter cut shows how the spins turn inside two magnetic textures. | 3D | cutaway, field, counterfactual, layers | `assets/calibration/kent-hopfion.png` |
| [`t3ss-needle`](cases/t3ss-needle.md) | Cut the needle complex in half to see the substrate in the channel. | 3D | cutaway, zoom | `assets/calibration/t3ss-needle.png` |
| [`wolf-tomography`](cases/wolf-tomography.md) | Two tilt series and one constraint give the full 3D magnetic field. | 3D | rays, field | `assets/calibration/wolf-tomography.png` |
| [`bioprint4d`](cases/bioprint4d.md) | Translate a target shape into the local directions that create it. | 3D | inverse, field, sequence | `assets/calibration/bioprint4d-figure.jpg` |
| [`christoffersen-lake`](cases/christoffersen-lake.md) | A lake that drains opens crevasses and speeds up the ice in a chain. | 3D | block, sequence | `assets/calibration/christoffersen-lake.jpg` |
| [`tokamak`](cases/tokamak.md) | Cut the vessel open: coils outside, plasma inside, and the section that the controller shapes. | 3D | cutaway, zoom | `assets/calibration/tokamak-cutaway.png` |
| [`caustics`](cases/caustics.md) | Make the desired image become a physical ray map. | 3D | inverse, rays | `assets/calibration/caustics-context.png` |
| [`nerf`](cases/nerf.md) | Follow one ray all the way to one pixel. | 3D | rays, loop | `assets/calibration/14900912-nerf.png` |
| [`kplanes`](cases/kplanes.md) | A point in space and time is read from six planes. | 3D | rays, layers, index | `assets/calibration/kplanes.png` |
| [`rfdiffusion`](cases/rfdiffusion.md) | Keep the constraint visible while structure emerges. | 3D | sequence, ghost | `assets/calibration/rfdiffusion-figure.png` |
| [`myosin-stroke`](cases/myosin-stroke.md) | The lever arm swings 34 nanometres on one motor domain. | 3D | sequence, ghost | `assets/calibration/myosin-stroke.png` |
| [`cohesin-ratchet`](cases/cohesin-ratchet.md) | One gripping cycle moves the DNA a step and makes the loop larger. | 3D | sequence, loop | `assets/calibration/cohesin-ratchet.jpg` |
| [`frenzel-chiral`](cases/frenzel-chiral.md) | A chiral lattice turns the polarisation of a wave as the wave travels. | 3D | zoom, ghost, field | `assets/calibration/frenzel-chiral.png` |
| [`zheng-hopfion`](cases/zheng-hopfion.md) | Rings of twisted magnetisation link round skyrmion strings. | 3D | field | `assets/calibration/zheng-hopfion.png` |
| [`birch-skyrmion`](cases/birch-skyrmion.md) | Skyrmion tubes run through the sample and end at Bloch points. | 3D | field, ghost, zoom | `assets/calibration/birch-skyrmion.png` |
| [`kennaway-growth`](cases/kennaway-growth.md) | The same sheet grows into different shapes when the polarity field is different. | 3D | sequence, field, counterfactual | `assets/calibration/kennaway-growth.png` |
| [`kirigami`](cases/kirigami.md) | The boundary predicts how the sheet bends. | 3D | sequence, inverse | `assets/calibration/fc3c6acf-kirigami.jpg` |
| [`diffusive-machines`](cases/diffusive-machines.md) | Show time as a wave of changing geometry. | 3D | sequence, zoom | `assets/calibration/diffusive-machines-figure.png` |
| [`mechanical`](cases/mechanical.md) | Let the mechanism grow inside the same object. | 3D | inverse, ghost | `assets/calibration/mechanical-figure.png` |
| [`piezo-dome`](cases/piezo-dome.md) | The protein curves the membrane into a dome, and the dome deforms the membrane far beyond it. | 3D | zoom, ghost, cutaway | `assets/calibration/piezo-dome.jpg` |
| [`torus`](cases/torus.md) | Many fields become one place on a torus. | 3D | unroll, state-space | `assets/calibration/a4bc70a9-torus-a.png` |
| [`dreamfusion`](cases/dreamfusion.md) | The feedback returns to the object that changes. | 3D | loop, rays | `assets/calibration/f022cea5-dreamfusion.png` |
| [`alphatensor`](cases/alphatensor.md) | Matrix multiplication is a 3D block of ones and zeros. | 3D | index, exploded | `assets/calibration/alphatensor-block.png` |
| [`safaie-dynamics`](cases/safaie-dynamics.md) | Two brains hold the same trajectory in planes with different orientations. | 3D | state-space, counterfactual | `assets/calibration/safaie-dynamics.png` |
| [`cohen-untangling`](cases/cohen-untangling.md) | Layer by layer, two tangled manifolds come apart. | 3D and flat | state-space, sequence | `assets/calibration/cohen-untangling.png` |
| [`hulse-compass`](cases/hulse-compass.md) | A ring of neurons maps to two shifted copies in the bridge. | 3D and flat | unroll, index, ghost | `assets/calibration/hulse-compass.png` |
| [`genomnimatte`](cases/genomnimatte.md) | Give an object’s nonlocal effects their own visible layer. | 3D and flat | layers, counterfactual | `assets/calibration/genomnimatte-figure.png` |
| [`fip`](cases/fip.md) | Many parameter locations, nearly the same function. | 3D and flat | state-space | `assets/calibration/c1bbd0b1-fip.png` |
| [`cellrank`](cases/cellrank.md) | A local direction becomes a possible future. | 3D and flat | zoom, state-space | `assets/calibration/e3277e8e-cellrank.png` |
| [`alphafold`](cases/alphafold.md) | A tensor update becomes a route around a triangle. | Flat | index | `assets/calibration/82942714-alphafold.png` |
| [`scvelo`](cases/scvelo.md) | The lag draws the direction. | Flat | state-space | `assets/calibration/17c20634-scvelo.png` |
| [`flow`](cases/flow.md) | Show when structure forms—and what a coarse solver misses. | Flat | counterfactual, sequence | `assets/calibration/e65934cc-flow.jpg` |
| [`congealing`](cases/congealing.md) | Use an edit as a probe of correspondence. | Flat | counterfactual | `assets/calibration/afe52f89-congealing.jpg` |
| [`aardvark`](cases/aardvark.md) | Evidence stays attached to the event it explains. | Flat | counterfactual | `assets/calibration/af521a16-aardvark.jpg` |
