# Repository instructions

## Commands

- Start dependencies and apps: `docker compose up --build`
- API tests: `cd apps/api && pytest`
- API lint: `cd apps/api && ruff check .`
- API formatting: `cd apps/api && ruff format --check .`
- Web install: `pnpm install`
- Web lint/typecheck: `pnpm --filter web lint && pnpm --filter web typecheck`
- Migration: `cd apps/api && alembic upgrade head`

## Guardrails

- Every tenant-owned record and query must be scoped by `organization_id`.
- Every new endpoint needs authorization tests and a cross-tenant test.
- Do not change compliance rules without tests and a source reference.
- Never log credentials, secrets, PII, or sensitive health data.
- Do not call live external APIs in default tests.
- Do not auto-publish WordPress. MVP integrations may only create `draft` posts.
- Migrations require a data-impact note and rollback strategy.

