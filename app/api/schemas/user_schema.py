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


class AdminCreateUserSchema(RegisterUserSchema):

    role: str = "hotel_user"

    @field_validator("role")
    @classmethod
    def validate_role(
        cls,
        value
    ):

        if value not in {
            "admin",
            "hotel_user"
        }:

            raise ValueError(
                "Role must be admin or hotel_user"
            )

        return value


class UserRoleUpdateSchema(BaseModel):

    role: str

    @field_validator("role")
    @classmethod
    def validate_role(
        cls,
        value
    ):

        if value not in {
            "admin",
            "hotel_user"
        }:

            raise ValueError(
                "Role must be admin or hotel_user"
            )

        return value
