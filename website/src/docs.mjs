export const labels = { guides: 'Guides', examples: 'Examples', bundles: 'Knowledge bundles', reviews: 'Reviewed sources', assets: 'Firmware assets' };
export const readRoute = (path, anchor = '') => '#/read/' + encodeURIComponent(path) + (anchor ? '?anchor=' + encodeURIComponent(anchor) : '');
export const assetURL = path => (import.meta.env?.BASE_URL || '/') + 'content/' + path.split('/').map(encodeURIComponent).join('/');
export const staticURL = path => (import.meta.env?.BASE_URL || '/') + path;
export const slug = text => text.toLowerCase().trim().replace(/[^\p{L}\p{N}\s_-]/gu, '').replace(/\s/g, '-');

export function parseRoute(hash) {
  const [page, query = ''] = (hash.replace(/^#/, '') || '/').split('?');
  const params = new URLSearchParams(query);
  if (page === '/progress') return { kind: 'reader', path: 'docs/STATUS.md', params };
  if (page.startsWith('/read/')) {
    try { return { kind: 'reader', path: decodeURIComponent(page.slice(6)), params }; }
    catch { return { kind: 'reader', path: '', params }; }
  }
  return { kind: page === '/library' ? 'library' : 'home', params };
}

export function shortTitle(doc) {
  return ({ 'README.md': 'Getting started', 'README_DETAILED.md': 'Detailed setup guide',
    'CHANGELOG.md': 'Changelog', 'docs/README.md': 'Documentation guide',
    'docs/system-design.md': 'System design & theory', 'docs/architecture.md': 'Architecture & modules',
    'docs/sequences.md': 'Sequence diagrams', 'docs/asset-contract.md': 'Knowledge & firmware assets',
    'docs/STATUS.md': 'Milestone status', 'docs/PUBLICATION_READINESS.md': 'Publication readiness',
    'docs/AGENT_INSTRUCTIONS.md': 'Agent instructions', 'CONTRIBUTING.md': 'Contributing' })[doc.path]
    || doc.title.replace(/^Project Praxis\s*[:—–-]?\s*/i, '');
}

export function searchDocuments(documents, params) {
  const q = params.get('q') || '', collection = params.get('collection') || '', bundle = params.get('bundle') || '';
  const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
  return documents.filter(doc => (!collection || doc.collection === collection) && (!bundle || doc.bundle === bundle))
    .map(doc => {
      const title = doc.title.toLowerCase(), name = doc.path.toLowerCase(), body = doc.content.toLowerCase();
      if (!terms.every(term => title.includes(term) || name.includes(term) || body.includes(term))) return null;
      const score = terms.reduce((n, term) => n + (title.includes(term) ? 15 : 0) + (name.includes(term) ? 7 : 0) + (body.includes(term) ? 1 : 0), 0) + (doc.collection === 'guides' ? 3 : 0);
      let excerpt = doc.summary || doc.path;
      if (terms.length && !terms.some(term => excerpt.toLowerCase().includes(term))) {
        const start = body.indexOf(terms[0]);
        if (start >= 0) excerpt = (start > 60 ? '…' : '') + doc.content.slice(Math.max(0, start - 60), start + 180).replace(/\s+/g, ' ') + '…';
      }
      return { doc, score, excerpt };
    }).filter(Boolean).sort((a, b) => b.score - a.score || a.doc.path.localeCompare(b.doc.path));
}

export function normalizePath(value) {
  const parts = [];
  for (const part of value.split('/')) {
    if (!part || part === '.') continue;
    if (part === '..') { if (!parts.length) return null; parts.pop(); }
    else parts.push(part);
  }
  return parts.join('/');
}

export function resolveReference(docPath, href, documents, attachments) {
  if (!href) return { kind: 'missing' };
  if (/^(https?:|mailto:|tel:)/i.test(href)) return { kind: 'external', href };
  if (/^[a-z][a-z0-9+.-]*:|^\/\//i.test(href)) return { kind: 'missing' };
  if (href.startsWith('#/')) return { kind: 'route', href };
  try {
    const url = new URL(href, 'https://local.invalid/' + docPath);
    const target = href.startsWith('#') ? docPath : decodeURIComponent(url.pathname.slice(1));
    const anchor = decodeURIComponent(url.hash.slice(1));
    if (documents.has(target) || attachments.has(target)) return { kind: 'registered', path: target, href: readRoute(target, anchor) };
    const index = target.replace(/\/$/, '') + '/README.md';
    if (documents.has(index)) return { kind: 'registered', path: index, href: readRoute(index, anchor) };
  } catch { /* Malformed references stay inert. */ }
  return { kind: 'missing' };
}

export function wikiTarget(docPath, reference) {
  const [name, anchor = ''] = reference.split('#');
  const root = docPath.includes('/wiki/') ? docPath.split('/wiki/')[0] + '/wiki/' : docPath.slice(0, docPath.lastIndexOf('/') + 1);
  const target = normalizePath(root + name.replace(/\.md$/, '') + '.md');
  return target ? readRoute(target, anchor) : '';
}

const plainText = node => node.value || node.alt || (node.children || []).map(plainText).join('');
export function remarkDocumentation({ docPath }) {
  return tree => {
    const ids = new Map();
    function visit(node) {
      if (node.type === 'heading') {
        const base = slug(plainText(node)), count = ids.get(base) || 0;
        node.data = { ...node.data, hProperties: { ...node.data?.hProperties, id: base + (count ? '-' + count : '') } };
        ids.set(base, count + 1);
      }
      if (!node.children || ['link', 'linkReference', 'code', 'inlineCode', 'html'].includes(node.type)) return;
      node.children = node.children.flatMap(child => {
        if (child.type !== 'text') { visit(child); return [child]; }
        const result = []; let offset = 0;
        for (const match of child.value.matchAll(/\[\[([^\]\n]+)\]\]/g)) {
          if (match.index > offset) result.push({ type: 'text', value: child.value.slice(offset, match.index) });
          const [reference, label] = match[1].split('|');
          result.push({ type: 'link', url: wikiTarget(docPath, reference), children: [{ type: 'text', value: label || reference }] });
          offset = match.index + match[0].length;
        }
        if (!result.length) return [child];
        if (offset < child.value.length) result.push({ type: 'text', value: child.value.slice(offset) });
        return result;
      });
    }
    visit(tree);
  };
}
