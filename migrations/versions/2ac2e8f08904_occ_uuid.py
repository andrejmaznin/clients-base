"""occ_uuid

Revision ID: 2ac2e8f08904
Revises: f9a7acad0104
Create Date: 2023-01-22 13:56:22.282890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2ac2e8f08904'
down_revision = 'f9a7acad0104'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('occupation', sa.Column('id', postgresql.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('occupation', 'id')
    # ### end Alembic commands ###
