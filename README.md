# AI SEO Clinic

Foundation slice for the Vietnamese medical-aesthetics SEO platform described in
`AI_SEO_THAM_MY_MVP_SPEC.md`.

## Included

- FastAPI API with development identity abstraction.
- Tenant-scoped organizations, memberships, clinics, licenses, professional
  scopes, services, and append-only audit records.
- Backend-enforced RBAC.
- Alembic foundation migration.
- Minimal Next.js administration UI.
- Cross-tenant and permission tests.
- Supabase-compatible PostgreSQL production configuration.
- Cloudflare R2 direct-upload flow for images, audio, and video.

WordPress publishing, AI generation, keyword planning, and image consent are not
implemented in this slice. There is no auto-publish endpoint.

## Production topology

```text
GitHub repository
  ├─ Vercel project: apps/web (Next.js)
  └─ Vercel project: apps/api (FastAPI)
         ├─ Supabase PostgreSQL: relational data and media metadata
         └─ Cloudflare R2: private image, audio, and video objects
```

The browser asks FastAPI for a short-lived, tenant-scoped presigned URL and then
uploads the binary directly to R2. Vercel never proxies large media bodies.
Credentials for Supabase and R2 are server-side Vercel environment variables.

## Run with Docker

1. Copy `.env.example` to `.env`.
2. Run `docker compose up --build`.
3. Open the UI at http://localhost:3000 and API docs at
   http://localhost:8000/docs.

The development bootstrap creates two isolated demo organizations:

- User `00000000-0000-0000-0000-000000000001`, Organization
  `10000000-0000-0000-0000-000000000001` (`ORG_ADMIN`)
- User `00000000-0000-0000-0000-000000000002`, Organization
  `20000000-0000-0000-0000-000000000002` (`VIEWER`)

The local UI sends the selected IDs through development-only identity headers.
Production must replace this adapter with a verified OIDC/session adapter.

## Run API tests locally

```text
cd apps/api
python -m venv .venv
.venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/pytest
```

## Architecture notes

- `X-User-Id` and `X-Organization-Id` are parsed only by the development auth
  adapter. Handlers depend on an `IdentityContext`, not raw headers.
- Tenant IDs are taken from that context. Payload schemas do not accept an
  organization ID.
- Mutations and verification actions write an audit record in the same database
  transaction.
- License verification requires `ORG_ADMIN` or `COMPLIANCE_REVIEWER`.
- R2 object keys start with the organization ID; callers cannot supply an
  arbitrary key.
- Media is private by default. Read access uses short-lived presigned URLs.
- Supabase stores metadata and application records; R2 stores binary media.

## Deploy from GitHub to Vercel

1. Push this repository to GitHub.
2. Import it twice in Vercel:
   - Web project root directory: `apps/web`
   - API project root directory: `apps/api`
3. Set `NEXT_PUBLIC_API_BASE_URL` on the web project to the API project URL.
4. Set `DATABASE_URL`, Supabase variables, and all `R2_*` variables only on the
   API project.
5. Run `alembic upgrade head` against Supabase before the first production
   deployment and after schema migrations.
6. Configure the R2 bucket CORS policy to allow `PUT` and `GET` from the exact
   Vercel production and preview origins.

Vercel automatically creates deployments for commits and pull requests after
the GitHub repository is connected. Do not commit `.env` or Vercel credentials.
