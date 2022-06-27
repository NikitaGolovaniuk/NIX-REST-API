"""Pydantic movies schema"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional, List
import datetime
from pydantic import BaseModel, validator
from flaskr.schemas.directors import DirectorsSchema
from flaskr.schemas.genres import GenresSchema


class MoviesSchema(BaseModel):
    """Schema for movies"""
    name: Optional[str]
    release_date: Optional[datetime.date]
    description: Optional[str]
    rating: Optional[int]
    poster_url: Optional[str]
    directors: Optional[List[DirectorsSchema]]
    genres: Optional[List[GenresSchema]]
    user_id: Optional[int]

    @validator('rating')
    def rating_match(cls, v):
        """rating should be between 1 and 10 values"""
        if 1 <= v <= 10:
            return v
        raise ValueError

    class Config:
        """config"""
        orm_mode = True
