from fastapi import APIRouter

from fastapi import HTTPException

from api.schemas.guest_input_schema import (
GuestInputSchema
)

from api.services.prediction_service import (
PredictionService
)

from api.services.recommendation_service import (
RecommendationService
)

from api.services.operational_service import (
OperationalService
)

from api.services.history_service import (
    HistoryService
)

router = APIRouter()

prediction_service = (
PredictionService()
)

recommendation_service = (
RecommendationService()
)

operational_service = (
OperationalService()
)

history_service = HistoryService()

@router.post("/predict-cluster")
def predict_cluster(guest_data: GuestInputSchema):

    try:

        prediction_result = (

            prediction_service.predict_cluster(
                guest_data.dict()
            )
        )

        cluster_id = (
            prediction_result["cluster_id"]
        )

        confidence = (
            prediction_result[
                "cluster_confidence"
            ]
        )

        cluster_details = (

            recommendation_service
            .get_cluster_details(
                cluster_id
            )
        )

        history_service.save_prediction(

            guest_data.model_dump(),

            prediction_result,

            cluster_details[
                "cluster_name"
            ]
        )

        operational_insights = (

            operational_service
            .get_operational_insights(
                cluster_id
            )
        )

        return {

            "predicted_cluster":
                cluster_id,

            "cluster_confidence":
                confidence,

            "cluster_name":
                cluster_details[
                    "cluster_name"
                ],

            "recommendations":
                cluster_details[
                    "recommendations"
                ],

            "operational_insights":
                operational_insights
        }

    except Exception as error:

        raise HTTPException(

            status_code=500,

            detail=str(error)
        )

