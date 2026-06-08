class RecommendationService:

    CLUSTER_DETAILS = {

        # Family + Dining Guests

        0: {

            "cluster_name":
                "Family Dining Guests",

            "recommendations": [

                "Family Fun Package",

                "Kids Club Access",

                "Restaurant Loyalty Rewards"
            ]
        },

        # Budget / Minimal Guests

        1: {

            "cluster_name":
                "Budget Minimal Guests",

            "recommendations": [

                "Budget-Friendly Stay",

                "Express Service Experience",

                "Seasonal Discount Offers"
            ]
        },

        # Business + Mixed Guests

        2: {

            "cluster_name":
                "Business Leisure Guests",

            "recommendations": [

                "Business Travel Package",

                "Airport Transfer Service",

                "Laundry Express Service"
            ]
        },

        # Luxury Wellness Guests

        3: {

            "cluster_name":
                "Luxury Wellness Guests",

            "recommendations": [

                "Luxury Wellness Retreat",

                "Spa & Gym Combo",

                "Poolside Relaxation Package"
            ]
        }
    }

    def get_cluster_details(
        self,
        cluster_id: int
    ):

        return self.CLUSTER_DETAILS.get(

            cluster_id,

            {

                "cluster_name":
                    "Unknown Cluster",

                "recommendations": []
            }
        )