# Motion walkthrough

The gallery now contains an authored, 60-second explanation and a standalone `skills/mechanism-figures/assets/motion.html`. It is editorial motion, not an agent execution, research experiment, or generated-output claim.

## Narrative

0–7 s: four input categories become one scientific question.
7–16 s: DreamFusion and AlphaFold demonstrate actual image inspection and the extraction of a visual operation.
16–29 s: attention follows the unchanged DreamFusion figure through mutable state, rendering, frozen evaluator, and return update.
29–39 s: concrete questions inspect scientific meaning and final-size clarity; the threshold is labeled policy, never a live score.
39–47 s: the required deliverable set appears beside the published reference: vector, preview, caption, code/evidence, and version-bound review.
47–60 s: GraphCast, CellRank, AlphaFold and Neural Congealing illustrate the reference-quality target across different scientific constructions. Their publication credits and not-generated-by-the-skill boundary remain visible.

## Image integrity

Every scientific image is an existing approved calibration asset, byte-checked by the builder. The motion uses six image files (five publications, including a full/focused AlphaFold pair) and adds no scientific image to the 20-reference / 29-asset canon. Native text and moving frames are editorial annotations; they do not alter source pixels, fabricate measurements, or demonstrate causal validation. Full provenance is in `assets/motion-story.json` and `THIRD_PARTY.md` within the skill.

## Interaction

Play/pause, replay, a continuous seek slider, six jump-to-chapter controls, and manually selectable final references. Space plays/pauses and arrow keys seek when the player itself is focused; native controls keep their normal keyboard behavior. Autoplay happens once when visible, not indefinitely. Hidden tabs, offscreen players, source inspection and explicit pause suspend playback; it never claims to keep scientific work running.

Reduced-motion preference disables autoplay and interpolated movement. The user can step through chapters instantly; a text transcript provides the full narrative without motion. The optional motion toggle can explicitly reenable full motion. The website does not use audio, a model, paid APIs, analytics, external scripts, remote fonts, or third-party image hotlinks. The storyboard is implemented by time-sampled transforms rather than uncontrolled CSS loops.

## Maintenance

Edit `tools/motion.html`, `tools/motion.css`, `tools/motion.js`, and `tools/build_motion.py`. `python3 tools/build_gallery.py` regenerates both public pages and the image-provenance manifest. Do not edit generated output alone. The existing gallery remains fully readable without JavaScript; the motion's text transcript also remains available.

This demonstration does not replace cross-agent evaluation or independent scientific/visual review. It explains the skill's process and intended quality target.
