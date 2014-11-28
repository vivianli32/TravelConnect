from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
messages = Table('messages', post_meta,
    Column('mess_id', Integer, primary_key=True, nullable=False),
    Column('sender', Integer),
    Column('receiver', Integer),
    Column('text', String(length=5000)),
    Column('time', DateTime),
)

ratings = Table('ratings', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('rating_user', Integer),
    Column('rated_user', Integer),
    Column('rating', Float(precision=1)),
    Column('comment', Text(length=600)),
    Column('time', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['messages'].create()
    post_meta.tables['ratings'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['messages'].drop()
    post_meta.tables['ratings'].drop()
