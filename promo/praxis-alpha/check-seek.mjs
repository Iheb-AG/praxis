import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import os from 'node:os';
const skill=process.env.MOTIONMAXXING_SKILL||path.join(os.homedir(),'.codex/skills/motionmaxxing');
const {launchChrome}=await import(pathToFileURL(path.join(skill,'scripts/_cdp.mjs')).href);
const browser=await launchChrome({args:['--allow-file-access-from-files']});
try{
 const page=await browser.newPage({width:1920,height:1080,scale:1});
 await page.goto(pathToFileURL(path.resolve('promo/praxis-alpha/index.html')).href);
 await page.eval('window.__ready',{timeout:60000});
 const result=await page.eval('Motion.selfTest(window.__film,{samples:32})',{timeout:180000});
 fs.writeFileSync('promo/praxis-alpha/seek-check.json',JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify(result));
 if(!result.ok)process.exitCode=1;
} finally {await browser.close();}
