# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Toolbelt is a collection of utility tools with a SvelteKit frontend and Django REST backend. Current tools:

- **Password Generator** (`/password`) — the only tool using the backend API
- **Base64 Encoder/Decoder** (`/base64`) — client-side only
- **URL Encoder/Decoder** (`/url-encoder`) — client-side only
- **HTML Entity Encoder/Decoder** (`/html-entities`) — client-side only
- **JSON Formatter** (`/json-formatter`) — client-side only
- **JWT Decoder** (`/jwt-decoder`) — client-side only, decode-only (never verifies the signature)

Simple transformation tools are implemented purely client-side in Svelte (no API call). Only tools requiring server-side logic (e.g., secure password generation) go through the Django backend.

## Architecture

- **Frontend**: SvelteKit 2 + Svelte 5 with Tailwind CSS 4 (the `flowbite` package is used only as a Tailwind plugin in `app.css` — no Flowbite components are imported)
  - Located in `frontend/`
  - Uses **pnpm only** as package manager — do not use npm or yarn (no `package-lock.json`)
  - Vite proxies `/api/*` requests to Django backend at `localhost:8000`
  - Tool pages live in `frontend/src/routes/<tool-name>/+page.svelte`
  - `frontend/src/lib/tools.ts` is the single source of truth for the sidebar, the home page cards and page titles: adding a tool means one entry there plus its route. Icons are drawn by `frontend/src/lib/components/ToolIcon.svelte` — a new icon means one path in its `paths` map and one name in `ToolIconName`
  - `+layout.svelte` derives `<title>` and the meta description from the current route via `toolByPath()`, so pages must not declare their own `<svelte:head><title>`
  - Encode/decode tools are thin wrappers around the shared `frontend/src/lib/components/EncoderDecoderTool.svelte` component. New transformation tools should reuse it (see below)

- **Backend**: Django 5.2 with Django REST Framework
  - `backend/` is the working directory (holds `manage.py`); it is **not** a Python package
  - `backend/backend/` is the project package (`settings.py`, `urls.py`, `wsgi.py`)
  - `backend/password_generator/` is the only app; its URLs are mounted at `/password/`
  - CORS via `django-cors-headers`: allowed origins `http://localhost:5173` and `http://127.0.0.1:5173` (configured in `backend/backend/settings.py`)

## Shared EncoderDecoderTool component

`frontend/src/lib/components/EncoderDecoderTool.svelte` provides the whole encode/decode UI (mode toggle, two textareas, char counters, Swap/Copy/Clear).

- Required props: `title`, `description`, `encodedLabel`, `transform(input, mode)` where `mode` is `'encode' | 'decode'`
- Optional props: `decodePlaceholder`, `encodeError`, `decodeError`
- Snippets: `controls` and `info` are `Snippet<[Mode]>` (they receive the current mode); `footer` takes no argument
- `modes` defaults to `['encode', 'decode']`; pass a single mode (e.g. `modes={['decode']}`, as `/jwt-decoder` does) to hide the toggle and the Swap button for one-way tools
- Recomputation runs through a `$effect` that calls `transform`. **A custom control only triggers a recompute if `transform` itself reads that `$state`** — see `url-encoder/+page.svelte` and `html-entities/+page.svelte`
- A `transform` that throws displays `encodeError` / `decodeError` depending on the mode

## Password API contract

`GET /password/` (`backend/password_generator/views.py`) — function view with `@api_view(['GET'])`, no serializer.

- Query params: `lower`, `upper`, `digits`, `special` (string `"true"`/`"false"`, default `true`), `length` (default 16, bounds 4–128)
- `200` → `{"password": "..."}`
- `400` → `{"error": "..."}` when `length` is not an integer, is out of bounds, or no character type is selected

## Common Commands

### Frontend (from `frontend/` directory)
```bash
pnpm install          # Install dependencies
pnpm dev              # Start dev server (port 5173)
pnpm build            # Production build
pnpm preview          # Serve the production build
pnpm check            # TypeScript/Svelte type checking
pnpm check:watch      # Same, in watch mode
```

`frontend/pnpm-workspace.yaml` declares `allowBuilds` for `@tailwindcss/oxide` and `esbuild`. pnpm 11 moved post-install build approval there from `pnpm.onlyBuiltDependencies` in `package.json` (now obsolete) — without this file a fresh install skips Tailwind's native binary and the build breaks.

### Backend (from `backend/` directory)
```bash
pip install -r requirements.txt    # Install dependencies
python manage.py runserver         # Start dev server (port 8000)
python manage.py migrate           # Built-in Django migrations only
```

## Tooling state

- No ESLint, no Prettier, no frontend tests, no CI (`.github/` does not exist). `pnpm check` (svelte-check, `tsconfig.json` with `strict: true` and `checkJs: true`) is the only quality gate
- No backend tests either: `backend/password_generator/tests.py` is an untouched stub, so `python manage.py test` runs nothing
- No models and no `migrations/` directory — don't reach for `makemigrations` unless you actually add a model
- `SECRET_KEY` and `DEBUG = True` are hardcoded in `backend/backend/settings.py`; no environment variable is read anywhere. `env.example` and `docker-compose.yml` exist but are **empty files** — do not assume env-based config
- `backend/db.sqlite3` exists locally and is gitignored

## Development Setup

Run both servers for local development:
1. Backend: `cd backend && python manage.py runserver` (runs on :8000)
2. Frontend: `cd frontend && pnpm dev` (runs on :5173, proxies API calls to backend)

## API Proxy Configuration

Frontend Vite config (`frontend/vite.config.ts`) proxies `/api/*` to the Django backend, stripping the `/api` prefix. Example: frontend calls `/api/password/` → backend receives `/password/`.
