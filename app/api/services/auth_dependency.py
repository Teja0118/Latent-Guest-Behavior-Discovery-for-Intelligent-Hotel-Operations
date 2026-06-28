from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from database.database import SessionLocal

from database.models import User

from api.services.security_service import (
    verify_token
)

oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="login"
)


def get_current_user(

    token: str = Depends(
        oauth2_scheme
    )
):

    payload = verify_token(token)

    if not payload:

        raise HTTPException(

            status_code=401,

            detail="Invalid token"
        )

    try:

        user_id = int(
            payload.get(
                "sub"
            )
        )

    except (
        TypeError,
        ValueError
    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid token"
        )

    database = SessionLocal()

    try:

        user = (
            database.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:

            raise HTTPException(

                status_code=401,

                detail="User not found"
            )

        return user

    finally:

        database.close()


def require_admin(

    current_user: User = Depends(
        get_current_user
    )
):

    if current_user.role != "admin":

        raise HTTPException(

            status_code=403,

            detail="Admin access required"
        )

    return current_user
