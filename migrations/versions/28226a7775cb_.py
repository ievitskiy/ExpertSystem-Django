"""empty message

Revision ID: 28226a7775cb
Revises: 08be43518c03
Create Date: 2022-06-07 00:30:34.204853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28226a7775cb'
down_revision = '08be43518c03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('reg_time', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_reg_time'), 'user', ['reg_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_reg_time'), table_name='user')
    op.drop_column('user', 'reg_time')
    # ### end Alembic commands ###
