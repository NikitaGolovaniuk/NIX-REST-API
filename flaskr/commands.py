"""Fill database tables by fake data using faker"""
# pylint: disable=R0913, R0903, E0401
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from flaskr.models.directors import Directors
from flaskr.models.user_groups import UserGroups
from flaskr.models.users import Users
from flaskr.models.genres import Genres
from flaskr.models.movies import Movies, movie_genre, movie_director
from . import app

engine = create_engine("postgresql://admin:admin@db:5432/my_db")
session = sessionmaker(bind=engine)
s = session()
faker = Faker()
ROW_SEED = 50
genres = ("Action", "Comedy", "Drama",
          "Fantasy", "Horror", "Mystery",
          "Romance", "Thriller", "Western")


def is_db_empty():
    """check db.Movie table is empty"""
    row_num = s.query(Movies).count()
    return row_num < ROW_SEED


def seed_directors():
    """Fill database.directors table by fake data using faker"""
    for _ in range(ROW_SEED):
        director: Directors = Directors(name=faker.name())
        s.add(director)
        s.commit()


def seed_groups():
    """Fill database.groups table by fake data using faker"""
    groups = ('user', 'admin')
    for i in groups:
        user_group = UserGroups(name=i)
        s.add(user_group)
        s.commit()


def seed_users():
    """Fill database.users table by fake data using faker"""
    for _ in range(ROW_SEED):
        user = Users(name=faker.name(),
                     username=faker.user_name(),
                     password=faker.password(),
                     user_group_id=random.randint(1, 2))
        s.add(user)
        s.commit()


def seed_genres():
    """Fill database.genres table by fake data using faker"""
    for i in genres:
        genre = Genres(name=i)
        s.add(genre)
        s.commit()


def seed_movies():
    """Fill database.movies table by fake data using faker"""
    for _ in range(ROW_SEED):
        movie = Movies(name=faker.name(),
                       release_date=faker.date(),
                       description=faker.sentences(),
                       rating=random.randint(1, 10),
                       poster_url=faker.image_url(),
                       user_id=random.randint(1, ROW_SEED),
                       )
        s.add(movie)
        s.commit()


def seed_movie_genre():
    """Fill database.movie_genre table by fake data using faker"""
    genres_amount = len(genres)
    for i in range(1, ROW_SEED + 1):
        genres_per_movie = random.randint(1, genres_amount-1)
        genres_id_list = random.sample(range(1, genres_amount), genres_per_movie)
        for j in genres_id_list:
            insert_data = movie_genre.insert().values(movie_id=i, genre_id=j)
            s.execute(insert_data)
            s.commit()


def seed_movie_director():
    """Fill database.movie_director table by fake data using faker"""
    for i in range(1, ROW_SEED + 1):
        directors_per_movie = random.randint(1, ROW_SEED - 1)
        direcrors_id_list = random.sample(range(1, ROW_SEED), directors_per_movie)
        for j in direcrors_id_list:
            insert_data = movie_director.insert().values(movie_id=i, director_id=j)
            s.execute(insert_data)
            s.commit()


@app.cli.command('seed')
def seed():
    """Use flask seed command to fill database"""
    if is_db_empty():
        seed_directors()
        seed_groups()
        seed_users()
        seed_genres()
        seed_movies()
        seed_movie_genre()
        seed_movie_director()
        print("DB was filled by fake data")
    else:
        print("DB is not empty")
