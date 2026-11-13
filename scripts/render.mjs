#!/usr/bin/env node
/** Render a stage figure module with the installed Chrome. No download, no network except this local server.
 *  node scripts/render.mjs figure.mjs [--out dir] [--scale 4] [--tiles 2]
 *  Writes figure.png, figure.svg (raster 3D + editable vector labels), figure-gray.png, detail-R-C.png, report.json.
 *  Also renders a finished .svg or .html file: the same PNG, grayscale and detail outputs, without the stage. */
import fs from 'node:fs';
import os from 'node:os';
import http from 'node:http';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const args = process.argv.slice(2);
if (!args.length || args.includes('--help')) {
  console.log('node scripts/render.mjs figure.mjs|figure.svg|page.html [--out dir] [--scale 4] [--tiles 2]');
  process.exit(args.length ? 0 : 2);
}
const input = path.resolve(args.shift());
const opt = {out: path.dirname(input), scale: 4, tiles: 2};
while (args.length) { const k = args.shift().replace(/^--/, ''); if (!(k in opt) || !args.length) throw new Error('Unknown option --' + k); opt[k] = k === 'out' ? path.resolve(args.shift()) : Number(args.shift()); }
if (!fs.existsSync(input)) throw new Error('Missing input: ' + input);
const KIT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../kit');
const name = path.basename(input), stem = name.replace(/\.[^.]+$/, ''), isStage = /\.m?js$/.test(name);
const chrome = [process.env.CHROME_PATH, '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
  process.env.PROGRAMFILES && path.join(process.env.PROGRAMFILES, 'Google/Chrome/Application/chrome.exe')].filter(Boolean).find(p => fs.existsSync(p));
if (!chrome) throw new Error('No Chrome or Chromium found. Set CHROME_PATH.');

