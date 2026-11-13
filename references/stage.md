# The stage

The stage is a small studio for 3D mechanism figures. It uses three.js r170, which is in `kit/vendor`. It gives you an orthographic camera, a z-up world, one key light, soft contact shadows, dark outlines, capped cuts, exploded parts and vector labels.

## Run

```bash
node scripts/render.mjs figure.mjs --out out
```

Use the absolute path of `scripts/render.mjs` in the installed skill. The command needs Node 22 or later and an installed Chrome or Chromium. Set `CHROME_PATH` if the browser is in a different location. The command uses no network.

| Output | Use |
|---|---|
| `figure.png` | The figure at 4 times screen resolution. Open it after each render. |
| `figure.svg` | The 3D raster with the labels as editable vector text. This is the file for the paper. |
| `figure-detail-R-C.png` | Four tiles at twice the zoom. Check joins, outlines and text. Open them after pass C and after the last repair. |
| `figure-gray.png` | Grayscale copy. Check the entry point and the colour-free distinctions. |
| `figure.report.json` | Warnings: hidden label anchors, text out of the frame, small text, text collisions. |

Options: `--scale 4` sets the pixel density. `--tiles 2` sets the number of detail tiles on each side. The command also accepts a finished `.svg` or `.html` file and gives the PNG, tile and grayscale outputs for it.

To start, copy `kit/template.mjs`.

## The figure module

```js
export const view = {width: 180, height: 100, azim: -50, elev: 28};
export default function build(S, THREE, beat) { /* add objects */ }
```

`view` options:

| Option | Default | Meaning |
|---|---|---|
| `width`, `height` | 180, 110 | Final size in millimetres |
| `azim`, `elev` | -50, 28 | Camera angles in degrees. The z-axis is up. At `azim: -90` the camera is on the −y side, and +x points to the right of the page. At the default −50, +x goes right and toward the viewer, and +y goes right and away. |
| `zoom`, `shift` | 1, [0, 0] | Scale of the fitted scene, and an offset in millimetres |
| `margin` | 8 | Space for labels round the fitted scene, in millimetres. The camera fits the objects and not the labels. If the report says that text leaves the frame, increase `margin` or move the label. |
| `frame` | none | `{center, size}` in world units. Fixes the camera. Necessary for beats. |
| `fov` | 0 | A value above 0 gives a perspective camera. Use it only for a scene that a camera sees. |
| `ground` | true | `false` removes the shadow ground. A number sets its height. |
| `shadow` | 0.13 | Opacity of the contact shadow |
| `edgeWidth` | 0.28 | Outline width in millimetres |
| `minFont` | 6.5 | The report warns below this size, in points |

The camera fits all objects automatically. You do not set a position.

## Objects

All calls return a three.js object. You can set `position`, `rotation` and `scale`, or add the object to a `THREE.Group`. three.js primitives have their axis on y. `S.cyl` and `S.arrow` take two points, thus you do not have to rotate them.

| Call | Makes |
|---|---|
| `S.solid(geometry, opts)` | A mesh from any three.js geometry with the house look |
| `S.box(center, [sx, sy, sz], opts)` | A box |
| `S.sphere(center, r, opts)` | A sphere |
| `S.cyl(a, b, r, opts)` | A cylinder from point `a` to point `b`. `r2` gives a cone. `open: true` removes the caps. |
| `S.tube(points, opts)` | A smooth tube through points. `radius`, `closed`. |
| `S.surface(f, opts)` | A parametric surface. `f(u, v)` returns `[x, y, z]`, with `u` and `v` from 0 to 1. `value(u, v, p)`, `range` and `ramp` paint a field. `nu`, `nv` set the resolution. |
| `S.plane(point, normal, [w, h], opts)` | A translucent reference plane |
| `S.arrow(a, b, opts)` | A solid 3D arrow. `radius`, `head`. |
| `S.curve(points, opts)` | A line of constant width on the page. `width` in millimetres. `dash` in world units. |

Options for solids: `color`, `opacity` (below 1 gives a ghost), `edges` (crease lines), `outline` (silhouette), `flat`, `roughness`, `side`, `id` (the name in the report), `parent`, `shadow` and `receive`.

**Shadows and data.** A shadow on a cell or a field changes its tone, and the reader takes the tone for a value. `shadow: false` gives a part no shadow and lets no shadow fall on it. `receive: false` lets the part cast a shadow on the ground but keeps its own faces clean. Use `receive: false` for grids of cells, stacked slabs and all surfaces whose colour is data. `S.surface` with `value` does this automatically.

## Operations

| Call | Does |
|---|---|
| `S.cut(objects, point, normal, {cap})` | Removes the side to which `normal` points and caps the section. `cap` is a colour. `cap: false` is for thin open shells. Call it two times for a quarter cut. |
| `S.explode(object, offset)` | Moves a part and draws a dashed tether to its home position |
| `S.right(d)`, `S.up(d)`, `S.toward(d)` | World vectors along screen right, screen up and toward the viewer. Use `S.right` to put states side by side with an identical view. |

## Words and overlay

Labels are vector text on top of the render. Sizes are in points. Offsets are in millimetres on the page, with y down.

| Call | Does |
|---|---|
| `S.label(point, text, {dx, dy, size, leader, color, weight, italic, align})` | Text with a leader to a 3D anchor. A negative `dx` puts the text at the left of the anchor and aligns it to the right. `leader: false` puts text near a point with no line. `\n` makes a new line. |
| `S.text(x, y, text, opts)` | Text at a page position in millimetres: panel letters, claim titles |
| `S.link(from, to, {text, bend, dash, color})` | A flat overlay arrow. Each end is a 3D point or `[x, y]` in millimetres. `bend` curves it, and the text sits at the middle of the curve. Do not let it cross the objects that it joins. Use it for narrative only. |

## Colour

`S.palette` has `ink`, `line`, `context`, `quiet`, `focus`, `act`, `good`, `warn`, `violet` and `gold`. Import `ramps` and `ramp` from `'mf'` for fields: `ramps.viridis`, `ramps.magma`, `ramps.diverging`.

## Beats

Export `beats`, an array of card texts, and read the third argument of `build`. See [story.md](story.md).

## Full three.js

`THREE` is the full library. Use `ExtrudeGeometry`, `LatheGeometry`, `TorusKnotGeometry`, `BufferGeometry` with your own vertices, or `InstancedMesh` for many copies. Pass the geometry to `S.solid` to get the house look. In a figure module, `import {ramp, ramps, palette} from 'mf'` and `import * as THREE from 'three'` work.

To load real data, put a JSON file adjacent to the figure module and read it with `await (await fetch('/fig/data.json')).json()`. `build` can be an `async` function.

## Limits

- The output is a raster with vector labels. The 3D geometry is not vector.
- Transparent objects sort by their centres. Many overlapping ghosts can sort in the wrong sequence.
- A cap needs a closed mesh. For an open shell, use `cap: false`.
- The silhouette outline is correct for an orthographic camera.
- The report does not judge the figure. You must look.

## Other renderers

Use the renderer of the project when the geometry comes from it: PyMOL or ChimeraX for molecules, ParaView for fields, Blender for complex scenes, the simulation's own viewer. Export a PNG with a transparent or white background and an orthographic camera. Then add labels in SVG, and run `node scripts/render.mjs figure.svg` to get the detail tiles and the grayscale copy. All rules in this skill apply.
