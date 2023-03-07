"""empty message

Revision ID: 3ed38b920ce8
Revises: 37a43993e2d0
Create Date: 2023-02-11 11:40:58.795633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ed38b920ce8'
down_revision = '37a43993e2d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activity', sa.String(length=120), nullable=True))
        batch_op.drop_column('corps')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('corps', sa.VARCHAR(length=120), nullable=True))
        batch_op.drop_column('activity')

    # ### end Alembic commands ###