"""empty message

Revision ID: 24ffbd1312c8
Revises: a725ff6e90a0
Create Date: 2023-04-04 11:40:02.819890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24ffbd1312c8'
down_revision = 'a725ff6e90a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
    sa.Column('qid', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.Column('session', sa.Integer(), nullable=True),
    sa.Column('questions', sa.String(length=5000), nullable=True),
    sa.Column('answers', sa.String(length=1000), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('qid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz')
    # ### end Alembic commands ###
