from dataclasses import dataclass

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Membership


@dataclass(frozen=True)
class IdentityContext:
    user_id: str
    organization_id: str
    roles: frozenset[str]


def get_identity(
    x_user_id: str = Header(...),
    x_organization_id: str = Header(...),
    db: Session = Depends(get_db),
) -> IdentityContext:
    membership = db.scalar(
        select(Membership).where(
            Membership.user_id == x_user_id,
            Membership.organization_id == x_organization_id,
        )
    )
    if membership is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Membership not found")
    return IdentityContext(x_user_id, x_organization_id, frozenset(membership.roles))


def require_roles(*allowed: str):
    def dependency(identity: IdentityContext = Depends(get_identity)) -> IdentityContext:
        if identity.roles.isdisjoint(allowed):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
        return identity

    return dependency
