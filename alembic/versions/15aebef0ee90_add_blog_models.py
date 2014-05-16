"""add blog models

Revision ID: 15aebef0ee90
Revises: 8fd997c518b
Create Date: 2014-05-15 17:31:55.736000

"""

# revision identifiers, used by Alembic.
revision = '15aebef0ee90'
down_revision = '8fd997c518b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__blog_blog__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__blog_blog')),
    sa.UniqueConstraint('title', name=op.f('uq__blog_blog__title'))
    )
    op.create_table('blog_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ref_comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog_blog.id'], name=op.f('fk__blog_comment__blog_id__blog_blog')),
    sa.ForeignKeyConstraint(['ref_comment_id'], ['blog_comment.id'], name=op.f('fk__blog_comment__ref_comment_id__blog_comment')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__blog_comment__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__blog_comment'))
    )
    ### end Alembic commands ###
def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_comment')
    op.drop_table('blog_blog')
    ### end Alembic commands ###
