"""Pydantic UserGroupsSchema schema"""
# pylint: disable=R0913, R0903, E0401
from typing import Optional
from pydantic import BaseModel


class UserGroupsSchema(BaseModel):
    """UserGroupsSchema schema"""
    name: Optional[str]

    class Config:
        """config"""
        orm_mode = True
