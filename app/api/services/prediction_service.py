import joblib

from api.services.inference_preprocessor import (
    InferencePreprocessor
)


class PredictionService:

    def __init__(self):

        self.model = joblib.load(
            "models/gmm_guest_clustering_model.pkl"
        )

        self.preprocessor = (
            InferencePreprocessor()
        )

    def predict_cluster(
        self,
        guest_data: dict
    ):

        try:

            processed_dataframe = (

                self.preprocessor.preprocess_input(
                    guest_data
                )
            )

            cluster_prediction = (

                self.model.predict(
                    processed_dataframe
                )[0]
            )

            cluster_probabilities = (

                self.model.predict_proba(
                    processed_dataframe
                )[0]
            )

            return {

                "cluster_id":
                    int(cluster_prediction),

                "cluster_confidence":
                    round(
                        max(
                            cluster_probabilities
                        ) * 100,
                        2
                    )
            }

        except Exception as error:

            raise Exception(
                f"Error during cluster "
                f"prediction: {error}"
            )