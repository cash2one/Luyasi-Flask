"""change user_class with is_charger

Revision ID: 3933c26bd40b
Revises: 2deb650e1183
Create Date: 2015-01-06 12:47:38.791000

"""

# revision identifiers, used by Alembic.
revision = '3933c26bd40b'
down_revision = '2deb650e1183'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('xiaoyuan_class_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('is_charger', sa.Boolean(name='is_charger'), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['xiaoyuan_class.id'], name=op.f('fk__xiaoyuan_class_user__class_id__xiaoyuan_class')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_class_user__user_id__security_user')),
    sa.PrimaryKeyConstraint('user_id', 'class_id', name=op.f('pk__xiaoyuan_class_user'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('xiaoyuan_class_user')
    ### end Alembic commands ###
