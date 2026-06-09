from pydantic import BaseModel

from pydantic import Field


class GuestInputSchema(BaseModel):

    restaurant_visits: float = Field(default=0)

    restaurant_spend_usd: float = Field(default=0)

    room_service_orders: float = Field(default=0)

    bar_lounge_visits: float = Field(default=0)

    spa_treatments_count: float = Field(default=0)

    spa_spend_usd: float = Field(default=0)

    gym_checkins_count: float = Field(default=0)

    pool_beach_visits_count: float = Field(default=0)

    activity_bookings_count: float = Field(default=0)

    kids_club_sessions: float = Field(default=0)

    tour_bookings_count: float = Field(default=0)

    business_center_hours: float = Field(default=0)

    concierge_requests_count: float = Field(default=0)

    transport_requests_count: float = Field(default=0)

    laundry_requests_count: float = Field(default=0)

    special_requests_count: float = Field(default=0)

    service_complaint_count: float = Field(default=0)