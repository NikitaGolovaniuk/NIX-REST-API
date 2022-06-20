from pydantic import BaseModel
from typing import Optional


class UsersSchema(BaseModel):
    """Users schema"""
    name: Optional[str]
    password: Optional[str]
    username: Optional[str]
    user_group_id: Optional[int]

    class Config:
        orm_mode = True

