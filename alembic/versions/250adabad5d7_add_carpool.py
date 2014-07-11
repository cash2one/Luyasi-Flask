"""add carpool

Revision ID: 250adabad5d7
Revises: 140690d9bf74
Create Date: 2014-07-09 11:25:09.209000

"""

# revision identifiers, used by Alembic.
revision = '250adabad5d7'
down_revision = '140690d9bf74'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carpool_carpoolinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.String(length=50), nullable=True),
    sa.Column('target', sa.String(length=50), nullable=True),
    sa.Column('route', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('contact_info', sa.String(length=128), nullable=True),
    sa.Column('delete', sa.Boolean(name='deleted'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__carpool_carpoolinfo__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__carpool_carpoolinfo'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carpool_carpoolinfo')
    ### end Alembic commands ###