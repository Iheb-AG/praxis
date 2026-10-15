# Praxis documentation

Independent React + Vite documentation website for [Project Praxis](https://github.com/Iheb-AG/praxis).
The public guides, architecture, sequence diagrams, examples, reports and reviewed hardware
references are owned by this repository under `documentation-source/`. The original Praxis
logo and background are included.

## Run locally

Use Node **24.x** and run from this repository's root:

```bash
npm ci --include=dev
npm run dev
```

For a production check:

```bash
npm test
npm run build
npm run preview
```

## Documentation lives here

```text
praxis-documentation/
├── documentation-source/
│   ├── README.md             # Praxis project introduction
│   ├── docs/                 # Guides, architecture, diagrams and reports
│   ├── examples/             # Example guides and linked source files
│   ├── bundles/              # Published Markdown reference snapshots
│   ├── sources/              # Reviewed reference material
│   └── assets/               # Linked public supporting files and notices
├── public/branding/          # Original logo and background
├── src/                      # React reader, search and diagram controls
├── build.mjs                 # Builds a catalog from local documentation only
└── vercel.json
```

This content was copied once from Praxis. Builds never read the parent repository, clone
Praxis, pull its Git history or use `PRAXIS_DOCS_SOURCE`. No synchronization or ingestion job
is required. Links to GitHub and manufacturer references are ordinary citations, not feeds.

Edit or add Markdown **directly in `documentation-source/`**, keeping relative links and
complete tables. Run `npm run catalog` after content changes during development and refresh
the page; `npm run build` regenerates the catalog automatically. Its hash describes the
current local content, so edits do not require an external inventory or re-export.
The included hardware snapshots document experimental support; editing this website does
not modify or certify an operational Praxis MCP bundle.

The catalog includes complete Markdown and explicitly linked public attachments, preserving
source bytes and provenance. It excludes private paths, raw manuals, firmware binaries and
symlinks. Search runs in the browser; Markdown uses React Markdown/GFM and Mermaid diagrams
load on demand. The site contains no local command log, probe credentials or hardware controls.

## Deploy to Vercel

Import **Iheb-AG/praxis-documentation** with:

| Setting | Value |
| --- | --- |
| Root Directory | `.` |
| Framework | Vite |
| Node.js Version | 24.x |
| Install Command | `npm ci --include=dev` |
| Build Command | `npm run build` |
| Output Directory | `dist` |

`vercel.json` records the commands. Remove old dashboard overrides referring to `website/`
and obsolete `PRAXIS_DOCS_SOURCE` settings. Commit `documentation-source/`, the frontend,
configuration and npm lockfile. Dependencies and outputs (`node_modules/`, `.generated/`,
`dist/`) are regenerated and ignored. Pushes to **this documentation repository** trigger
its deployment; changes to the Praxis repository do not alter this site.

`LICENSE` covers the project. Imported material retains its existing notices. Builds emit
installed dependency notices as `THIRD_PARTY_NOTICES.txt`.
