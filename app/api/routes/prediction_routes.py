from fastapi import APIRouter

from api.schemas.guest_input_schema import GuestInputSchema
from api.services.prediction_service import PredictionService
from api.services.recommendation_service import RecommendationService
from api.services.operational_service import OperationalService

router = APIRouter()

prediction_service = PredictionService()
recommendation_service = RecommendationService()
operational_service = OperationalService()


@router.post("/predict-cluster")
def predict_cluster(guest_input: GuestInputSchema):
    
    cluster_prediction = prediction_service.predict_cluster(
        guest_input.model_dump()
    )

    cluster_details = (
        recommendation_service.get_cluster_details(
            cluster_prediction
        )
    )

    operational_insights = (
        operational_service.get_operational_insights(
            cluster_prediction
        )
    )

    return {

        "predicted_cluster": cluster_prediction,

        "cluster_name": (
            cluster_details["cluster_name"]
        ),

        "recommendations": (
            cluster_details["recommendations"]
        ),

        "operational_insights": (
            operational_insights
        )
    }