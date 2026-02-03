"""baseline

Revision ID: 20201527768f
Revises: 
Create Date: 2026-02-02 14:49:41.801534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20201527768f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    pass


def downgrade():
    """Downgrade schema."""
    pass
