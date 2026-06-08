import pandas as pd


class ClusterAnalyzer:

    def __init__(
        self,
        dataframe: pd.DataFrame,
        cluster_labels
    ):

        self.dataframe = dataframe.copy()

        self.dataframe[
            "guest_cluster"
        ] = cluster_labels

    def analyze_clusters(self):

        try:

            numerical_columns = (

                self.dataframe.select_dtypes(

                    include=[
                        "int64",
                        "float64"
                    ]

                ).columns
            )

            numerical_columns = [

                column
                for column in numerical_columns
                if column != "guest_cluster"
            ]

            cluster_summary = (

                self.dataframe.groupby(
                    "guest_cluster"
                )[numerical_columns].mean()

            )

            print(
                "\nCluster Analysis "
                "Summary:\n"
            )

            print(
                cluster_summary
            )

            print(
                "\nCluster Sizes:\n"
            )

            print(

                self.dataframe[
                    "guest_cluster"
                ].value_counts()

            )

            return cluster_summary

        except Exception as error:

            print(
                f"Error during cluster "
                f"analysis: {error}"
            )

    def save_clustered_dataset(
        self,
        output_path
    ):

        try:

            self.dataframe.to_csv(

                output_path,

                index=False
            )

            print(

                f"\nClustered dataset "
                f"saved successfully at:\n"

                f"{output_path}"
            )

        except Exception as error:

            print(
                f"Error while saving "
                f"clustered dataset: "
                f"{error}"
            )