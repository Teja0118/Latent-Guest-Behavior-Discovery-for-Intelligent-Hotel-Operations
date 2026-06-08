import pandas as pd


class OperationalInsights:

    def __init__(
        self,
        clustered_dataframe: pd.DataFrame
    ):

        self.clustered_dataframe = (
            clustered_dataframe.copy()
        )

    def generate_operational_insights(self):

        try:

            numerical_columns = (

                self.clustered_dataframe.select_dtypes(

                    include=[
                        "int64",
                        "float64"
                    ]

                ).columns
            )

            numerical_columns = [

                column
                for column in numerical_columns
                if column != "guest_cluster"
            ]

            cluster_summary = (

                self.clustered_dataframe.groupby(
                    "guest_cluster"
                )[numerical_columns].mean()

            )

            print(
                "\nOperational Intelligence "
                "Insights:\n"
            )

            for cluster_id, row in (
                cluster_summary.iterrows()
            ):

                print(
                    f"\nCluster {cluster_id}: \n"
                )

                if row.get(
                    "concierge_requests_count",
                    0
                ) > 2:

                    print(
                        "- Increase concierge staffing."
                    )

                if row.get(
                    "spa_treatments_count",
                    0
                ) > 2:

                    print(
                        "- Increase spa staff allocation."
                    )

                if row.get(
                    "transport_requests_count",
                    0
                ) > 2:

                    print(
                        "- Improve transport availability."
                    )

                if row.get(
                    "service_complaint_count",
                    0
                ) > 1:

                    print(
                        "- Improve customer service response."
                    )

                if row.get(
                    "kids_club_sessions",
                    0
                ) > 3:

                    print(
                        "- Increase kids club resources."
                    )

        except Exception as error:

            print(
                f"Error while generating "
                f"operational insights: "
                f"{error}"
            )