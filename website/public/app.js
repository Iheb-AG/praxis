'use strict';

const main = document.querySelector('#main');
const search = document.querySelector('#search');
const labels = {guides: 'Guides', examples: 'Examples', bundles: 'Knowledge bundles', reviews: 'Reviewed sources', assets: 'Firmware assets'};
let catalog, byPath, attachmentPaths, renderRevision = 0, searchTimer, toastTimer;
const esc = value => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const readRoute = (path, anchor = '') => '#/read/' + encodeURIComponent(path) + (anchor ? '?anchor=' + encodeURIComponent(anchor) : '');
const assetURL = path => 'content/' + path.split('/').map(encodeURIComponent).join('/');
const link = (path, label, cls = '') => `<a class="${cls}" href="${readRoute(path)}">${label}</a>`;
const slug = text => text.toLowerCase().trim().replace(/[^\p{L}\p{N}\s_-]/gu, '').replace(/\s/g, '-');
function notify(message) {
  const toast = document.querySelector('#toast');
  toast.textContent = message; toast.hidden = false;
  clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.hidden = true, 4500);
}
function theme() {
  return document.documentElement.dataset.theme === 'dark' ? 'dark' : 'default';
}
function setTheme(value) {
  document.documentElement.dataset.theme = value;
  try { localStorage.setItem('praxis-docs-theme-v2', value); } catch {}
  document.querySelector('#theme-button').setAttribute('aria-label', `Switch to ${value === 'dark' ? 'light' : 'dark'} theme`);
}
try { setTheme(localStorage.getItem('praxis-docs-theme-v2') || 'dark'); } catch { setTheme('dark'); }
document.querySelector('#theme-button').addEventListener('click', () => {
  setTheme(theme() === 'dark' ? 'light' : 'dark'); route(false);
});
document.querySelector('#menu-button').addEventListener('click', () => {
  const open = document.querySelector('#sidebar').classList.toggle('is-open');
  document.querySelector('#menu-button').setAttribute('aria-expanded', String(open));
});
document.querySelector('#close-diagram').addEventListener('click', () => document.querySelector('#diagram-dialog').close());
document.querySelector('#diagram-dialog').addEventListener('click', event => {
  if (event.target === event.currentTarget) event.currentTarget.close();
});
document.querySelector('#back-top').addEventListener('click', () => window.scrollTo({top:0, behavior:'smooth'}));
window.addEventListener('scroll', () => document.querySelector('#back-top').hidden = window.scrollY < 500, {passive:true});
document.addEventListener('keydown', event => {
  if ((event.key === '/' || ((event.ctrlKey || event.metaKey) && event.key === 'k')) && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
    event.preventDefault(); search.focus(); search.select();
  }
  if (event.key === 'Escape') { search.blur(); document.querySelector('#sidebar').classList.remove('is-open'); document.querySelector('#menu-button').setAttribute('aria-expanded','false'); }
});
document.querySelector('#search-form').addEventListener('submit', event => {event.preventDefault(); navigateSearch();});
search.addEventListener('input', () => {clearTimeout(searchTimer); searchTimer = setTimeout(navigateSearch, 180);});
function navigateSearch() {
  const hash = '#/library' + (search.value.trim() ? '?q=' + encodeURIComponent(search.value.trim()) : '');
  if (location.hash === hash) route(); else location.hash = hash;
}
function breadcrumb(name) {
  return `<div class="page-meta"><div class="breadcrumb"><a href="#/">Documentation</a><span>/</span><span>${esc(name)}</span></div><span class="pill">Read-only snapshot</span></div>`;
}
function footer() {
  return `<footer class="footer"><span>Project Praxis · Documentation library</span><span>Snapshot ${catalog.snapshotHash.slice(0,12)} · No connection to your board</span></footer>`;
}
function buildNavigation() {
  const target = document.querySelector('#document-nav');
  target.innerHTML = catalog.groups.map((group, index) => {
    const docs = catalog.documents.filter(d => d.collection === 'guides' && d.group === group);
    const priority = {
      'Start here':['README.md','README_DETAILED.md','docs/README.md','docs/system-design.md','docs/architecture.md','docs/sequences.md','docs/asset-contract.md'],
      'Project & contribution':['CHANGELOG.md','docs/STATUS.md','docs/PUBLICATION_READINESS.md','CONTRIBUTING.md'],
    }[group];
    if (priority) docs.sort((a,b)=>priority.indexOf(a.path)-priority.indexOf(b.path));
    if (!docs.length) return '';
    return `<details class="nav-group" ${index < 2 ? 'open' : ''}><summary>${esc(group)}</summary>${docs.map(doc => link(doc.path, esc(shortTitle(doc)))).join('')}</details>`;
  }).join('') + `<details class="nav-group" open><summary>Reference library</summary>${Object.entries(labels).filter(([id]) => id !== 'guides').map(([id,label]) => `<a href="#/library?collection=${id}">${label} <span style="float:right;color:var(--muted)">${catalog.documents.filter(d => d.collection === id).length}</span></a>`).join('')}</details>`;
}
function shortTitle(doc) {
  const names = {
    'README.md':'Getting started', 'README_DETAILED.md':'Detailed setup guide', 'CHANGELOG.md':'Changelog', 'docs/README.md':'Documentation guide', 'docs/system-design.md':'System design & theory',
    'docs/architecture.md':'Architecture & modules', 'docs/sequences.md':'Sequence diagrams', 'docs/asset-contract.md':'Knowledge & firmware assets',
    'docs/STATUS.md':'Milestone status', 'docs/PUBLICATION_READINESS.md':'Publication readiness',
    'docs/AGENT_INSTRUCTIONS.md':'Agent instructions', 'CONTRIBUTING.md':'Contributing',
  };
  return names[doc.path] || doc.title.replace(/^Project Praxis\s*[:—–-]?\s*/i,'');
}
function home() {
  const docs = catalog.documents;
  const bundleCount = new Set(docs.filter(d => d.bundle).map(d => d.bundle)).size;
  const diagrams = docs.reduce((n,d) => n+d.diagrams,0);
  const cards = [
    ['docs/system-design.md','◫','Understand the architecture','How sources become trusted knowledge, and how the compiler, MCP services and coding assistant fit together.','Explore the system'],
    ['docs/sequences.md','⇄','Follow the interactions','Trace ingestion, retrieval, compilation and hardware workflows through the project’s sequence diagrams.','View sequence diagrams'],
    ['README.md','⌘','Run your first workflow','Set up Praxis, connect your MCP client and find the right instructions for your next firmware task.','Open the setup guide'],
  ];
  const row = (path, icon, text) => link(path, `<span class="list-icon">${icon}</span><span>${text}</span><span class="arrow">↗</span>`);
  main.innerHTML = breadcrumb('Overview') + `
    <section class="brand-banner" aria-label="Project Praxis octopus artwork and wordmark">
      <div class="banner-top"><span>PROJECT PRAXIS</span><span>LOCAL / VECTORLESS / SOURCE-BACKED</span></div>
      <div class="banner-bottom">${window.praxisMonitor ? '<span>DOCUMENTATION & PROGRESS</span><a href="#/progress">Follow the implementation ↗</a>' : '<span>ENGINEERING DOCUMENTATION</span><a href="https://github.com/Iheb-AG/praxis" target="_blank" rel="noopener noreferrer">View on GitHub ↗</a>'}</div>
    </section>
    <section class="hero"><div class="eyebrow">PROJECT PRAXIS / KNOWLEDGE LIBRARY</div><h1>From hardware knowledge<br>to <span>working understanding.</span></h1><p>A connected view of the project’s architecture, compiler, MCP tools and verification evidence. Explore the documentation without getting lost in a folder of Markdown files.</p><div class="hero-actions">${link('docs/README.md','Start reading <span>→</span>','button primary')}<a class="button" href="#/library">Browse the library <span>↗</span></a></div><div class="stats"><div class="stat"><strong>${docs.filter(d=>d.collection==='guides').length}</strong> project guides</div><div class="stat"><strong>${bundleCount}</strong> bundle snapshots</div><div class="stat"><strong>${diagrams}</strong> diagrams</div><div class="stat"><strong>Local</strong> in-browser search</div></div></section>
    <div class="section-heading"><h2>A good place to start</h2><a href="#/library?collection=guides">All guides →</a></div>
    <div class="cards">${cards.map(([path,icon,title,text,cta]) => link(path,`<span class="card-icon">${icon}</span><h3>${title}</h3><p>${text}</p><span class="card-footer">${cta}<span>↗</span></span>`,'card')).join('')}</div>
    <div class="section-heading"><h2>The project, at a glance</h2>${link('docs/system-design.md','Architecture in detail →')}</div>
    <section class="flow-panel"><p class="flow-caption">Evidence moves through distinct stages. Each has its own responsibility.</p><div class="flow">${[
      ['docs/board-ingestion.md','01','Engineering sources','Headers · manuals · netlists'],
      ['docs/manual-review-compiler.md','02','Review & compile','Normalize · validate · publish'],
      ['docs/asset-contract.md','03','Knowledge bundle','Indexed Markdown · provenance'],
      ['docs/AGENT_INSTRUCTIONS.md','04','MCP & assistant','Retrieve · reason · generate'],
      ['docs/build-service.md','05','Verify & observe','Build · approved board tests'],
    ].map(([path,num,title,detail],i) => `${i ? '<span class="flow-arrow">→</span>' : ''}${link(path,`<span class="step-number">${num}</span><strong>${title}</strong><small>${detail}</small>`,'flow-node')}`).join('')}</div></section>
    <div class="bottom-grid"><section><div class="section-heading"><h2>Implementation & evidence</h2></div><div class="reading-list">${row('docs/STATUS.md','◷','Milestones and current project state')}${row('docs/reports/can-rx-results.md','↗','Latest physical test: CAN RX loopback result')}${row('docs/PUBLICATION_READINESS.md','✓','Release readiness and remaining gaps')}</div></section><section><div class="section-heading"><h2>Go further</h2></div><div class="reading-list">${row('docs/mcp-test-prompts.md','⌘','MCP testing scenarios and prompts')}${row('bundles/stm32f407g-disc1-e01-can-rx-v1/wiki/index.md','▦','STM32F407 Discovery · CAN RX bundle')}${row('CONTRIBUTING.md','+','Contribute a board, feature or workflow')}</div></section></div>
    <aside class="notice"><strong>Knowledge coverage and hardware qualification are different.</strong>This site presents the documentation as written, including blocked capabilities, historical results and known limitations. Consult the ${link('docs/PUBLICATION_READINESS.md','publication assessment')} for current release claims.</aside>${footer()}`;
}
function highlight(text, words) {
  let html = esc(text);
  const safeWords = words.filter(w => /^[\p{L}\p{N}_-]+$/u.test(w));
  if (!safeWords.length) return html;
  return html.replace(new RegExp('(' + safeWords.map(w => w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|') + ')','gi'), '<mark>$1</mark>');
}
function library(params) {
  const q = params.get('q') || '', selected = params.get('collection') || '', bundle = params.get('bundle') || '';
  const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
  let results = catalog.documents.filter(d => (!selected || selected === d.collection) && (!bundle || d.bundle === bundle));
  results = results.map(doc => {
    const title = doc.title.toLowerCase(), path = doc.path.toLowerCase(), body = doc.content.toLowerCase();
    if (!terms.every(t => title.includes(t) || path.includes(t) || body.includes(t))) return null;
    const score = terms.reduce((n,t) => n + (title.includes(t)?15:0) + (path.includes(t)?7:0) + (body.includes(t)?1:0),0) + (doc.collection === 'guides' ? 3 : 0);
    let excerpt = doc.summary;
    if (q && terms.length && !terms.some(t => excerpt.toLowerCase().includes(t))) {
      const i = body.indexOf(terms[0]); if (i >= 0) excerpt = (i > 60 ? '…' : '') + doc.content.slice(Math.max(0,i-60),i+180).replace(/\s+/g,' ') + '…';
    }
    return {doc,score,excerpt};
  }).filter(Boolean).sort((a,b) => b.score-a.score || a.doc.path.localeCompare(b.doc.path));
  const collectionURL = value => '#/library?' + new URLSearchParams({...q ? {q} : {}, ...value ? {collection:value} : {}});
  const bundles = [...new Set(catalog.documents.filter(d=>d.bundle).map(d=>d.bundle))].sort();
  main.innerHTML = breadcrumb(q ? 'Search' : 'Library') + `<h1 class="library-title">${q ? 'Find it in the documentation.' : 'The complete library.'}</h1><p class="subheading">${q ? `Results for “${esc(q)}” across titles, paths and full document text.` : 'Guides, examples, reviewed evidence and every published bundle snapshot in one place.'}</p><nav class="filters" aria-label="Filter collection"><a class="filter ${!selected?'active':''}" href="${collectionURL('')}">Everything</a>${Object.entries(labels).map(([id,label]) => `<a class="filter ${selected===id?'active':''}" href="${collectionURL(id)}">${label}</a>`).join('')}</nav>${selected === 'bundles' ? `<label class="subheading" for="bundle-select">Bundle revision </label><select class="bundle-select" id="bundle-select"><option value="">All bundle revisions</option>${bundles.map(b=>`<option value="${esc(b)}" ${bundle===b?'selected':''}>${esc(b)}</option>`).join('')}</select>` : ''}<p class="result-count">${results.length} ${results.length===1?'document':'documents'}${bundle?' · '+esc(bundle):''}</p><div class="results">${results.map(({doc,excerpt}) => link(doc.path,`<span class="category">${labels[doc.collection]}${doc.bundle?' · '+esc(doc.bundle):''}</span><h2>${highlight(doc.title,terms)}</h2><p>${highlight(excerpt || doc.path,terms)}</p><div class="path">${highlight(doc.path,terms)}</div>`,'result')).join('')}</div>${!results.length?'<div class="empty">No matching documents. Try a peripheral name, tool name or a shorter phrase.</div>':''}${footer()}`;
  document.querySelector('#bundle-select')?.addEventListener('change', event => {
    const next = new URLSearchParams(params); next.set('collection','bundles');
    if (event.target.value) next.set('bundle',event.target.value); else next.delete('bundle');
    location.hash = '#/library?' + next;
  });
}
function normalizePath(parts) {
  const result = [];
  for (const part of parts.split('/')) {
    if (!part || part === '.') continue;
    if (part === '..') { if (!result.length) return null; result.pop(); } else result.push(part);
  }
  return result.join('/');
}
function wikiTarget(doc, reference) {
  const [path, anchor=''] = reference.split('#');
  const bundleRoot = doc.path.includes('/wiki/') ? doc.path.split('/wiki/')[0] + '/wiki/' : doc.path.slice(0,doc.path.lastIndexOf('/')+1);
  return {path:normalizePath(bundleRoot + path.replace(/\.md$/,'') + '.md'), anchor};
}
function renderMarkdown(doc) {
  const renderer = new marked.Renderer();
  renderer.html = ({text}) => esc(text);
  renderer.image = ({href,text}) => `<img data-source="${esc(href)}" alt="${esc(text)}">`;
  const wikiExtension = {name:'wikilink',level:'inline',start:src=>src.indexOf('[['),tokenizer(src){
    const match = /^\[\[([^\]\n]+)\]\]/.exec(src);
    if (match) return {type:'wikilink',raw:match[0],text:match[1]};
  },renderer(token){
    const [reference,label] = token.text.split('|');
    const target = wikiTarget(doc,reference);
    return `<a href="${esc(readRoute(target.path,target.anchor))}" data-wiki="true">${esc(label || reference)}</a>`;
  }};
  const parser = new marked.Marked({gfm:true,breaks:false,renderer,extensions:[wikiExtension]});
  return DOMPurify.sanitize(parser.parse(doc.content), {ADD_ATTR:['data-wiki'], FORBID_TAGS:['style','iframe','form','input'],FORBID_ATTR:['style']});
}
function rewriteLinks(root, doc) {
  root.querySelectorAll('a').forEach(anchor => {
    const raw = anchor.getAttribute('href');
    if (!raw || anchor.dataset.wiki) return;
    if (/^https?:\/\//i.test(raw)) { anchor.target='_blank';anchor.rel='noopener noreferrer';return; }
    if (/^(mailto:|tel:)/i.test(raw)) return;
    if (raw.startsWith('#/')) return;
    if (/^[a-z][a-z0-9+.-]*:/i.test(raw)) {anchor.removeAttribute('href');return;}
    const url = new URL(raw,'https://local.invalid/' + doc.path);
    const path = decodeURIComponent(url.pathname.replace(/^\//,''));
    const fragment = decodeURIComponent(url.hash.slice(1));
    const target = raw.startsWith('#') ? doc.path : path;
    if (byPath.has(target) || attachmentPaths.has(target)) anchor.href=readRoute(target,fragment);
    else if (byPath.has(target.replace(/\/$/,'') + '/README.md')) anchor.href=readRoute(target.replace(/\/$/,'') + '/README.md');
    else {
      anchor.href='#'; anchor.title='This reference is outside the public documentation snapshot: '+raw;
      anchor.addEventListener('click',event=>{event.preventDefault();notify('Outside this snapshot: '+raw);});
    }
  });
  root.querySelectorAll('img').forEach(img => {
    const raw = img.getAttribute('data-source') || img.getAttribute('src') || '';
    const url = new URL(raw, 'https://local.invalid/' + doc.path);
    const path = decodeURIComponent(url.pathname.replace(/^\//,''));
    if (url.origin === 'https://local.invalid' && attachmentPaths.has(path) && /\.(png|jpe?g|webp|gif)$/i.test(path)) {
      img.src = assetURL(path); img.loading = 'lazy';
    } else {
      img.replaceWith(Object.assign(document.createElement('span'),{textContent:img.alt || '[External image]'}));
    }
  });
}
async function copyText(text, button) {
  try {await navigator.clipboard.writeText(text);button.textContent='Copied';setTimeout(()=>button.textContent='Copy',1600);}
  catch {notify('Copy is unavailable in this browser. Select the code to copy it.');}
}
function diagramCard(code) {
  const card = document.createElement('section'); card.className='diagram-card';
  card.innerHTML=`<div class="diagram-toolbar"><span>Mermaid diagram</span><button data-action="out" aria-label="Zoom diagram out">−</button><button data-action="fit">Fit</button><button data-action="in" aria-label="Zoom diagram in">+</button><button data-action="expand">Expand ↗</button></div><div class="diagram-viewport"><div class="loading">Rendering diagram…</div></div><details class="diagram-source"><summary>View diagram source</summary><pre><code>${esc(code)}</code></pre></details>`;
  let naturalWidth=800, naturalHeight=500, ratio=1, svg;
  const viewport = card.querySelector('.diagram-viewport');
  const update = () => {if (svg) {
    const width=Math.max(200,naturalWidth*ratio),height=width*naturalHeight/naturalWidth;
    svg.style.width=width+'px';svg.style.height=height+'px';svg.setAttribute('width',String(width));svg.setAttribute('height',String(height));
  }};
  card.querySelector('.diagram-toolbar').addEventListener('click',event=>{
    const action=event.target.dataset.action;if (!action || !svg) return;
    if (action==='expand') {
      const copy=svg.cloneNode(true),width=Math.min(1800,Math.max(900,naturalWidth));
      copy.style.width=width+'px';copy.style.height=width*naturalHeight/naturalWidth+'px';
      document.querySelector('#expanded-diagram').replaceChildren(copy);document.querySelector('#diagram-dialog').showModal();return;
    }
    if (action==='fit') ratio=Math.min(1,(viewport.clientWidth-36)/naturalWidth);
    if (action==='in') ratio=Math.min(4,ratio*1.25);
    if (action==='out') ratio=Math.max(.15,ratio/1.25);
    update();
  });
  card.draw = async (id,revision) => {
    try {
      // Sequence-message semicolons are literal text in the authored documents.
      // Mermaid treats bare semicolons as statement separators; escape them only
      // in the rendering input, keeping the original snapshot and source intact.
      const renderSource = /^\s*sequenceDiagram/m.test(code) ? code.split('\n').map(line=>{
        const colon=line.indexOf(':');
        return colon<0 || line.trim().startsWith('%%') ? line : line.slice(0,colon+1)+line.slice(colon+1).replaceAll(';','#59;');
      }).join('\n') : code;
      const result = await mermaid.render(id,renderSource);
      if (revision !== renderRevision || !card.isConnected) return;
      viewport.innerHTML=DOMPurify.sanitize(result.svg,{USE_PROFILES:{svg:true,svgFilters:true},ADD_TAGS:['style','foreignObject','div','span','p'],ADD_ATTR:['xmlns','class','style']});
      svg=viewport.querySelector('svg');
      const viewBox=svg?.viewBox.baseVal;
      naturalWidth=viewBox?.width || parseFloat(svg?.getAttribute('width')) || 800;
      naturalHeight=viewBox?.height || parseFloat(svg?.getAttribute('height')) || 500;
      ratio=Math.min(1,(viewport.clientWidth-36)/naturalWidth);update();
    } catch(error) {
      if (revision !== renderRevision || !card.isConnected) return;
      viewport.innerHTML=`<div class="diagram-error">This diagram could not be rendered. Its complete source is available below.</div>`;
      console.warn('Diagram rendering failed',error.message);
    }
  };
  return card;
}
async function readDocument(path, anchor, revision) {
  const doc=byPath.get(path);
  if (!doc) {
    if (attachmentPaths.has(path)) return readAttachment(path,revision);
    main.innerHTML=breadcrumb('Not found')+'<h1>Document not found.</h1><p>This path is not in the documentation snapshot.</p><a class="button" href="#/library">Browse the library →</a>';return;
  }
  document.title=shortTitle(doc)+' — Praxis Docs';
  main.innerHTML=breadcrumb(labels[doc.collection]) + `<div class="reader-layout"><div class="reader"><div class="reader-top"><span class="source-path">${esc(path)}</span><span>${Math.max(1,Math.ceil(doc.words/220))} min read</span><a href="${assetURL(path)}" download>Download .md ↗</a><button id="print-page">Print</button></div><article class="markdown">${renderMarkdown(doc)}</article><div class="doc-end"><a href="#/library?collection=${doc.collection}">← ${labels[doc.collection]}</a>${link('docs/README.md','Reading guide →')}</div>${footer()}</div><aside class="toc" aria-label="On this page"><strong>On this page</strong><nav></nav></aside></div>`;
  document.querySelector('#print-page').addEventListener('click',()=>window.print());
  const article=main.querySelector('.markdown');
  rewriteLinks(article,doc);
  const ids=new Map();
  article.querySelectorAll('h1,h2,h3,h4').forEach(heading=>{
    const base=slug(heading.textContent),count=ids.get(base)||0;
    heading.id=base+(count?'-'+count:'');ids.set(base,count+1);
  });
  const toc=main.querySelector('.toc nav');
  const headings=[...article.querySelectorAll('h2,h3')];
  toc.innerHTML=headings.map(h=>`<a class="level-${h.tagName.slice(1)}" href="${readRoute(path,h.id)}">${esc(h.textContent)}</a>`).join('') || '<span>No sections</span>';
  article.querySelectorAll('table').forEach(table=>{const wrapper=document.createElement('div');wrapper.className='table-wrap';wrapper.tabIndex=0;wrapper.setAttribute('role','region');wrapper.setAttribute('aria-label','Scrollable documentation table');table.replaceWith(wrapper);wrapper.append(table);});
  const diagrams=[];
  article.querySelectorAll('pre > code').forEach(code=>{
    const pre=code.parentElement;
    if (code.classList.contains('language-mermaid')) {
      const card=diagramCard(code.textContent);pre.replaceWith(card);diagrams.push(card);
    } else {
      const wrapper=document.createElement('div');wrapper.className='code-wrap';pre.replaceWith(wrapper);wrapper.append(pre);
      const button=document.createElement('button');button.className='copy-button';button.textContent='Copy';button.setAttribute('aria-label','Copy code block');button.addEventListener('click',()=>copyText(code.textContent,button));wrapper.append(button);
    }
  });
  if (anchor) requestAnimationFrame(()=>document.getElementById(anchor)?.scrollIntoView());
  mermaid.initialize({startOnLoad:false,securityLevel:'strict',theme:'base',themeVariables:{darkMode:theme()==='dark',background:theme()==='dark'?'#11151b':'#ffffff',primaryColor:theme()==='dark'?'#162a33':'#e8f5f8',primaryTextColor:theme()==='dark'?'#f4f6f8':'#17212b',primaryBorderColor:theme()==='dark'?'#7cc7e6':'#00687d',lineColor:theme()==='dark'?'#a7b1be':'#536474',secondaryColor:theme()==='dark'?'#1a242d':'#edf2f6',tertiaryColor:theme()==='dark'?'#20282f':'#f0f4f7',textColor:theme()==='dark'?'#d8dee7':'#293440',actorBkg:theme()==='dark'?'#162a33':'#e8f5f8',actorTextColor:theme()==='dark'?'#f4f6f8':'#17212b',actorBorder:theme()==='dark'?'#7cc7e6':'#00687d',signalColor:theme()==='dark'?'#d8dee7':'#293440',signalTextColor:theme()==='dark'?'#d8dee7':'#293440',noteBkgColor:theme()==='dark'?'#20282f':'#edf2f6',noteTextColor:theme()==='dark'?'#d8dee7':'#293440'},suppressErrorRendering:true,maxTextSize:150000,flowchart:{htmlLabels:false},sequence:{useMaxWidth:false},fontFamily:'Segoe UI, system-ui, sans-serif'});
  for (let i=0;i<diagrams.length;i++) {
    if (revision !== renderRevision) return;
    await diagrams[i].draw(`diagram-${revision}-${i}`,revision);
  }
  if (anchor && revision === renderRevision) document.getElementById(anchor)?.scrollIntoView();
}
async function readAttachment(path,revision) {
  main.innerHTML=breadcrumb('Supporting source')+'<div class="loading">Opening supporting file…</div>';
  try {
    const response=await fetch(assetURL(path));if (!response.ok) throw new Error('File unavailable');
    let text=await response.text();
    if (revision!==renderRevision) return;
    if (path.endsWith('.json')) {try{text=JSON.stringify(JSON.parse(text),null,2);}catch{}}
    document.title=path.split('/').pop()+' — Praxis Docs';
    main.innerHTML=breadcrumb('Supporting source')+`<h1 class="library-title">${esc(path.split('/').pop())}</h1><div class="reader-top"><span class="source-path">${esc(path)}</span><a href="${assetURL(path)}" download>Download source ↗</a></div><pre class="attachment-content">${esc(text)}</pre>${footer()}`;
  } catch {if (revision===renderRevision) main.innerHTML=breadcrumb('Error')+'<p>This supporting file could not be loaded. Refresh the snapshot and try again.</p>';}
}
async function route(resetScroll=true) {
  if (!catalog) return;
  const revision=++renderRevision;
  const hash=location.hash.slice(1)||'/',[page,query='']=hash.split('?'),params=new URLSearchParams(query);
  const path=page.startsWith('/read/')?decodeURIComponent(page.slice(6)):null;
  document.title='Praxis — Documentation';
  if (page==='/progress') { search.value='';if (window.praxisMonitor) window.praxisMonitor.render();else await readDocument('docs/STATUS.md','',revision); } else if (page==='/library') {
    search.value=params.get('q')||'';library(params);
  } else if (path) { search.value='';await readDocument(path,params.get('anchor')||'',revision); }
  else {search.value='';home();}
  if (revision!==renderRevision) return;
  const active=path ? byPath.get(path)?.collection : (page==='/progress' ? 'progress' : page==='/library' ? params.get('collection') : 'home');
  document.querySelectorAll('[data-nav]').forEach(a=>a.classList.toggle('active',a.dataset.nav===active));
  document.querySelectorAll('#document-nav a').forEach(a=>{
    const current=a.getAttribute('href')===readRoute(path);a.classList.toggle('active',current);
    if (current) {a.closest('details').open=true;a.setAttribute('aria-current','page');}else a.removeAttribute('aria-current');
  });
  if (resetScroll && !params.has('anchor')) window.scrollTo({top:0,behavior:'instant'});
  document.querySelector('#sidebar').classList.remove('is-open');
  document.querySelector('#menu-button').setAttribute('aria-expanded','false');
}
window.addEventListener('hashchange',()=>{route().catch(error=>{console.error(error);notify('Could not open this page. Try the library.');});});
async function init() {
  const response=await fetch('catalog.json');
  if (!response.ok) throw new Error('Documentation catalog is missing. Run sync_docs.py.');
  catalog=await response.json();byPath=new Map(catalog.documents.map(doc=>[doc.path,doc]));attachmentPaths=new Set(catalog.attachments);
  buildNavigation();await route();window.praxisMonitor?.start();
}
init().catch(error=>{main.innerHTML=`<div class="empty"><h1>The documentation could not be opened.</h1><p>${esc(error.message)}</p><p>The documentation snapshot could not be loaded. Refresh the page or check the site build.</p></div>`;console.error(error);});

// Server-pushed public snapshot refresh; no changes to the source repository.
window.refreshPraxisCatalog = async () => {
  const response = await fetch('catalog.json', {cache:'no-store'});
  if (!response.ok) throw new Error('Catalog unavailable');
  const next = await response.json();
  if (next.snapshotHash === catalog.snapshotHash) return;
  catalog = next; byPath = new Map(catalog.documents.map(doc=>[doc.path,doc]));
  attachmentPaths = new Set(catalog.attachments); buildNavigation();
  await route(false); notify('Documentation updated from local sources.');
};
