from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

import joblib


class KMeansTrainer:

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

    def evaluate_k_range(self):

        print(
            "\nKMEANS K-SELECTION RESULTS\n"
        )

        for k in range(3, 8):

            model = KMeans(

                n_clusters=k,

                random_state=42,

                n_init=10
            )

            labels = (
                model.fit_predict(
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

            print(

                f"K={k}"

                f" | Silhouette={silhouette:.4f}"

                f" | DB={davies:.4f}"

                f" | CH={calinski:.2f}"
            )

    def train(
        self,
        n_clusters=5
    ):

        self.model = KMeans(

            n_clusters=n_clusters,

            random_state=42,

            n_init=10
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

        print("\nFINAL KMEANS RESULTS\n")

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

            "models/kmeans_model_v2.pkl"
        )

        joblib.dump(

            self.scaler,

            "models/kmeans_scaler_v2.pkl"
        )