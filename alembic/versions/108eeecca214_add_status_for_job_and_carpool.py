"""add status for job and carpool

Revision ID: 108eeecca214
Revises: 553451d4194b
Create Date: 2014-10-27 11:36:55.839000

"""

# revision identifiers, used by Alembic.
revision = '108eeecca214'
down_revision = '553451d4194b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpool_carpoolinfo', sa.Column('status', sa.Integer(), nullable=False))
    op.add_column('job_job', sa.Column('status', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_job', 'status')
    op.drop_column('carpool_carpoolinfo', 'status')
    ### end Alembic commands ###