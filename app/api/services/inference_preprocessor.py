import joblib

import pandas as pd


class InferencePreprocessor:

    FEATURE_COLUMNS = [

        "restaurant_visits",
        "restaurant_spend_usd",

        "bar_lounge_visits",

        "spa_treatments_count",
        "spa_spend_usd",

        "gym_checkins_count",
        "pool_beach_visits_count",

        "activity_bookings_count",

        "kids_club_sessions",

        "tour_bookings_count",

        "business_center_hours",

        "concierge_requests_count",

        "transport_requests_count",

        "laundry_requests_count",

        "service_complaint_count",

        "total_dining_spend",

        "total_wellness_usage",

        "total_business_services",

        "family_activity_score"
    ]

    def __init__(self):

        self.preprocessor = joblib.load(
            "models/clustering_preprocessor.pkl"
        )

    def preprocess_input(
        self,
        guest_data: dict
    ):

        try:

            guest_data[
                "total_dining_spend"
            ] = (

                guest_data[
                    "restaurant_spend_usd"
                ]
            )

            guest_data[
                "total_wellness_usage"
            ] = (

                guest_data[
                    "spa_treatments_count"
                ]

                +

                guest_data[
                    "gym_checkins_count"
                ]

                +

                guest_data[
                    "pool_beach_visits_count"
                ]
            )

            guest_data[
                "total_business_services"
            ] = (

                guest_data[
                    "business_center_hours"
                ]

                +

                guest_data[
                    "concierge_requests_count"
                ]

                +

                guest_data[
                    "transport_requests_count"
                ]

                +

                guest_data[
                    "laundry_requests_count"
                ]
            )

            guest_data[
                "family_activity_score"
            ] = (

                guest_data[
                    "kids_club_sessions"
                ]

                +

                guest_data[
                    "activity_bookings_count"
                ]

                +

                guest_data[
                    "tour_bookings_count"
                ]
            )

            dataframe = pd.DataFrame(
                [guest_data]
            )

            dataframe = dataframe[
                self.FEATURE_COLUMNS
            ]

            processed_dataframe = (
                self.preprocessor.transform(
                    dataframe
                )
            )

            return processed_dataframe

        except Exception as error:

            raise Exception(
                f"Inference preprocessing "
                f"error: {error}"
            )