"""empty message

Revision ID: f0c4bdc825de
Revises: 
Create Date: 2022-06-17 03:36:06.433997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0c4bdc825de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directors',
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('director_id')
    )
    op.create_table('genres',
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('genre_id')
    )
    op.create_table('user_groups',
    sa.Column('user_group_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('user_group_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('user_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_group_id'], ['user_groups.user_group_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('movies',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('release_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('poster_url', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('movie_id')
    )
    op.create_table('movie_director',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('director_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['directors.director_id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.movie_id'], )
    )
    op.create_table('movie_genre',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.genre_id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.movie_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_genre')
    op.drop_table('movie_director')
    op.drop_table('movies')
    op.drop_table('users')
    op.drop_table('user_groups')
    op.drop_table('genres')
    op.drop_table('directors')
    # ### end Alembic commands ###
