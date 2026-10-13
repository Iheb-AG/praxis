import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { createSnapshot } from '../build.mjs';

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
  write('docs/README.md', '# Docs\n\n[private](../.monitor/state.json) [raw](../sources/demo/raw/secret.json) [escape](../../outside.txt) [link](linked.json)\n');
  write('.monitor/state.json', 'private'); write('sources/demo/raw/secret.json', 'private');
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
