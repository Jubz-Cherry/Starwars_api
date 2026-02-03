"""create user_favorites table

Revision ID: da638591c5ec
Revises: f49b2393c324
Create Date: 2026-02-02 14:55:53.315232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da638591c5ec'
down_revision: Union[str, Sequence[str], None] = 'f49b2393c324'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
