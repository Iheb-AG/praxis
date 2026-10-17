import json, re, shutil, hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[2]
film=Path(__file__).resolve().parent
assets=film/'assets'
def table(text, heading):
    section=text.split('## '+heading+'\n',1)[1].split('\n## ',1)[0]
    rows=[line for line in section.splitlines() if line.startswith('|')]
    return [[v.strip() for v in row.strip('|').split('|')] for row in rows if not re.match(r'^\|\s*---',row)]
gpio=(assets/'gpio.md').read_text()
net=(assets/'led-net.md').read_text()
main=(root/'examples/stm32f407g-disc1-led-button/application/main.c').read_text()
shutil.copy2(root/'examples/stm32f407g-disc1-led-button/application/main.c',assets/'main.c')
data={'gpio_registers':table(gpio,'Register map'), 'gpio_fields':table(gpio,'Bit fields'), 'net_rows':table(net,'Separate circuit net: LD4_ANODE'), 'code':main, 'gpio_prerequisite':next(l for l in gpio.splitlines() if l.startswith('Prerequisites:'))}
(assets/'facts.js').write_text('window.PRAXIS_FACTS='+json.dumps(data)+';\n')
records=[]
for p in sorted(assets.iterdir()):
    if p.is_file(): records.append({'file':str(p.relative_to(film)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(film/'SOURCES.json').write_text(json.dumps({'project':'https://github.com/Iheb-AG/praxis','capture':'2026-10-16','bundle':'bundles/stm32f407g-disc1-e01-timer-irq-v1','files':records,'claim_limits':'Four read-only MCP calls. No build, flash or physical test performed for this film. Rendered package is illustrative.'},indent=2)+'\n')
