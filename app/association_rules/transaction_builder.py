import pandas as pd

class TransactionBuilder:

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def build_transactions(self):

        try:
            transaction_df = pd.DataFrame()
            transaction_df["Restaurant"] = (
                self.dataframe["restaurant_visits"] > 0
            )
            transaction_df["Room_Service"] = (
                self.dataframe["room_service_orders"] > 0
            )
            transaction_df["Bar_Lounge"] = (
                self.dataframe["bar_lounge_visits"] > 0
            )

            transaction_df["Spa"] = (
                self.dataframe["spa_treatments_count"] > 0
            )

            transaction_df["Gym"] = (
                self.dataframe["gym_checkins_count"] > 0
            )

            transaction_df["Pool_Beach"] = (
                self.dataframe["pool_beach_visits_count"] > 0
            )

            transaction_df["Activity"] = (
                self.dataframe["activity_bookings_count"] > 0
            )

            transaction_df["Kids_Club"] = (
                self.dataframe["kids_club_sessions"] > 0
            )

            transaction_df["Tour"] = (
                self.dataframe["tour_bookings_count"] > 0
            )

            transaction_df["Concierge"] = (
                self.dataframe["concierge_requests_count"] > 0
            )

            transaction_df["Transport"] = (
                self.dataframe["transport_requests_count"] > 0
            )

            transaction_df["Laundry"] = (
                self.dataframe["laundry_requests_count"] > 0
            )

            transaction_df["Gift_Shop"] = (
                self.dataframe["gift_shop_spend_usd"] > 0
            )

            transaction_df["Business_Center"] = (
                self.dataframe["business_center_hours"] > 0
            )

            print("\nTransaction dataset created successfully.")
            return transaction_df
        
        except Exception as error:
            print(
                f"Error while building transactions: {error}"
            )