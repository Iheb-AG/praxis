# Public documentation on Vercel

The public site is built from this repository, using `website/` and the root `vercel.json`.
Its host is independent of the knowledge/build MCP processes and the connected development board.
Publishing the site does not expose a probe, local API, command feed or MCP server to the internet.

## Deploy from GitHub

1. Push the new `website/`, `vercel.json`, `.vercelignore` and associated documentation changes
   to [Iheb-AG/praxis](https://github.com/Iheb-AG/praxis).
2. In Vercel, add a project and import that repository.
3. Keep **Root Directory** at the repository root (`.`). Select Framework **Other** if asked.
4. Use **Build Command** `node website/build.mjs`, **Output Directory** `website/dist`, and
   skip dependency installation. The checked-in configuration supplies these values.
5. Deploy, then verify the actual returned URL, search, source downloads and a sequence diagram.
   Add that URL to the GitHub repository's About/Website field after deployment succeeds.

No service API keys or board details are required. GitHub/Vercel account access is required
to connect the repository and create the hosted deployment. This environment currently has
no Vercel credential or linked project; a prepared build is not a deployed URL.

Vercel supports repository imports and file-based build/output configuration; see its
[Git deployment guide](https://vercel.com/docs/git) and
[vercel.json reference](https://vercel.com/docs/project-configuration/vercel-json).

## Build and verify locally

```bash
node --test website/tests/*.test.mjs
node website/build.mjs
python3 -m http.server 4184 --bind 127.0.0.1 --directory website/dist
```

Open `http://127.0.0.1:4184/`. The public app needs only static hosting, and uses hash routes
for guide/library navigation. It does not need an SPA fallback that could turn missing
JSON or private API requests into successful HTML responses.

The build copies complete Markdown and explicitly linked public attachments. It excludes
raw/private paths, PDF originals, firmware binaries and symlinks; it validates local image
signatures and computes a deterministic snapshot hash. Tests cover complete table preservation,
hash changes, private/escaped/symlink rejection and image/evidence handling.

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
