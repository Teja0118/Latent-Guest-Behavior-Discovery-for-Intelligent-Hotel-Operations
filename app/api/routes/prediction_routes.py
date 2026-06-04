from fastapi import APIRouter

from api.schemas.guest_input_schema import GuestInputSchema
from api.services.prediction_service import PredictionService

router = APIRouter()

prediction_service = PredictionService()

@router.post("/predict-cluster")
def predict_cluster(guest_input: GuestInputSchema):
    
    cluster_prediction = prediction_service.predict_cluster(
        guest_input.model_dump()
    )

    return {
        "predicted_cluster": cluster_prediction
    }