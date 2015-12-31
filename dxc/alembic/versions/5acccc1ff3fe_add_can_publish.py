"""add can_publish

Revision ID: 5acccc1ff3fe
Revises: 3e9b1a34ae5a
Create Date: 2015-12-13 21:18:45.292000

"""

# revision identifiers, used by Alembic.
revision = '5acccc1ff3fe'
down_revision = '3e9b1a34ae5a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_blog', sa.Column('can_publish', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_blog', 'can_publish')
    ### end Alembic commands ###