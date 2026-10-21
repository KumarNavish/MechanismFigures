#!/usr/bin/env node
/** Capture local authored figures and 4x details; no downloads, model calls, or sandbox relaxation. */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {pathToFileURL} from 'node:url';

const args = process.argv.slice(2);
if (args.includes('--help') || !args.length) {
  console.log('node scripts/capture.mjs figure.svg --out-dir review --selector svg [--width 1200 --height 900 --tiles 2] [--allow-active] [--time 27]');
  console.log('Captures 1x and 4x details. Uses an existing CHROME_PATH or installed Chrome. HTML needs --allow-active. All HTTP(S)/WS requests are blocked. Read every PNG; capture is not a quality pass.');
  process.exit(0);
}
const input = path.resolve(args.shift());
const opts = {width:1200,height:900,tiles:2,selector:'svg',active:false,time:null};
while (args.length) {
  const flag=args.shift();
  if (flag==='--allow-active') {opts.active=true;continue;}
  const key={'--out-dir':'out','--selector':'selector','--width':'width','--height':'height','--tiles':'tiles','--time':'time'}[flag];
  if (!key || !args.length) throw new Error('Unknown or incomplete option: '+flag);
  opts[key]=['width','height','tiles','time'].includes(key)?Number(args.shift()):args.shift();
}
if (!opts.out) throw new Error('--out-dir is required; existing directories are not overwritten');
for (const key of ['width','height','tiles']) if (!Number.isInteger(opts[key]) || opts[key]<1 || opts[key]>(key==='tiles'?4:4096)) throw new Error('Invalid '+key);
if (opts.time!==null && (!Number.isFinite(opts.time)||opts.time<0)) throw new Error('Invalid animation time');
const output=path.resolve(opts.out);
if (fs.existsSync(output)) throw new Error('Output exists; use a new revision directory');
if (!fs.existsSync(input) || !['.svg','.html'].includes(path.extname(input))) throw new Error('Input must be a local SVG or HTML file');
const data=fs.readFileSync(input,'utf8');
if (path.extname(input)==='.html' && !opts.active) throw new Error('HTML executes code. Review your authored file and explicitly pass --allow-active.');
if (path.extname(input)==='.svg' && /<!DOCTYPE|<!ENTITY|<script|<foreignObject|\bon\w+\s*=/i.test(data)) throw new Error('Refusing active SVG; use the passive export');
const candidates=[process.env.CHROME_PATH,'/usr/bin/google-chrome','/usr/bin/chromium','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',process.env.PROGRAMFILES&&path.join(process.env.PROGRAMFILES,'Google/Chrome/Application/chrome.exe')].filter(Boolean);
const executable=candidates.find(p=>fs.existsSync(p));
if (!executable) throw new Error('No installed Chrome found. Set CHROME_PATH. No browser is downloaded.');
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'mf-capture-'));
let browser,browserClosed,ws,sid,serial=0;const pending=new Map(),errors=[],requests=[];
const sha=file=>crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
function command(method,params={},sessionId=sid) {
  return new Promise((resolve,reject)=>{const id=++serial,timer=setTimeout(()=>{pending.delete(id);reject(new Error('CDP timeout: '+method));},20000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{})}));});
}
async function evaluate(expression) {
  const r=await command('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description||r.exceptionDetails.text);
  return r.result.value;
}
try {
  browser=spawn(executable,['--headless=new','--remote-debugging-port=0','--user-data-dir='+temp,'--no-first-run','--disable-extensions','--disable-background-networking','--disable-sync','about:blank'],{stdio:['ignore','ignore','pipe']});
  browserClosed=new Promise(resolve=>browser.once('close',resolve));
  const endpoint=await new Promise((resolve,reject)=>{let log='';const timer=setTimeout(()=>reject(new Error('Browser did not start; use an allowed host, not weaker sandbox settings. '+log.slice(-500))),15000);browser.on('error',e=>{clearTimeout(timer);reject(e);});browser.stderr.on('data',b=>{log+=b;const m=log.match(/DevTools listening on (ws:\/\/[^\s]+)/);if(m){clearTimeout(timer);resolve(m[1]);}});browser.on('exit',code=>{clearTimeout(timer);if(!log.includes('DevTools listening'))reject(new Error('Browser exited '+code+': '+log.slice(-500)));});});
  ws=new WebSocket(endpoint);await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true});});
  ws.addEventListener('message',e=>{const m=JSON.parse(e.data),p=pending.get(m.id);if(p){pending.delete(m.id);clearTimeout(p.timer);m.error?p.reject(new Error(JSON.stringify(m.error))):p.resolve(m.result);}if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails.text);if(m.method==='Network.requestWillBeSent')requests.push(m.params.request.url);});
  const target=await command('Target.createTarget',{url:'about:blank'},null);sid=(await command('Target.attachToTarget',{targetId:target.targetId,flatten:true},null)).sessionId;
  await command('Page.enable');await command('Runtime.enable');await command('Network.enable');
  await command('Network.setBlockedURLs',{urls:['http://*','https://*','ws://*','wss://*']});
  await command('Emulation.setDeviceMetricsOverride',{width:opts.width,height:opts.height,deviceScaleFactor:1,mobile:false});
  await command('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
  const targetURL=pathToFileURL(input).href;
  await command('Page.navigate',{url:targetURL});
  let loaded=false;
  for(let i=0;i<160;i++){if(await evaluate('location.href==='+JSON.stringify(targetURL)+'&&document.readyState==="complete"')){loaded=true;break;}await new Promise(r=>setTimeout(r,50));}
  if(!loaded) throw new Error('Document did not finish loading: '+JSON.stringify(await evaluate('({url:location.href,state:document.readyState,title:document.title,text:document.body?.innerText?.slice(0,300)})')));
  await evaluate('document.fonts.ready');
  await evaluate('Promise.all([...document.querySelectorAll("img")].map(i=>{i.loading="eager";return i.decode().catch(()=>null)}))');
  if(opts.time!==null) await evaluate('(()=>{if(!window.MechanismMotion)throw Error("No MechanismMotion interface on this page");MechanismMotion.setReduced(true);MechanismMotion.seek('+opts.time+');})()');
  const measurement=await evaluate(`(()=>{const target=document.querySelector(${JSON.stringify(opts.selector)});if(!target)throw Error('Missing target selector');const r=target.getBoundingClientRect();return {box:{x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height},labels:[...target.querySelectorAll('[data-mf-label]')].map(n=>{const b=n.getBoundingClientRect();return {id:n.id,text:n.textContent,clipped:b.left<r.left||b.top<r.top||b.right>r.right||b.bottom>r.bottom}}),brokenImages:[...document.querySelectorAll("img")].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src'))};})()`);
  const b=measurement.box;if(b.width<=0||b.height<=0||b.width*b.height>20e6)throw new Error('Invalid or excessive capture bounds');
  fs.mkdirSync(path.dirname(output),{recursive:true});fs.mkdirSync(output,{recursive:false});const captures=[];
  async function shot(name,clip){const r=await command('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,fromSurface:true,clip});const dest=path.join(output,name);fs.writeFileSync(dest,Buffer.from(r.data,'base64'));captures.push({file:name,sha256:sha(dest),clip});}
  await shot('figure-1x.png',{...b,scale:1});
  for(let row=0;row<opts.tiles;row++)for(let col=0;col<opts.tiles;col++){
    const x=b.x+b.width*col/opts.tiles,y=b.y+b.height*row/opts.tiles;
    await shot(`detail-${row+1}-${col+1}-4x.png`,{x,y,width:b.width/opts.tiles,height:b.height/opts.tiles,scale:4});
  }
  const report={status:errors.length||measurement.brokenImages.length?'needs_render_repair':'needs_visual_review',input_sha256:sha(input),selector:opts.selector,viewport:{width:opts.width,height:opts.height},measurement,captures,errors,blockedNetworkRequests:requests.filter(u=>/^(https?|wss?):/.test(u)),notice:'Read every PNG. Bounds/DOM checks are diagnostics, not a scientific, aesthetic or physical-print certification. HTTP(S)/WS blocked; no sandbox relaxation.'};
  fs.writeFileSync(path.join(output,'capture.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,output,captures:captures.length,errors,brokenImages:measurement.brokenImages}));
  if(report.status==='needs_render_repair')process.exitCode=2;
} catch(error) {console.error(error.message);process.exitCode=2;}
finally {
  if(ws&&ws.readyState===WebSocket.OPEN){try{await command('Browser.close',{},null);}catch{}ws.close();}
  for(const p of pending.values())clearTimeout(p.timer);
  // Browser.close replies before Chrome has finished writing its profile.
  // Let it exit gracefully before deleting the directory it still owns.
  async function waitForBrowserClose(){
    let timer;
    try{return await Promise.race([browserClosed.then(()=>true),new Promise(resolve=>{timer=setTimeout(()=>resolve(false),5000);})]);}
    finally{clearTimeout(timer);}
  }
  let closed=!browser||await waitForBrowserClose();
  if(!closed){browser.kill('SIGTERM');closed=await waitForBrowserClose();}
  if(closed)await fs.promises.rm(temp,{recursive:true,force:true,maxRetries:3,retryDelay:100});
  else{console.error('Browser has not closed; retained its profile at '+temp);process.exitCode=2;}
}
