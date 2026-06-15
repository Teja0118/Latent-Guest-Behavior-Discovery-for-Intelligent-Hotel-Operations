from sqlalchemy import func
from database.database import SessionLocal
from database.models import PredictionHistory

class AnalyticsService:
        
    def get_summary(self):

        database = SessionLocal()

        try:

            total_predictions = (
                database.query(
                    PredictionHistory
                ).count()
            )

            average_confidence = (

                database.query(
                    func.avg(
                        PredictionHistory.confidence
                    )
                ).scalar()
            )

            top_cluster_result = (

                database.query(
                    PredictionHistory.cluster_name,
                    func.count(
                        PredictionHistory.id
                    ).label("count")
                )
                .group_by(
                    PredictionHistory.cluster_name
                )
                .order_by(
                    func.count(
                        PredictionHistory.id
                    ).desc()
                )
                .first()
            )

            total_clusters = (

                database.query(
                    PredictionHistory.cluster_name
                )
                .distinct()
                .count()
            )

            return {

                "total_predictions":
                    total_predictions,

                "average_confidence":
                    round(
                        average_confidence or 0,
                        2
                    ),

                "total_clusters":
                    total_clusters,

                "top_cluster":
                    top_cluster_result[0]
                    if top_cluster_result
                    else "N/A"
            }

        finally:

            database.close()

    def get_cluster_distribution(self):

        database = SessionLocal()

        try:

            results = (

                database.query(
                    PredictionHistory.cluster_name,
                    func.count(
                        PredictionHistory.id
                    )
                )
                .group_by(
                    PredictionHistory.cluster_name
                )
                .all()
            )

            distribution = []

            for cluster_name, count in results:

                distribution.append({

                    "cluster_name":
                        cluster_name,

                    "count":
                        count
                })

            return distribution

        finally:

            database.close()

    def get_recent_predictions(self):
        database = SessionLocal()

        try:
            results = (
                database.query(
                    PredictionHistory
                )
                .order_by(
                    PredictionHistory.created_at.desc()
                )
                .limit(10)
                .all()
            )

            recent_predictions = []

            for row in results:
                recent_predictions.append({
                    "cluster_name": row.cluster_name,
                    "confidence": round(
                        float(row.confidence),
                        2
                    ),
                    "created_at": str(row.created_at)
                })
            return recent_predictions
        
        finally:
            database.close()