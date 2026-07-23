"""Foundation tenant, RBAC, clinic and audit schema.

Data impact: creates new tables only.
Rollback: drops the new tables in reverse dependency order.
"""

from alembic import op

from app.models import (
    AuditLog,
    Clinic,
    ClinicLicense,
    Membership,
    Organization,
    ProfessionalScope,
    Service,
    User,
)

revision = "0001_foundation"
down_revision = None
branch_labels = None
depends_on = None

FOUNDATION_TABLES = [
    Organization.__table__,
    User.__table__,
    Membership.__table__,
    Clinic.__table__,
    ClinicLicense.__table__,
    ProfessionalScope.__table__,
    Service.__table__,
    AuditLog.__table__,
]


def upgrade() -> None:
    bind = op.get_bind()
    for table in FOUNDATION_TABLES:
        table.create(bind=bind)


def downgrade() -> None:
    bind = op.get_bind()
    for table in reversed(FOUNDATION_TABLES):
        table.drop(bind=bind)
