"""empty message

Revision ID: 24a96f57af6e
Revises: cb1d52940d17
Create Date: 2023-03-27 11:09:52.249556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24a96f57af6e'
down_revision = 'cb1d52940d17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_tag_association',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tag_association')
    op.drop_table('tags')
    # ### end Alembic commands ###
