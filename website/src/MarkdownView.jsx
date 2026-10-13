import { Children, isValidElement, memo, useMemo, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import MermaidDiagram from './MermaidDiagram.jsx';
import { assetURL, remarkDocumentation, resolveReference } from './docs.mjs';

function CodeBlock({ code, className, notify }) {
  const [copied, setCopied] = useState(false);
  async function copy() {
    try { await navigator.clipboard.writeText(code); setCopied(true); }
    catch { notify('Copy is unavailable in this browser. Select the code to copy it.'); }
  }
  return <div className="code-wrap"><pre><code className={className}>{code}</code></pre>
    <button className="copy-button" aria-label="Copy code block" onClick={copy}>{copied ? 'Copied' : 'Copy'}</button></div>;
}

export default memo(function MarkdownView({ doc, byPath, attachments, theme, notify }) {
  const components = useMemo(() => ({
    a({ href, children }) {
      const target = resolveReference(doc.path, href, byPath, attachments);
      if (target.kind === 'external') return <a href={target.href} target="_blank" rel="noopener noreferrer">{children}</a>;
      if (target.href) return <a href={target.href}>{children}</a>;
      return <a href="#" title="Outside this documentation snapshot" onClick={event => { event.preventDefault(); notify('Outside this snapshot: ' + (href || 'unknown reference')); }}>{children}</a>;
    },
    img({ src, alt }) {
      const target = resolveReference(doc.path, src, byPath, attachments);
      if (target.kind === 'registered' && attachments.has(target.path) && /\.(png|jpe?g|webp|gif)$/i.test(target.path)) {
        return <img src={assetURL(target.path)} alt={alt || ''} loading="lazy" />;
      }
      return <span>{alt || '[External image]'}</span>;
    },
    table({ children }) { return <div className="table-wrap" tabIndex={0} role="region" aria-label="Scrollable documentation table"><table>{children}</table></div>; },
    pre({ children }) {
      const child = Children.toArray(children).find(isValidElement);
      const code = String(child?.props.children ?? ''), className = child?.props.className || '';
      return /language-mermaid\b/.test(className) ? <MermaidDiagram code={code.trimEnd()} theme={theme} />
        : <CodeBlock code={code} className={className} notify={notify} />;
    },
  }), [doc.path, byPath, attachments, theme, notify]);
  const plugins = useMemo(() => [remarkGfm, [remarkDocumentation, { docPath: doc.path }]], [doc.path]);
  return <ReactMarkdown remarkPlugins={plugins} components={components}>{doc.content}</ReactMarkdown>;
});
