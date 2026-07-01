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

                    "cluster_name":
                        row.cluster_name,

                    "created_at":
                        str(row.created_at)
                })

            return recent_predictions

        finally:

            database.close()

    def get_cluster_insights(self):

        database = SessionLocal()

        try:

            results = (

                database.query(
                    PredictionHistory.cluster_name,
                    func.count(
                        PredictionHistory.id
                    ).label("count")
                )

                .group_by(
                    PredictionHistory.cluster_name
                )

                .all()
            )

            total_predictions = sum(
                row.count
                for row in results
            )

            insights = []

            highest_count = max(
                [row.count for row in results],
                default=0
            )

            for row in results:

                percentage = round(

                    (
                        row.count
                        / total_predictions
                    ) * 100,

                    2
                ) if total_predictions else 0

                if row.count == highest_count:

                    status = "Most Popular"

                elif percentage >= 15:

                    status = "High Activity"

                else:

                    status = "Underrepresented"

                insights.append({

                    "cluster_name":
                        row.cluster_name,

                    "count":
                        row.count,

                    "percentage":
                        percentage,

                    "status":
                        status
                })

            return insights

        finally:

            database.close()

    def get_operational_kpis(self):

        database = SessionLocal()

        try:

            results = (

                database.query(
                    PredictionHistory.cluster_name,
                    func.count(
                        PredictionHistory.id
                    ).label("count")
                )

                .group_by(
                    PredictionHistory.cluster_name
                )

                .all()
            )

            total_predictions = sum(
                row.count
                for row in results
            )

            dining = 0
            wellness = 0
            family = 0
            business = 0

            for row in results:

                cluster = (
                    row.cluster_name
                    .lower()
                )

                if "wellness" in cluster:

                    wellness += row.count

                elif "family" in cluster:

                    family += row.count

                elif "business" in cluster:

                    business += row.count

                elif "luxury dining" in cluster:

                    dining += row.count

            def calculate(value):

                if total_predictions == 0:

                    return 0

                return round(
                    (
                        value
                        / total_predictions
                    ) * 100,
                    2
                )

            return {

                "dining_demand":
                    calculate(dining),

                "wellness_demand":
                    calculate(wellness),

                "family_demand":
                    calculate(family),

                "business_demand":
                    calculate(business)
            }

        finally:

            database.close()

    def get_segment_popularity(self):

        database = SessionLocal()

        try:

            results = (

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

                .all()
            )

            popularity = []

            for row in results:

                popularity.append({

                    "cluster_name":
                        row.cluster_name,

                    "count":
                        row.count
                })

            return popularity

        finally:

            database.close()


        database = SessionLocal()

        try:

            results = (

                database.query(
                    PredictionHistory.cluster_name,

                    func.avg(
                        PredictionHistory.confidence
                    ).label("avg_confidence")
                )

                .group_by(
                    PredictionHistory.cluster_name
                )

                .all()
            )

            confidence_data = []

            for row in results:

                confidence_data.append({

                    "cluster_name":
                        row.cluster_name,

                    "avg_confidence":
                        round(
                            float(
                                row.avg_confidence
                            ),
                            2
                        )
                })

            return confidence_data

        finally:

            database.close()