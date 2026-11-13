# Clarity and cinematic flow

Two public pages set the standard for this guide. Open them when you have network access. Take the method. Do not copy the look.

- **Clarity:** OpenAI, [Work at the Frontier: AI's effect on freelance work](https://openai.com/index/ai-effect-on-freelance-work/).
- **Cinematic flow:** Anthropic, [Scenarios for our Economic Future](https://www.anthropic.com/institute/econ-scenarios).

## Clarity: the reader must not work

What the first page does, and the rule that follows.

| The page does this | Your rule |
|---|---|
| Each section heading is the finding: "Freelance demand is shifting as AI use grows". | The title of a figure or a panel is the claim, as a sentence. It is not the topic. |
| Below each chart title is one line that tells the reader how to read the chart: "Each dot represents one work category." | Give each panel one decode line: what one mark is, and what position or colour means. |
| Values sit on the bars. The legend is two words at the top. | Label directly. Do not send the eye to a distant legend. |
| Two colours in the full article. Blue is one platform and green is the other, each time. | One colour, one meaning, in the full document. |
| The quadrants of the scatter plot contain their own reading: "Higher use, lost share · 22 categories · 34.9%". | Write the interpretation in the region where it applies. |
| One comparison stands alone as two large numbers with an arrow: 14.6 → 21.2. | Isolate the one fact that matters most. Give it space. |
| Method details are below the chart, small, and can collapse. | Keep caveats near, but out of the reading path. |
| Generous white space. One card for one figure. | One idea for one frame. |

Apply these rules to 3D figures also. A 3D panel needs its claim title and its decode line more than a chart does, because the reader does not know the convention.

**The clarity test.** Give the figure to a reader for five seconds. Ask what it claims. If the answer is a topic ("it is about attention") and not a relation ("each head routes one token to another"), the figure is not clear.

## Cinematic flow: one stage, one change for each beat

What the second page does, and the rule that follows.

| The page does this | Your rule |
|---|---|
| It starts with one nurse and her tasks, not with the economy. | Start with **one concrete instance** that the reader knows. |
| The task tiles stay on screen through the full sequence. They change colour, leave, arrive and multiply. | Keep **one persistent stage**. Objects persist and transform. Do not cut to a new picture when you can transform the current one. |
| Each scroll step changes one thing and shows one short card: a bold line and two sentences. | **One beat, one change, one card.** If a beat needs two changes, make two beats. |
| The tiles are neutral until the text names the categories. Then colour arrives. | **Colour arrives with its meaning.** Do not show an encoding before you explain it. |
| One nurse becomes millions of instances. The tiles assemble into the whole economy. | **Pull back**: from the instance to the population, with the same marks. |
| Three scenarios appear in the same frame and the same scale. | Compare outcomes in a **fixed frame**. |
| At the end, the reader sets the parameters. | When the reader has the model, **give the reader the controls**. |

### The beat sequence

Use this sequence for an explainer, a talk, a scroll page, or the panels of a figure.

1. **Establish.** The object, alone, grey, in its resting state. One label.
2. **Introduce the cast.** Name the persistent object. It gets its colour now.
3. **Operate.** The operation occurs. One thing moves, cuts, folds or flows. This is the longest beat.
4. **Consequence.** The result of the operation, in the same frame.
5. **Counterfactual.** Remove or change the operation. The consequence changes. This beat proves the mechanism.
6. **Pull back.** From one instance to many: the lattice, the population, the full system.
7. **Hand over** (interactive only). The reader changes a parameter.

A static figure is the same sequence, compressed. Panel a is beats 1 to 3. Panel b is beats 4 and 5. Panel c is beat 6. Most weak figures have beat 6 only.

### Beats on the stage

A figure module can export `beats`. The renderer builds one frame for each beat with an identical camera, and it writes a scroll page with a sticky stage and caption cards.

```js
export const view = {width: 180, height: 96, azim: -84, elev: 20,
  frame: {center: [4.2, 0, 1], size: [10.6, 2.2, 2.2]}};      // the frame fixes the camera for all beats
export const beats = [
  'A helix winds round a cylinder|Its slope looks different at each point of the view.',
  'Cut the cylinder and unroll it|The cut edge keeps its colour.',
  'The helix becomes a straight line|One turn covers 2πr and rises by the pitch.',
];
export default function build(S, THREE, beat) {
  // draw the objects of beat 0 always; add objects when beat >= 1, beat >= 2, ...
}
```

`node scripts/render.mjs figure.mjs --out out` writes `figure-beat1.png`, `figure-beat2.png`, and so on, and `figure-story.html`. Look at each frame. Then look at adjacent frames in sequence: only the planned change must differ.

Rules for beats:

- Set `view.frame`. Without it, the camera fits each beat to its own content, and the picture jumps.
- An object that exists in two beats has the same position, size and colour in the two beats, unless that change is the beat.
- A card has a bold line of at most eight words and a body of at most two sentences.
- Three to seven beats. More beats mean that the mechanism sentence is two mechanisms.
- The last frame must work alone, because readers share it as the static figure.
