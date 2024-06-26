"""Added date to note table

Revision ID: dce24d04f064
Revises: 0f2a6810e7b2
Create Date: 2024-04-11 18:20:36.530100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dce24d04f064'
down_revision: Union[str, None] = '0f2a6810e7b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'date')
    # ### end Alembic commands ###
