from sklearn.mixture import GaussianMixture

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

from sklearn.preprocessing import StandardScaler

import joblib


class ClusteringTrainer:

    def __init__(
        self,
        dataframe
    ):

        self.dataframe = dataframe

        self.scaler = StandardScaler()

        self.processed_dataframe = (
            self.scaler.fit_transform(
                self.dataframe
            )
        )

    def save_preprocessor(
        self,
        output_path: str
    ):

        try:

            joblib.dump(
                self.scaler,
                output_path
            )

            print(
                f"\nPreprocessor saved "
                f"successfully at:\n"
                f"{output_path}"
            )

        except Exception as error:

            print(
                f"Error while saving "
                f"preprocessor: {error}"
            )

    def silhouette_analysis(self):

        try:

            print(
                "\nClustering Evaluation Metrics\n"
            )

            for k in range(2, 11):

                model = GaussianMixture(

                    n_components=k,

                    covariance_type="full",

                    random_state=42
                )

                cluster_labels = (
                    model.fit_predict(
                        self.processed_dataframe
                    )
                )

                silhouette = (
                    silhouette_score(
                        self.processed_dataframe,
                        cluster_labels
                    )
                )

                db_score = (
                    davies_bouldin_score(
                        self.processed_dataframe,
                        cluster_labels
                    )
                )

                ch_score = (
                    calinski_harabasz_score(
                        self.processed_dataframe,
                        cluster_labels
                    )
                )

                print(

                    f"K={k}"

                    f" | Silhouette={silhouette:.4f}"

                    f" | DB={db_score:.4f}"

                    f" | CH={ch_score:.2f}"
                )

        except Exception as error:

            print(
                f"Error during clustering "
                f"evaluation: {error}"
            )

    def train_final_model(
        self,
        n_clusters: int = 5
    ):

        try:

            self.model = GaussianMixture(

                n_components=n_clusters,

                covariance_type="full",

                random_state=42
            )

            cluster_labels = (
                self.model.fit_predict(
                    self.processed_dataframe
                )
            )

            silhouette = (
                silhouette_score(
                    self.processed_dataframe,
                    cluster_labels
                )
            )

            db_score = (
                davies_bouldin_score(
                    self.processed_dataframe,
                    cluster_labels
                )
            )

            ch_score = (
                calinski_harabasz_score(
                    self.processed_dataframe,
                    cluster_labels
                )
            )

            print(
                f"\nFinal GMM Model "
                f"trained successfully "
                f"with K={n_clusters}"
            )

            print(
                f"\nFinal Metrics:"
            )

            print(
                f"Silhouette Score : "
                f"{silhouette:.4f}"
            )

            print(
                f"Davies-Bouldin Score : "
                f"{db_score:.4f}"
            )

            print(
                f"Calinski-Harabasz Score : "
                f"{ch_score:.2f}"
            )

            return cluster_labels

        except Exception as error:

            print(
                f"Error during final "
                f"model training: "
                f"{error}"
            )

    def save_model(
        self,
        output_path: str
    ):

        try:

            joblib.dump(
                self.model,
                output_path
            )

            print(
                f"\nClustering model "
                f"saved successfully at:\n"
                f"{output_path}"
            )

        except Exception as error:

            print(
                f"Error while saving "
                f"model: {error}"
            )