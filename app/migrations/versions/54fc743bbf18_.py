"""empty message

Revision ID: 54fc743bbf18
Revises: a3e87ab7383b
Create Date: 2023-02-22 11:27:44.146151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54fc743bbf18'
down_revision = 'a3e87ab7383b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('activity',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=550),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('activity',
               existing_type=sa.String(length=550),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###
