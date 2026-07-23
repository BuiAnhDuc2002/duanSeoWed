from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class OrganizationOut(ORMModel):
    id: str
    name: str
    slug: str
    status: str


class ClinicCreate(BaseModel):
    legal_name: str = Field(min_length=2, max_length=250)
    brand_name: str = Field(min_length=2, max_length=250)
    address: str = Field(min_length=3, max_length=1000)


class ClinicOut(ClinicCreate, ORMModel):
    id: str
    organization_id: str
    verification_status: str


class LicenseCreate(BaseModel):
    license_number: str = Field(min_length=2, max_length=120)
    issuing_authority: str = Field(min_length=2, max_length=250)


class LicenseOut(LicenseCreate, ORMModel):
    id: str
    clinic_id: str
    status: str


class ScopeCreate(BaseModel):
    code: str = Field(min_length=2, max_length=100)
    name: str = Field(min_length=2, max_length=250)
    description: str = Field(default="", max_length=2000)


class ScopeOut(ScopeCreate, ORMModel):
    id: str
    clinic_license_id: str
    status: str


class ServiceCreate(BaseModel):
    clinic_id: str
    name: str = Field(min_length=2, max_length=250)
    slug: str = Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    risk_level: Literal["LOW", "MEDIUM", "HIGH"]
    verified_facts: dict = Field(default_factory=dict)


class ServiceOut(ServiceCreate, ORMModel):
    id: str
    status: str


class AuditOut(ORMModel):
    id: str
    action: str
    resource_type: str
    resource_id: str
    after_summary: dict


class MediaUploadRequest(BaseModel):
    filename: str = Field(min_length=1, max_length=255)
    content_type: str = Field(min_length=3, max_length=120)
    size_bytes: int = Field(gt=0)
    checksum_sha256: str | None = Field(default=None, pattern=r"^[a-fA-F0-9]{64}$")
    contains_patient: bool = False


class MediaUploadTicket(BaseModel):
    media_id: str
    object_key: str
    upload_url: str
    method: Literal["PUT"] = "PUT"
    required_headers: dict[str, str]
    expires_in_seconds: int


class MediaOut(ORMModel):
    id: str
    original_filename: str
    media_type: str
    content_type: str
    expected_size_bytes: int
    actual_size_bytes: int | None
    status: str
    contains_patient: bool


class MediaDownloadTicket(BaseModel):
    download_url: str
    expires_in_seconds: int
