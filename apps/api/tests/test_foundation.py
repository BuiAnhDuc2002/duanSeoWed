from app.bootstrap import ORG_A
from app.storage import ObjectMetadata


def test_health_disables_auto_publish(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["auto_publish_enabled"] is False


def test_create_clinic_is_tenant_scoped_and_audited(client, admin_headers):
    response = client.post(
        "/api/v1/clinics",
        headers=admin_headers,
        json={
            "legal_name": "Công ty Phòng khám A",
            "brand_name": "Thẩm mỹ A",
            "address": "Quận 1, TP.HCM",
        },
    )
    assert response.status_code == 201
    clinic = response.json()
    assert clinic["organization_id"] == ORG_A

    logs = client.get("/api/v1/audit-logs", headers=admin_headers)
    assert logs.status_code == 200
    assert logs.json()[0]["action"] == "clinic.create"


def test_cross_tenant_clinic_access_returns_not_found(client, admin_headers, viewer_headers):
    created = client.post(
        "/api/v1/clinics",
        headers=admin_headers,
        json={"legal_name": "Clinic A", "brand_name": "A Brand", "address": "Hà Nội"},
    ).json()
    response = client.get(f"/api/v1/clinics/{created['id']}", headers=viewer_headers)
    assert response.status_code == 404


def test_viewer_cannot_create_clinic(client, viewer_headers):
    response = client.post(
        "/api/v1/clinics",
        headers=viewer_headers,
        json={"legal_name": "Clinic B", "brand_name": "B Brand", "address": "Đà Nẵng"},
    )
    assert response.status_code == 403


def test_forged_membership_context_is_rejected(client, admin_headers):
    forged = {**admin_headers, "X-Organization-Id": "20000000-0000-0000-0000-000000000002"}
    response = client.get("/api/v1/clinics", headers=forged)
    assert response.status_code == 403


def test_license_verification_creates_audit(client, admin_headers):
    clinic = client.post(
        "/api/v1/clinics",
        headers=admin_headers,
        json={"legal_name": "Clinic A", "brand_name": "A Brand", "address": "TP.HCM"},
    ).json()
    license_record = client.post(
        f"/api/v1/clinics/{clinic['id']}/licenses",
        headers=admin_headers,
        json={"license_number": "GP-001", "issuing_authority": "Sở Y tế"},
    ).json()
    verified = client.post(
        f"/api/v1/licenses/{license_record['id']}/verify",
        params={"reason": "Đã đối chiếu tài liệu gốc"},
        headers=admin_headers,
    )
    assert verified.status_code == 200
    assert verified.json()["status"] == "VERIFIED"
    actions = [
        item["action"] for item in client.get("/api/v1/audit-logs", headers=admin_headers).json()
    ]
    assert "license.verify" in actions


def test_r2_media_upload_is_tenant_scoped_and_direct(client, admin_headers, viewer_headers):
    prepared = client.post(
        "/api/v1/media/uploads",
        headers=admin_headers,
        json={
            "filename": "../../patient-photo.jpg",
            "content_type": "image/jpeg",
            "size_bytes": 1024,
            "contains_patient": True,
        },
    )
    assert prepared.status_code == 201
    ticket = prepared.json()
    assert ticket["object_key"].startswith(f"{ORG_A}/image/")
    assert ticket["upload_url"].startswith("https://r2.example.test/upload/")
    assert ticket["required_headers"] == {"Content-Type": "image/jpeg"}

    client.fake_storage.objects[ticket["object_key"]] = ObjectMetadata(
        size_bytes=1024, content_type="image/jpeg"
    )
    completed = client.post(f"/api/v1/media/{ticket['media_id']}/complete", headers=admin_headers)
    assert completed.status_code == 200
    assert completed.json()["status"] == "AVAILABLE"
    assert completed.json()["original_filename"] == "patient-photo.jpg"

    cross_tenant = client.post(
        f"/api/v1/media/{ticket['media_id']}/download", headers=viewer_headers
    )
    assert cross_tenant.status_code == 404


def test_r2_media_rejects_unsupported_type_and_oversized_file(client, admin_headers):
    unsupported = client.post(
        "/api/v1/media/uploads",
        headers=admin_headers,
        json={
            "filename": "payload.exe",
            "content_type": "application/octet-stream",
            "size_bytes": 10,
        },
    )
    assert unsupported.status_code == 422

    oversized = client.post(
        "/api/v1/media/uploads",
        headers=admin_headers,
        json={
            "filename": "large.jpg",
            "content_type": "image/jpeg",
            "size_bytes": 25 * 1024 * 1024 + 1,
        },
    )
    assert oversized.status_code == 413
