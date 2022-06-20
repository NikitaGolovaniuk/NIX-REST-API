from typing import Any, Optional, List
import datetime
from pydantic import BaseModel, validator
from app.schemas.directors import DirectorsSchema
from app.schemas.genres import GenresSchema


class MoviesSchema(BaseModel):
    name: Optional[str]
    release_date: datetime.date
    description: Optional[str]
    rating: Optional[int]
    poster_url: Optional[str]
    directors: Optional[List[DirectorsSchema]]
    id_genre: Optional[List[GenresSchema]]
    user_id: Optional[int]

    class Config:
        orm_mode = True


class MoviesSchemaAdd(BaseModel):
    name: Optional[str]
    release_date: Optional[datetime.date]
    description: Optional[str]
    rating: Optional[int]
    poster_url: Optional[str]

    class Config:
        orm_mode = True





