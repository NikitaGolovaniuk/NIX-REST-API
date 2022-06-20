from pydantic import BaseModel
from typing import Optional

class UserGroupsSchema(BaseModel):
    """UserGroupsSchema schema"""
    name: Optional[str]

    class Config:
        orm_mode = True



