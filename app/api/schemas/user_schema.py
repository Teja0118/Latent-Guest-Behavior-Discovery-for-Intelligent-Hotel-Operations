from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import field_validator

import re


class RegisterUserSchema(BaseModel):

    name: str

    email: EmailStr

    password: str

    @field_validator("password")
    @classmethod
    def validate_password(
        cls,
        value
    ):

        if len(value) < 8:

            raise ValueError(
                "Password must contain at least 8 characters"
            )

        if not re.search(
            r"[A-Z]",
            value
        ):

            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not re.search(
            r"[a-z]",
            value
        ):

            raise ValueError(
                "Password must contain at least one lowercase letter"
            )

        if not re.search(
            r"\d",
            value
        ):

            raise ValueError(
                "Password must contain at least one number"
            )

        if not re.search(
            r"[!@#$%^&*(),.?\":{}|<>]",
            value
        ):

            raise ValueError(
                "Password must contain at least one special character"
            )

        return value


class LoginSchema(BaseModel):

    email: EmailStr

    password: str