// Starting template and API demonstration. It is NOT a quality reference: study the atlas for quality.
// Mechanism sentence: a helix has a constant slope because it is a straight line on the unrolled cylinder.
// Moves: ghost and focus, unroll pair, beats. Geometry status: derived from the equation of a helix.
export const view = {width: 180, height: 96, azim: -84, elev: 20, margin: 12, frame: {center: [4.2, 0, 1], size: [10.6, 2.2, 2.2]}};
// One beat adds one idea. Text before "|" is the card title; text after it is the card body.
export const beats = [
  'A helix winds round a cylinder|Its slope looks different at each point of the view.',
  'Cut the cylinder and unroll it|The cut edge keeps its colour, so the eye can follow the surface.',
  'The helix becomes a straight line|One turn covers the circumference 2πr and rises by the pitch p.',
];
const R = 1, PITCH = 1, TURNS = 2, H = PITCH * TURNS;

export default function build(S, THREE, beat) {
  const P = S.palette;
  const helix = n => Array.from({length: n + 1}, (_, i) => { const t = i / n * TURNS * 2 * Math.PI; return [R * Math.cos(t), R * Math.sin(t), PITCH * t / (2 * Math.PI)]; });
  // The persistent object: the helix. It keeps one colour in every beat.
  S.cyl([0, 0, 0], [0, 0, H], R, {color: P.context, opacity: 0.28, id: 'cylinder'});
  S.tube(helix(160), {radius: 0.045, color: P.act, id: 'helix'});
  S.curve([[R, 0, 0], [R, 0, H]], {color: P.focus, width: 0.6});                       // the cut line
  S.label([0, -R, 0.75 * PITCH], 'helix', {dx: -16, dy: 4});
  if (beat >= 1) {
    const x0 = 2.4, W = 2 * Math.PI * R;                                                // the unrolled sheet, to scale
    const sheet = S.box([x0 + W / 2, 0, H / 2], [W, 0.02, H], {color: beat >= 2 ? P.quiet : P.context, id: 'sheet'});
    S.curve([[x0, -0.02, 0], [x0, -0.02, H]], {color: P.focus, width: 0.6});
    S.curve([[x0 + W, -0.02, 0], [x0 + W, -0.02, H]], {color: P.focus, width: 0.6});
    S.link([R, 0, H * 0.55], [x0, 0, H * 0.55], {text: 'unroll', bend: -0.18, dash: '1 1'});
    S.label([x0, 0, H], 'cut edge', {dx: 3, dy: -7, color: P.focus});
    if (beat >= 2) {
      for (let k = 0; k < TURNS; k++) S.tube([[x0, -0.03, k * PITCH], [x0 + W, -0.03, (k + 1) * PITCH]], {radius: 0.035, color: P.act, shadow: false});
      S.label([x0 + W / 2, 0, 0], '2πr', {dx: 0, dy: 5, leader: false, italic: true});
      S.label([x0 + W, 0, PITCH / 2], 'pitch p', {dx: 6, dy: 0, leader: false, italic: true});
    }
  }
}
