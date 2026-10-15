# Hosting the standalone documentation website

This website is maintained in [Iheb-AG/praxis-documentation](https://github.com/Iheb-AG/praxis-documentation).
It owns its content under `documentation-source/` and builds independently of the Praxis
codebase. The guides, examples, diagrams, reports and hardware reference snapshots were
copied once; subsequent edits belong to this documentation repository.

## Local development

Use Node 24.x. From the documentation repository root:

```bash
npm ci --include=dev
npm run dev
```

Edit Markdown directly in `documentation-source/`. During development, run `npm run catalog`
and refresh after editing content. No compiler run, external source checkout, hash-inventory
refresh or re-export is needed. To check production:

```bash
npm test
npm run build
npm run preview
```

The build creates a deterministic local catalog in `.generated/`, collects dependency
notices and bundles React with Vite into `dist/`. Navigation, full-text search, complete
Markdown tables and Mermaid diagrams work from the deployed static files. Hash routes
preserve guide bookmarks. There is no Python backend or documentation synchronization API.

## Vercel configuration

Import **Iheb-AG/praxis-documentation**, then use:

| Setting | Value |
| --- | --- |
| Root Directory | `.` |
| Framework | Vite |
| Node.js Version | 24.x |
| Install Command | `npm ci --include=dev` |
| Build Command | `npm run build` |
| Output Directory | `dist` |

The root `vercel.json` supplies these commands. Remove earlier dashboard overrides using
`--prefix website` or `website/dist`, and remove obsolete `PRAXIS_DOCS_SOURCE` environment
variables. The build ignores that variable and always reads this repository's content.

Commit `documentation-source/` with the frontend sources, configuration and lockfile.
Do not commit `node_modules/`, `.generated/` or `dist/`; Vercel creates them during its build.
If `documentation-source/docs/README.md` is missing, restore it in this repository. The
builder deliberately does not fall back to a parent checkout or download external content.

Push to this documentation repository to deploy its changes. A push to the Praxis codebase
alone has no effect on this site. The documentation can be edited and versioned independently.

## Publication boundaries

Ordinary links to GitHub and manufacturers preserve reference attribution; following a link
is optional and does not feed the catalog. The catalog includes only local Markdown and
explicitly linked public attachments. Raw manuals, private paths, symlinks and firmware
binaries are excluded. Original branding and existing source notices are retained.

The public site has no MCP server, board connection, flashing controls, private telemetry,
local progress API or development command feed. The separate local development monitor
remains separate. Hardware reference snapshots describe their recorded experimental support;
site edits do not publish or validate new operational knowledge bundles.

**Next:** commit the standalone content and configuration, push this repository, then check
its Vercel deployment and production URL.
