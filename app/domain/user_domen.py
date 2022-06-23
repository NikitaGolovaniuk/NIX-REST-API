from typing import Dict
from app.crud.abstract_repo import AbstractRepository
from app.schemas.users import UsersSchema

def add_user(data: Dict, repo: AbstractRepository):
    schema = UsersSchema(**data)
    return repo.create(user_schema=schema)