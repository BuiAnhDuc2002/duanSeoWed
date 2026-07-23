import enum
import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, DateTime, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def uuid_string() -> str:
    return str(uuid.uuid4())


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class Role(str, enum.Enum):
    ORG_ADMIN = "ORG_ADMIN"
    SEO_MANAGER = "SEO_MANAGER"
    CONTENT_EDITOR = "CONTENT_EDITOR"
    MEDICAL_REVIEWER = "MEDICAL_REVIEWER"
    COMPLIANCE_REVIEWER = "COMPLIANCE_REVIEWER"
    PUBLISHER = "PUBLISHER"
    VIEWER = "VIEWER"


class Organization(Base):
    __tablename__ = "organizations"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    name: Mapped[str] = mapped_column(String(200))
    slug: Mapped[str] = mapped_column(String(120), unique=True)
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    email: Mapped[str] = mapped_column(String(320), unique=True)
    display_name: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE")


class Membership(Base):
    __tablename__ = "organization_members"
    __table_args__ = (UniqueConstraint("organization_id", "user_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    roles: Mapped[list[str]] = mapped_column(JSON, default=list)


class Clinic(Base):
    __tablename__ = "clinics"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    legal_name: Mapped[str] = mapped_column(String(250))
    brand_name: Mapped[str] = mapped_column(String(250))
    address: Mapped[str] = mapped_column(Text)
    verification_status: Mapped[str] = mapped_column(String(30), default="UNVERIFIED")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    licenses: Mapped[list["ClinicLicense"]] = relationship(cascade="all, delete-orphan")
    services: Mapped[list["Service"]] = relationship(cascade="all, delete-orphan")


class ClinicLicense(Base):
    __tablename__ = "clinic_licenses"
    __table_args__ = (UniqueConstraint("organization_id", "license_number"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    clinic_id: Mapped[str] = mapped_column(ForeignKey("clinics.id"), index=True)
    license_number: Mapped[str] = mapped_column(String(120))
    issuing_authority: Mapped[str] = mapped_column(String(250))
    status: Mapped[str] = mapped_column(String(30), default="UNVERIFIED")
    verified_by: Mapped[str | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    scopes: Mapped[list["ProfessionalScope"]] = relationship(cascade="all, delete-orphan")


class ProfessionalScope(Base):
    __tablename__ = "professional_scopes"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    clinic_license_id: Mapped[str] = mapped_column(ForeignKey("clinic_licenses.id"), index=True)
    code: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE")


class Service(Base):
    __tablename__ = "services"
    __table_args__ = (UniqueConstraint("organization_id", "clinic_id", "slug"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    clinic_id: Mapped[str] = mapped_column(ForeignKey("clinics.id"), index=True)
    name: Mapped[str] = mapped_column(String(250))
    slug: Mapped[str] = mapped_column(String(120))
    risk_level: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(String(30), default="DRAFT")
    verified_facts: Mapped[dict] = mapped_column(JSON, default=dict)


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    actor_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    action: Mapped[str] = mapped_column(String(100))
    resource_type: Mapped[str] = mapped_column(String(100))
    resource_id: Mapped[str] = mapped_column(String(36))
    after_summary: Mapped[dict] = mapped_column(JSON, default=dict)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class MediaObject(Base):
    __tablename__ = "media_objects"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_string)
    organization_id: Mapped[str] = mapped_column(ForeignKey("organizations.id"), index=True)
    created_by: Mapped[str] = mapped_column(ForeignKey("users.id"))
    object_key: Mapped[str] = mapped_column(String(700), unique=True)
    original_filename: Mapped[str] = mapped_column(String(255))
    media_type: Mapped[str] = mapped_column(String(20))
    content_type: Mapped[str] = mapped_column(String(120))
    expected_size_bytes: Mapped[int] = mapped_column()
    actual_size_bytes: Mapped[int | None] = mapped_column(nullable=True)
    checksum_sha256: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="PENDING_UPLOAD", index=True)
    contains_patient: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
