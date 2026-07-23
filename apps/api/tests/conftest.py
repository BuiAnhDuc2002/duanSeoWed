import os

os.environ["APP_ENV"] = "test"
os.environ["DATABASE_URL"] = "sqlite://"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.bootstrap import ADMIN_USER, ORG_A, ORG_B, VIEWER_USER, bootstrap_development
from app.database import get_db
from app.main import app
from app.models import Base
from app.storage import ObjectMetadata, get_object_storage


class FakeObjectStorage:
    def __init__(self):
        self.objects = {}

    def create_upload_url(self, object_key: str, content_type: str) -> str:
        self.objects[object_key] = ObjectMetadata(size_bytes=0, content_type=content_type)
        return f"https://r2.example.test/upload/{object_key}"

    def create_download_url(self, object_key: str, filename: str) -> str:
        return f"https://r2.example.test/download/{object_key}?filename={filename}"

    def head(self, object_key: str) -> ObjectMetadata:
        return self.objects[object_key]


@pytest.fixture()
def db():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    bootstrap_development(session)
    yield session
    session.close()


@pytest.fixture()
def client(db):
    fake_storage = FakeObjectStorage()
    app.dependency_overrides[get_db] = lambda: db
    app.dependency_overrides[get_object_storage] = lambda: fake_storage
    with TestClient(app) as test_client:
        test_client.fake_storage = fake_storage
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture()
def admin_headers():
    return {"X-User-Id": ADMIN_USER, "X-Organization-Id": ORG_A}


@pytest.fixture()
def viewer_headers():
    return {"X-User-Id": VIEWER_USER, "X-Organization-Id": ORG_B}
