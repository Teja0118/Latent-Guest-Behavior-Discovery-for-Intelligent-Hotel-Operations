class OperationalService:

    OPERATIONAL_INSIGHTS = {

        # Family Dining Guests

        0: [

            "Increase kids club staffing.",

            "Improve restaurant capacity management.",

            "Enhance family activity coordination."
        ],

        # Budget Minimal Guests

        1: [

            "Reduce operational costs for low-engagement guests.",

            "Maintain efficient basic service operations.",

            "Improve customer support response."
        ],

        # Business Leisure Guests

        2: [

            "Improve concierge availability.",

            "Improve airport transport coordination.",

            "Enhance business support services."
        ],

        # Luxury Wellness Guests

        3: [

            "Increase spa staff allocation.",

            "Improve premium wellness experience.",

            "Enhance luxury guest engagement services."
        ]
    }

    def get_operational_insights(
        self,
        cluster_id: int
    ):

        return self.OPERATIONAL_INSIGHTS.get(

            cluster_id,

            []
        )