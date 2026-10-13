// Include installed dependency notices alongside the production browser assets.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const lock = JSON.parse(fs.readFileSync(path.join(root, 'package-lock.json'), 'utf8'));
const sections = ['Project Praxis documentation — third-party dependency notices',
  'Dependencies are pinned in website/package-lock.json. This inventory includes installed build dependencies.'];
for (const [location, entry] of Object.entries(lock.packages).sort(([a], [b]) => a.localeCompare(b))) {
  if (!location.startsWith('node_modules/')) continue;
  const directory = path.join(root, location);
  if (!fs.existsSync(directory)) continue; // Optional binaries for another platform.
  const manifest = JSON.parse(fs.readFileSync(path.join(directory, 'package.json'), 'utf8'));
  sections.push(`\n${'='.repeat(72)}\n${manifest.name} ${entry.version}\nDeclared license: ${manifest.license || 'See upstream package'}\n`);
  for (const name of fs.readdirSync(directory).sort()) {
    if (/^(licen[sc]e|copying|notice)([-.]|$)/i.test(name) && fs.statSync(path.join(directory, name)).isFile()) {
      sections.push(name + '\n' + fs.readFileSync(path.join(directory, name), 'utf8'));
    }
  }
}
fs.mkdirSync(path.join(root, '.generated'), { recursive: true });
fs.writeFileSync(path.join(root, '.generated', 'THIRD_PARTY_NOTICES.txt'), sections.join('\n') + '\n');
console.log('Dependency notices written for the production website.');
