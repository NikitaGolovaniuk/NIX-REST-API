"""Pydantic director schema"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from pydantic import BaseModel


class DirectorsSchema(BaseModel):
    """Directors schema"""
    name: Optional[str]

    class Config:
        """config"""
        orm_mode = True
