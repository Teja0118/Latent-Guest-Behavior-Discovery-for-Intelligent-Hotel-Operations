from ..api.services.prediction_service import (
    PredictionService
)

from ..api.services.recommendation_service import (
    RecommendationService
)

from ..api.services.operational_service import (
    OperationalService
)

from testing.test_prediction_payloads import (
    payloads
)


prediction_service = PredictionService()

recommendation_service = (
    RecommendationService()
)

operational_service = (
    OperationalService()
)


for name, payload in payloads.items():

    print("\n" + "=" * 60)

    print(f"\nTEST CASE: {name}")

    prediction = (
        prediction_service.predict_cluster(
            payload
        )
    )

    cluster_id = (
        prediction["cluster_id"]
    )

    cluster_details = (

        recommendation_service.get_cluster_details(
            cluster_id
        )
    )

    insights = (

        operational_service.get_operational_insights(
            cluster_id
        )
    )

    print(
        f"\nPredicted Cluster: "
        f"{cluster_id}"
    )

    print(
        f"\nCluster Name: "
        f"{cluster_details['cluster_name']}"
    )

    print(
        "\nRecommendations:"
    )

    for item in (
        cluster_details[
            "recommendations"
        ]
    ):

        print(
            f"- {item}"
        )

    print(
        "\nOperational Insights:"
    )

    for item in insights:

        print(
            f"- {item}"
        )