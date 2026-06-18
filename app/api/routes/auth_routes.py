from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from database.database import SessionLocal

from database.models import User

from api.schemas.user_schema import (
    RegisterUserSchema
)

from api.schemas.user_schema import (
    LoginSchema
)

from api.services.security_service import (
    hash_password
)

from api.services.security_service import (
    verify_password
)

from api.services.security_service import (
    create_access_token
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.post("/register")
def register_user(

    user: RegisterUserSchema,

    db: Session = Depends(get_db)
):

    existing_user = (

        db.query(User)

        .filter(
            User.email == user.email
        )

        .first()
    )

    if existing_user:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"
        )

    print("PASSWORD:", user.password)
    print("LENGTH:", len(user.password))

    new_user = User(

        name=user.name,

        email=user.email,

        hashed_password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    return {

        "message":
            "Registration successful"
    }

@router.post("/login")
def login(

    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)
):

    user = (

        db.query(User)

        .filter(
            User.email ==
            form_data.username
        )

        .first()
    )

    if not user:

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"
        )

    if not verify_password(

        form_data.password,

        user.hashed_password
    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"
        )

    token = create_access_token(

        {
            "sub": str(user.id)
        }
    )

    return {

        "access_token": token,

        "token_type": "bearer"
    }

'''
@router.post("/login")
def login(

    credentials: LoginSchema,

    db: Session = Depends(get_db)
):

    user = (

        db.query(User)

        .filter(
            User.email ==
            credentials.email
        )

        .first()
    )

    if not user:

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"
        )

    if not verify_password(

        credentials.password,

        user.hashed_password
    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"
        )

    token = create_access_token(

        {
            "sub":
                str(user.id)
        }
    )

    return {

        "access_token": token,

        "token_type": "bearer"
    }
'''
