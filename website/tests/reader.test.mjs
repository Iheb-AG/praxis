import assert from 'node:assert/strict';
import test from 'node:test';
import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { parseRoute, readRoute, remarkDocumentation, resolveReference, searchDocuments } from '../src/docs.mjs';

test('existing hash links, encoded paths, anchors and progress bookmarks are preserved', () => {
  const route = parseRoute(readRoute('docs/clock modes.md', 'clock-tree'));
  assert.equal(route.path, 'docs/clock modes.md'); assert.equal(route.params.get('anchor'), 'clock-tree');
  assert.equal(parseRoute('#/progress').path, 'docs/STATUS.md');
  assert.doesNotThrow(() => parseRoute('#/read/%malformed'));
});

test('link resolution uses registered exact paths and rejects executable/unknown references', () => {
  const docs = new Map([['docs/clock.md', {}], ['docs/README.md', {}]]), attachments = new Set(['docs/proof.json']);
  assert.equal(resolveReference('docs/index.md', 'clock.md#tree', docs, attachments).href, readRoute('docs/clock.md', 'tree'));
  assert.equal(resolveReference('README.md', 'docs', docs, attachments).path, 'docs/README.md');
  assert.equal(resolveReference('docs/index.md', 'proof.json', docs, attachments).path, 'docs/proof.json');
  for (const href of ['javascript:alert(1)', 'data:text/html,unsafe', '//example.invalid/x', '../absent.md']) {
    assert.equal(resolveReference('docs/index.md', href, docs, attachments).kind, 'missing');
  }
});

test('React Markdown preserves complete tables, canonical wiki links and duplicate heading anchors', () => {
  const markdown = '# GPIO\n\n## Setup\n\n[[peripherals/rcc|Clocks]]\n\n| Register | Offset |\n| --- | --- |\n| MODER | 0x00 |\n| AFRH | 0x24 |\n\n## Setup\n\n`[[not-a-link]]`\n\n<script>alert(1)</script>';
  const html = renderToStaticMarkup(createElement(ReactMarkdown, {
    remarkPlugins: [remarkGfm, [remarkDocumentation, { docPath: 'bundles/demo/wiki/peripherals/gpio.md' }]],
  }, markdown));
  assert.match(html, /<table>/); assert.match(html, /MODER/); assert.match(html, /AFRH/); assert.match(html, /0x24/);
  assert.match(html, /id="setup"/); assert.match(html, /id="setup-1"/);
  assert.ok(html.includes(readRoute('bundles/demo/wiki/peripherals/rcc.md')));
  assert.match(html, /<code>\[\[not-a-link\]\]<\/code>/); assert.ok(!html.includes('<script>'));
});

test('full-text search and bundle filtering remain deterministic', () => {
  const documents = [
    { path: 'bundles/a/uart.md', title: 'UART', summary: '', content: 'Baud divisor and clock', collection: 'bundles', bundle: 'a' },
    { path: 'docs/baud.md', title: 'Baud', summary: '', content: 'UART divisor', collection: 'guides', bundle: null },
  ];
  assert.equal(searchDocuments(documents, new URLSearchParams('q=uart+divisor')).length, 2);
  const result = searchDocuments(documents, new URLSearchParams('q=divisor&collection=bundles&bundle=a'));
  assert.equal(result.length, 1); assert.equal(result[0].doc.path, 'bundles/a/uart.md');
});
