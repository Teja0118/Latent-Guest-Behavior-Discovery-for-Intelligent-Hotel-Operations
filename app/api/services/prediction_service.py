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

            print(
                "\n========================"
            )

            print(
                f"Predicted Cluster ID: "
                f"{cluster_prediction}"
            )

            distances = (

                self.model.transform(
                    processed_dataframe
                )[0]
            )

            print(
                f"Distances: {distances}"
            )

            print(
                "========================\n"
            )

            return {

                "cluster_id":
                    int(
                        cluster_prediction
                    )
            }

        except Exception as error:

            raise Exception(

                f"Error during cluster "
                f"prediction: {error}"
            )