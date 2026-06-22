import joblib

from api.services.inference_preprocessor import (
    InferencePreprocessor
)


class PredictionService:

    def __init__(self):

        self.model = joblib.load(
            "models/pca_kmeans_model.pkl"
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

            return {

                "cluster_id":
                    int(cluster_prediction),

                "cluster_confidence":
                    100.0
            }

        except Exception as error:

            raise Exception(

                f"Error during cluster "
                f"prediction: {error}"
            )