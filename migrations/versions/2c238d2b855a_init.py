"""init

Revision ID: 2c238d2b855a
Revises: 
Create Date: 2023-01-18 23:23:10.913617

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2c238d2b855a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('occupation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('occupation', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('occupation')
    )
    op.create_table('user',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('birthdate', sa.DATE(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('avatar_url', sa.String(), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('firstname_idx', 'user', ['firstname'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    op.create_index('lastname_idx', 'user', ['lastname'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.create_table('client',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('user', postgresql.UUID(), nullable=True),
    sa.Column('occupation', sa.String(length=30), nullable=True),
    sa.Column('work_place', sa.String(length=30), nullable=True),
    sa.Column('income', sa.String(length=30), nullable=True),
    sa.Column('imgs', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('telegram_id', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['user.email'], ),
    sa.ForeignKeyConstraint(['occupation'], ['occupation.occupation'], ),
    sa.ForeignKeyConstraint(['phone_number'], ['user.phone_number'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('email_idx', 'client', ['email'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.create_index('imgs_idx', 'client', ['imgs'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.create_index('occupation_idx', 'client', ['occupation'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.create_index('user_idx', 'client', ['user'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.create_index('work_place_idx', 'client', ['work_place'], unique=False, postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('work_place_idx', table_name='client', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_index('user_idx', table_name='client', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_index('occupation_idx', table_name='client', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_index('imgs_idx', table_name='client', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_index('email_idx', table_name='client', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_table('client')
    op.drop_index('lastname_idx', table_name='user', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index('firstname_idx', table_name='user', postgresql_ops={'description': 'gin_trgm_ops'}, postgresql_using='gin')
    op.drop_table('user')
    op.drop_table('occupation')
    # ### end Alembic commands ###