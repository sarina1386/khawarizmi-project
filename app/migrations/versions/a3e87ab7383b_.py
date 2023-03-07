"""empty message

Revision ID: a3e87ab7383b
Revises: 3ed38b920ce8
Create Date: 2023-02-14 16:33:19.172769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3e87ab7383b'
down_revision = '3ed38b920ce8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contents',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('lesson', sa.Integer(), nullable=True),
    sa.Column('session', sa.Integer(), nullable=True),
    sa.Column('script', sa.String(length=550), nullable=True),
    sa.Column('video', sa.String(length=120), nullable=True),
    sa.Column('deaf', sa.String(length=120), nullable=True),
    sa.Column('quiz', sa.String(length=550), nullable=True),
    sa.Column('tabs_num', sa.Integer(), nullable=True),
    sa.Column('tabs_content', sa.String(length=550), nullable=True),
    sa.PrimaryKeyConstraint('cid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contents')
    # ### end Alembic commands ###