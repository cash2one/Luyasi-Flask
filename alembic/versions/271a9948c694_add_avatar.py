"""add avatar

Revision ID: 271a9948c694
Revises: 38996390258c
Create Date: 2014-06-19 11:10:47.667000

"""

# revision identifiers, used by Alembic.
revision = '271a9948c694'
down_revision = '38996390258c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('security_user', sa.Column('avatar', sa.String(length=255), nullable=True))
    ### end Alembic commands ###
def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('security_user', 'avatar')
    ### end Alembic commands ###