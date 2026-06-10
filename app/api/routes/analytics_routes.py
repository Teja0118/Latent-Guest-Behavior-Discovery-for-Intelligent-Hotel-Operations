from fastapi import APIRouter

from api.services.analytics_service import (
    AnalyticsService
)

router = APIRouter()

analytics_service = AnalyticsService()


@router.get("/analytics/summary")
def get_summary():

    return analytics_service.get_summary()


@router.get(
    "/analytics/cluster-distribution"
)
def get_cluster_distribution():

    return (
        analytics_service
        .get_cluster_distribution()
    )


@router.get(
    "/analytics/recent-predictions"
)
def get_recent_predictions():

    return (
        analytics_service
        .get_recent_predictions()
    )