class OperationalService:

    OPERATIONAL_INSIGHTS = {

        # Luxury Dining Guests

        0: [

            "Increase restaurant staffing.",

            "Improve premium dining services.",

            "Expand lounge capacity."
        ],

        # Family Leisure Guests

        1: [

            "Increase kids club resources.",

            "Expand family activities.",

            "Improve activity scheduling."
        ],

        # Wellness Luxury Guests

        2: [

            "Increase spa staffing.",

            "Enhance wellness facilities.",

            "Promote premium wellness packages."
        ],

        # Business Travelers

        3: [

            "Increase concierge staffing.",

            "Improve transport coordination.",

            "Enhance business support services."
        ],

        # Budget Minimal Guests

        4: [

            "Optimize operational costs.",

            "Maintain efficient basic services.",

            "Promote upselling opportunities."
        ],

        # Premium Family Business Guests

        5: [

            "Balance family and business services.",

            "Increase concierge support.",

            "Improve multi-service coordination."
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