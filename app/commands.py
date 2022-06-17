import random
from . import app
from faker import Faker
from app.models.directors import Directors
from app.models.user_groups import UserGroups
from app.models.users import Users
from app.models.genres import Genres
from app.models.movies import Movies, movie_genre, movie_director
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("postgresql://admin:admin@0.0.0.0:5432/my_db")
session = sessionmaker(bind=engine)
s = session()
faker = Faker()
groups = ('user', 'admin')
genres = ("Action", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Thriller", "Western")
rows_seed = 50

@app.cli.command('seed')
def seed():
    for _ in range(rows_seed):
        director = Directors(name=faker.name())
        s.add(director)
        s.commit()

    for i in groups:
        user_group = UserGroups(name=i)
        s.add(user_group)
        s.commit()

    for _ in range(rows_seed):
        user = Users(name=faker.name(), password=faker.password(), user_group_id=random.randint(1, 2))
        s.add(user)
        s.commit()

    for i in genres:
        genre = Genres(name=i)
        s.add(genre)
        s.commit()

    for _ in range(rows_seed):
        movie = Movies(name=faker.name(),
                       release_date=faker.date(),
                       description=faker.sentences(),
                       rating=random.randint(1, 10),
                       poster_url=faker.image_url(),
                       user_id=random.randint(1, rows_seed),
                       )
        s.add(movie)
        s.commit()

    genres_amount = len(genres)
    for i in range(1, rows_seed+1):
        genres_per_movie = random.randint(1, genres_amount-1)
        genres_id_list = random.sample(range(1, genres_amount), genres_per_movie)
        for j in genres_id_list:
            insert_data = movie_genre.insert().values(movie_id=i, genre_id=j)
            s.execute(insert_data)
            s.commit()


    for i in range(1, rows_seed+1):
        directors_per_movie = random.randint(1, rows_seed-1)
        direcrors_id_list = random.sample(range(1, rows_seed), directors_per_movie)
        for j in direcrors_id_list:
            insert_data = movie_director.insert().values(movie_id=i, director_id=j)
            s.execute(insert_data)
            s.commit()



