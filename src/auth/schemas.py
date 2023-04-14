from typing import Optional
from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    username: str


class UserCreate(BaseUser):
    password: str
    password_repeat: str
    name: str
    surname: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
