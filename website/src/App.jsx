import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import MarkdownView from './MarkdownView.jsx';
import { assetURL, labels, parseRoute, readRoute, searchDocuments, shortTitle, staticURL } from './docs.mjs';

const REPOSITORY = 'https://github.com/Iheb-AG/praxis';
function Breadcrumb({ name }) {
  return <div className="page-meta"><div className="breadcrumb"><a href="#/">Documentation</a><span>/</span><span>{name}</span></div></div>;
}
function Footer({ catalog }) {
  return <footer className="footer"><span>Project Praxis · Documentation library · <a href={staticURL('THIRD_PARTY_NOTICES.txt')}>Dependency notices</a></span><span>Snapshot {catalog.snapshotHash.slice(0, 12)} · No connection to your board</span></footer>;
}
function DocLink({ path, children, className = '' }) { return <a className={className} href={readRoute(path)}>{children}</a>; }

function Sidebar({ catalog, activePath, open, search, setSearch, submit, input }) {
  return <aside id="sidebar" className={'sidebar' + (open ? ' is-open' : '')} aria-label="Documentation navigation">
    <form className="search-box" id="search-form" role="search" onSubmit={event => { event.preventDefault(); submit(); }}>
      <span aria-hidden="true">⌕</span><input ref={input} id="search" aria-label="Search all documentation" placeholder="Search documentation…" autoComplete="off" value={search} onChange={event => setSearch(event.target.value)} /><kbd>/</kbd>
    </form><a className="overview-link" href="#/"><span>◈</span> Project overview <span>↗</span></a>
    <nav id="document-nav" aria-label="Guides">{catalog.groups.map((group, index) => {
      const docs = catalog.documents.filter(doc => doc.collection === 'guides' && doc.group === group);
      if (!docs.length) return null;
      return <details className="nav-group" key={group} open={index < 2 || docs.some(doc => doc.path === activePath)}><summary>{group}</summary>
        {docs.map(doc => <a key={doc.path} href={readRoute(doc.path)} className={doc.path === activePath ? 'active' : ''} aria-current={doc.path === activePath ? 'page' : undefined}>{shortTitle(doc)}</a>)}</details>;
    })}<details className="nav-group" open><summary>Reference library</summary>{Object.entries(labels).filter(([id]) => id !== 'guides').map(([id, label]) =>
      <a key={id} href={'#/library?collection=' + id}>{label} <span className="nav-count">{catalog.documents.filter(doc => doc.collection === id).length}</span></a>)}</details></nav>
    <div className="sidebar-bottom"><strong>YOUR DOCUMENTATION, CONNECTED.</strong><p>Sources → knowledge → code → evidence</p><a href="#/library">Browse the full library <span>→</span></a></div>
  </aside>;
}

