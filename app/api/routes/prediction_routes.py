from fastapi import APIRouter

from fastapi import HTTPException

from fastapi import Depends

from api.schemas.guest_input_schema import (
    GuestInputSchema
)

from api.services.prediction_service import (
    PredictionService
)

from api.services.auth_dependency import (
    get_current_user
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

from api.services.llm_service import (
    LLMService
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

history_service = (
    HistoryService()
)

llm_service = (
    LLMService()
)


@router.post("/predict-cluster")
def predict_cluster(

    guest_data: GuestInputSchema,

    current_user=Depends(
        get_current_user
    )
):

    try:

        prediction_result = (

            prediction_service.predict_cluster(

                guest_data.dict()

            )
        )

        cluster_id = (

            prediction_result[
                "cluster_id"
            ]
        )

        cluster_details = (

            recommendation_service
            .get_cluster_details(

                cluster_id

            )
        )

        operational_insights = (

            operational_service
            .get_operational_insights(

                cluster_id

            )
        )

        ai_behavior_analysis = (

            llm_service
            .generate_behavior_analysis(

                cluster_name=

                cluster_details[
                    "cluster_name"
                ],

                recommendations=

                cluster_details[
                    "recommendations"
                ],

                operational_insights=

                operational_insights
            )
        )

        history_service.save_prediction(

            guest_data.model_dump(),

            prediction_result,

            cluster_details[
                "cluster_name"
            ],

            user_id=current_user.id,

            top_recommendation=(

                cluster_details[
                    "recommendations"
                ][0]

                if

                cluster_details[
                    "recommendations"
                ]

                else None
            ),

            operational_focus=(

                operational_insights[0]

                if operational_insights

                else None
            )
        )

        return {

            "predicted_cluster":

                cluster_id,

            "cluster_name":

                cluster_details[
                    "cluster_name"
                ],

            "recommendations":

                cluster_details[
                    "recommendations"
                ],

            "operational_insights":

                operational_insights,

            "ai_behavior_analysis":

                ai_behavior_analysis
        }

    except Exception as error:

        raise HTTPException(

            status_code=500,

            detail=str(error)
        )