import joblib 
import pandas as pd

class PredictionService:

    def __init__(self):
        self.model = joblib.load(
            "models/kmeans_guest_clustering_model.pkl"
        )
    
    def predict_cluster(self, guest_data: dict):
        try:
            dataframe = pd.DataFrame([guest_data])
            cluster_prediction = self.model.predict(
                dataframe
            )[0]
            return int(cluster_prediction)
        except Exception as error:
            raise Exception(
                f"Error during cluster prediction: {error}"
            )