function Home({ catalog }) {
  const cards = [
    ['docs/system-design.md', '◫', 'Understand the architecture', 'How sources become trusted knowledge, and how the compiler, MCP services and coding assistant fit together.', 'Explore the system'],
    ['docs/sequences.md', '⇄', 'Follow the interactions', 'Trace ingestion, retrieval, compilation and hardware workflows through the project’s sequence diagrams.', 'View sequence diagrams'],
    ['README.md', '⌘', 'Run your first workflow', 'Set up Praxis, connect your MCP client and find the right instructions for your next firmware task.', 'Open the setup guide'],
  ];
  const flow = [
    ['docs/board-ingestion.md', '01', 'Engineering sources', 'Headers · manuals · netlists'],
    ['docs/manual-review-compiler.md', '02', 'Review & compile', 'Normalize · validate · publish'],
    ['docs/asset-contract.md', '03', 'Knowledge bundle', 'Indexed Markdown · provenance'],
    ['docs/AGENT_INSTRUCTIONS.md', '04', 'MCP & assistant', 'Retrieve · reason · generate'],
    ['docs/build-service.md', '05', 'Verify & observe', 'Build · approved board tests'],
  ];
  const row = (path, icon, text) => <DocLink path={path}><span className="list-icon">{icon}</span><span>{text}</span><span className="arrow">↗</span></DocLink>;
  return <><Breadcrumb name="Overview" />
    <section className="brand-banner" aria-label="Project Praxis octopus artwork and wordmark"><div className="banner-top"><span>PROJECT PRAXIS</span><span>LOCAL / VECTORLESS / SOURCE-BACKED</span></div><div className="banner-bottom"><span>ENGINEERING DOCUMENTATION</span><a href={REPOSITORY} target="_blank" rel="noopener noreferrer">View on GitHub ↗</a></div></section>
    <section className="hero"><div className="eyebrow">PROJECT PRAXIS / KNOWLEDGE LIBRARY</div><h1>From hardware knowledge<br />to <span>working understanding.</span></h1><p>A connected view of the project’s architecture, compiler, MCP tools and verification evidence. Explore the documentation without getting lost in a folder of Markdown files.</p>
      <div className="hero-actions"><DocLink path="docs/README.md" className="button primary">Start reading <span>→</span></DocLink><a className="button" href="#/library">Browse the library ↗</a></div>
      <div className="stats"><div className="stat"><strong>{catalog.documents.filter(doc => doc.collection === 'guides').length}</strong> project guides</div><div className="stat"><strong>{new Set(catalog.documents.filter(doc => doc.bundle).map(doc => doc.bundle)).size}</strong> bundle snapshots</div><div className="stat"><strong>{catalog.documents.reduce((n, doc) => n + doc.diagrams, 0)}</strong> diagrams</div><div className="stat"><strong>Local</strong> in-browser search</div></div>
    </section>
    <div className="section-heading"><h2>A good place to start</h2><a href="#/library?collection=guides">All guides →</a></div>
    <div className="cards">{cards.map(([path, icon, title, text, cta]) => <DocLink key={path} path={path} className="card"><span className="card-icon">{icon}</span><h3>{title}</h3><p>{text}</p><span className="card-footer">{cta}<span>↗</span></span></DocLink>)}</div>
    <div className="section-heading"><h2>The project, at a glance</h2><DocLink path="docs/system-design.md">Architecture in detail →</DocLink></div>
    <section className="flow-panel"><p className="flow-caption">Evidence moves through distinct stages. Each has its own responsibility.</p><div className="flow">{flow.map(([path, number, title, detail], index) => <div className="flow-step" key={path}>{index > 0 && <span className="flow-arrow">→</span>}<DocLink path={path} className="flow-node"><span className="step-number">{number}</span><strong>{title}</strong><small>{detail}</small></DocLink></div>)}</div></section>
    <div className="bottom-grid"><section><div className="section-heading"><h2>Implementation & evidence</h2></div><div className="reading-list">{row('docs/STATUS.md', '◷', 'Milestones and current project state')}{row('docs/reports/can-rx-results.md', '↗', 'Physical test: CAN RX loopback result')}{row('docs/PUBLICATION_READINESS.md', '✓', 'Release readiness and remaining gaps')}</div></section><section><div className="section-heading"><h2>Go further</h2></div><div className="reading-list">{row('docs/mcp-test-prompts.md', '⌘', 'MCP testing scenarios and prompts')}{row('bundles/stm32f407g-disc1-e01-arm-core-v2/wiki/index.md', '▦', 'STM32F407 Discovery · ARM core bundle')}{row('CONTRIBUTING.md', '+', 'Contribute a board, feature or workflow')}</div></section></div>
    <aside className="notice"><strong>Knowledge coverage and hardware qualification are different.</strong>This site presents the documentation as written, including blocked capabilities, historical results and known limitations. Consult the <DocLink path="docs/PUBLICATION_READINESS.md">publication assessment</DocLink> for current release claims.</aside><Footer catalog={catalog} />
  </>;
}

