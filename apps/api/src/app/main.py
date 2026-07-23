from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
import uuid

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.audit import record_audit
from app.auth import IdentityContext, get_identity, require_roles
from app.bootstrap import bootstrap_development
from app.config import settings
from app.database import SessionLocal, get_db
from app.models import (
    AuditLog,
    Base,
    Clinic,
    ClinicLicense,
    MediaObject,
    Organization,
    ProfessionalScope,
    Service,
    utcnow,
)
from app.database import engine
from app.schemas import (
    AuditOut,
    ClinicCreate,
    ClinicOut,
    LicenseCreate,
    LicenseOut,
    MediaDownloadTicket,
    MediaOut,
    MediaUploadRequest,
    MediaUploadTicket,
    OrganizationOut,
    ScopeCreate,
    ScopeOut,
    ServiceCreate,
    ServiceOut,
)
from app.storage import ObjectStorage, get_object_storage


@asynccontextmanager
async def lifespan(_: FastAPI):
    if settings.app_env in {"development", "test"}:
        Base.metadata.create_all(engine)
        with SessionLocal() as db:
            bootstrap_development(db)
    yield


app = FastAPI(title="AI SEO Clinic API", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_MEDIA_TYPES = {
    "image/jpeg": ("IMAGE", ".jpg"),
    "image/png": ("IMAGE", ".png"),
    "image/webp": ("IMAGE", ".webp"),
    "image/avif": ("IMAGE", ".avif"),
    "audio/mpeg": ("AUDIO", ".mp3"),
    "audio/wav": ("AUDIO", ".wav"),
    "audio/ogg": ("AUDIO", ".ogg"),
    "video/mp4": ("VIDEO", ".mp4"),
    "video/webm": ("VIDEO", ".webm"),
    "video/quicktime": ("VIDEO", ".mov"),
}


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "environment": settings.app_env,
        "auto_publish_enabled": settings.wordpress_allow_auto_publish,
    }


@app.get("/api/v1/organizations/current", response_model=OrganizationOut)
def current_organization(
    identity: IdentityContext = Depends(get_identity), db: Session = Depends(get_db)
):
    return db.get(Organization, identity.organization_id)


@app.get("/api/v1/clinics", response_model=list[ClinicOut])
def list_clinics(identity: IdentityContext = Depends(get_identity), db: Session = Depends(get_db)):
    return db.scalars(
        select(Clinic).where(Clinic.organization_id == identity.organization_id)
    ).all()


@app.post("/api/v1/clinics", response_model=ClinicOut, status_code=201)
def create_clinic(
    payload: ClinicCreate,
    identity: IdentityContext = Depends(require_roles("ORG_ADMIN", "COMPLIANCE_REVIEWER")),
    db: Session = Depends(get_db),
):
    clinic = Clinic(organization_id=identity.organization_id, **payload.model_dump())
    db.add(clinic)
    db.flush()
    record_audit(db, identity, "clinic.create", "clinic", clinic.id, payload.model_dump())
    db.commit()
    db.refresh(clinic)
    return clinic


def tenant_clinic(db: Session, organization_id: str, clinic_id: str) -> Clinic:
    clinic = db.scalar(
        select(Clinic).where(Clinic.id == clinic_id, Clinic.organization_id == organization_id)
    )
    if clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic


@app.get("/api/v1/clinics/{clinic_id}", response_model=ClinicOut)
def get_clinic(
    clinic_id: str,
    identity: IdentityContext = Depends(get_identity),
    db: Session = Depends(get_db),
):
    return tenant_clinic(db, identity.organization_id, clinic_id)


@app.post("/api/v1/clinics/{clinic_id}/licenses", response_model=LicenseOut, status_code=201)
def create_license(
    clinic_id: str,
    payload: LicenseCreate,
    identity: IdentityContext = Depends(require_roles("ORG_ADMIN", "COMPLIANCE_REVIEWER")),
    db: Session = Depends(get_db),
):
    tenant_clinic(db, identity.organization_id, clinic_id)
    license_record = ClinicLicense(
        organization_id=identity.organization_id, clinic_id=clinic_id, **payload.model_dump()
    )
    db.add(license_record)
    db.flush()
    record_audit(
        db, identity, "license.create", "clinic_license", license_record.id, payload.model_dump()
    )
    db.commit()
    db.refresh(license_record)
    return license_record


