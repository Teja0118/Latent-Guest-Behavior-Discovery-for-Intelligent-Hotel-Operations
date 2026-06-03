import pandas as pd

class RecommendationEngine:

    def __init__(self, clustered_dataframe: pd.DataFrame):
        self.dataframe = clustered_dataframe

    def generate_cluster_recommendations(self):
        try:
            recommendations = {
                0: [
                    "Premium Dining Package",
                    "Weekend Leisure Offer",
                    "Restaurant Loyalty Rewards"
                ],

                1: [
                    "Luxury Wellness Retreat",
                    "Spa & Gym Combo",
                    "Poolside Relaxation Package"
                ],

                2: [
                    "Business Travel Package",
                    "Airport Transfer Service",
                    "Laundry Express Service"
                ],

                3: [
                    "Customer Recovery Offer",
                    "Fast Check-in Upgrade",
                    "Service Experience Improvement"
                ],

                4: [
                    "Family Fun Package",
                    "Kids Club Access",
                    "Adventure Activity Bundle"
                ]
            }
            print("\nCluster-wise Recommendations:\n")

            for cluster, recommendation_list in (
                recommendations.items()
            ):
                print(f"\nCluster {cluster}:\n")
                for recommendation in recommendation_list:
                    print(f" - {recommendation}")
            return recommendations
        
        except Exception as error:
            print(
                f"Error while generaind recommendations: {error}"
            )