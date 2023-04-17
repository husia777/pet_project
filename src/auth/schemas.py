from typing import Optional
from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str
    password_repeat: str
    name: str
    surname: str


class User(BaseUser):
    id: Optional[int] = Field(primary_key=True)

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
