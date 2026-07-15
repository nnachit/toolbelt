# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Toolbelt is a collection of utility tools with a SvelteKit frontend and Django REST backend. Current tools:

- **Password Generator** (`/password`) — the only tool using the backend API
- **Base64 Encoder/Decoder** (`/base64`) — client-side only
- **URL Encoder/Decoder** (`/url-encoder`) — client-side only
- **HTML Entity Encoder/Decoder** (`/html-entities`) — client-side only

Simple transformation tools are implemented purely client-side in Svelte (no API call). Only tools requiring server-side logic (e.g., secure password generation) go through the Django backend.

## Architecture

- **Frontend**: SvelteKit 2 + Svelte 5 with Tailwind CSS 4 and Flowbite components (`flowbite-svelte`, `flowbite-svelte-icons`)
  - Located in `frontend/`
  - Uses **pnpm only** as package manager — do not use npm or yarn (no `package-lock.json`)
  - Vite proxies `/api/*` requests to Django backend at `localhost:8000`
  - Tool pages live in `frontend/src/routes/<tool-name>/+page.svelte`; the nav is in `+layout.svelte`

- **Backend**: Django 5.2 with Django REST Framework
  - Located in `backend/`
  - Django apps are inside `backend/` (e.g., `backend/password_generator/`)
  - API endpoints mounted under URL paths (e.g., `/password/`)
  - CORS via `django-cors-headers`: allowed origins `http://localhost:5173` and `http://127.0.0.1:5173` (configured in `backend/backend/settings.py`)

## Common Commands

### Frontend (from `frontend/` directory)
```bash
pnpm install          # Install dependencies
pnpm dev              # Start dev server (port 5173)
pnpm build            # Production build
pnpm check            # TypeScript/Svelte type checking
```

### Backend (from `backend/` directory)
```bash
pip install -r requirements.txt    # Install dependencies
python manage.py runserver         # Start dev server (port 8000)
python manage.py migrate           # Run database migrations
python manage.py test              # Run tests
python manage.py test password_generator  # Run tests for specific app
```

## Development Setup

Run both servers for local development:
1. Backend: `cd backend && python manage.py runserver` (runs on :8000)
2. Frontend: `cd frontend && pnpm dev` (runs on :5173, proxies API calls to backend)

## API Proxy Configuration

Frontend Vite config (`frontend/vite.config.ts`) proxies `/api/*` to the Django backend, stripping the `/api` prefix. Example: frontend calls `/api/password/` → backend receives `/password/`.
