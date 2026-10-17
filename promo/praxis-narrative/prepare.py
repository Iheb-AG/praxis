import json,re,hashlib,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[2];F=Path(__file__).resolve().parent;A=F/'assets'
trace=json.loads((R/'.praxis-output/promo-narrative/full-trace.json').read_text())
b=next(t['response'] for t in trace if t['tool']=='build_firmware')
e=json.loads((A/'evidence.json').read_text());e['build_receipt']=b
s=(A/'usart.md').read_text();p=s.split('## Register map\n',1)[1].split('\n## ',1)[0]
e['table']=[[v.strip() for v in l.strip('|').split('|')] for l in p.splitlines() if l.startswith('|') and not re.match(r'^\|\s*---',l)]
source=R/'examples/stm32f407g-disc1-uart-loopback/application/main.c';shutil.copy2(source,A/'main.c');e['code']=source.read_text()
e['command']=next(c for c in b['commands'] if '/src/main.c' in c['arguments'])
e['isolation']=['--network=none','--read-only','--cap-drop=ALL','--memory=1g --cpus=1','--pids-limit=64']
(A/'build-receipt.json').write_text(json.dumps(b,indent=2)+'\n')
(A/'facts.js').write_text('window.EVIDENCE='+json.dumps(e)+';\n')
(F/'SOURCES.json').write_text(json.dumps({'reference':'https://www.youtube.com/watch?v=6xJWQRVl9nw','bundle_revision':e['build']['bundle_revision'],'artifact_id':e['build']['artifact_id'],'actual_mcp_calls':len(trace),'hardware_tools_enabled':False,'hook':'Illustrative IDE and simulated fault; no execution on physical MCU','assets':[{'file':str(p.relative_to(F)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(A.iterdir()) if p.is_file()]},indent=2)+'\n')
