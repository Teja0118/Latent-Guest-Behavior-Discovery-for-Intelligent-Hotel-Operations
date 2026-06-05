class OperationalService:

    OPERATIONAL_INSIGHTS = {

        0: [
            "Maintain strong dining operations.",
            "Optimize leisure service staffing."
        ],

        1: [
            "Increase spa staff allocation.",
            "Improve wellness service capacity."
        ],

        2: [
            "Improve transport availability.",
            "Increase laundry service efficiency."
        ],

        3: [
            "Improve customer support response.",
            "Reduce check-in waiting times."
        ],

        4: [
            "Increase kids club staffing.",
            "Improve family activity scheduling."
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