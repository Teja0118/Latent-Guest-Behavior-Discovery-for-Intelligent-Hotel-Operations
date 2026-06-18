from pydantic import BaseModel, Field
from pydantic import EmailStr


class RegisterUserSchema(BaseModel):

    name: str

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=50
    )


class LoginSchema(BaseModel):

    email: EmailStr

    password: str