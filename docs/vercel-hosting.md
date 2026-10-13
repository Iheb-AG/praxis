# Public documentation on Vercel

The public site uses **React + Vite**, built from `website/` and the root `vercel.json`.
Its host is independent of the knowledge/build MCP processes and the connected development board.
Publishing the site does not expose a probe, local API, command feed or MCP server to the internet.

## Deploy from GitHub

1. Push the new `website/`, `vercel.json`, `.vercelignore` and associated documentation changes
   to [Iheb-AG/praxis](https://github.com/Iheb-AG/praxis).
2. In Vercel, add a project and import that repository.
3. Keep **Root Directory** at the repository root (`.`). Select Framework **Vite** if asked.
4. Use **Install Command** `npm ci --prefix website --include=dev`, **Build Command**
   `npm run build --prefix website`, and **Output Directory** `website/dist`.
   The checked-in configuration supplies these values. Remove any previous dashboard overrides
   that skip installation or run only the old catalog command. Use Node 22.12+ or Node 24+.
5. Deploy, then verify the actual returned URL, search, source downloads and a sequence diagram.
   Add that URL to the GitHub repository's About/Website field after deployment succeeds.

No service API keys or board details are required. GitHub/Vercel account access is required
to connect the repository and create the hosted deployment. This environment currently has
no Vercel credential or linked project; a prepared build is not a deployed URL.

Vercel supports repository imports and file-based build/output configuration; see its
[Git deployment guide](https://vercel.com/docs/git) and
[vercel.json reference](https://vercel.com/docs/project-configuration/vercel-json) and
[Vite integration](https://vercel.com/docs/frameworks/frontend/vite).

## Build and verify locally

```bash
npm ci --prefix website
npm test --prefix website
npm run build --prefix website
npm run preview --prefix website -- --port 4184
```

Open `http://127.0.0.1:4184/`. For development use `npm run dev --prefix website` and the
printed Vite URL (normally port 5173). The production app needs static hosting and uses hash routes
for guide/library navigation. It does not need an SPA fallback that could turn missing
JSON or private API requests into successful HTML responses.

The snapshot compiler copies complete Markdown and explicitly linked public attachments. It excludes
raw/private paths, PDF originals, firmware binaries and symlinks; it validates local image
signatures and computes a deterministic snapshot hash. Tests cover complete table preservation,
hash changes, private/escaped/symlink rejection and image/evidence handling. Reader tests cover
legacy routes, exact registered links, wiki resolution, duplicate heading anchors, complete React
Markdown tables, inert HTML and deterministic search. React Markdown and GFM render the content;
Mermaid is an on-demand dependency with sanitized SVG output and React zoom/fullscreen controls.

Vite bundles the React application and CSS into hashed production assets. `package-lock.json`
pins npm dependencies. Installed dependency notices are emitted as `THIRD_PARTY_NOTICES.txt`.
Installation needs package registry access; runtime reading fetches only the deployed static assets.
No Next.js server, native Python runtime, or filesystem-reading API is deployed.

The public theme uses neutral off-white text on graphite backgrounds, cyan links, larger
monospace code and reference tables, and matching diagram colors. Light mode is also neutral.
Source documentation is unchanged by rendering and site builds.

## Local progress monitoring

The separate development website retains Python/SSE live monitoring. The Vercel build has
no monitor script, local command history or API backend. Public readers can open `docs/STATUS.md`
for the authored milestone assessment; it updates when documentation is committed and deployed.
The public site does not advertise this as a live development feed.

**Next:** push the prepared website files, connect the repository in Vercel, deploy and record
the real site URL. Hosted behavior remains unverified until an actual deployment is available.
