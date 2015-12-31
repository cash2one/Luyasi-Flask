"""init

Revision ID: 3a65141913b1
Revises: 
Create Date: 2015-12-02 15:53:44.575000

"""

# revision identifiers, used by Alembic.
revision = '3a65141913b1'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('security_right',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=50), nullable=True),
    sa.Column('app', sa.String(length=50), nullable=True),
    sa.Column('entity', sa.String(length=50), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_right'))
    )
    op.create_table('security_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_role')),
    sa.UniqueConstraint('name', name=op.f('uq__security_role__name'))
    )
    op.create_table('security_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(name='active'), nullable=True),
    sa.Column('nickname', sa.String(length=80), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('bind_username', sa.String(length=255), nullable=True),
    sa.Column('bind_email', sa.String(length=80), nullable=True),
    sa.Column('bind_remind', sa.Boolean(name='bind_remind'), nullable=True),
    sa.Column('openid', sa.String(length=80), nullable=True),
    sa.Column('provider', sa.String(length=20), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('current_login_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_ip', sa.String(length=80), nullable=True),
    sa.Column('current_login_ip', sa.String(length=80), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_user')),
    sa.UniqueConstraint('email', name=op.f('uq__security_user__email')),
    sa.UniqueConstraint('openid', 'provider', name='uq__user__openid__provider'),
    sa.UniqueConstraint('username', name=op.f('uq__security_user__username'))
    )
    op.create_table('security_app',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('app_version', sa.String(length=32), nullable=True),
    sa.Column('app_vercode', sa.Integer(), nullable=True),
    sa.Column('update_url', sa.String(length=255), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_app')),
    sa.UniqueConstraint('name', name=op.f('uq__security_app__name'))
    )
    op.create_table('security_users_apps',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('app_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['app_id'], ['security_app.id'], name=op.f('fk__security_users_apps__app_id__security_app')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__security_users_apps__user_id__security_user'))
    )
    op.create_table('security_users_roles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['security_role.id'], name=op.f('fk__security_users_roles__role_id__security_role')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__security_users_roles__user_id__security_user'))
    )
    op.create_table('garage_garagerent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('position', sa.String(length=20), nullable=True),
    sa.Column('contact', sa.String(length=20), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('close', sa.Boolean(name='close'), nullable=False),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('read', sa.Integer(), nullable=True),
    sa.Column('publisher_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['publisher_id'], ['security_user.id'], name=op.f('fk__garage_garagerent__publisher_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__garage_garagerent'))
    )
    op.create_table('security_sysmessage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=512), nullable=False),
    sa.Column('is_read', sa.Boolean(name='is_read'), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['receiver_id'], ['security_user.id'], name=op.f('fk__security_sysmessage__receiver_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_sysmessage'))
    )
    op.create_table('security_roles_rights',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['security_right.id'], name=op.f('fk__security_roles_rights__right_id__security_right')),
    sa.ForeignKeyConstraint(['role_id'], ['security_role.id'], name=op.f('fk__security_roles_rights__role_id__security_role'))
    )
    op.create_table('security_users_rights',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['security_right.id'], name=op.f('fk__security_users_rights__right_id__security_right')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__security_users_rights__user_id__security_user'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('security_users_rights')
    op.drop_table('security_roles_rights')
    op.drop_table('security_sysmessage')
    op.drop_table('garage_garagerent')
    op.drop_table('security_users_roles')
    op.drop_table('security_users_apps')
    op.drop_table('security_app')
    op.drop_table('security_user')
    op.drop_table('security_role')
    op.drop_table('security_right')
    ### end Alembic commands ###