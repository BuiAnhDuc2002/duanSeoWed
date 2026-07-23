"""Add tenant-scoped R2 media metadata.

Data impact: creates media_objects only; binaries remain in Cloudflare R2.
Rollback: drops metadata table and does not delete R2 objects.
"""

from alembic import op

from app.models import MediaObject

revision = "0002_media_objects"
down_revision = "0001_foundation"
branch_labels = None
depends_on = None


def upgrade() -> None:
    MediaObject.__table__.create(bind=op.get_bind())


def downgrade() -> None:
    MediaObject.__table__.drop(bind=op.get_bind())
