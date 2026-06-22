class RecommendationService:

    CLUSTER_DETAILS = {

        # Luxury Dining Guests

        0: {

            "cluster_name":
                "Luxury Dining Guests",

            "recommendations": [

                "Luxury Dining Experience",

                "Fine Dining Package",

                "Premium Beverage Package"
            ]
        },

        # Family Leisure Guests

        1: {

            "cluster_name":
                "Family Leisure Guests",

            "recommendations": [

                "Family Fun Package",

                "Kids Club Access",

                "Adventure Activity Bundle"
            ]
        },

        # Wellness Luxury Guests

        2: {

            "cluster_name":
                "Wellness Luxury Guests",

            "recommendations": [

                "Luxury Wellness Retreat",

                "Spa & Gym Combo",

                "Premium Wellness Membership"
            ]
        },

        # Business Travelers

        3: {

            "cluster_name":
                "Business Travelers",

            "recommendations": [

                "Business Travel Package",

                "Executive Lounge Access",

                "Airport Transfer Service"
            ]
        },

        # Budget Minimal Guests

        4: {

            "cluster_name":
                "Budget Minimal Guests",

            "recommendations": [

                "Budget-Friendly Stay",

                "Seasonal Discount Offer",

                "Quick Check-In Package"
            ]
        },

        # Premium Family Business Guests

        5: {

            "cluster_name":
                "Premium Family Business Guests",

            "recommendations": [

                "Family Business Package",

                "Executive Family Suite",

                "Premium Concierge Services"
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