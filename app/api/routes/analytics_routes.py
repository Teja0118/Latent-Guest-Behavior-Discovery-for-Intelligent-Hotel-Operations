from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import StreamingResponse

import io
import csv

from api.services.analytics_service import (
    AnalyticsService
)

from api.services.auth_dependency import (
    get_current_user
)

from api.services.history_service import (
    HistoryService
)

from api.services.analytics_ai_service import (
    AnalyticsAIService
)


router = APIRouter()

analytics_service = AnalyticsService()

history_service = HistoryService()

analytics_ai_service = (
    AnalyticsAIService()
)


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


@router.get(
    "/analytics/cluster-insights"
)
def get_cluster_insights(

    current_user=Depends(
        get_current_user
    )
):

    return (
        analytics_service
        .get_cluster_insights()
    )

@router.get(
    "/history/summary"
)
def get_history_summary(

    current_user=Depends(
        get_current_user
    )
):

    return (
        history_service
        .get_history_summary()
    )

@router.get(
    "/history/all"
)
def get_all_predictions(

    current_user=Depends(
        get_current_user
    )
):

    return (
        history_service
        .get_all_predictions()
    )

@router.get(
    "/analytics/operational-kpis"
)
def get_operational_kpis(

    current_user=Depends(
        get_current_user
    )
):

    return (
        analytics_service
        .get_operational_kpis()
    )

@router.get(
    "/history/export-csv"
)
def export_history_csv(

    current_user=Depends(
        get_current_user
    )
):

    records = (
        history_service
        .get_all_predictions()
    )

    output = io.StringIO()

    writer = csv.writer(
        output
    )

    writer.writerow([

        "User",

        "Cluster",

        "Top Recommendation",

        "Operational Focus",

        "Created At"
    ])

    for row in records:

        writer.writerow([

            row["user_name"],

            row["cluster_name"],

            row["top_recommendation"],

            row["operational_focus"],

            row["created_at"]
        ])

    output.seek(0)

    return StreamingResponse(

        iter([output.getvalue()]),

        media_type="text/csv",

        headers={

            "Content-Disposition":

            "attachment; filename=prediction_history.csv"
        }
    )

@router.get(
    "/analytics/segment-popularity"
)
def get_segment_popularity(

    current_user=Depends(
        get_current_user
    )
):

    return (
        analytics_service
        .get_segment_popularity()
    )


@router.get(
    "/analytics/ai-summary"
)
def get_ai_summary(

    current_user=Depends(
        get_current_user
    )
):

    return (

        analytics_ai_service
        .generate_summary()
    )