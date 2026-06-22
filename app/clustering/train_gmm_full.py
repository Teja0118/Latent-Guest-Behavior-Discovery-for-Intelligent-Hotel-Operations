from sklearn.mixture import GaussianMixture

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

from sklearn.preprocessing import StandardScaler

import joblib


class GMMFullTrainer:

    def __init__(
        self,
        dataframe
    ):

        self.scaler = StandardScaler()

        self.X = (
            self.scaler.fit_transform(
                dataframe
            )
        )

    def train(
        self,
        n_clusters=5
    ):

        self.model = GaussianMixture(

            n_components=n_clusters,

            covariance_type="full",

            random_state=42
        )

        labels = (
            self.model.fit_predict(
                self.X
            )
        )

        silhouette = (
            silhouette_score(
                self.X,
                labels
            )
        )

        davies = (
            davies_bouldin_score(
                self.X,
                labels
            )
        )

        calinski = (
            calinski_harabasz_score(
                self.X,
                labels
            )
        )

        print("\nGMM FULL RESULTS")
        print(
            f"Silhouette: {silhouette:.4f}"
        )
        print(
            f"Davies Bouldin: {davies:.4f}"
        )
        print(
            f"Calinski Harabasz: {calinski:.4f}"
        )

        return labels

    def save(self):

        joblib.dump(

            self.model,

            "models/gmm_full_model.pkl"
        )

        joblib.dump(

            self.scaler,

            "models/gmm_full_scaler.pkl"
        )