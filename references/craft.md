# Craft

These rules make a 3D figure clear at the first look. Read them before the blockout pass.

## Camera

- **Orthographic.** The stage default. It keeps parallel lines parallel. It makes side-by-side copies identical in view.
- **Three-quarter view.** Start with `azim: -50, elev: 28`. Keep the elevation between 18 and 40 degrees. Below 15 degrees, the top faces disappear and layers merge. Above 50 degrees, the height disappears.
- **Turn the operation to the viewer.** The axis of motion, the cut face or the direction of flow must lie near the image plane. Depth compresses what points at the camera.
- **Break alignments.** If two edges that are not related line up in the image, the reader sees one object. Change the azimuth by 5 to 10 degrees.
- **Reading direction.** The process goes from left to right or from top to bottom. Put the cause at the left.
- **One camera for each comparison.** Do not rotate between states.
- **Fill the frame.** The object uses 60 to 80 percent of the area. Labels use the remainder. Use `zoom` and `shift` to adjust.

## Depth cues

The reader gets depth from these cues, in this order of strength. Use the first three always.

1. **Occlusion.** Near parts cover far parts. Arrange the scene so that the important overlaps occur.
2. **Contact shadow.** A soft shadow on the ground tells the reader that a part rests or floats. An exploded part with no shadow link looks like an error.
3. **Shading.** One key light from the upper left of the view. The stage sets it. Do not add coloured lights.
4. **Outline.** A dark thin line on silhouettes and creases separates parts that have the same tone.
5. **Tone with distance.** Make far context lighter. Use this only for context.

Do not use fog, depth of field, reflections, gloss, textures or gradients on the background. They are decoration, and they lower contrast where the mechanism is.

## Material and colour

- Materials are matte. Roughness 0.7, no metal. A shiny highlight looks like a data value.
- **Grey is context.** `palette.context` and `palette.quiet`.
- **One colour is the persistent object. One colour is the operation or intervention.** `palette.focus` (blue) and `palette.act` (orange) are a pair that stays distinct in grayscale and for colour-blind readers. Add a third colour only for a third entry in your cast list.
- A colour keeps its meaning in all panels and in the caption.
- A scalar field gets one ramp: `viridis` for magnitude, `diverging` when zero has a meaning. Show the ramp with units.
- Important differences must stay visible in the grayscale copy. Add a second cue: solid against dashed, filled against outline, a direct label.
- A ghost is 15 to 30 percent opaque. Do not overlap more than two ghosts.

## Labels

- A label names a visible thing and sits adjacent to it. If the label is not adjacent, use a thin leader with a dot on the thing.
- The anchor must be on a visible point. The report tells you when another object hides it.
- Leaders are short and straight. They do not cross each other. They do not cross the operation.
- Put labels in empty space, not on shaded surfaces.
- **Name the change, not the part.** "same centre, larger support" is better than "our method".
- 8 pt for labels, 7 pt for secondary text, 10 to 11 pt bold for panel letters. No text below 6.5 pt at print size. Do not shrink text to make it fit: remove words or move the object.
- One font family. Italic for variables. Sentence case.
- Use few labels. Five to nine in one panel is the usual limit. If you need more, the panel has too many parts.

## Composition

- **One entry point.** Squint. The operation must be the first thing that you see: the strongest colour, the highest contrast, the most space.
- **Three eye actions.** Write them with verbs that can be seen: *find* the ray, *follow* it through the grid, *compare* the two samples. Put the labels where each action occurs.
- **Whitespace is structure.** Leave empty space round the operation. Do not fill empty areas with logos, icons or frames.
- **No frames, no rounded boxes round panels, no background tints.** Alignment and space make the groups.
- **A 3D view with a flat partner.** When the reader must read a quantity, put a flat plot or map adjacent to the 3D view. Link them with a shared colour and a shared mark.
- **Panels answer different questions.** Mechanism, consequence, limit. Remove a panel that repeats the text.
- Align the edges of panels and the baselines of state names. Use equal gaps.

## Scale and exaggeration

- Use real proportions when you have them.
- If a thin layer, a small angle or a small displacement must be larger to be visible, write the factor on the figure: "thickness ×20".
- Each quantity axis in a block diagram or a state space has a name and a unit.
- A scale bar is better than a number in the caption.

## Arrows

| Arrow | Meaning | Stage call |
|---|---|---|
| Solid 3D arrow | A physical vector: force, velocity, field, ray direction | `S.arrow` |
| Tube or line with a head | A path through space or state space | `S.tube`, `S.curve` |
| Flat overlay arrow | Narrative: then, becomes, maps to | `S.link` |
| Dashed line | A tether, a correspondence, or an inferred relation | `S.explode`, `S.curve({dash})` |

Do not use one arrow style for two meanings. Do not draw an arrow that has no source object and no target object.

## Print check

Set `width` and `height` to the final size in millimetres before you build: 89 mm for one journal column, 180 mm for two columns. The detail tiles show the figure at a higher zoom. All text and all joins must be clean in the tiles.
