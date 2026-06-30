from database.database import SessionLocal

from database.models import PredictionHistory
from database.models import User
from sqlalchemy import func


class HistoryService:

    def save_prediction(
        self,
        guest_data: dict,
        prediction_result: dict,
        cluster_name: str,
        user_id: int = None,
        top_recommendation: str = None,
        operational_focus: str = None
    ):

        database = SessionLocal()

        try:

            cleaned_guest_data = {}

            history_columns = {
                column.name
                for column in PredictionHistory.__table__.columns
            }

            for key, value in guest_data.items():

                if key not in history_columns:
                    continue

                if value in [
                    None,
                    "",
                    "null"
                ] or str(value) == "nan":

                    cleaned_guest_data[key] = 0.0

                else:

                    cleaned_guest_data[key] = (
                        float(value)
                    )

            history = PredictionHistory(

                cluster_id=int(
                    prediction_result[
                        "cluster_id"
                    ]
                ),

                cluster_name=cluster_name,

                confidence=float(
                    prediction_result[
                        "cluster_confidence"
                    ]
                ),

                user_id=user_id,

                top_recommendation=top_recommendation,

                operational_focus=operational_focus,

                **cleaned_guest_data
            )

            database.add(history)

            database.commit()

        except Exception as error:

            database.rollback()

            raise Exception(
                f"Database logging error: "
                f"{error}"
            )

        finally:

            database.close()

    def get_history_summary(self):

        database = SessionLocal()

        try:

            total_records = (
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

            top_cluster = (
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

            latest_prediction = (
                database.query(
                    PredictionHistory
                )
                .order_by(
                    PredictionHistory.created_at.desc()
                )
                .first()
            )

            return {

                "total_records":
                    total_records,

                "top_cluster":
                    top_cluster[0]
                    if top_cluster
                    else "N/A",

                "latest_prediction":
                    str(
                        latest_prediction.created_at
                    )
                    if latest_prediction
                    else "N/A",

                "average_confidence":
                    round(
                        average_confidence or 0,
                        2
                    )
            }

        finally:

            database.close()

    def get_all_predictions(self):

        database = SessionLocal()

        try:

            results = (

                database.query(
                    PredictionHistory,
                    User.name
                )
                .outerjoin(
                    User,
                    PredictionHistory.user_id == User.id
                )

                .order_by(
                    PredictionHistory.created_at.desc()
                )

                .all()
            )

            history = []

            for row, user_name in results:

                history.append({

                    "user_name":
                        user_name or "Unknown User",

                    "cluster_name":
                        row.cluster_name,

                    "confidence":
                        round(
                            float(
                                row.confidence
                            ),
                            2
                        ),

                    "created_at":
                        str(
                            row.created_at
                        ),

                    "top_recommendation":
                        row.top_recommendation
                        or "N/A",

                    "operational_focus":
                        row.operational_focus
                        or "N/A"
                })

            return history

        finally:

            database.close()
