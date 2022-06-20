from pydantic import BaseModel
from typing import Optional


class DirectorsSchema(BaseModel):
    """Directors schema"""
    name: Optional[str]

    class Config:
        orm_mode = True