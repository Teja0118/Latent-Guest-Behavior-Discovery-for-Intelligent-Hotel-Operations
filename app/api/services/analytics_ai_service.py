import os

from groq import Groq

from dotenv import load_dotenv

from api.services.analytics_service import (
    AnalyticsService
)

load_dotenv()


class AnalyticsAIService:

    def __init__(self):

        self.analytics_service = (
            AnalyticsService()
        )

        self.client = Groq(

            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def generate_summary(self):

        summary = (

            self.analytics_service
            .get_summary()
        )

        operational = (

            self.analytics_service
            .get_operational_kpis()
        )

        cluster_distribution = (

            self.analytics_service
            .get_cluster_distribution()
        )

        prompt = f"""
You are a hospitality business analyst.

Generate a concise executive summary
(120-150 words).

Analytics:

Total Predictions:
{summary["total_predictions"]}

Top Cluster:
{summary["top_cluster"]}

Guest Categories:
{summary["total_clusters"]}


Operational Demand:

Dining:
{operational["dining_demand"]}%

Wellness:
{operational["wellness_demand"]}%

Family:
{operational["family_demand"]}%

Business:
{operational["business_demand"]}%

Cluster Distribution:

{cluster_distribution}

Write an executive summary for hotel management.

Do NOT use bullet points.

Use professional language.
"""

        response = (

            self.client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.4,

                max_completion_tokens=250
            )
        )

        return {

            "summary":

            response.choices[
                0
            ].message.content
        }