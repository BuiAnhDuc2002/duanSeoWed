from sqlalchemy.orm import Session

from app.auth import IdentityContext
from app.models import AuditLog


def record_audit(
    db: Session,
    identity: IdentityContext,
    action: str,
    resource_type: str,
    resource_id: str,
    summary: dict,
    reason: str | None = None,
) -> None:
    db.add(
        AuditLog(
            organization_id=identity.organization_id,
            actor_id=identity.user_id,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            after_summary=summary,
            reason=reason,
        )
    )
