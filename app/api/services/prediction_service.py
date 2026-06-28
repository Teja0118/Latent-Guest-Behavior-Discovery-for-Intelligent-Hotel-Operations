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

            sorted_distances = sorted(
                distances
            )

            nearest_distance = (
                sorted_distances[0]
            )

            second_nearest_distance = (
                sorted_distances[1]
            )

            confidence = float(round(

                (
                    second_nearest_distance
                    /
                    (
                        nearest_distance
                        +
                        second_nearest_distance
                    )
                ) * 100,

                2
            ))

            if confidence < 56:
                confidence_band = "Low"
            elif confidence < 67:
                confidence_band = "Medium"
            else:
                confidence_band = "High"

            return {

                "cluster_id":
                    int(
                        cluster_prediction
                    ),

                "cluster_confidence":
                    confidence,

                "cluster_assignment_strength":
                    confidence,

                "confidence_band":
                    confidence_band
            }

        except Exception as error:

            raise Exception(

                f"Error during cluster "
                f"prediction: {error}"
            )


'''
#v1

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

            distances = (

                self.model.transform(
                    processed_dataframe
                )[0]
            )

            sorted_distances = sorted(
                distances
            )

            nearest_distance = (
                sorted_distances[0]
            )

            second_nearest_distance = (
                sorted_distances[1]
            )

            confidence = round(

                (
                    second_nearest_distance
                    /
                    (
                        nearest_distance
                        +
                        second_nearest_distance
                    )
                ) * 100,

                2
            )

            return {

                "cluster_id":
                    int(
                        cluster_prediction
                    ),

                "cluster_confidence":
                    confidence
            }

        except Exception as error:

            raise Exception(

                f"Error during cluster "
                f"prediction: {error}"
            )


#vr2
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

            distances = (

                self.model.transform(
                    processed_dataframe
                )[0]
            )

            sorted_distances = sorted(
                distances
            )

            nearest_distance = (
                sorted_distances[0]
            )

            second_nearest_distance = (
                sorted_distances[1]
            )

            raw_confidence = (

                second_nearest_distance
                /
                (
                    nearest_distance
                    +
                    second_nearest_distance
                )
            )

            confidence = round(

                70 +

                (
                    raw_confidence * 29
                ),

                2
            )

            confidence = min(
                confidence,
                99.0
            )

            return {

                "cluster_id":
                    int(
                        cluster_prediction
                    ),

                "cluster_confidence":
                    confidence
            }

        except Exception as error:

            raise Exception(

                f"Error during cluster "
                f"prediction: {error}"
            )

#v3
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

            distances = (

                self.model.transform(
                    processed_dataframe
                )[0]
            )

            sorted_distances = sorted(
                distances
            )

            nearest_distance = (
                sorted_distances[0]
            )

            second_nearest_distance = (
                sorted_distances[1]
            )

            confidence = round(

                85 +

                (
                    (
                        second_nearest_distance
                        /
                        (
                            nearest_distance
                            +
                            second_nearest_distance
                        )
                    )
                    * 14
                ),

                2
            )

            confidence = min(
                confidence,
                99.5
            )

            return {

                "cluster_id":
                    int(
                        cluster_prediction
                    ),

                "cluster_confidence":
                    confidence
            }

        except Exception as error:

            raise Exception(

                f"Error during cluster "
                f"prediction: {error}"
            )

'''
