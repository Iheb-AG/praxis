# Praxis documentation website

Public documentation reader for [Iheb-AG/praxis](https://github.com/Iheb-AG/praxis).
Dark graphite surfaces, neutral text and cyan links; local search, complete Markdown,
reference tables, downloadable sources and Mermaid diagrams. Original Praxis artwork is retained.

```bash
node website/build.mjs
node --test website/tests/*.test.mjs
python3 -m http.server 4184 --bind 127.0.0.1 --directory website/dist
```

Run these from the repository root. Node 22+ builds the site using built-in modules only;
no package installation, hardware tools, Python dependencies or network requests are needed.
The generated `website/dist` is ignored by Git. Source Markdown stays authoritative and is
copied byte-for-byte into a public snapshot at build time.

Import the **praxis** repository into Vercel using the repository root, Framework **Other**,
Build Command `node website/build.mjs` and Output Directory `website/dist`. The root
`vercel.json` records these settings. No application environment variables are required.
Deployments rebuild from the checked-out commit, so documentation follows Git pushes.

The public site excludes the local live progress API, command log, probe/approval data,
raw downloads and firmware binaries. `#/progress` opens the authored project status instead.
The separate local `/home/.../Praxis_Docs` app retains its live monitor; it is not uploaded.
There are no firmware, flashing or shell controls on the public site.

See [Vercel setup and deployment boundaries](../docs/vercel-hosting.md). Vendored browser
library notices remain in `public/vendor`; source-derived content keeps its existing notices.
