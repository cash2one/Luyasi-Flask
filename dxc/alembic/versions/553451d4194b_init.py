"""init

Revision ID: 553451d4194b
Revises: None
Create Date: 2014-10-10 11:46:33.187000

"""

# revision identifiers, used by Alembic.
revision = '553451d4194b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
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
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_user')),
    sa.UniqueConstraint('email', name=op.f('uq__security_user__email')),
    sa.UniqueConstraint('openid', 'provider', name='uq__user__openid__provider'),
    sa.UniqueConstraint('username', name=op.f('uq__security_user__username'))
    )
    op.create_table('security_right',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=50), nullable=True),
    sa.Column('app', sa.String(length=50), nullable=True),
    sa.Column('entity', sa.String(length=50), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_right'))
    )
    op.create_table('xiaoyuan_academy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.PrimaryKeyConstraint('id', name=op.f('pk__xiaoyuan_academy')),
    sa.UniqueConstraint('name', name=op.f('uq__xiaoyuan_academy__name'))
    )
    op.create_table('security_app',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.PrimaryKeyConstraint('id', name=op.f('pk__security_app')),
    sa.UniqueConstraint('name', name=op.f('uq__security_app__name'))
    )
    op.create_table('qingbank_department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.PrimaryKeyConstraint('id', name=op.f('pk__qingbank_department')),
    sa.UniqueConstraint('name', name=op.f('uq__qingbank_department__name'))
    )
    op.create_table('qingbank_doc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('is_leaf', sa.Boolean(name='is_leaf'), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['parent_id'], ['qingbank_doc.id'], name=op.f('fk__qingbank_doc__parent_id__qingbank_doc')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__qingbank_doc'))
    )
    op.create_table('xiaoyuan_academies_users',
    sa.Column('academy_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['academy_id'], ['xiaoyuan_academy.id'], name=op.f('fk__xiaoyuan_academies_users__academy_id__xiaoyuan_academy')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_academies_users__user_id__security_user'))
    )
    op.create_table('job_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('content', sa.String(length=5120), nullable=True),
    sa.Column('job_type', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Boolean(name='deleted'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__job_job__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__job_job'))
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
    op.create_table('qingbank_contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('name_pinyin', sa.String(length=30), nullable=True),
    sa.Column('name_shot', sa.String(length=10), nullable=True),
    sa.Column('duty', sa.String(length=10), nullable=True),
    sa.Column('mobile', sa.String(length=14), nullable=True),
    sa.Column('telephone', sa.String(length=20), nullable=True),
    sa.Column('innerphone', sa.String(length=20), nullable=True),
    sa.Column('fax', sa.String(length=14), nullable=True),
    sa.Column('qq', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['department_id'], ['qingbank_department.id'], name=op.f('fk__qingbank_contact__department_id__qingbank_department')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__qingbank_contact__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__qingbank_contact'))
    )
    op.create_table('xiaoyuan_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('academy_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['academy_id'], ['xiaoyuan_academy.id'], name=op.f('fk__xiaoyuan_class__academy_id__xiaoyuan_academy')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__xiaoyuan_class')),
    sa.UniqueConstraint('name', name=op.f('uq__xiaoyuan_class__name'))
    )
    op.create_table('blog_blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__blog_blog__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__blog_blog'))
    )
    op.create_table('carpool_carpoolinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.String(length=50), nullable=True),
    sa.Column('target', sa.String(length=50), nullable=True),
    sa.Column('route', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('contact_info', sa.String(length=128), nullable=True),
    sa.Column('deleted', sa.Boolean(name='deleted'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__carpool_carpoolinfo__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__carpool_carpoolinfo'))
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
    op.create_table('xiaoyuan_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=256), nullable=True),
    sa.Column('reply_message_id', sa.Integer(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['reply_message_id'], ['xiaoyuan_message.id'], name=op.f('fk__xiaoyuan_message__reply_message_id__xiaoyuan_message')),
    sa.ForeignKeyConstraint(['sender_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_message__sender_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__xiaoyuan_message'))
    )
    op.create_table('job_report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('is_audit', sa.Boolean(name='is_audit'), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['job_id'], ['job_job.id'], name=op.f('fk__job_report__job_id__job_job')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__job_report'))
    )
    op.create_table('xiaoyuan_messages_users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('is_read', sa.Boolean(name='is_read'), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['xiaoyuan_message.id'], name=op.f('fk__xiaoyuan_messages_users__message_id__xiaoyuan_message')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_messages_users__user_id__security_user')),
    sa.PrimaryKeyConstraint('user_id', 'message_id', name=op.f('pk__xiaoyuan_messages_users'))
    )
    op.create_table('blog_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=True),
    sa.Column('floor', sa.Integer(), nullable=True),
    sa.Column('first_comment_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ref_comment_id', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),    sa.Column('create_at', sa.DateTime(), nullable=True),    sa.Column('version', sa.Integer(), nullable=False),    sa.ForeignKeyConstraint(['blog_id'], ['blog_blog.id'], name=op.f('fk__blog_comment__blog_id__blog_blog')),
    sa.ForeignKeyConstraint(['first_comment_id'], ['blog_comment.id'], name=op.f('fk__blog_comment__first_comment_id__blog_comment')),
    sa.ForeignKeyConstraint(['ref_comment_id'], ['blog_comment.id'], name=op.f('fk__blog_comment__ref_comment_id__blog_comment')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__blog_comment__user_id__security_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__blog_comment'))
    )
    op.create_table('xiaoyuan_academies_classes',
    sa.Column('academy_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['academy_id'], ['xiaoyuan_academy.id'], name=op.f('fk__xiaoyuan_academies_classes__academy_id__xiaoyuan_academy')),
    sa.ForeignKeyConstraint(['class_id'], ['xiaoyuan_class.id'], name=op.f('fk__xiaoyuan_academies_classes__class_id__xiaoyuan_class'))
    )
    op.create_table('xiaoyuan_msges_users',
    sa.Column('messsage_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['messsage_id'], ['xiaoyuan_message.id'], name=op.f('fk__xiaoyuan_msges_users__messsage_id__xiaoyuan_message')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_msges_users__user_id__security_user'))
    )
    op.create_table('xiaoyuan_classes_users',
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['xiaoyuan_class.id'], name=op.f('fk__xiaoyuan_classes_users__class_id__xiaoyuan_class')),
    sa.ForeignKeyConstraint(['user_id'], ['security_user.id'], name=op.f('fk__xiaoyuan_classes_users__user_id__security_user'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('xiaoyuan_classes_users')
    op.drop_table('xiaoyuan_msges_users')
    op.drop_table('xiaoyuan_academies_classes')
    op.drop_table('blog_comment')
    op.drop_table('xiaoyuan_messages_users')
    op.drop_table('job_report')
    op.drop_table('xiaoyuan_message')
    op.drop_table('security_users_roles')
    op.drop_table('security_users_apps')
    op.drop_table('carpool_carpoolinfo')
    op.drop_table('blog_blog')
    op.drop_table('xiaoyuan_class')
    op.drop_table('qingbank_contact')
    op.drop_table('security_users_rights')
    op.drop_table('security_roles_rights')
    op.drop_table('job_job')
    op.drop_table('xiaoyuan_academies_users')
    op.drop_table('qingbank_doc')
    op.drop_table('qingbank_department')
    op.drop_table('security_app')
    op.drop_table('xiaoyuan_academy')
    op.drop_table('security_right')
    op.drop_table('security_user')
    op.drop_table('security_role')
    ### end Alembic commands ###
