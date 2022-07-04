from typing import List, Union
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str | None = None

class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    pass


class UserBase(BaseModel):
    username: str
    email: str
    last_active: str
    avatar: str


class UserCreate(UserBase):
    hashed_password: str
    phone_number: str | None = None


class User(UserBase):
    id: int
    is_active: bool
    items: list[Book] = []

    class Config:
        orm_mode = True