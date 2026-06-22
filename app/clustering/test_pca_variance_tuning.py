from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)


class PCAVarianceTuner:

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

    def evaluate_variances(self):

        print(
            "\nPCA VARIANCE TUNING RESULTS\n"
        )

        for variance in [

            0.90,
            0.92,
            0.94,
            0.95,
            0.97,
            0.99
        ]:

            pca = PCA(
                n_components=variance,
                random_state=42
            )

            X_pca = pca.fit_transform(
                self.X
            )

            kmeans = KMeans(

                n_clusters=6,

                random_state=42,

                n_init=10
            )

            labels = (
                kmeans.fit_predict(
                    X_pca
                )
            )

            silhouette = (
                silhouette_score(
                    X_pca,
                    labels
                )
            )

            davies = (
                davies_bouldin_score(
                    X_pca,
                    labels
                )
            )

            calinski = (
                calinski_harabasz_score(
                    X_pca,
                    labels
                )
            )

            print(
                f"Variance={variance:.2f}"
                f" | Components={X_pca.shape[1]}"
                f" | Silhouette={silhouette:.4f}"
                f" | DB={davies:.4f}"
                f" | CH={calinski:.2f}"
            )