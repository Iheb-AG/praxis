# Praxis documentation website — React + Vite

Public documentation reader for [Iheb-AG/praxis](https://github.com/Iheb-AG/praxis).
Dark graphite surfaces, neutral text and cyan links; local search, complete Markdown,
reference tables, downloadable sources and Mermaid diagrams. Original Praxis artwork is retained.

```bash
npm ci --prefix website
npm run dev --prefix website
```

Run these from the repository root with Node 22.12+ or Node 24+. Vite supplies the development
server and React/CSS hot updates. React owns navigation, search, filters, Markdown reading,
themes and diagram controls. Dependency versions and integrity hashes are in `package-lock.json`.
After editing source Markdown, regenerate with `npm run catalog --prefix website` and refresh.

```bash
npm test --prefix website
npm run build --prefix website
npm run preview --prefix website
```

Production builds generate a validated Markdown snapshot in `.generated/`, collect dependency
notices, then use Vite to produce `dist/` with hashed assets. Mermaid is loaded on demand.
Both output directories and `node_modules` are ignored by Git. Source Markdown is copied
byte-for-byte; no hardware tools, Python ingestion dependencies, model or embeddings are used.

Import the **praxis** repository into Vercel using the repository root, Framework **Vite**,
Install Command `npm ci --prefix website --include=dev`, Build Command `npm run build --prefix website`,
and Output Directory `website/dist`. The root `vercel.json` records these settings.
Remove any old dashboard overrides that skip installation or run only `node website/build.mjs`.
No application environment variables are required.
Deployments rebuild from the checked-out commit, so documentation follows Git pushes.

The public site excludes the local live progress API, command log, probe/approval data,
raw downloads and firmware binaries. `#/progress` opens the authored project status instead.
The separate local `/home/.../Praxis_Docs` app retains its live monitor; it is not uploaded.
There are no firmware, flashing or shell controls on the public site.

See [Vercel setup and deployment boundaries](../docs/vercel-hosting.md). The generated
`THIRD_PARTY_NOTICES.txt` retains installed dependency notices; source-derived content keeps
its existing notices. The previous standalone public renderer and vendored JS bundles are removed.
