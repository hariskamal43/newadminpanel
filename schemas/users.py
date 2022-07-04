from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
    email: str
    username: str
    password: str

class LoginSchema(BaseModel):
    username: str
    password: str