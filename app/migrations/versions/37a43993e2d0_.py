"""empty message

Revision ID: 37a43993e2d0
Revises: 
Create Date: 2023-02-11 11:38:47.980336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a43993e2d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=12), nullable=False),
    sa.Column('fname', sa.String(length=20), nullable=False),
    sa.Column('lname', sa.String(length=20), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('join_date', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('corps', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###