from pydantic import BaseModel
from typing import Optional


class GenresSchema(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True