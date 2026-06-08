import pandas as pd


class RecommendationEngine:

    def __init__(
        self,
        clustered_dataframe: pd.DataFrame
    ):

        self.dataframe = clustered_dataframe

    def generate_cluster_recommendations(self):

        try:

            recommendations = {

                # Family + Dining Guests

                0: [

                    "Family Fun Package",

                    "Kids Club Access",

                    "Restaurant Loyalty Rewards"
                ],

                # Budget Minimal Guests

                1: [

                    "Budget-Friendly Stay",

                    "Express Service Experience",

                    "Seasonal Discount Offers"
                ],

                # Business + Mixed Activity Guests

                2: [

                    "Business Travel Package",

                    "Airport Transfer Service",

                    "Laundry Express Service"
                ],

                # Luxury Wellness Guests

                3: [

                    "Luxury Wellness Retreat",

                    "Spa & Gym Combo",

                    "Poolside Relaxation Package"
                ]
            }

            print(
                "\nCluster-wise Recommendations:\n"
            )

            for cluster, recommendation_list in (
                recommendations.items()
            ):

                print(
                    f"\nCluster {cluster}:\n"
                )

                for recommendation in (
                    recommendation_list
                ):

                    print(
                        f" - {recommendation}"
                    )

            return recommendations

        except Exception as error:

            print(
                f"Error while generating "
                f"recommendations: {error}"
            )