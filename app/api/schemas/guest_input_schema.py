from pydantic import BaseModel

class GuestInputSchema(BaseModel):
    restaurant_visits: float
    restaurant_spend_usd: float

    room_service_orders: float
    room_service_spend_usd: float

    bar_lounge_visits: float
    minibar_charges_usd: float

    spa_treatments_count: float
    spa_spend_usd: float

    gym_checkins_count: float
    pool_beach_visits_count: float

    activity_bookings_count: float
    activity_spend_usd: float

    kids_club_sessions: float
    tour_bookings_count: float

    concierge_requests_count: float
    transport_requests_count: float

    laundry_requests_count: float
    special_requests_count: float

    in_room_entertainment_hours: float

    gift_shop_spend_usd: float

    business_center_hours: float

    extra_housekeeping_requests: float

    avg_service_response_minutes: float

    maintenance_calls_count: float

    checkin_wait_minutes: float

    service_complaint_count: float