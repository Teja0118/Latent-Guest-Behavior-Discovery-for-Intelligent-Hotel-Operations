from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)


class PCAKMeansTrainerV2:

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

            n_components=0.90,

            random_state=42
        )

        self.X = (

            self.pca.fit_transform(
                scaled_data
            )
        )

        print(
            f"\nPCA Components: "
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

        model = KMeans(

            n_clusters=n_clusters,

            random_state=42,

            n_init=10
        )

        labels = model.fit_predict(
            self.X
        )

        print(
            "\nPCA KMEANS V2 RESULTS\n"
        )

        print(
            f"Silhouette: "
            f"{silhouette_score(self.X, labels):.4f}"
        )

        print(
            f"Davies Bouldin: "
            f"{davies_bouldin_score(self.X, labels):.4f}"
        )

        print(
            f"Calinski Harabasz: "
            f"{calinski_harabasz_score(self.X, labels):.4f}"
        )

        return labels