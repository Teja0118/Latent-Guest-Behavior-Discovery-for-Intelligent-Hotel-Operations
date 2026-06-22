from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

import joblib


class PCAKMeansTrainer:

    def __init__(
        self,
        dataframe
    ):

        self.scaler = StandardScaler()

        scaled_data = (
            self.scaler.fit_transform(
                dataframe
            )
        )

        self.pca = PCA(
            n_components=0.85,
            random_state=42
        )

        self.X = (
            self.pca.fit_transform(
                scaled_data
            )
        )

        print(
            f"\nPCA Components Retained: "
            f"{self.pca.n_components_}"
        )

        print(
            f"Explained Variance: "
            f"{self.pca.explained_variance_ratio_.sum():.4f}"
        )

    def train(
        self,
        n_clusters=6
    ):

        self.model = KMeans(

            n_clusters=n_clusters,

            random_state=42,

            n_init=20
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

        print(
            "\nFINAL PCA KMEANS RESULTS\n"
        )

        print(
            f"Silhouette: "
            f"{silhouette:.4f}"
        )

        print(
            f"Davies Bouldin: "
            f"{davies:.4f}"
        )

        print(
            f"Calinski Harabasz: "
            f"{calinski:.4f}"
        )

        return labels

    def save(self):

        joblib.dump(

            self.model,

            "models/pca_kmeans_model.pkl"
        )

        joblib.dump(

            self.scaler,

            "models/pca_kmeans_scaler.pkl"
        )

        joblib.dump(

            self.pca,

            "models/pca_transformer.pkl"
        )

        print(
            "\nPCA KMeans artifacts saved."
        )