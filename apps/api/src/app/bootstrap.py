from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Membership, Organization, User

ADMIN_USER = "00000000-0000-0000-0000-000000000001"
VIEWER_USER = "00000000-0000-0000-0000-000000000002"
ORG_A = "10000000-0000-0000-0000-000000000001"
ORG_B = "20000000-0000-0000-0000-000000000002"


def bootstrap_development(db: Session) -> None:
    if db.scalar(select(Organization.id).limit(1)):
        return
    db.add_all(
        [
            Organization(id=ORG_A, name="Phòng khám Demo A", slug="demo-a"),
            Organization(id=ORG_B, name="Phòng khám Demo B", slug="demo-b"),
            User(id=ADMIN_USER, email="admin-a@example.test", display_name="Admin A"),
            User(id=VIEWER_USER, email="viewer-b@example.test", display_name="Viewer B"),
            Membership(organization_id=ORG_A, user_id=ADMIN_USER, roles=["ORG_ADMIN"]),
            Membership(organization_id=ORG_B, user_id=VIEWER_USER, roles=["VIEWER"]),
        ]
    )
    db.commit()
