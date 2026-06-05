class RecommendationService:

    CLUSTER_DETAILS = {

        0: {
            "cluster_name": "Dining & Leisure Guests",
            "recommendations": [
                "Premium Dining Package",
                "Weekend Leisure Offer",
                "Restaurant Loyalty Rewards"
            ]
        },

        1: {
            "cluster_name": "Wellness Guests",
            "recommendations": [
                "Luxury Wellness Retreat",
                "Spa & Gym Combo",
                "Poolside Relaxation Package"
            ]
        },

        2: {
            "cluster_name": "Business Travelers",
            "recommendations": [
                "Business Travel Package",
                "Airport Transfer Service",
                "Laundry Express Service"
            ]
        },

        3: {
            "cluster_name": "Minimal-Service Guests",
            "recommendations": [
                "Customer Recovery Offer",
                "Fast Check-in Upgrade",
                "Service Experience Improvement"
            ]
        },

        4: {
            "cluster_name": "Family Leisure Guests",
            "recommendations": [
                "Family Fun Package",
                "Kids Club Access",
                "Adventure Activity Bundle"
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
                "cluster_name": "Unknown Cluster",
                "recommendations": []
            }
        )