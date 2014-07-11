"""create job

Revision ID: 30d48827b2f
Revises: 271a9948c694
Create Date: 2014-07-04 09:49:05.727000

"""

# revision identifiers, used by Alembic.
revision = '30d48827b2f'
down_revision = '271a9948c694'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('content', sa.String(length=5120), nullable=True),
    sa.Column('job_type', sa.Integer(), nullable=True),
    sa.Column('delete', sa.Boolean(name='deleted'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__job_job__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__job_job'))
    )
    op.create_table('job_report',
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('is_audit', sa.Boolean(name='is_audit'), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job_job.id'], name=op.f('fk__job_report__job_id__job_job')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__job_report'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job_report')
    op.drop_table('job_job')
    ### end Alembic commands ###