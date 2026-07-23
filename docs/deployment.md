# Production deployment: GitHub → Vercel → Supabase/R2

## Responsibility boundaries

- GitHub stores source code and review history; it stores no application data.
- Vercel deploys `apps/web` and `apps/api` as separate projects.
- Supabase PostgreSQL stores users, tenants, clinics, audit, and media metadata.
- Cloudflare R2 stores private image, video, and audio binaries.

## Supabase

Use the connection string displayed by Supabase Dashboard > Connect. For Vercel,
prefer a pooler connection suitable for serverless connections. Convert the URL
scheme to `postgresql+psycopg://` for SQLAlchemy.

Run migrations from a trusted CI job or administrator workstation:

```text
cd apps/api
DATABASE_URL="postgresql+psycopg://..." alembic upgrade head
```

Do not expose `SUPABASE_SERVICE_ROLE_KEY` to the browser.

## Cloudflare R2

Create one private bucket and an R2 API token restricted to that bucket. Set a
CORS policy allowing the exact Vercel web origins, methods `PUT`, `GET`, and
`HEAD`, and headers `Content-Type`.

Upload sequence:

1. Browser requests `/api/v1/media/uploads`.
2. API validates role, type, and size, creates tenant-scoped metadata, and signs
   a short-lived R2 `PUT` URL.
3. Browser uploads directly to R2 with the required `Content-Type`.
4. Browser calls `/api/v1/media/{id}/complete`.
5. API checks the R2 object size/type before marking it available.

Presigned URLs are bearer credentials. Keep their lifetime short and never log
the complete URL.

## Vercel projects

Create two projects from the same GitHub repository:

| Project | Root directory | Runtime |
|---|---|---|
| `ai-seo-clinic-web` | `apps/web` | Next.js |
| `ai-seo-clinic-api` | `apps/api` | FastAPI/Python |

Set `NEXT_PUBLIC_API_BASE_URL` on the web project. Set database, Supabase, and R2
secrets only on the API project. Configure matching Preview and Production
values explicitly.
