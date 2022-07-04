from typing import Optional

from pydantic import BaseModel


class TokenResponseSchema(BaseModel):
    email: str
    username: str
    password: str
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
