import pandas as pd

class OperationalInsights:
    def __init__(self, clustered_dataframe: pd.DataFrame):
        self.dataframe = clustered_dataframe

    def generate_operational_insights(self):
        try:
            print("\nOperational Intelligence Insights:\n")
            cluster_summary = self.dataframe.groupby(
                "guest_cluster"
            ).mean()
            for cluster_id in cluster_summary.index:
                print(f"\nCluster {cluster_id}: \n")
                if(
                    cluster_summary.loc[
                        cluster_id,
                        "concierge_requests_count"
                    ] > 0
                ):
                    print("- Increase concierge staffing.")
                
                if (
                    cluster_summary.loc[
                        cluster_id,
                        "spa_treatments_count"
                    ] > 0
                ):

                    print(
                        "- Increase spa staff allocation."
                    )

                if (
                    cluster_summary.loc[
                        cluster_id,
                        "transport_requests_count"
                    ] > 0
                ):

                    print(
                        "- Improve transport availability."
                    )

                if (
                    cluster_summary.loc[
                        cluster_id,
                        "kids_club_sessions"
                    ] > 0
                ):

                    print(
                        "- Increase kids club resources."
                    )

                if (
                    cluster_summary.loc[
                        cluster_id,
                        "service_complaint_count"
                    ] > 0
                ):

                    print(
                        "- Improve customer service response."
                    )
        except Exception as error:
            print(
                f"Error while generating operational insights: "
                f"{error}"
            )
                