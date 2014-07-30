"""change message

Revision ID: 307bbde4a79b
Revises: 3b2e937e56a1
Create Date: 2014-07-29 11:36:28.866000

"""

# revision identifiers, used by Alembic.
revision = '307bbde4a79b'
down_revision = '3b2e937e56a1'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('xiaoyuan_messages_users',
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['xiaoyuan_message.id'], name=op.f('fk__xiaoyuan_messages_users__message_id__xiaoyuan_message')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_messages_users__user_id__security_user'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('xiaoyuan_messages_users')
    ### end Alembic commands ###
