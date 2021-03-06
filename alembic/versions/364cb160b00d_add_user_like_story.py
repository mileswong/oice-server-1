"""Add user_like_story

Revision ID: 364cb160b00d
Revises: 6635f10c7907
Create Date: 2017-06-22 10:17:16.874859

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '364cb160b00d'
down_revision = '6635f10c7907'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user_like_story',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('story_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['story_id'], ['story.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'story_id', name='user_like_story_unique')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_like_story')
    # ### end Alembic commands ###
