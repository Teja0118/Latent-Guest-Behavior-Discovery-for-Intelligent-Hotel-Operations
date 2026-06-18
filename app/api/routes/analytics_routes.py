from fastapi import APIRouter
from fastapi import Depends

from api.services.analytics_service import (
    AnalyticsService
)

from api.services.auth_dependency import (
    get_current_user
)

router = APIRouter()

analytics_service = AnalyticsService()


@router.get("/analytics/summary")
def get_summary(

    current_user=Depends(
        get_current_user
    )
):

    return analytics_service.get_summary()


@router.get(
    "/analytics/cluster-distribution"
)
def get_cluster_distribution(
    current_user=Depends(
        get_current_user
    )
):

    return (
        analytics_service
        .get_cluster_distribution()
    )


@router.get(
    "/analytics/recent-predictions"
)
def get_recent_predictions(
    current_user=Depends(
        get_current_user
    )
):

    return (
        analytics_service
        .get_recent_predictions()
    )