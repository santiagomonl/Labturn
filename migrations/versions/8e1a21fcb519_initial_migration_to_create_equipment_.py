"""Initial migration to create equipment and reservation tables

Revision ID: 8e1a21fcb519
Revises: 
Create Date: 2025-02-02 00:35:28.016997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1a21fcb519'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=100), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=50), nullable=False),
    sa.Column('start_time', sa.String(length=5), nullable=False),
    sa.Column('end_time', sa.String(length=5), nullable=False),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    op.drop_table('equipment')
    # ### end Alembic commands ###
