import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';
import { createSnapshot, resolveSourceRoot } from '../build.mjs';
import { spawnSync } from 'node:child_process';

const WEBSITE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'praxis-public-docs-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const write = (name, content) => { const file = path.join(root, name); fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, content); };
  write('docs/README.md', '# Documentation\n\nA complete reference.\n');
  return { root, write };
}

test('snapshots preserve whole Markdown and produce deterministic hashes', t => {
  const { root, write } = fixture(t);
  const content = '# GPIO\n\n| register | offset |\n| --- | --- |\n| MODER | 0x00 |\n';
  write('bundles/demo/wiki/peripherals/gpio.md', content);
  write('README_DETAILED.md', '# Detailed setup\n');
  const first = createSnapshot(root), second = createSnapshot(root);
  assert.deepEqual(first.catalog, second.catalog);
  assert.equal(first.files.get('bundles/demo/wiki/peripherals/gpio.md').toString(), content);
  assert.ok(first.catalog.documents.some(d => d.path === 'README_DETAILED.md'));
  write('docs/README.md', '# Documentation\n\nChanged.\n');
  assert.notEqual(createSnapshot(root).catalog.snapshotHash, first.catalog.snapshotHash);
});

test('private paths, raw sources, escaped links and symbolic links never enter the export', t => {
  const { root, write } = fixture(t);
  write('docs/README.md', '# Docs\n\n[private](../.monitor/state.json) [raw](../sources/demo/raw/secret.json) [escape](../../outside.txt) [link](linked.json) [generated](../website/.generated/private.json)\n');
  write('.monitor/state.json', 'private'); write('sources/demo/raw/secret.json', 'private');
  write('website/.generated/private.json', 'private');
  write('docs/imports/raw.md', '# Private'); write('sources/demo/reviewed/gpio.md', '# Reviewed');
  write('outside.txt', 'private'); fs.symlinkSync(path.join(root, 'outside.txt'), path.join(root, 'docs/linked.json'));
  const result = createSnapshot(root);
  assert.deepEqual(result.catalog.attachments, []);
  assert.ok(result.files.has('sources/demo/reviewed/gpio.md'));
  assert.ok(!result.files.has('docs/imports/raw.md'));
  assert.ok(!result.files.has('docs/linked.json'));
});

test('local images and public evidence attachments are retained; external images are not fetched', t => {
  const { root, write } = fixture(t);
  write('docs/README.md', '# Docs\n\n![art](banner.jpg) ![remote](https://example.invalid/logo.png) [proof](proof.json) [manual](manual.pdf)\n');
  write('docs/banner.jpg', Buffer.from([255,216,255,224]));
  write('docs/proof.json', '{"passed":true}\n'); write('docs/manual.pdf', '%PDF-1.4');
  const result = createSnapshot(root);
  assert.deepEqual(result.catalog.attachments, ['docs/banner.jpg', 'docs/proof.json']);
  assert.ok(!result.files.has('docs/manual.pdf'));
  write('docs/banner.jpg', 'not an image');
  assert.throws(() => createSnapshot(root), /signature mismatch/);
});

test('source resolution uses only owned content, ignoring a parent checkout and legacy environment', t => {
  const { root, write } = fixture(t);
  const websiteRoot = path.join(root, 'site');
  const previous = process.env.PRAXIS_DOCS_SOURCE;
  process.env.PRAXIS_DOCS_SOURCE = root;
  t.after(() => { if (previous === undefined) delete process.env.PRAXIS_DOCS_SOURCE; else process.env.PRAXIS_DOCS_SOURCE = previous; });
  assert.throws(() => resolveSourceRoot({ websiteRoot }), /Missing checked-in documentation-source/);
  write('site/documentation-source/docs/README.md', '# Owned docs\n');
  assert.equal(resolveSourceRoot({ websiteRoot }), path.join(websiteRoot, 'documentation-source'));
  fs.unlinkSync(path.join(websiteRoot, 'documentation-source/docs/README.md'));
  assert.throws(() => resolveSourceRoot({ websiteRoot }), /Builds use only local/);
});

test('owned documentation can be edited and extended without an export or inventory refresh', t => {
  const { root, write } = fixture(t);
  const before = createSnapshot(root).catalog;
  write('docs/README.md', '# Documentation\n\nEdited independently.\n');
  write('docs/new-guide.md', '# A new guide\n\nOwned here.\n');
  const after = createSnapshot(root).catalog;
  assert.notEqual(before.snapshotHash, after.snapshotHash);
  assert.ok(after.documents.some(d => d.path === 'docs/new-guide.md'));
  assert.match(after.documents.find(d => d.path === 'docs/README.md').content, /Edited independently/);
});

test('catalog generation works from an isolated website with an unrelated current directory', t => {
  const { root, write } = fixture(t);
  const websiteRoot = path.join(root, 'site');
  write('site/documentation-source/docs/README.md', '# Independent docs\n\nOnly local content.\n');
  write('site/public/branding/placeholder.txt', 'branding');
  fs.copyFileSync(path.join(WEBSITE, 'build.mjs'), path.join(websiteRoot, 'build.mjs'));
  const run = () => spawnSync(process.execPath, [path.join(websiteRoot, 'build.mjs')], {
    cwd: os.tmpdir(), encoding: 'utf8', env: { ...process.env, PRAXIS_DOCS_SOURCE: root },
  });
  const first = run();
  assert.equal(first.status, 0, first.stderr);
  const catalog = fs.readFileSync(path.join(websiteRoot, '.generated/catalog.json'));
  assert.match(catalog.toString(), /Independent docs/);
  assert.ok(!catalog.toString().includes('A complete reference'));
  write('docs/README.md', '# Parent changed\n');
  const second = run();
  assert.equal(second.status, 0, second.stderr);
  assert.deepEqual(fs.readFileSync(path.join(websiteRoot, '.generated/catalog.json')), catalog);
});

test('the website contains its own guides, diagrams, examples, references, notices and deployment config', () => {
  const source = resolveSourceRoot();
  const { catalog, files } = createSnapshot(source);
  for (const name of ['docs/README.md', 'docs/sequences.md', 'docs/images/praxis-banner.jpg']) assert.ok(files.has(name), name);
  assert.match(files.get('docs/sequences.md').toString(), /```mermaid/);
  for (const collection of ['guides', 'examples', 'bundles', 'reviews']) assert.ok(catalog.documents.some(d => d.collection === collection), collection);
  assert.ok(fs.existsSync(path.join(WEBSITE, 'LICENSE')));
  const config = JSON.parse(fs.readFileSync(path.join(WEBSITE, 'vercel.json'), 'utf8'));
  assert.equal(config.installCommand, 'npm ci --include=dev');
  assert.equal(config.buildCommand, 'npm run build');
  assert.equal(config.outputDirectory, 'dist');
  assert.ok(!fs.readFileSync(path.join(WEBSITE, '.gitignore'), 'utf8').includes('documentation-source'));
});
