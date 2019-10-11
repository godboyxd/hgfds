"""Moved some text columns to longtext type

Revision ID: 40cbd3e0f22d
Revises: 9bf2adbc33e8
Create Date: 2017-07-10 00:01:53.940034

"""

# revision identifiers, used by Alembic.
revision = '40cbd3e0f22d'
down_revision = '9bf2adbc33e8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cosmetics', 'css',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('guild_members', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guild_members', 'banned',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False,
               existing_server_default=sa.text(u"'0'"))
    op.alter_column('guilds', 'bracket_links',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guilds', 'channels',
               existing_type=mysql.MEDIUMTEXT(collation=u'utf8mb4_unicode_ci'),
               type_=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               existing_nullable=False)
    op.alter_column('guilds', 'chat_links',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guilds', 'emojis',
               existing_type=mysql.TEXT(collation=u'utf8mb4_unicode_ci'),
               type_=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               existing_nullable=False)
    op.alter_column('guilds', 'roles',
               existing_type=mysql.MEDIUMTEXT(collation=u'utf8mb4_unicode_ci'),
               type_=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               existing_nullable=False)
    op.alter_column('guilds', 'unauth_users',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guilds', 'visitor_view',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('guilds', 'webhooks',
               existing_type=mysql.TEXT(collation=u'utf8mb4_unicode_ci'),
               type_=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               existing_nullable=False)
    op.alter_column('unauthenticated_users', 'revoked',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False,
               existing_server_default=sa.text(u"'0'"))
    op.alter_column('user_css', 'css',
               existing_type=mysql.MEDIUMTEXT(collation=u'utf8mb4_unicode_ci'),
               type_=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_css', 'css',
               existing_type=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               type_=mysql.MEDIUMTEXT(collation=u'utf8mb4_unicode_ci'),
               existing_nullable=True)
    op.alter_column('unauthenticated_users', 'revoked',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False,
               existing_server_default=sa.text(u"'0'"))
    op.alter_column('guilds', 'webhooks',
               existing_type=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               type_=mysql.TEXT(collation=u'utf8mb4_unicode_ci'),
               existing_nullable=False)
    op.alter_column('guilds', 'visitor_view',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('guilds', 'unauth_users',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guilds', 'roles',
               existing_type=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               type_=mysql.MEDIUMTEXT(collation=u'utf8mb4_unicode_ci'),
               existing_nullable=False)
    op.alter_column('guilds', 'emojis',
               existing_type=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               type_=mysql.TEXT(collation=u'utf8mb4_unicode_ci'),
               existing_nullable=False)
    op.alter_column('guilds', 'chat_links',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guilds', 'channels',
               existing_type=sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'),
               type_=mysql.MEDIUMTEXT(collation=u'utf8mb4_unicode_ci'),
               existing_nullable=False)
    op.alter_column('guilds', 'bracket_links',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('guild_members', 'banned',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False,
               existing_server_default=sa.text(u"'0'"))
    op.alter_column('guild_members', 'active',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False,
               existing_server_default=sa.text(u"'1'"))
    op.alter_column('cosmetics', 'css',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
