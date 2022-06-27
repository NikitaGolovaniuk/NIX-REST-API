"""Pydantic users schema"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from pydantic import BaseModel


class UsersSchema(BaseModel):
    """Users schema"""
    name: Optional[str]
    password: Optional[str]
    username: Optional[str]
    user_group_id: Optional[int]

    class Config:
        """config"""
        orm_mode = True
