# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Toolbelt is a collection of utility tools with a SvelteKit frontend and Django REST backend. Currently features a password generator tool.

## Architecture

- **Frontend**: SvelteKit 2 + Svelte 5 with Tailwind CSS 4 and Flowbite components
  - Located in `frontend/`
  - Uses pnpm as package manager
  - Vite proxies `/api/*` requests to Django backend at `localhost:8000`

- **Backend**: Django 5.2 with Django REST Framework
  - Located in `backend/`
  - Django apps are inside `backend/` (e.g., `backend/password_generator/`)
  - API endpoints mounted under URL paths (e.g., `/password/`)

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
