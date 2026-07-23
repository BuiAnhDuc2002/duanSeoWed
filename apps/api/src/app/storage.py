from dataclasses import dataclass

import boto3
from botocore.client import BaseClient

from app.config import settings


@dataclass(frozen=True)
class ObjectMetadata:
    size_bytes: int
    content_type: str


class ObjectStorage:
    def create_upload_url(self, object_key: str, content_type: str) -> str:
        raise NotImplementedError

    def create_download_url(self, object_key: str, filename: str) -> str:
        raise NotImplementedError

    def head(self, object_key: str) -> ObjectMetadata:
        raise NotImplementedError


class R2ObjectStorage(ObjectStorage):
    def __init__(self, client: BaseClient | None = None):
        if client is not None:
            self.client = client
            return
        if not all(
            [settings.r2_account_id, settings.r2_access_key_id, settings.r2_secret_access_key]
        ):
            raise RuntimeError("R2 credentials are not configured")
        self.client = boto3.client(
            "s3",
            endpoint_url=f"https://{settings.r2_account_id}.r2.cloudflarestorage.com",
            aws_access_key_id=settings.r2_access_key_id,
            aws_secret_access_key=settings.r2_secret_access_key,
            region_name="auto",
        )

    def create_upload_url(self, object_key: str, content_type: str) -> str:
        return self.client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": settings.r2_bucket_private,
                "Key": object_key,
                "ContentType": content_type,
            },
            ExpiresIn=settings.r2_presigned_url_ttl_seconds,
        )

    def create_download_url(self, object_key: str, filename: str) -> str:
        safe_name = filename.replace('"', "")
        return self.client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": settings.r2_bucket_private,
                "Key": object_key,
                "ResponseContentDisposition": f'attachment; filename="{safe_name}"',
            },
            ExpiresIn=settings.r2_presigned_url_ttl_seconds,
        )

    def head(self, object_key: str) -> ObjectMetadata:
        response = self.client.head_object(Bucket=settings.r2_bucket_private, Key=object_key)
        return ObjectMetadata(
            size_bytes=int(response["ContentLength"]),
            content_type=str(response.get("ContentType", "application/octet-stream")),
        )


def get_object_storage() -> ObjectStorage:
    return R2ObjectStorage()
