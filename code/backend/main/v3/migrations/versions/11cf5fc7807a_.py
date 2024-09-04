"""empty message

Revision ID: 11cf5fc7807a
Revises: 
Create Date: 2024-08-11 16:01:24.378386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11cf5fc7807a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('role', sa.String(length=6), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
