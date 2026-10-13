// Generate the public Markdown snapshot consumed by Vite. No ingestion/model calls.
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT_GUIDES = ['README.md', 'README_DETAILED.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'website/README.md'];
const PUBLIC_DIRS = ['docs', 'examples', 'bundles', 'assets', 'sources'];
const EXCLUDED = new Set(['raw', 'imports', 'temp', '.git', '.venv', '.praxis-output', '.aws',
  '.codex', '.agents', '.monitor', '.vercel', '.generated', '.build-staging', '__pycache__', 'node_modules', 'dist', 'build']);
const GROUPS = {
  'Start here': ['README.md', 'README_DETAILED.md', 'docs/README.md', 'docs/system-design.md',
    'docs/architecture.md', 'docs/sequences.md', 'docs/asset-contract.md'],
  'Ingestion & knowledge': ['docs/board-ingestion.md', 'docs/web-ingestion.md', 'docs/ingestion-mcp.md',
    'docs/manual-review-compiler.md', 'docs/peripheral-discovery.md', 'docs/capability-support.md',
    'docs/peripheral-modes.md', 'docs/clock-modes.md', 'docs/adc-expansion.md', 'docs/bundle-advisories.md'],
  'Build & hardware': ['docs/verification.md', 'docs/build-service.md', 'docs/hardware-inspection.md',
    'docs/hardware-programming.md', 'docs/hardware-recovery.md', 'docs/hardware-verification.md',
    'docs/firmware-telemetry.md', 'docs/flash-demo.md', 'docs/docker.md'],
  'Testing & evidence': ['docs/evaluation.md', 'docs/milestone1.md', 'docs/mcp-test-prompts.md'],
  'Project & contribution': ['CHANGELOG.md', 'CONTRIBUTING.md', 'docs/STATUS.md',
    'docs/PUBLICATION_READINESS.md', 'docs/experimental-release.md', 'docs/vercel-hosting.md', 'website/README.md'],
};
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const decode = bytes => new TextDecoder('utf-8', { fatal: true }).decode(bytes);
const forbidden = name => name.split('/').some(part => EXCLUDED.has(part) || part.startsWith('.env'));

function safeFile(root, name) {
  if (!name || forbidden(name) || path.posix.isAbsolute(name) || name.split('/').includes('..')) return null;
  const parts = name.split('/');
  try {
    for (let i = 1; i <= parts.length; i++) {
      if (fs.lstatSync(path.join(root, ...parts.slice(0, i))).isSymbolicLink()) return null;
    }
    const file = path.join(root, ...parts);
    return fs.statSync(file).isFile() && fs.statSync(file).size <= 2 * 1024 * 1024 ? file : null;
  } catch (error) {
    if (['ENOENT', 'ENOTDIR'].includes(error.code)) return null;
    throw error;
  }
}

function walk(root, relative, found) {
  if (forbidden(relative)) return;
  const directory = path.join(root, relative);
  if (!fs.existsSync(directory) || fs.lstatSync(directory).isSymbolicLink()) return;
  for (const entry of fs.readdirSync(directory, { withFileTypes: true }).sort((a,b) => a.name.localeCompare(b.name, 'en'))) {
    const name = path.posix.join(relative, entry.name);
    if (forbidden(name) || entry.isSymbolicLink()) continue;
    if (entry.isDirectory()) walk(root, name, found);
    else if (entry.isFile() && name.endsWith('.md')) found.add(name);
  }
}

export function createSnapshot(source) {
  const root = fs.realpathSync(source);
  if (!safeFile(root, 'docs/README.md')) throw new Error('Source must contain docs/README.md');
  const candidates = new Set(ROOT_GUIDES.filter(name => safeFile(root, name)));
  for (const directory of PUBLIC_DIRS) walk(root, directory, candidates);
  const documents = [], files = new Map(), attachments = new Set();
  for (const name of [...candidates].sort()) {
    if (name.startsWith('sources/') && !name.split('/').includes('reviewed')) continue;
    const file = safeFile(root, name);
    if (!file) continue;
    const raw = fs.readFileSync(file), content = decode(raw);
    files.set(name, raw);
    let title = /^#\s+(.+)$/m.exec(content)?.[1].trim() || path.posix.basename(name, '.md');
    if (name.startsWith('examples/')) title = name.split('/')[1].replaceAll('-', ' ') + ' · ' + title;
    const collection = name.startsWith('bundles/') ? 'bundles' : name.startsWith('examples/') ? 'examples'
      : name.startsWith('sources/') ? 'reviews' : name.startsWith('assets/') ? 'assets' : 'guides';
    let group = Object.entries(GROUPS).find(([, paths]) => paths.includes(name))?.[0] || 'More documentation';
    if (name.startsWith('docs/scenarios/')) group = 'Scenarios';
    if (name.startsWith('docs/reports/')) group = 'Results & reports';
    const summary = (content.split(/\n\s*\n/).find(p => p.trim() && !/^(#|\||```|-|\*|>|!\[)/.test(p.trim())) || '')
      .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[`*_]/g, '').replace(/\s+/g, ' ').trim().slice(0, 230);
    documents.push({ path: name, title, summary, group, collection, content, sha256: hash(raw),
      bundle: collection === 'bundles' ? name.split('/')[1] : null,
      words: content.split(/\s+/).filter(Boolean).length, diagrams: [...content.matchAll(/^```mermaid\s*$/gm)].length });
    // Follow explicit local attachments only. Reject private paths, symlinks, raw
    // manuals, firmware binaries and unsupported binary formats.
    for (const match of content.matchAll(/!?\[[^\]\n]*\]\(([^)\n]+)\)/g)) {
      const value = match[1].replace(/^<|>$/g, '');
      if (/^[a-z][a-z0-9+.-]*:|^\/\/|^#/i.test(value)) continue;
      let target;
      try { target = path.posix.normalize(path.posix.join(path.posix.dirname(name), decodeURIComponent(value.split('#')[0]))); }
      catch { continue; }
      const attachment = safeFile(root, target);
      if (!attachment || /\.(md|pdf|bin|elf|hex|map)$/i.test(target)) continue;
      const bytes = fs.readFileSync(attachment);
      if (/\.(png|jpe?g|webp|gif)$/i.test(target)) {
        const valid = /\.png$/i.test(target) ? bytes.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]))
          : /\.jpe?g$/i.test(target) ? bytes.subarray(0,3).equals(Buffer.from([255,216,255]))
          : /\.gif$/i.test(target) ? bytes.subarray(0,3).toString() === 'GIF'
          : bytes.subarray(0,4).toString() === 'RIFF' && bytes.subarray(8,12).toString() === 'WEBP';
        if (!valid) throw new Error('Image extension/signature mismatch: ' + target);
      } else {
        try { decode(bytes); } catch { continue; }
      }
      attachments.add(target); files.set(target, bytes);
    }
  }
  const snapshotHash = hash(JSON.stringify([...files].sort(([a],[b]) => a < b ? -1 : a > b ? 1 : 0)
    .map(([name, bytes]) => [name, hash(bytes)])));
  return { files, catalog: { documents, attachments: [...attachments].sort(),
    groups: [...Object.keys(GROUPS), 'Scenarios', 'Results & reports', 'More documentation'],
    sourceName: 'praxis', repositoryURL: 'https://github.com/Iheb-AG/praxis', snapshotHash } };
}

export function build(source = path.dirname(HERE)) {
  const { catalog, files } = createSnapshot(source);
  const output = path.join(HERE, '.generated'), staging = path.join(HERE, '.build-staging');
  fs.rmSync(staging, { recursive: true, force: true });
  fs.cpSync(path.join(HERE, 'public'), staging, { recursive: true });
  for (const [name, bytes] of files) {
    const destination = path.join(staging, 'content', name);
    fs.mkdirSync(path.dirname(destination), { recursive: true }); fs.writeFileSync(destination, bytes);
  }
  fs.writeFileSync(path.join(staging, 'catalog.json'), JSON.stringify(catalog) + '\n');
  const report = { publicDocumentationOnly: true, documents: catalog.documents.length,
    attachments: catalog.attachments.length, snapshotHash: catalog.snapshotHash,
    privateMonitorIncluded: false, repositoryURL: catalog.repositoryURL };
  fs.writeFileSync(path.join(staging, 'build-report.json'), JSON.stringify(report, null, 2) + '\n');
  fs.rmSync(output, { recursive: true, force: true }); fs.renameSync(staging, output);
  console.log(JSON.stringify(report, null, 2));
  return report;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) build();
