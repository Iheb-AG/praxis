import { useEffect, useId, useRef, useState } from 'react';
import DOMPurify from 'dompurify';

let modulePromise;
const loadMermaid = () => modulePromise ||= import('mermaid').then(module => module.default);

function configuration(theme) {
  const dark = theme === 'dark', text = dark ? '#d8dee7' : '#293440';
  return { startOnLoad: false, securityLevel: 'strict', theme: 'base', suppressErrorRendering: true,
    maxTextSize: 150000, flowchart: { htmlLabels: false }, sequence: { useMaxWidth: false },
    fontFamily: 'Segoe UI, system-ui, sans-serif', themeVariables: {
      darkMode: dark, background: dark ? '#11151b' : '#ffffff', primaryColor: dark ? '#162a33' : '#e8f5f8',
      primaryTextColor: dark ? '#f4f6f8' : '#17212b', primaryBorderColor: dark ? '#7cc7e6' : '#00687d',
      lineColor: dark ? '#a7b1be' : '#536474', secondaryColor: dark ? '#1a242d' : '#edf2f6',
      tertiaryColor: dark ? '#20282f' : '#f0f4f7', textColor: text,
      actorBkg: dark ? '#162a33' : '#e8f5f8', actorTextColor: text,
      actorBorder: dark ? '#7cc7e6' : '#00687d', signalColor: text, signalTextColor: text,
      noteBkgColor: dark ? '#20282f' : '#edf2f6', noteTextColor: text } };
}

export default function MermaidDiagram({ code, theme }) {
  const id = useId().replace(/[^a-z0-9]/gi, ''), revision = useRef(0);
  const viewport = useRef(null), dialog = useRef(null);
  const [drawing, setDrawing] = useState(null), [error, setError] = useState('');
  const [ratio, setRatio] = useState(1);
  useEffect(() => {
    let cancelled = false; const serial = ++revision.current;
    setDrawing(null); setError('');
    (async () => {
      const mermaid = await loadMermaid();
      if (cancelled) return;
      mermaid.initialize(configuration(theme));
      const source = /^\s*sequenceDiagram/m.test(code) ? code.split('\n').map(line => {
        const colon = line.indexOf(':');
        return colon < 0 || line.trim().startsWith('%%') ? line : line.slice(0, colon + 1) + line.slice(colon + 1).replaceAll(';', '#59;');
      }).join('\n') : code;
      const result = await mermaid.render(`praxis-${id}-${serial}`, source);
      if (cancelled) return;
      const svg = DOMPurify.sanitize(result.svg, { USE_PROFILES: { svg: true, svgFilters: true },
        ADD_TAGS: ['style', 'foreignObject', 'div', 'span', 'p'], ADD_ATTR: ['xmlns', 'class', 'style'] });
      const parsed = new DOMParser().parseFromString(svg, 'image/svg+xml').documentElement;
      const box = parsed.getAttribute('viewBox')?.split(/[ ,]+/).map(Number);
      const width = box?.[2] || parseFloat(parsed.getAttribute('width')) || 800;
      const height = box?.[3] || parseFloat(parsed.getAttribute('height')) || 500;
      setDrawing({ svg, width, height });
      setRatio(Math.min(1, Math.max(200, (viewport.current?.clientWidth || 800) - 36) / width));
    })().catch(failure => { if (!cancelled) setError(failure.message || 'Diagram rendering failed'); });
    return () => { cancelled = true; };
  }, [code, theme, id]);
  const fit = () => drawing && setRatio(Math.min(1, Math.max(200, viewport.current.clientWidth - 36) / drawing.width));
  const size = drawing ? { width: Math.max(200, drawing.width * ratio), '--diagram-height': drawing.height * ratio + 'px' } : undefined;
  return <section className="diagram-card">
    <div className="diagram-toolbar"><span>Mermaid diagram</span>
      <button onClick={() => setRatio(value => Math.max(.15, value / 1.25))} aria-label="Zoom diagram out">−</button>
      <button onClick={fit}>Fit</button><button onClick={() => setRatio(value => Math.min(4, value * 1.25))} aria-label="Zoom diagram in">+</button>
      <button disabled={!drawing} onClick={() => dialog.current.showModal()}>Expand ↗</button></div>
    <div className="diagram-viewport" ref={viewport}>
      {drawing ? <div className="diagram-svg" style={size} dangerouslySetInnerHTML={{ __html: drawing.svg }} />
        : error ? <div className="diagram-error">This diagram could not be rendered. Its complete source is below.</div>
          : <div className="loading">Rendering diagram…</div>}
    </div>
    <details className="diagram-source"><summary>View diagram source</summary><pre><code>{code}</code></pre></details>
    <dialog ref={dialog} aria-label="Expanded diagram" onClick={event => { if (event.target === event.currentTarget) dialog.current.close(); }}>
      <div className="dialog-toolbar"><strong>Diagram viewer</strong><button className="button" onClick={() => dialog.current.close()}>Close ✕</button></div>
      <div className="expanded-diagram">{drawing && <div className="diagram-svg" style={{ width: Math.min(1800, Math.max(900, drawing.width)) }} dangerouslySetInnerHTML={{ __html: drawing.svg }} />}</div>
    </dialog>
  </section>;
}
