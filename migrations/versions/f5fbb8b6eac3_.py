"""empty message

Revision ID: f5fbb8b6eac3
Revises: e8a6acb6100f
Create Date: 2021-11-09 17:30:15.997896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5fbb8b6eac3'
down_revision = 'e8a6acb6100f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('name', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_movies_name'), 'movies', ['name'], unique=True)
    op.add_column('tv_shows', sa.Column('name', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_tv_shows_name'), 'tv_shows', ['name'], unique=True)
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    op.drop_index(op.f('ix_tv_shows_name'), table_name='tv_shows')
    op.drop_column('tv_shows', 'name')
    op.drop_index(op.f('ix_movies_name'), table_name='movies')
    op.drop_column('movies', 'name')
    # ### end Alembic commands ###