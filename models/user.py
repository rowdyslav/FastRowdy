# Shared properties
# class UserBase(SQLModel):
#     email: EmailStr = Field(unique=True, index=True, max_length=255)
#     is_active: bool = True
#     is_superuser: bool = False
#     full_name: str | None = Field(default=None, max_length=255)


from typing import Annotated, Optional

from beanie import Link, PydanticObjectId
from fastapi_users_db_beanie import BeanieBaseUserDocument
from pydantic import EmailStr, Field

from models.item import Item


class UserBase(BeanieBaseUserDocument):
    full_name: Annotated[Optional[str], Field(max_length=255)] = None


# Database model, database table inferred from class name
class User(UserBase):
    items: list[Link[Item]]


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: PydanticObjectId


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=40)


class UserUpdateMe(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int
