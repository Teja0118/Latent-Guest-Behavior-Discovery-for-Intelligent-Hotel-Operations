from pydantic import BaseModel


class GuestInputSchema(BaseModel):

    restaurant_visits: float

    restaurant_spend_usd: float

    bar_lounge_visits: float

    spa_treatments_count: float

    spa_spend_usd: float

    gym_checkins_count: float

    pool_beach_visits_count: float

    activity_bookings_count: float

    kids_club_sessions: float

    tour_bookings_count: float

    business_center_hours: float

    concierge_requests_count: float

    transport_requests_count: float

    laundry_requests_count: float

    service_complaint_count: float