const TYPES = {'.mjs': 'text/javascript', '.js': 'text/javascript', '.html': 'text/html', '.svg': 'image/svg+xml', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.css': 'text/css'};
const shell = `<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:#fff}</style>
<script type="importmap">{"imports":{"three":"/kit/vendor/three.module.min.js","three/addons/":"/kit/vendor/addons/","mf":"/kit/stage.mjs"}}</script>
<div id="fig"></div><script type="module">
import {createStage, THREE} from 'mf';
try { const m = await import('/fig/${name}'); const beat = Number(new URLSearchParams(location.search).get('beat') || 0); const S = createStage({...(m.view || {}), mount: document.getElementById('fig')}); await m.default(S, THREE, beat); if (!window.__mf) S.done(); window.__mf.beats = m.beats || null; }
catch (e) { window.__mf = {error: String(e && e.stack || e)}; }
</script>`;
const server = http.createServer((req, res) => {
  const url = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  if (url === '/') { res.writeHead(200, {'content-type': 'text/html'}); return res.end(shell); }
  const base = url.startsWith('/kit/') ? KIT : url.startsWith('/fig/') ? path.dirname(input) : null;
  const file = base && path.resolve(base, url.slice(5));
  if (!file || !file.startsWith(base + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, {'content-type': TYPES[path.extname(file)] || 'application/octet-stream', 'cache-control': 'no-store'}); fs.createReadStream(file).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const origin = 'http://127.0.0.1:' + server.address().port;
const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'mf-render-'));
let browser, ws, sid, serial = 0, failed = false; const pending = new Map(), errors = [];
const send = (method, params = {}, sessionId = sid) => new Promise((resolve, reject) => {
  const id = ++serial, timer = setTimeout(() => { pending.delete(id); reject(new Error('Chrome timeout: ' + method)); }, 60000);
  pending.set(id, {resolve, reject, timer}); ws.send(JSON.stringify({id, method, params, ...(sessionId ? {sessionId} : {})}));
});
const evaluate = async expression => {
  const r = await send('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true});
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text);
  return r.result.value;
};
try {
  browser = spawn(chrome, ['--headless=new', '--remote-debugging-port=0', '--user-data-dir=' + temp, '--no-first-run', '--disable-extensions',
    '--disable-background-networking', '--disable-sync', '--hide-scrollbars', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', 'about:blank'], {stdio: ['ignore', 'ignore', 'pipe']});
  const endpoint = await new Promise((resolve, reject) => {
    let log = ''; const timer = setTimeout(() => reject(new Error('Chrome did not start. ' + log.slice(-400))), 20000);
    browser.stderr.on('data', b => { log += b; const m = log.match(/DevTools listening on (ws:\/\/[^\s]+)/); if (m) { clearTimeout(timer); resolve(m[1]); } });
    browser.on('error', reject);
  });
  ws = new WebSocket(endpoint);
  await new Promise((resolve, reject) => { ws.addEventListener('open', resolve, {once: true}); ws.addEventListener('error', reject, {once: true}); });
  ws.addEventListener('message', ev => {
    const m = JSON.parse(ev.data), p = pending.get(m.id);
    if (p) { pending.delete(m.id); clearTimeout(p.timer); m.error ? p.reject(new Error(JSON.stringify(m.error))) : p.resolve(m.result); }
    if (m.method === 'Runtime.exceptionThrown') errors.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
    if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error') errors.push(m.params.args.map(a => a.value ?? a.description).join(' '));
  });
  const target = await send('Target.createTarget', {url: 'about:blank'}, null);
  sid = (await send('Target.attachToTarget', {targetId: target.targetId, flatten: true}, null)).sessionId;
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', {width: 1400, height: 1000, deviceScaleFactor: opt.scale, mobile: false});
  let clip; const beats = []; let report = {input: name, warnings: []};
  for (let beat = 0, total = 1; beat < total; beat++) {
  const tag = total > 1 || beat ? stem + '-beat' + (beat + 1) : stem;
  await evaluate('window.__mf=undefined,1').catch(() => {});
  await send('Page.navigate', {url: isStage ? origin + '/?beat=' + beat : origin + '/fig/' + name});
  let state;
  for (let i = 0; i < 600; i++) {
    state = await evaluate(isStage ? `!!window.__mf && location.search==='?beat=${beat}'` : 'document.readyState==="complete"').catch(() => false);
    if (state) break; await new Promise(r => setTimeout(r, 100));
  }
  if (!state) throw new Error('The figure did not finish within 60 s. ' + errors.join(' | '));
  
  if (isStage) {
    const mf = await evaluate('window.__mf');
    if (mf.error) throw new Error(mf.error);
    if (mf.beats && total === 1 && mf.beats.length > 1) { total = mf.beats.length; beat = -1; continue; }
    report = {...report, ...mf.audit, warnings: [...report.warnings, ...mf.audit.warnings.map(w => total > 1 ? `beat ${beat + 1}: ${w}` : w)], width_mm: mf.width, height_mm: mf.height};
    if (mf.beats) beats.push({title: mf.beats[beat], png: tag + '.png'});
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${mf.width} ${mf.height}" width="${mf.width}mm" height="${mf.height}mm">` +
      `<image href="${mf.raster}" x="0" y="0" width="${mf.width}" height="${mf.height}"/>${mf.overlay}</svg>\n`;
    fs.mkdirSync(opt.out, {recursive: true}); fs.writeFileSync(path.join(opt.out, tag + '.svg'), svg);
    clip = await evaluate('(()=>{const r=document.getElementById("fig").getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}})()');
  } else {
    await evaluate('document.fonts.ready.then(()=>1)');
    await evaluate('Promise.all([...document.images].map(i=>{i.loading="eager";return i.decode().catch(()=>0)})).then(()=>1)');
    clip = await evaluate('(()=>{const e=document.querySelector("svg")||document.body;const r=e.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:Math.ceil(r.width),height:Math.ceil(r.height)}})()');
    report.warnings = await evaluate(`[...document.querySelectorAll('svg text')].filter(t=>{const b=t.getBoundingClientRect(),r=t.ownerSVGElement.getBoundingClientRect();return b.left<r.left-1||b.top<r.top-1||b.right>r.right+1||b.bottom>r.bottom+1}).map(t=>'text "'+t.textContent.slice(0,40)+'" leaves the frame')`);
    fs.mkdirSync(opt.out, {recursive: true});
  }
  const shot = async (file, c, scale = 1) => {
    const r = await send('Page.captureScreenshot', {format: 'png', captureBeyondViewport: true, clip: {...c, scale}});
    fs.writeFileSync(path.join(opt.out, file), Buffer.from(r.data, 'base64')); return file;
  };
  report.files = report.files || []; const files = report.files; files.push(await shot(tag + '.png', clip));
  for (let r = 0; r < opt.tiles; r++) for (let c = 0; c < opt.tiles; c++) {
    files.push(await shot(`${tag}-detail-${r + 1}-${c + 1}.png`, {x: clip.x + clip.width * c / opt.tiles, y: clip.y + clip.height * r / opt.tiles, width: clip.width / opt.tiles, height: clip.height / opt.tiles}, 2));
  }
  await evaluate('document.documentElement.style.filter="grayscale(1)",1');
  files.push(await shot(tag + '-gray.png', clip, 0.5));
  }
  if (beats.length > 1) {
    const cards = beats.map((b, i) => `<section data-i="${i}"><div><b>${String(b.title).split('|')[0]}</b><p>${String(b.title).split('|')[1] || ''}</p></div></section>`).join('');
    fs.writeFileSync(path.join(opt.out, stem + '-story.html'), `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${stem}</title>
<style>body{margin:0;background:#faf9f5;color:#1b2430;font:17px/1.5 Georgia,serif}#stage{position:sticky;top:0;height:100vh;display:grid;place-items:center}#stage img{grid-area:1/1;max-width:92vw;max-height:92vh;opacity:0;transition:opacity .6s ease}#stage img.on{opacity:1}
section{height:100vh;display:flex;align-items:flex-end;padding:0 0 12vh 5vw;position:relative;box-sizing:border-box}section div{max-width:21em;background:#fffffff2;border:1px solid #e3e0d6;border-radius:6px;padding:14px 18px;box-shadow:0 2px 12px #0001}section b{font:600 15px/1.4 -apple-system,Helvetica,Arial,sans-serif}section p{margin:.4em 0 0}#steps{margin-top:-100vh}
@media (prefers-reduced-motion:reduce){#stage img{transition:none}}</style>
<div id="stage">${beats.map((b, i) => `<img src="${b.png}" alt="${String(b.title).replace(/"/g, '&quot;')}"${i ? '' : ' class="on"'}>`).join('')}</div><div id="steps">${cards}</div>
<script>const imgs=[...document.querySelectorAll('#stage img')];const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)imgs.forEach((m,i)=>m.classList.toggle('on',i==e.target.dataset.i))}),{threshold:.5});document.querySelectorAll('section').forEach(s=>io.observe(s));</script>\n`);
    report.files.push(stem + '-story.html');
  }
  const files = report.files;
  report.errors = errors; report.files = files; report.pixels = [Math.round(clip.width * opt.scale), Math.round(clip.height * opt.scale)];
  report.next = 'Read ' + stem + '.png, every detail tile and the grayscale file. A clean report is not a visual pass.';
  if (isStage) fs.writeFileSync(path.join(opt.out, stem + '.report.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report, null, 2));
  if (errors.length) failed = true;
} catch (error) { console.error('render failed: ' + error.message); failed = true; }
finally {
  if (ws && ws.readyState === WebSocket.OPEN) { try { await send('Browser.close', {}, null); } catch {} ws.close(); }
  for (const p of pending.values()) clearTimeout(p.timer);
  server.close();
  if (browser) await Promise.race([new Promise(r => browser.once('close', r)), new Promise(r => setTimeout(r, 4000))]).then(() => browser.kill());
  await fs.promises.rm(temp, {recursive: true, force: true, maxRetries: 3, retryDelay: 100}).catch(() => {});
  process.exit(failed ? 2 : 0);
}