function Highlight({ text, terms }) {
  const words = terms.filter(term => /^[\p{L}\p{N}_-]+$/u.test(term));
  if (!words.length) return text;
  const pattern = new RegExp('(' + words.map(word => word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')', 'gi');
  return text.split(pattern).map((part, index) => index % 2 ? <mark key={index}>{part}</mark> : part);
}
function Library({ catalog, params }) {
  const q = params.get('q') || '', selected = params.get('collection') || '', bundle = params.get('bundle') || '';
  const results = useMemo(() => searchDocuments(catalog.documents, params), [catalog, params]);
  const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
  const collectionURL = value => '#/library?' + new URLSearchParams({ ...(q ? { q } : {}), ...(value ? { collection: value } : {}) });
  const bundles = [...new Set(catalog.documents.filter(doc => doc.bundle).map(doc => doc.bundle))].sort();
  return <><Breadcrumb name={q ? 'Search' : 'Library'} /><h1 className="library-title">{q ? 'Find it in the documentation.' : 'The complete library.'}</h1><p className="subheading">{q ? `Results for “${q}” across titles, paths and full document text.` : 'Guides, examples, reviewed evidence and every published bundle snapshot in one place.'}</p>
    <nav className="filters" aria-label="Filter collection"><a className={'filter ' + (!selected ? 'active' : '')} href={collectionURL('')}>Everything</a>{Object.entries(labels).map(([id, label]) => <a key={id} className={'filter ' + (selected === id ? 'active' : '')} href={collectionURL(id)}>{label}</a>)}</nav>
    {selected === 'bundles' && <><label className="subheading" htmlFor="bundle-select">Bundle revision </label><select className="bundle-select" id="bundle-select" value={bundle} onChange={event => { const next = new URLSearchParams(params); if (event.target.value) next.set('bundle', event.target.value); else next.delete('bundle'); window.location.hash = '/library?' + next; }}><option value="">All bundle revisions</option>{bundles.map(name => <option key={name} value={name}>{name}</option>)}</select></>}
    <p className="result-count" aria-live="polite">{results.length} {results.length === 1 ? 'document' : 'documents'}{bundle ? ' · ' + bundle : ''}</p>
    <div className="results">{results.map(({ doc, excerpt }) => <DocLink key={doc.path} path={doc.path} className="result"><span className="category">{labels[doc.collection]}{doc.bundle ? ' · ' + doc.bundle : ''}</span><h2><Highlight text={doc.title} terms={terms} /></h2><p><Highlight text={excerpt} terms={terms} /></p><div className="path"><Highlight text={doc.path} terms={terms} /></div></DocLink>)}</div>
    {!results.length && <div className="empty">No matching documents. Try a peripheral name, tool name or a shorter phrase.</div>}<Footer catalog={catalog} />
  </>;
}

function Attachment({ path, catalog }) {
  const [state, setState] = useState({ loading: true });
  useEffect(() => {
    const controller = new AbortController(); setState({ loading: true });
    fetch(assetURL(path), { signal: controller.signal }).then(response => { if (!response.ok) throw new Error('Supporting file is unavailable.'); return response.text(); })
      .then(text => setState({ text })).catch(error => { if (error.name !== 'AbortError') setState({ error: error.message }); });
    return () => controller.abort();
  }, [path]);
  return <><Breadcrumb name="Supporting source" /><h1 className="library-title">{path.split('/').pop()}</h1><div className="reader-top"><span className="source-path">{path}</span><a href={assetURL(path)} download>Download source ↗</a></div>
    {state.loading ? <div className="loading">Opening supporting file…</div> : state.error ? <p>{state.error}</p> : <pre className="attachment-content">{state.text}</pre>}<Footer catalog={catalog} /></>;
}
function Reader({ path, anchor, catalog, byPath, attachments, theme, notify }) {
  const doc = byPath.get(path), article = useRef(null), [headings, setHeadings] = useState([]), [active, setActive] = useState('');
  useEffect(() => {
    if (!doc || !article.current) { setHeadings([]); return; }
    const nodes = [...article.current.querySelectorAll('h2,h3')];
    setHeadings(nodes.map(node => ({ id: node.id, title: node.textContent, level: node.tagName.slice(1) })));
    const observer = new IntersectionObserver(entries => { const visible = entries.find(entry => entry.isIntersecting); if (visible) setActive(visible.target.id); }, { rootMargin: '-90px 0px -70% 0px' });
    nodes.forEach(node => observer.observe(node)); return () => observer.disconnect();
  }, [doc]);
  useEffect(() => {
    if (!anchor) return;
    const frame = requestAnimationFrame(() => document.getElementById(anchor)?.scrollIntoView());
    return () => cancelAnimationFrame(frame);
  }, [doc, anchor]);
  if (!doc) return attachments.has(path) ? <Attachment key={path} path={path} catalog={catalog} />
    : <><Breadcrumb name="Not found" /><h1>Document not found.</h1><p>This path is not in the documentation snapshot.</p><a className="button" href="#/library">Browse the library →</a></>;
  return <><Breadcrumb name={labels[doc.collection]} /><div className="reader-layout"><div className="reader">
    <div className="reader-top"><span className="source-path">{path}</span><span>{Math.max(1, Math.ceil(doc.words / 220))} min read</span><a href={assetURL(path)} download>Download .md ↗</a><button id="print-page" onClick={() => window.print()}>Print</button></div>
    <article ref={article} className="markdown"><MarkdownView doc={doc} byPath={byPath} attachments={attachments} theme={theme} notify={notify} /></article>
    <div className="doc-end"><a href={'#/library?collection=' + doc.collection}>← {labels[doc.collection]}</a><DocLink path="docs/README.md">Reading guide →</DocLink></div><Footer catalog={catalog} /></div>
    <aside className="toc" aria-label="On this page"><strong>On this page</strong><nav>{headings.map(heading => <a key={heading.id} className={`level-${heading.level}` + (active === heading.id ? ' active' : '')} href={readRoute(path, heading.id)}>{heading.title}</a>)}{!headings.length && <span>No sections</span>}</nav></aside>
  </div></>;
}

export default function App() {
  const [catalog, setCatalog] = useState(null), [error, setError] = useState(''), [hash, setHash] = useState(window.location.hash);
  const [theme, setTheme] = useState(() => { try { return localStorage.getItem('praxis-docs-theme-v2') === 'light' ? 'light' : 'dark'; } catch { return 'dark'; } });
  const [menuOpen, setMenuOpen] = useState(false), [search, setSearch] = useState(''), [toast, setToast] = useState(''), [backTop, setBackTop] = useState(false);
  const input = useRef(null), searchTimer = useRef(null), toastTimer = useRef(null);
  const route = useMemo(() => parseRoute(hash), [hash]);
  const byPath = useMemo(() => new Map(catalog?.documents.map(doc => [doc.path, doc]) || []), [catalog]);
  const attachments = useMemo(() => new Set(catalog?.attachments || []), [catalog]);
  const notify = useCallback(message => { setToast(message); clearTimeout(toastTimer.current); toastTimer.current = setTimeout(() => setToast(''), 4500); }, []);
  useEffect(() => {
    const controller = new AbortController();
    fetch(staticURL('catalog.json'), { signal: controller.signal }).then(response => { if (!response.ok) throw new Error('Documentation catalog is unavailable.'); return response.json(); })
      .then(next => { if (!Array.isArray(next.documents) || !Array.isArray(next.attachments)) throw new Error('Invalid documentation catalog.'); setCatalog(next); })
      .catch(failure => { if (failure.name !== 'AbortError') setError(failure.message); });
    return () => controller.abort();
  }, []);
  useEffect(() => { const change = () => setHash(window.location.hash); window.addEventListener('hashchange', change); return () => window.removeEventListener('hashchange', change); }, []);
  useEffect(() => { document.documentElement.dataset.theme = theme; try { localStorage.setItem('praxis-docs-theme-v2', theme); } catch { /* Storage may be disabled. */ } }, [theme]);
  useEffect(() => {
    clearTimeout(searchTimer.current); setSearch(route.kind === 'library' ? route.params.get('q') || '' : ''); setMenuOpen(false);
    if (!route.params.has('anchor')) window.scrollTo({ top: 0, behavior: 'instant' });
    document.title = route.path && byPath.has(route.path) ? shortTitle(byPath.get(route.path)) + ' — Praxis Docs' : 'Praxis — Documentation';
  }, [route, byPath]);
  useEffect(() => {
    const scroll = () => setBackTop(window.scrollY > 500);
    const key = event => {
      if ((event.key === '/' || ((event.ctrlKey || event.metaKey) && event.key === 'k')) && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { event.preventDefault(); input.current?.focus(); input.current?.select(); }
      if (event.key === 'Escape') { input.current?.blur(); setMenuOpen(false); }
    };
    window.addEventListener('scroll', scroll, { passive: true }); document.addEventListener('keydown', key);
    return () => { window.removeEventListener('scroll', scroll); document.removeEventListener('keydown', key); clearTimeout(searchTimer.current); clearTimeout(toastTimer.current); };
  }, []);
  const searchNow = value => { clearTimeout(searchTimer.current); window.location.hash = '/library' + (value.trim() ? '?q=' + encodeURIComponent(value.trim()) : ''); };
  const changeSearch = value => { setSearch(value); clearTimeout(searchTimer.current); searchTimer.current = setTimeout(() => searchNow(value), 180); };
  const active = route.kind === 'reader' ? byPath.get(route.path)?.collection : route.kind === 'library' ? route.params.get('collection') : 'home';
  return <><a className="skip" href="#main" onClick={event => { event.preventDefault(); document.getElementById('main')?.focus(); }}>Skip to content</a>
    <header className="topbar"><button className="icon-button mobile-menu" id="menu-button" aria-label="Toggle navigation" aria-expanded={menuOpen} onClick={() => setMenuOpen(value => !value)}>☰</button>
      <a className="brand" href="#/" aria-label="Praxis documentation home"><span className="brand-mark"><img src={staticURL('branding/praxis-logo.png')} alt="" width="669" height="373" /></span><span>praxis<span className="brand-divider">/</span><span className="brand-label">docs</span></span></a>
      <nav className="top-nav" aria-label="Main"><a href={REPOSITORY} target="_blank" rel="noopener noreferrer">GitHub ↗</a>{[['home', '#/', 'Overview'], ['guides', '#/library?collection=guides', 'Guides'], ['bundles', '#/library?collection=bundles', 'Bundles'], ['examples', '#/library?collection=examples', 'Examples']].map(([id, href, label]) => <a key={id} href={href} data-nav={id} className={active === id ? 'active' : ''}>{label}</a>)}</nav>
      <div className="top-actions"><span className="offline"><i /> Experimental alpha</span><button className="icon-button" id="theme-button" aria-label={'Switch to ' + (theme === 'dark' ? 'light' : 'dark') + ' theme'} title="Switch theme" onClick={() => setTheme(value => value === 'dark' ? 'light' : 'dark')}>◐</button></div>
    </header><div className="layout">{catalog && <Sidebar catalog={catalog} activePath={route.path} open={menuOpen} search={search} setSearch={changeSearch} submit={() => searchNow(search)} input={input} />}
      <main id="main" tabIndex={-1}>{error ? <div className="empty"><h1>The documentation could not be opened.</h1><p>{error}</p><p>Refresh the page or check the site build.</p></div> : !catalog ? <div className="loading">Opening your documentation…</div>
        : route.kind === 'library' ? <Library catalog={catalog} params={route.params} />
          : route.kind === 'reader' ? <Reader key={route.path} path={route.path} anchor={route.params.get('anchor') || ''} catalog={catalog} byPath={byPath} attachments={attachments} theme={theme} notify={notify} /> : <Home catalog={catalog} />}</main>
    </div><button id="back-top" className="back-top icon-button" aria-label="Back to top" hidden={!backTop} onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>↑</button>{toast && <div id="toast" className="toast" role="status">{toast}</div>}
  </>;
}
