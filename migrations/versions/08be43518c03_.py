"""empty message

Revision ID: 08be43518c03
Revises: 590fb12db843
Create Date: 2022-06-06 23:54:41.523892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08be43518c03'
down_revision = '590fb12db843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_quest', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('second_quest', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'second_quest')
    op.drop_column('user', 'first_quest')
    # ### end Alembic commands ###