@app.post("/api/v1/licenses/{license_id}/verify", response_model=LicenseOut)
def verify_license(
    license_id: str,
    reason: str = Query(min_length=3, max_length=500),
    identity: IdentityContext = Depends(require_roles("ORG_ADMIN", "COMPLIANCE_REVIEWER")),
    db: Session = Depends(get_db),
):
    license_record = db.scalar(
        select(ClinicLicense).where(
            ClinicLicense.id == license_id,
            ClinicLicense.organization_id == identity.organization_id,
        )
    )
    if license_record is None:
        raise HTTPException(status_code=404, detail="License not found")
    license_record.status = "VERIFIED"
    license_record.verified_by = identity.user_id
    license_record.verified_at = utcnow()
    record_audit(
        db,
        identity,
        "license.verify",
        "clinic_license",
        license_record.id,
        {"status": "VERIFIED"},
        reason,
    )
    db.commit()
    db.refresh(license_record)
    return license_record


@app.post("/api/v1/licenses/{license_id}/scopes", response_model=ScopeOut, status_code=201)
def create_scope(
    license_id: str,
    payload: ScopeCreate,
    identity: IdentityContext = Depends(require_roles("ORG_ADMIN", "COMPLIANCE_REVIEWER")),
    db: Session = Depends(get_db),
):
    license_record = db.scalar(
        select(ClinicLicense).where(
            ClinicLicense.id == license_id,
            ClinicLicense.organization_id == identity.organization_id,
        )
    )
    if license_record is None:
        raise HTTPException(status_code=404, detail="License not found")
    scope = ProfessionalScope(
        organization_id=identity.organization_id,
        clinic_license_id=license_id,
        **payload.model_dump(),
    )
    db.add(scope)
    db.flush()
    record_audit(db, identity, "scope.create", "professional_scope", scope.id, payload.model_dump())
    db.commit()
    db.refresh(scope)
    return scope


@app.get("/api/v1/services", response_model=list[ServiceOut])
def list_services(identity: IdentityContext = Depends(get_identity), db: Session = Depends(get_db)):
    return db.scalars(
        select(Service).where(Service.organization_id == identity.organization_id)
    ).all()


@app.post("/api/v1/services", response_model=ServiceOut, status_code=201)
def create_service(
    payload: ServiceCreate,
    identity: IdentityContext = Depends(require_roles("ORG_ADMIN")),
    db: Session = Depends(get_db),
):
    tenant_clinic(db, identity.organization_id, payload.clinic_id)
    service = Service(organization_id=identity.organization_id, **payload.model_dump())
    db.add(service)
    db.flush()
    record_audit(db, identity, "service.create", "service", service.id, payload.model_dump())
    db.commit()
    db.refresh(service)
    return service


@app.get("/api/v1/audit-logs", response_model=list[AuditOut])
def list_audit_logs(
    identity: IdentityContext = Depends(require_roles("ORG_ADMIN", "COMPLIANCE_REVIEWER")),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(AuditLog)
        .where(AuditLog.organization_id == identity.organization_id)
        .order_by(AuditLog.created_at.desc())
    ).all()


def media_size_limit(media_type: str) -> int:
    return {
        "IMAGE": settings.r2_max_image_bytes,
        "AUDIO": settings.r2_max_audio_bytes,
        "VIDEO": settings.r2_max_video_bytes,
    }[media_type]


def tenant_media(db: Session, organization_id: str, media_id: str) -> MediaObject:
    media = db.scalar(
        select(MediaObject).where(
            MediaObject.id == media_id,
            MediaObject.organization_id == organization_id,
        )
    )
    if media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media


@app.get("/api/v1/media", response_model=list[MediaOut])
def list_media(identity: IdentityContext = Depends(get_identity), db: Session = Depends(get_db)):
    return db.scalars(
        select(MediaObject)
        .where(MediaObject.organization_id == identity.organization_id)
        .order_by(MediaObject.created_at.desc())
    ).all()


