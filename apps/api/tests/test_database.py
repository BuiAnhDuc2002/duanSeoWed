from app.database import normalize_database_url


def test_normalizes_supabase_postgresql_url_to_psycopg_v3():
    original = "postgresql://user:password@pooler.example.test:5432/postgres"
    assert normalize_database_url(original) == (
        "postgresql+psycopg://user:password@pooler.example.test:5432/postgres"
    )


def test_normalizes_legacy_postgres_url_to_psycopg_v3():
    original = "postgres://user:password@pooler.example.test:5432/postgres"
    assert normalize_database_url(original) == (
        "postgresql+psycopg://user:password@pooler.example.test:5432/postgres"
    )


def test_preserves_explicit_driver_and_sqlite_urls():
    explicit = "postgresql+psycopg://user:password@pooler.example.test/postgres"
    sqlite = "sqlite:///app.sqlite3"
    assert normalize_database_url(explicit) == explicit
    assert normalize_database_url(sqlite) == sqlite
