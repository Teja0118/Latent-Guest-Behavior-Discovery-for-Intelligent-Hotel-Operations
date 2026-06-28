from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy import func
from sqlalchemy.orm import Session

from api.schemas.user_schema import AdminCreateUserSchema
from api.schemas.user_schema import UserRoleUpdateSchema
from api.services.auth_dependency import require_admin
from api.services.security_service import hash_password
from database.database import SessionLocal
from database.models import PredictionHistory
from database.models import User


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


def serialize_user(user: User):

    return {

        "id":
            user.id,

        "name":
            user.name,

        "email":
            user.email,

        "role":
            user.role,

        "created_at":
            str(user.created_at)
    }


@router.get("/summary")
def get_admin_summary(

    current_user: User = Depends(
        require_admin
    ),

    db: Session = Depends(
        get_db
    )
):

    total_users = (
        db.query(User)
        .count()
    )

    admin_users = (
        db.query(User)
        .filter(User.role == "admin")
        .count()
    )

    hotel_users = (
        db.query(User)
        .filter(User.role == "hotel_user")
        .count()
    )

    total_predictions = (
        db.query(PredictionHistory)
        .count()
    )

    return {

        "total_users":
            total_users,

        "admin_users":
            admin_users,

        "hotel_users":
            hotel_users,

        "total_predictions":
            total_predictions
    }


@router.get("/users")
def get_users(

    current_user: User = Depends(
        require_admin
    ),

    db: Session = Depends(
        get_db
    )
):

    users = (
        db.query(User)
        .order_by(User.created_at.desc())
        .all()
    )

    return [
        serialize_user(user)
        for user in users
    ]


@router.post("/users")
def create_user(

    user: AdminCreateUserSchema,

    current_user: User = Depends(
        require_admin
    ),

    db: Session = Depends(
        get_db
    )
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        hashed_password=hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return serialize_user(
        new_user
    )


@router.patch("/users/{user_id}/role")
def update_user_role(

    user_id: int,

    role_update: UserRoleUpdateSchema,

    current_user: User = Depends(
        require_admin
    ),

    db: Session = Depends(
        get_db
    )
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if (
        user.id == current_user.id
        and role_update.role != "admin"
    ):

        raise HTTPException(
            status_code=400,
            detail="You cannot remove your own admin role"
        )

    user.role = role_update.role

    db.commit()
    db.refresh(user)

    return serialize_user(
        user
    )


@router.delete("/users/{user_id}")
def delete_user(

    user_id: int,

    current_user: User = Depends(
        require_admin
    ),

    db: Session = Depends(
        get_db
    )
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if user.id == current_user.id:

        raise HTTPException(
            status_code=400,
            detail="You cannot delete your own account"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted"
    }
