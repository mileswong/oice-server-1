"""add columns for story settings

Revision ID: 4b7c8549a10
Revises: 434f6152c11
Create Date: 2016-11-23 11:18:11.423902

"""

# revision identifiers, used by Alembic.
revision = '4b7c8549a10'
down_revision = '434f6152c11'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story', sa.Column('description', sa.Unicode(length=4096), server_default='', nullable=False))
    op.add_column('story', sa.Column('language', sa.Unicode(length=5), server_default='zh_HK', nullable=False))
    op.add_column('story', sa.Column('license', sa.SmallInteger(), server_default='0', nullable=False))
    op.add_column('story', sa.Column('on_going', sa.Boolean(), server_default=sa.text('1'), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('story', 'on_going')
    op.drop_column('story', 'license')
    op.drop_column('story', 'language')
    op.drop_column('story', 'description')
    ### end Alembic commands ###
