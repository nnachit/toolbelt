# Toolbelt — frontend

SvelteKit 2 + Svelte 5 + Tailwind CSS 4. See the [root README](../README.md) for the project overview and
[CLAUDE.md](../CLAUDE.md) for architecture notes.

**pnpm only** — do not use npm or yarn.

```bash
pnpm install    # Install dependencies
pnpm dev        # Dev server on :5173 (proxies /api/* to Django on :8000)
pnpm build      # Production build
pnpm preview    # Serve the production build
pnpm check      # Type checking (svelte-check)
```

The backend must be running for the password tool: `cd ../backend && python manage.py runserver`.
