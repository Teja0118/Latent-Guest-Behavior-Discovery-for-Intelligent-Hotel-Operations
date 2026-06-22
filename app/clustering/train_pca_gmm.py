from sklearn.decomposition import PCA

from sklearn.mixture import GaussianMixture

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

import joblib


class PCAGMMTrainer:

    def __init__(
        self,
        dataframe
    ):

        self.scaler = StandardScaler()

        scaled = (
            self.scaler.fit_transform(
                dataframe
            )
        )

        self.pca = PCA(

            n_components=0.95,

            random_state=42
        )

        self.X = (
            self.pca.fit_transform(
                scaled
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

        print("\nPCA GMM RESULTS")

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

            "models/pca_gmm_model.pkl"
        )

        joblib.dump(

            self.scaler,

            "models/pca_gmm_scaler.pkl"
        )

        joblib.dump(

            self.pca,

            "models/pca_transformer.pkl"
        )