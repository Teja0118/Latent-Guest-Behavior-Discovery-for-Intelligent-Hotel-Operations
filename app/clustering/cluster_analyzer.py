import pandas as pd

class ClusterAnalyzer:

    def __init__(
            self,
            dataframe: pd.DataFrame,
            cluster_labels
    ):
        self.dataframe = dataframe.copy()
        self.dataframe["guest_cluster"] = cluster_labels

    def analyze_clusters(self):
        try:
            cluster_summary = self.dataframe.groupby(
                "guest_cluster"
            ).mean()

            print("\nCluster Analysis Summary:\n")
            print(cluster_summary)

            return cluster_summary
        except Exception as error:
            print(f"Error during cluster analysis: {error}")

    def save_clustered_dataset(self, output_path):
        try:
            self.dataframe.to_csv(
                output_path,
                index=False
            )

            print(
                f"\nClustered dataset saved successfully at: \n"
                f"{output_path}"
            )

        except Exception as error:
            print(f"Error while saving clustered dataset: {error}")
            