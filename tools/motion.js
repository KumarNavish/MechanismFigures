/* MechanismFigures: authored, seekable editorial motion. No model, fake job or scoring. */
(() => {
  'use strict';
  const root = document.getElementById('how-it-works');
  if (!root) return;
  const shell = root.querySelector('.motion-shell');
  const scenes = [...root.querySelectorAll('[data-scene]')];
  const entries = scenes.map(scene => [...scene.querySelectorAll('[data-enter]')]);
  const starts = [0, 7, 16, 29, 39, 47];
  const duration = 60;
  const narratives = [
    ['Begin with a question, not a chart.', 'The agent extracts one defensible relationship from your context, mechanism, evidence and output constraints.'],
    ['Read the actual references.', 'Two published figures calibrate the visual operation and its composition. The agent records what it sees—not what it remembers.'],
    ['Give the mechanism a visible form.', 'Follow the same object from state to observation to feedback. Every position, frame and arrow must mean something scientifically true.'],
    ['Critique the picture. Return to the evidence.', 'Test the mechanism, the captionless prediction and the actual-size render. An ambiguous relation triggers a revision—not a better-sounding score.'],
    ['Deliver the figure and the reason to trust it.', 'The handoff includes editable geometry, a print-size preview, a scoped caption, reproducible evidence and a review bound to those exact files.'],
    ['One skill. Different scientific worlds.', 'These published examples show the caliber and variety of constructions the skill teaches—not outputs it has generated.']
  ];
  const traces = [
    {rect:[0.2,39.8,31.2,57.4], title:'Find the state that can change.', body:'The trainable 3D representation is the object being optimized.'},
    {rect:[27.1,1.5,39.4,74.3], title:'Carry its identity into an observation.', body:'The same object acquires shading and becomes a camera rendering.'},
    {rect:[68.1,1.2,31.3,57.8], title:'Separate the fixed evaluator from the mutable object.', body:'The frozen diffusion model supplies a signal; it is not the state being trained.'},
    {rect:[26.2,73.6,56.1,24.6], title:'Return the update to the object it changes.', body:'The feedback reaches the NeRF parameters. The loop is an operation, not decoration.'}
  ];
  const worlds = [
    {id:'graphcast',title:'Keep the physical world visible.',lesson:'Let the natural geometry carry the computation.',credit:'GraphCast · Lam et al. · Science 2023'},
    {id:'cellrank',title:'Let a local state acquire a future.',lesson:'Connect a local transition rule to global fate estimates.',credit:'CellRank · Lange et al. · Nature Methods 2022'},
    {id:'alphafold',title:'Make the mathematics spatial.',lesson:'Turn indexed relations into inspectable geometric operations.',credit:'AlphaFold · Jumper et al. · Nature 2021'},
    {id:'congealing',title:'Keep identity through change.',lesson:'A transported edit makes semantic correspondence visible.',credit:'Neural Congealing · Ofri-Amar et al. · CVPR 2023'}
  ];
  const el = id => document.getElementById(id);
  const media = matchMedia('(prefers-reduced-motion: reduce)');
  const state = {time:0, playing:false, started:false, ready:false, reduced:media.matches, visible:false, scene:0, world:0, manualWorld:null, ended:false, reason:'poster'};
  let frame = 0, previousTimestamp = null, drawnScene = -1, drawnTrace = -1, drawnWorld = -1, previousWorld = 0, worldChangedAt = 47, destroyed = false;
  const clamp = (v,lo=0,hi=1) => Math.max(lo, Math.min(hi,v));
  const ease = t => 1 - Math.pow(1-clamp(t),4);
  const mix = (a,b,t) => a + (b-a)*t;
  const sceneAt = time => {let n=0;for(let i=0;i<starts.length;i++) if(time>=starts[i]) n=i;return n;};
  const timeLabel = time => Math.floor(time/60)+':'+String(Math.floor(time%60)).padStart(2,'0');
  function status() {
    shell.dataset.playing = String(state.playing);
    shell.dataset.reduced = String(state.reduced);
    shell.dataset.sceneIndex = String(state.scene);
    shell.dataset.time = state.time.toFixed(3);
    const label = state.reduced ? 'Next step' : state.playing ? 'Pause' : state.ended ? 'Replay' : 'Play';
    el('motion-play-text').textContent = label;
    el('motion-play').setAttribute('aria-label', label + ' walkthrough');
    el('motion-play').querySelector('.play-symbol').textContent = state.reduced ? '→' : state.playing ? 'Ⅱ' : '▶';
    el('motion-mode').setAttribute('aria-pressed',String(state.reduced));
    el('motion-mode').textContent = state.reduced ? 'Motion off' : 'Reduced motion';
    el('motion-seek').value = state.time;
    el('motion-seek').setAttribute('aria-valuetext',Math.round(state.time)+' seconds of 60; '+narratives[state.scene][0]);
    el('motion-time').textContent = timeLabel(state.time);
  }
  function render(time, forceStatic=false) {
    state.time=clamp(Number(time)||0,0,duration);
    state.scene=sceneAt(state.time);
    const instant=state.reduced||forceStatic;
    scenes.forEach((scene,i)=>{
      const start=starts[i],end=starts[i+1]??duration+1;
      let opacity=instant?(i===state.scene?1:0):(i===0?1:ease((state.time-start)/0.72))*(1-ease((state.time-end)/0.62));
      if(state.time<start)opacity=0;
      const active=opacity>0.001;
      scene.style.opacity=opacity;
      scene.style.visibility=active?'visible':'hidden';
      scene.style.pointerEvents=i===state.scene?'auto':'none';
      scene.style.transform=instant?'none':'translate3d(0,'+((1-opacity)*(state.time>=end?-14:15)).toFixed(2)+'px,0)';
      scene.setAttribute('aria-hidden',String(i!==state.scene));
      scene.inert=i!==state.scene;
      if(!active)return;
      const local=instant?15:state.time-start;
      for(const node of entries[i]){
        const p=instant?1:ease((local-Number(node.dataset.enter))/1.1);
        node.style.opacity=p;
        node.style.transform='translate3d(0,'+((1-p)*23).toFixed(2)+'px,0)';
      }
      if(i===0){
        const join=instant?1:ease((local-2.4)/3.0);
        const paper=root.querySelector('.intake-paper');
        paper.style.transform='translate3d('+mix(20,0,join).toFixed(2)+'px,'+mix(15,0,join).toFixed(2)+'px,0) rotate('+mix(-5,-2,join).toFixed(2)+'deg)';
        for(const [j,slip] of [...root.querySelectorAll('.input-slip')].entries()){
          const p=instant?1:ease((local-.3-j*.5)/1.1);
          slip.style.transform='translate3d('+((1-p)*-18).toFixed(2)+'px,0,0)';
        }
      }
      if(i===1){
        const pair=[...root.querySelectorAll('.calibration-sheet')];
        for(let j=0;j<pair.length;j++){
          const p=instant?1:ease((local-.1-j*.7)/1.5);
          pair[j].style.transform='translate3d('+((1-p)*(j?48:-48)).toFixed(2)+'px,'+((1-p)*14).toFixed(2)+'px,0) rotate('+((1-p)*(j?2.4:-2.4)).toFixed(2)+'deg)';
        }
      }
    });
    if(drawnScene!==state.scene){
      drawnScene=state.scene;
      el('motion-step-count').textContent=String(state.scene+1).padStart(2,'0')+' / 06';
      el('motion-narration-index').textContent=String(state.scene+1).padStart(2,'0');
      el('motion-narration-title').textContent=narratives[state.scene][0];
      el('motion-narration-body').textContent=narratives[state.scene][1];
      root.querySelectorAll('[data-chapter]').forEach(b=>{if(Number(b.dataset.chapter)===state.scene)b.setAttribute('aria-current','step');else b.removeAttribute('aria-current');});
    }
    if(state.scene===2){
      const local=state.time-16,segment=3.15;
      const index=Math.min(3,Math.floor(local/segment));
      const p=instant?1:ease((local-index*segment)/.8);
      const from=traces[Math.max(0,index-1)].rect,to=traces[index].rect;
      const box=el('motion-focus');
      ['left','top','width','height'].forEach((key,j)=>box.style[key]=mix(from[j],to[j],p).toFixed(3)+'%');
      box.style.opacity=instant?1:ease(local/.8);
      if(drawnTrace!==index){
        drawnTrace=index;
        el('trace-number').textContent=String(index+1).padStart(2,'0');
        el('trace-title').textContent=traces[index].title;
        el('trace-body').textContent=traces[index].body;
      }
      root.querySelector('.trace-caption').style.transform=instant?'none':'translate3d(0,'+((1-p)*8).toFixed(2)+'px,0)';
    }
    if(state.scene===5){
      const world=state.manualWorld??Math.min(3,Math.floor((state.time-47)/3.25));
      state.world=world;
      if(drawnWorld!==world){
        previousWorld=drawnWorld<0?world:drawnWorld;
        drawnWorld=world;worldChangedAt=state.time;
        el('world-title').textContent=worlds[world].title;
        el('world-lesson').textContent=worlds[world].lesson;
        el('world-credit').textContent=worlds[world].credit;
        el('world-link').href='gallery.html#'+worlds[world].id;
        root.querySelectorAll('[data-world-select]').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.worldSelect)===world)));
      }
      const blend=instant||!state.playing?1:ease((state.time-worldChangedAt)/.7);
      root.querySelectorAll('[data-world]').forEach((img,j)=>{
        img.style.opacity=j===world?blend:j===previousWorld?1-blend:0;
        img.style.transform=instant?'none':'translate3d('+((j===world?1-blend:0)*12).toFixed(2)+'px,0,0)';
        img.setAttribute('aria-hidden',String(j!==world));
      });
    }
    status();
  }
  function pause(reason='user') {
    state.playing=false;state.reason=reason;previousTimestamp=null;
    if(frame)cancelAnimationFrame(frame);frame=0;status();
  }
  function tick(now){
    frame=0;if(!state.playing||destroyed)return;
    if(previousTimestamp===null)previousTimestamp=now;
    const delta=Math.min((now-previousTimestamp)/1000,.2);previousTimestamp=now;
    render(state.time+delta);
    if(state.time>=duration){state.ended=true;pause('ended');render(duration,true);return;}
    frame=requestAnimationFrame(tick);
  }
  function play(){
    if(!state.ready||destroyed)return;
    if(state.reduced){goChapter((state.scene+1)%6);return;}
    if(state.ended){state.time=0;state.ended=false;state.manualWorld=null;}
    state.started=true;state.playing=true;state.reason='playing';previousTimestamp=null;
    render(state.time);if(!frame)frame=requestAnimationFrame(tick);status();
  }
  function seek(value){pause('seek');state.started=true;state.ended=Number(value)>=duration;state.manualWorld=null;render(value,state.reduced);}
  function goChapter(index){const n=Math.max(0,Math.min(5,Number(index)));pause('chapter');state.started=true;state.ended=false;state.manualWorld=null;render(starts[n]+[4.5,6.7,1.0,7.2,5.3,1.0][n],true);}
  function setReduced(value){pause('motion preference');state.reduced=Boolean(value);render(state.time,true);}
  function replay(){pause('replay');state.time=0;state.ended=false;state.manualWorld=null;state.started=true;render(0,state.reduced);if(!state.reduced)play();}
  el('motion-play').addEventListener('click',()=>state.playing?pause():play());
  el('motion-replay').addEventListener('click',replay);
  el('motion-seek').addEventListener('input',e=>seek(e.target.value));
  el('motion-mode').addEventListener('click',()=>setReduced(!state.reduced));
  root.querySelectorAll('[data-chapter]').forEach(b=>b.addEventListener('click',()=>goChapter(b.dataset.chapter)));
  root.querySelectorAll('[data-world-select]').forEach(b=>b.addEventListener('click',()=>{
    pause('reference selection');state.started=true;state.manualWorld=Number(b.dataset.worldSelect);state.ended=false;render(48,true);
  }));
  root.querySelectorAll('a,summary').forEach(a=>a.addEventListener('click',()=>pause('inspection')));
  shell.addEventListener('keydown',e=>{
    if(e.target!==shell)return;
    if(e.code==='Space'){e.preventDefault();state.playing?pause():play();}
    else if(e.key==='ArrowRight'){e.preventDefault();seek(state.time+5);}
    else if(e.key==='ArrowLeft'){e.preventDefault();seek(state.time-5);}
    else if(e.key==='Home'){e.preventDefault();seek(0);}
    else if(e.key==='End'){e.preventDefault();seek(duration);}
  });
  document.addEventListener('visibilitychange',()=>{if(document.hidden)pause('hidden');});
  media.addEventListener('change',e=>setReduced(e.matches));
  const referenceViewer=document.getElementById('viewer');
  if(referenceViewer)new MutationObserver(()=>{if(referenceViewer.open)pause('reference viewer');}).observe(referenceViewer,{attributes:true,attributeFilter:['open']});
  const allowAutoplay=!new URLSearchParams(location.search).has('paused');
  const observer=new IntersectionObserver(entries=>{
    state.visible=entries[0].isIntersecting&&entries[0].intersectionRatio>=.25;
    if(!state.visible&&state.playing)pause('offscreen');
    else if(state.visible&&state.ready&&!state.started&&!state.reduced&&allowAutoplay)play();
  },{threshold:[0,.25,.45]});
  observer.observe(shell);
  window.addEventListener('pagehide',()=>{pause('pagehide');});
  render(0,true);
  Promise.all([...root.querySelectorAll('img')].map(img=>img.decode().catch(()=>null))).then(()=>{
    state.ready=true;
    const broken=[...root.querySelectorAll('img')].some(img=>!img.naturalWidth);
    shell.dataset.assetsReady=String(!broken);
    if(broken){pause('image unavailable');el('motion-play').disabled=true;el('motion-play-text').textContent='Image unavailable';return;}
    if(state.visible&&!state.started&&!state.reduced&&allowAutoplay)play();
  });
  // Small deterministic inspection interface; it never executes scientific work.
  window.MechanismMotion=Object.freeze({play,pause,seek,chapter:goChapter,replay,setReduced,duration,
    getState:()=>({...state}),
    timeline:()=>starts.map((t,i)=>({start:t,end:starts[i+1]??duration,title:narratives[i][0]}))});
})();
