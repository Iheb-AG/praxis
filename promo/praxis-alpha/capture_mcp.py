import asyncio, json, sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent/'assets'
async def main():
    params=StdioServerParameters(command=sys.executable,args=['-m','praxis','serve','--bundle',str(ROOT/'bundles/stm32f407g-disc1-e01-timer-irq-v1')],cwd=str(ROOT))
    trace=[]
    async with stdio_client(params) as (r,w), ClientSession(r,w) as c:
        await c.initialize()
        for name,args,file in [('read_wiki_index',{},'index'),('query_schematic_netlist',{'query_target':'LED_A'},'led-net'),('read_peripheral_doc',{'peripheral_name':'rcc'},'rcc'),('read_peripheral_doc',{'peripheral_name':'gpio'},'gpio')]:
            reply=await c.call_tool(name,args)
            text='\n'.join(b.text for b in reply.content if b.type=='text')
            if reply.isError: raise RuntimeError(text)
            (OUT/f'{file}.md').write_text(text)
            trace.append({'tool':name,'arguments':args,'response':text})
    (OUT/'mcp-capture.json').write_text(json.dumps(trace,indent=2)+'\n')
asyncio.run(main())
