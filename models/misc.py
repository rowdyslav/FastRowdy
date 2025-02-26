from typing import Annotated, Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: Optional[str] = None


class NewPassword(BaseModel):
    token: str
    new_password: Annotated[str, Field(min_length=8, max_length=40)]
