#!/usr/bin/env node
// Optional preview helper: Node 22+ and an existing Chrome/Chromium. No installs.
// Only local SVGs that passed the Python preflight should be supplied.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {pathToFileURL} from 'node:url';

const [input, output, browserArg] = process.argv.slice(2);
if (!input || !output) {console.error('Usage: node tools/render_svg.mjs figure.svg figure.png [existing-chrome-path]');process.exit(2);}
const chromePath = browserArg || process.env.CHROME_PATH || (process.platform === 'darwin' ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' : '/usr/bin/chromium');
if (!fs.existsSync(chromePath)) {console.error('Supply an installed Chrome path; no browser is downloaded.');process.exit(2);}
const raw = fs.readFileSync(path.resolve(input), 'utf8');
if (/<!DOCTYPE|<!ENTITY|<script|<foreignObject|\bon\w+\s*=|(?:href\s*=\s*["'](?!#))/i.test(raw)) {console.error('Refusing active or externally linked SVG.');process.exit(2);}
const vb = raw.match(/viewBox="([^"]+)"/);
if (!vb) throw new Error('SVG needs a viewBox');
const coords = vb[1].split(/[ ,]+/).map(Number);
if(coords.length!==4 || !coords.every(Number.isFinite) || coords[2]<=0 || coords[3]<=0) throw new Error('Invalid viewBox');
const width=1440, height=Math.round(width*coords[3]/coords[2]);
if(height>4000) throw new Error('Unexpectedly tall figure; inspect dimensions');
const temp = fs.mkdtempSync(path.join(os.tmpdir(),'mechanismfigures-render-'));
const htmlPath=path.join(temp,'preview.html');
fs.writeFileSync(htmlPath,'<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:white;width:100%;height:100%;overflow:hidden}svg{display:block;width:100vw;height:100vh}</style></head><body>'+raw+'</body></html>');
let chrome, ws, id=0;
const pending=new Map();
function call(method,params={},sessionId){return new Promise((resolve,reject)=>{const n=++id;const timer=setTimeout(()=>{pending.delete(n);reject(new Error('Timeout: '+method));},20000);pending.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params,...(sessionId?{sessionId}:{})}));});}
try {
 chrome=spawn(chromePath,['--headless=new','--remote-debugging-port=0','--user-data-dir='+path.join(temp,'profile'),'--no-first-run','--no-default-browser-check','--disable-background-networking','--disable-sync','--disable-extensions','about:blank'],{stdio:['ignore','ignore','pipe']});
 const url=await new Promise((resolve,reject)=>{let log='';const timer=setTimeout(()=>reject(new Error('Browser startup timeout')),20000);chrome.stderr.on('data',b=>{log+=b;const m=log.match(/DevTools listening on (ws:\/\/[^\s]+)/);if(m){clearTimeout(timer);resolve(m[1]);}});chrome.on('error',reject);chrome.on('exit',c=>{if(!log.includes('DevTools listening'))reject(new Error('Browser exited '+c));});});
 ws=new WebSocket(url);await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true});});
 ws.addEventListener('message',e=>{const m=JSON.parse(e.data),p=pending.get(m.id);if(p){pending.delete(m.id);clearTimeout(p.timer);m.error?p.reject(new Error(JSON.stringify(m.error))):p.resolve(m.result);}});
 const t=await call('Target.createTarget',{url:'about:blank'});
 const {sessionId:s}=await call('Target.attachToTarget',{targetId:t.targetId,flatten:true});
 await call('Page.enable',{},s);await call('Runtime.enable',{},s);await call('Network.enable',{},s);
 await call('Network.setBlockedURLs',{urls:['http://*','https://*']},s);
 await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:2,mobile:false},s);
 await call('Page.navigate',{url:pathToFileURL(htmlPath).href},s);
 let loaded=false;for(let i=0;i<100;i++){const r=await call('Runtime.evaluate',{expression:'document.readyState',returnByValue:true},s);if(r.result.value==='complete'){loaded=true;break;}await new Promise(r=>setTimeout(r,50));}
 if(!loaded) throw new Error('Preview failed to load');
 await call('Runtime.evaluate',{expression:'document.fonts.ready',awaitPromise:true},s);
 const screenshot=await call('Page.captureScreenshot',{format:'png',fromSurface:true,captureBeyondViewport:false},s);
 fs.writeFileSync(path.resolve(output),Buffer.from(screenshot.data,'base64'));
 console.log(JSON.stringify({output:path.resolve(output),width:width*2,height:height*2,renderer:'Installed isolated Chrome; HTTP(S) requests blocked',status:'rendered; visual inspection still required'}));
 await call('Browser.close');
} finally {
 for(const p of pending.values())clearTimeout(p.timer);
 if(ws)ws.close();if(chrome && chrome.exitCode===null)chrome.kill('SIGTERM');
 // Chrome releases the profile asynchronously; only this owned temporary tree is removed.
 await new Promise(r=>setTimeout(r,200));
 fs.rmSync(temp,{recursive:true,force:true,maxRetries:5,retryDelay:100});
}
