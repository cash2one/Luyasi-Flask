"""add read_count and type

Revision ID: 1d7a27a6f75
Revises: 108eeecca214
Create Date: 2014-12-05 15:01:18.065000

"""

# revision identifiers, used by Alembic.
revision = '1d7a27a6f75'
down_revision = '108eeecca214'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_blog', sa.Column('category', sa.Integer(), nullable=False))
    op.add_column('blog_blog', sa.Column('read_count', sa.Integer(), nullable=False))
    op.add_column('job_job', sa.Column('read_count', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_job', 'read_count')
    op.drop_column('blog_blog', 'read_count')
    op.drop_column('blog_blog', 'category')
    ### end Alembic commands ###