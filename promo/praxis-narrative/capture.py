import asyncio,json,os,sys
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent/'assets'
PRIVATE=ROOT/'.praxis-output/promo-narrative'
BUNDLE=ROOT/'bundles/stm32f407g-disc1-e01-timer-irq-v1'
def payload(r):
 if r.structuredContent is not None:
  v=r.structuredContent
  return v['result'] if set(v)=={'result'} else v
 t='\n'.join(b.text for b in r.content if b.type=='text')
 try:return json.loads(t)
 except ValueError:return t
async def main():
 trace=[];facts={}
 env={k:v for k,v in os.environ.items() if k!='PRAXIS_HARDWARE_AUTHORIZATION'}
 def server(args):return StdioServerParameters(command=sys.executable,args=['-m','praxis',*args],cwd=str(ROOT),env=env)
 async def call(c,tool,args,expected_error=False):
  r=await c.call_tool(tool,args);p=payload(r)
  if bool(r.isError)!=expected_error:raise RuntimeError(f'{tool}: {p}')
  trace.append({'tool':tool,'arguments':args,'is_error':bool(r.isError),'response':p})
  return p
 async with stdio_client(server(['serve','--bundle',str(BUNDLE)])) as (r,w),ClientSession(r,w) as c:
  await c.initialize()
  facts['index']=await call(c,'read_wiki_index',{})
  facts['gate_error']=await call(c,'read_peripheral_doc',{'peripheral_name':'usart'},True)
  for name in ('rcc','gpio','usart'):
   facts[name]=await call(c,'read_peripheral_doc',{'peripheral_name':name})
   (OUT/f'{name}.md').write_text(facts[name])
 args=['build-serve','--bundle',str(BUNDLE),'--assets',str(ROOT/'assets/stm32f407vg'),'--workspace',str(ROOT/'examples/stm32f407g-disc1-uart-loopback'),'--artifacts',str(PRIVATE/'build-artifacts'),'--lock',str(ROOT/'toolchain-f407.lock.json')]
 async with stdio_client(server(args)) as (r,w),ClientSession(r,w) as c:
  await c.initialize()
  names=sorted(t.name for t in (await c.list_tools()).tools)
  assert names==['build_firmware','get_build_profile','validate_firmware'],names
  profile=await call(c,'get_build_profile',{})
  build=await call(c,'build_firmware',{'source_directory':'application'})
  assert build.get('compile_passed') is True and build.get('image_validated') is True,build
  validation=await call(c,'validate_firmware',{'artifact_id':build['artifact_id']})
  assert validation.get('validation',{}).get('valid') is True,validation
  facts['build']={k:build.get(k) for k in ('artifact_id','compile_passed','image_validated','source_sha256','bundle_revision','asset_revision','image','compiler_versions')}
  facts['validation']=validation.get('validation')
  facts['profile']={k:profile.get(k) for k in ('target','bundle_revision','compiler_versions','image')}
  print(json.dumps(facts['build'],indent=2),flush=True)
 (PRIVATE/'full-trace.json').write_text(json.dumps(trace,indent=2)+'\n')
 (OUT/'evidence.json').write_text(json.dumps(facts,indent=2)+'\n')
 (OUT/'facts.js').write_text('window.EVIDENCE='+json.dumps(facts)+';\n')
asyncio.run(asyncio.wait_for(main(),120))
