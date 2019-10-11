"""Add file upload column to guilds table

Revision ID: ce2b9c930a7a
Revises: 12267ce662e9
Create Date: 2018-08-16 21:20:09.103071

"""

# revision identifiers, used by Alembic.
revision = 'ce2b9c930a7a'
down_revision = '12267ce662e9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guilds', sa.Column('file_upload', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guilds', 'file_upload')
    # ### end Alembic commands ###
