import os

from groq import Groq

from dotenv import load_dotenv


load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv(
            "GROQ_API_KEY"
        )

        if not api_key:

            raise Exception(
                "GROQ_API_KEY not found in .env"
            )

        self.client = Groq(
            api_key=api_key
        )

    def generate_behavior_analysis(

        self,

        cluster_name: str,

        recommendations: list,

        operational_insights: list

    ):

        try:

            prompt = f"""

You are a hospitality business intelligence expert.

A machine learning model has already classified a hotel guest.

Your job is NOT to predict the cluster.

Instead, explain the guest behaviour in business language.

Cluster:
{cluster_name}

Recommendations:
{", ".join(recommendations)}

Operational Insights:
{", ".join(operational_insights)}

Write:

1. One paragraph.
2. Around 70-100 words.
3. Explain WHY this guest belongs to this segment.
4. Mention likely behaviour.
5. Mention how the hotel can improve guest satisfaction.
6. Professional business language.
7. Do not repeat the recommendation list.
8. Do not use bullet points.
"""

            completion = (

                self.client.chat.completions.create(

                    model="llama-3.3-70b-versatile",

                    messages=[

                        {

                            "role": "system",

                            "content":

                            "You are an expert hospitality business analyst."

                        },

                        {

                            "role": "user",

                            "content": prompt

                        }

                    ],

                    temperature=0.4,

                    max_tokens=180

                )
            )

            return (

                completion

                .choices[0]

                .message.content

                .strip()

            )

        except Exception as error:

            return (

                "AI behavioral analysis "

                "is currently unavailable."

            )