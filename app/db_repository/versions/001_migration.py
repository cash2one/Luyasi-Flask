from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=255)),
    Column('username', VARCHAR(length=80)),
    Column('password', VARCHAR(length=255)),
    Column('active', BOOLEAN),
    Column('nickname', VARCHAR(length=80)),
    Column('bind_username', VARCHAR(length=255)),
    Column('bind_email', VARCHAR(length=80)),
    Column('openid', VARCHAR(length=80)),
    Column('provider', VARCHAR(length=20)),
    Column('confirmed_at', DATETIME),
    Column('last_login_at', DATETIME),
    Column('current_login_at', DATETIME),
    Column('last_login_ip', VARCHAR(length=80)),
    Column('current_login_ip', VARCHAR(length=80)),
    Column('login_count', INTEGER),
    Column('atest', VARCHAR),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['atest'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['atest'].create()
