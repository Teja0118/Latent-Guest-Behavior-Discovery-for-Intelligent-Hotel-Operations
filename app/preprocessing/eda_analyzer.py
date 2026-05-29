import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDAAnalyzer:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def correlation_heatmap(self):

        try:
            plt.figure(figsize=(20,12))

            correlation_matrix = self.dataframe.corr()
            sns.heatmap(
                correlation_matrix,
                cmap="coolwarm",
                linewidth=0.5
            )

            plt.title("Feature Correlation Heatmap")
            plt.tight_layout()
            plt.show()

        except Exception as error:
            print(f"Error while generating correlation heatmap: {error}")

    def spending_distribution_analysis(self):

        try:
            spending_columns = [
                "restaurant_spend_usd",
                "room_service_spend_usd",
                "spa_spend_usd",
                "activity_spend_usd",
                "gift_shop_spend_usd",
                "minibar_charges_usd"
            ]

            for column in spending_columns:
                plt.figure(figsize=(8,5))

                sns.histplot(
                    self.dataframe[column],
                    kde=True
                )
                plt.title(f"{column} Distribution")
                plt.tight_layout()
                plt.show()

        except Exception as error:
            print(f"Error while analyzing spending distribution: {error}")

    def service_usage_analysis(self):

        try:
            service_columns = [
                "restaurant_visits",
                "room_service_orders",
                "spa_treatments_count",
                "gym_checkins_count",
                "activity_bookings_count",
                "concierge_requests_count"
            ]

            for column in service_columns:
                plt.figure(figsize=(8,5))

                sns.boxplot(
                    x=self.dataframe[column]
                ) 
                plt.title(f"{column} Usage Analysis")
                plt.tight_layout()
                plt.show()

        except Exception as error:
            print(f"Error while analyzing service usage: {error}")

    def operational_metrics_analysis(self):

        try:
            operational_columns = [
                "avg_service_response_minutes",
                "maintenance_calls_count",
                "checkin_wait_minutes",
                "service_complaint_count"
            ]   

            for column in operational_columns:
                plt.figure(figsize=(8,5))
                sns.histplot(
                    self.dataframe[column],
                    kde=True
                )
                plt.title(f"{column} Operational Analysis")
                plt.tight_layout()
                plt.show()

        except Exception as error:
            print(f"Error while analyzing operational metrics: {error}")

    def categorical_feature_analysis(self):
        try:
            categorical_columns = self.dataframe.select_dtypes(
                include=["int64"]
            ).columns[:10]

            for column in categorical_columns:
                plt.figure(figsize=(8,5))
                
                sns.countplot(
                    x=self.dataframe[column]
                )

                plt.title(f"{column} Distribution")

                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
        except Exception as error:
            print(f"Error while analyzing categorical features: {error}")
