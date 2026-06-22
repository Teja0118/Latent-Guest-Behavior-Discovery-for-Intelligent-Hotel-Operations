from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

from sklearn.cluster import KMeans

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

import pandas as pd


class PCAKMeansGridSearch:

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

    def run(self):

        results = []

        variances = [

            0.85,
            0.88,
            0.90,
            0.92
        ]

        clusters = [

            4,
            5,
            6,
            7,
            8
        ]

        n_inits = [

            10,
            20,
            50
        ]

        print(
            "\nPCA KMEANS GRID SEARCH\n"
        )

        for variance in variances:

            pca = PCA(

                n_components=variance,

                random_state=42
            )

            X_pca = (
                pca.fit_transform(
                    self.X
                )
            )

            for k in clusters:

                for n_init in n_inits:

                    model = KMeans(

                        n_clusters=k,

                        random_state=42,

                        n_init=n_init
                    )

                    labels = (
                        model.fit_predict(
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

                    results.append({

                        "variance":
                            variance,

                        "components":
                            X_pca.shape[1],

                        "k":
                            k,

                        "n_init":
                            n_init,

                        "silhouette":
                            silhouette,

                        "db":
                            davies,

                        "ch":
                            calinski
                    })

                    print(

                        f"Variance={variance} "
                        f"| K={k} "
                        f"| n_init={n_init} "
                        f"| Silhouette={silhouette:.4f} "
                        f"| DB={davies:.4f}"
                    )

        results_df = pd.DataFrame(
            results
        )

        results_df = (
            results_df
            .sort_values(
                by="silhouette",
                ascending=False
            )
        )

        print(
            "\nTOP 10 CONFIGURATIONS\n"
        )

        print(
            results_df.head(10)
        )

        results_df.to_csv(

            "data/pca_kmeans_grid_search_results.csv",

            index=False
        )

        print(
            "\nResults saved to:\n"
            "data/pca_kmeans_grid_search_results.csv"
        )