@app.post("/api/v1/media/uploads", response_model=MediaUploadTicket, status_code=201)
def prepare_media_upload(
    payload: MediaUploadRequest,
    identity: IdentityContext = Depends(
        require_roles("ORG_ADMIN", "CONTENT_EDITOR", "COMPLIANCE_REVIEWER")
    ),
    db: Session = Depends(get_db),
    storage: ObjectStorage = Depends(get_object_storage),
):
    media_definition = ALLOWED_MEDIA_TYPES.get(payload.content_type.lower())
    if media_definition is None:
        raise HTTPException(status_code=422, detail="Unsupported media content type")
    media_type, safe_extension = media_definition
    if payload.size_bytes > media_size_limit(media_type):
        raise HTTPException(status_code=413, detail=f"{media_type} exceeds configured size limit")

    now = datetime.now(timezone.utc)
    media_id = str(uuid.uuid4())
    object_key = (
        f"{identity.organization_id}/{media_type.lower()}/{now:%Y/%m}/{media_id}{safe_extension}"
    )
    media = MediaObject(
        id=media_id,
        organization_id=identity.organization_id,
        created_by=identity.user_id,
        object_key=object_key,
        original_filename=Path(payload.filename).name,
        media_type=media_type,
        content_type=payload.content_type.lower(),
        expected_size_bytes=payload.size_bytes,
        checksum_sha256=payload.checksum_sha256.lower() if payload.checksum_sha256 else None,
        contains_patient=payload.contains_patient,
    )
    db.add(media)
    record_audit(
        db,
        identity,
        "media.upload.prepare",
        "media_object",
        media.id,
        {
            "media_type": media_type,
            "content_type": media.content_type,
            "size_bytes": media.expected_size_bytes,
            "contains_patient": media.contains_patient,
        },
    )
    upload_url = storage.create_upload_url(media.object_key, media.content_type)
    db.commit()
    return MediaUploadTicket(
        media_id=media.id,
        object_key=media.object_key,
        upload_url=upload_url,
        required_headers={"Content-Type": media.content_type},
        expires_in_seconds=settings.r2_presigned_url_ttl_seconds,
    )


@app.post("/api/v1/media/{media_id}/complete", response_model=MediaOut)
def complete_media_upload(
    media_id: str,
    identity: IdentityContext = Depends(
        require_roles("ORG_ADMIN", "CONTENT_EDITOR", "COMPLIANCE_REVIEWER")
    ),
    db: Session = Depends(get_db),
    storage: ObjectStorage = Depends(get_object_storage),
):
    media = tenant_media(db, identity.organization_id, media_id)
    if media.status == "AVAILABLE":
        return media
    try:
        metadata = storage.head(media.object_key)
    except Exception as error:
        raise HTTPException(status_code=409, detail="R2 object is not available") from error
    if metadata.size_bytes != media.expected_size_bytes:
        raise HTTPException(status_code=409, detail="Uploaded object size does not match")
    if metadata.content_type.lower() != media.content_type:
        raise HTTPException(status_code=409, detail="Uploaded object content type does not match")

    media.actual_size_bytes = metadata.size_bytes
    media.status = "AVAILABLE"
    record_audit(
        db,
        identity,
        "media.upload.complete",
        "media_object",
        media.id,
        {"status": media.status, "actual_size_bytes": media.actual_size_bytes},
    )
    db.commit()
    db.refresh(media)
    return media


@app.post("/api/v1/media/{media_id}/download", response_model=MediaDownloadTicket)
def create_media_download(
    media_id: str,
    identity: IdentityContext = Depends(get_identity),
    db: Session = Depends(get_db),
    storage: ObjectStorage = Depends(get_object_storage),
):
    media = tenant_media(db, identity.organization_id, media_id)
    if media.status != "AVAILABLE":
        raise HTTPException(status_code=409, detail="Media is not available")
    return MediaDownloadTicket(
        download_url=storage.create_download_url(media.object_key, media.original_filename),
        expires_in_seconds=settings.r2_presigned_url_ttl_seconds,
    )
