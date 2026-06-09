from database.database import SessionLocal

from database.models import PredictionHistory


class HistoryService:

    def save_prediction(
        self,
        guest_data: dict,
        prediction_result: dict,
        cluster_name: str
    ):

        database = SessionLocal()

        try:

            cleaned_guest_data = {}

            for key, value in guest_data.items():

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