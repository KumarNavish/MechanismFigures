"use strict";
const cards=[...document.querySelectorAll('article')],chips=[...document.querySelectorAll('.chips button')],count=document.getElementById('count');
function filter(m){let n=0;for(const a of cards){const on=m==='all'||(m==='3d'?a.dataset.dim!=='flat':a.dataset.moves.split(' ').includes(m));a.hidden=!on;n+=on;}
chips.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.move===m)));count.textContent=n+' of '+cards.length+' figures';}
chips.forEach(b=>b.addEventListener('click',()=>{filter(b.dataset.move);history.replaceState(null,'',b.dataset.move==='all'?location.pathname:'?move='+b.dataset.move);}));
filter(new URLSearchParams(location.search).get('move')||'all');
const viewer=document.getElementById('viewer'),big=document.getElementById('big');
document.querySelectorAll('[data-src]').forEach(b=>b.addEventListener('click',()=>{big.src=b.dataset.src;big.alt=b.dataset.cap;big.className='';document.getElementById('cap').textContent=b.dataset.cap;viewer.showModal();}));
big.addEventListener('click',()=>big.classList.toggle('native'));
viewer.addEventListener('click',e=>{if(e.target===viewer)viewer.close();});
