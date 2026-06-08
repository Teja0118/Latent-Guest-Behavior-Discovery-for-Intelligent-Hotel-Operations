import pandas as pd


class FeatureSelector:

    CLUSTERING_FEATURES = [

        # Dining

        "restaurant_visits",
        "restaurant_spend_usd",

        "bar_lounge_visits",

        # Wellness

        "spa_treatments_count",
        "spa_spend_usd",

        "gym_checkins_count",

        "pool_beach_visits_count",

        # Family

        "activity_bookings_count",

        "kids_club_sessions",

        "tour_bookings_count",

        # Business

        "business_center_hours",

        "concierge_requests_count",

        "transport_requests_count",

        "laundry_requests_count",

        # Service

        "service_complaint_count",

        # Engineered Features

        "total_dining_spend",

        "total_wellness_usage",

        "total_business_services",

        "family_activity_score"
    ]

    def __init__(
        self,
        dataframe: pd.DataFrame
    ):

        self.dataframe = dataframe.copy()

    def create_engineered_features(self):

        try:

            self.dataframe[
                "total_dining_spend"
            ] = (

                self.dataframe[
                    "restaurant_spend_usd"
                ]

                +

                self.dataframe[
                    "room_service_spend_usd"
                ]
            )

            self.dataframe[
                "total_wellness_usage"
            ] = (

                self.dataframe[
                    "spa_treatments_count"
                ]

                +

                self.dataframe[
                    "gym_checkins_count"
                ]

                +

                self.dataframe[
                    "pool_beach_visits_count"
                ]
            )

            self.dataframe[
                "total_business_services"
            ] = (

                self.dataframe[
                    "business_center_hours"
                ]

                +

                self.dataframe[
                    "concierge_requests_count"
                ]

                +

                self.dataframe[
                    "transport_requests_count"
                ]

                +

                self.dataframe[
                    "laundry_requests_count"
                ]
            )

            self.dataframe[
                "family_activity_score"
            ] = (

                self.dataframe[
                    "kids_club_sessions"
                ]

                +

                self.dataframe[
                    "activity_bookings_count"
                ]

                +

                self.dataframe[
                    "tour_bookings_count"
                ]
            )

            self.dataframe[
                "service_dependency_score"
            ] = (

                self.dataframe[
                    "special_requests_count"
                ]

                +

                self.dataframe[
                    "room_service_orders"
                ]
            )

            print(
                "\nEngineered features "
                "created successfully."
            )

        except Exception as error:

            print(
                f"Error while creating "
                f"engineered features: "
                f"{error}"
            )

    def get_clustering_features(self):

        try:

            self.create_engineered_features()

            clustering_dataframe = (

                self.dataframe[
                    self.CLUSTERING_FEATURES
                ]
            )

            print(
                "\nClustering features "
                "selected successfully."
            )

            return clustering_dataframe

        except Exception as error:

            print(
                f"Error while selecting "
                f"clustering features: "
                f"{error}"
            )