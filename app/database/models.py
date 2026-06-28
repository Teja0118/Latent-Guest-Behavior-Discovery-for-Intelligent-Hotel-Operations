from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import Float

from sqlalchemy import String

from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cluster_id = Column(
        Integer
    )

    cluster_name = Column(
        String
    )

    confidence = Column(
        Float
    )

    restaurant_visits = Column(
        Float
    )

    restaurant_spend_usd = Column(
        Float
    )

    room_service_orders = Column(
        Float
    )

    room_service_spend_usd = Column(
        Float
    )

    bar_lounge_visits = Column(
        Float
    )

    spa_treatments_count = Column(
        Float
    )

    spa_spend_usd = Column(
        Float
    )

    gym_checkins_count = Column(
        Float
    )

    pool_beach_visits_count = Column(
        Float
    )

    activity_bookings_count = Column(
        Float
    )

    kids_club_sessions = Column(
        Float
    )

    tour_bookings_count = Column(
        Float
    )

    business_center_hours = Column(
        Float
    )

    concierge_requests_count = Column(
        Float
    )

    transport_requests_count = Column(
        Float
    )

    laundry_requests_count = Column(
        Float
    )

    special_requests_count = Column(
        Float
    )

    service_complaint_count = Column(
        Float
    )

    created_at = Column(

        DateTime,

        default=datetime.utcnow
    )

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        nullable=False,
        default="hotel_user"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
