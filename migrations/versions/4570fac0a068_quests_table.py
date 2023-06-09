"""quests table

Revision ID: 4570fac0a068
Revises: a34527f1c0e4
Create Date: 2022-06-06 19:19:30.059189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4570fac0a068'
down_revision = 'a34527f1c0e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ind', sa.String(length=16), nullable=True),
    sa.Column('quest', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quests')
    # ### end Alembic commands ###
