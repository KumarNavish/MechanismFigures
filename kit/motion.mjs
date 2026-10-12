/** Deterministic presentation time. A project's pure stateAt(t) owns the science. */
export function follow(value, target, seconds, rate = 8) {
  if (![value, target, seconds, rate].every(Number.isFinite) || seconds < 0 || rate < 0) throw new TypeError('Finite values and nonnegative time/rate required');
  return target + (value - target) * Math.exp(-rate * seconds);
}

export function createPlayback({duration, stateAt, draw, element, autoplay = false}) {
  if (!Number.isFinite(duration) || duration <= 0 || typeof stateAt !== 'function' || typeof draw !== 'function' || !element) throw new TypeError('Duration, pure state function, renderer and observed element required');
  const media = matchMedia('(prefers-reduced-motion: reduce)');
  let t = 0, playing = false, raf = 0, last = null, disposed = false, started = false;
  const render = () => draw(stateAt(t), {time: t, reducedMotion: media.matches});
  const pause = () => {playing = false; last = null; cancelAnimationFrame(raf); raf = 0;};
  function tick(now) {
    if (!playing || disposed) return;
    if (last !== null) t = Math.min(duration, t + Math.max(0, (now-last)/1000));
    last = now; render();
    if (t >= duration) pause(); else raf = requestAnimationFrame(tick);
  }
  function play() {
    if (disposed || media.matches || document.hidden) return;
    if (t === duration) t = 0;
    if (!playing) {playing = true; started = true; last = null; raf = requestAnimationFrame(tick);}
  }
  function seek(seconds) {
    if (!Number.isFinite(seconds)) throw new TypeError('Finite time required');
    pause(); t = Math.min(duration, Math.max(0,seconds)); if (!disposed) render();
  }
  const changed = () => {if (media.matches) pause(); render();};
  const hidden = () => {if (document.hidden) pause();};
  const observer = new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) pause();
    else if (autoplay && !started) play();
  });
  media.addEventListener('change', changed); document.addEventListener('visibilitychange', hidden); observer.observe(element); render();
  return Object.freeze({play,pause,seek,getState:()=>({time:t,playing,reducedMotion:media.matches}),
    dispose(){pause();disposed=true;observer.disconnect();media.removeEventListener('change',changed);document.removeEventListener('visibilitychange',hidden);}});
}
