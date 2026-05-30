import pandas as pd

class FeatureSelector:

    CLUSTERING_FEATURES = [

        "restaurant_visits",
        "restaurant_spend_usd",

        "room_service_orders",
        "room_service_spend_usd",

        "bar_lounge_visits",
        "minibar_charges_usd",

        "spa_treatments_count",
        "spa_spend_usd",

        "gym_checkins_count",
        "pool_beach_visits_count",

        "activity_bookings_count",
        "activity_spend_usd",

        "kids_club_sessions",
        "tour_bookings_count",

        "concierge_requests_count",
        "transport_requests_count",
        "laundry_requests_count",
        "special_requests_count",

        "in_room_entertainment_hours",

        "gift_shop_spend_usd",
        "business_center_hours",

        "extra_housekeeping_requests",

        "avg_service_response_minutes",

        "maintenance_calls_count",

        "checkin_wait_minutes",

        "service_complaint_count"
    ]

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def get_clustering_features(self):
        
        try:
            clustering_dataframe = self.dataframe[
                self.CLUSTERING_FEATURES
            ]

            print("\nClustering features selected successfully.")

            return clustering_dataframe
        
        except Exception as error:
            print(f"Error while selecting clustering features: {error}")
            
