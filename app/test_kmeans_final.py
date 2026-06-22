import pandas as pd

from preprocessing.data_loader import DataLoader
from preprocessing.data_preprocessor import DataPreprocessor
from clustering.feature_selector import FeatureSelector
from clustering.train_kmeans import KMeansTrainer


def main():

    dataset_path = (
        "data/hospitality_operations_03.csv"
    )

    data_loader = DataLoader(
        dataset_path
    )

    df = data_loader.load_dataset()

    preprocessor = DataPreprocessor(
        df
    )

    preprocessor.drop_unnecessary_columns()

    original_df = (
        preprocessor.get_original_dataframe()
    )

    feature_selector = FeatureSelector(
        original_df
    )

    clustering_df = (
        feature_selector.get_clustering_features()
    )

    kmeans = KMeansTrainer(
        clustering_df
    )

    labels = kmeans.train(
        n_clusters=6
    )

    print(
        "\nCluster Sizes:\n"
    )

    print(
        pd.Series(labels)
        .value_counts()
        .sort_index()
    )

    print(
        "\nCluster Percentages:\n"
    )

    print(
        (
            pd.Series(labels)
            .value_counts(
                normalize=True
            )
            * 100
        )
        .round(2)
        .sort_index()
    )

    clustered_df = (
        clustering_df.copy()
    )

    clustered_df[
        "guest_cluster"
    ] = labels

    clustered_df.to_csv(

        "data/clustered_hospitality_operations_kmeans.csv",

        index=False
    )

    print(
        "\nKMeans clustered dataset saved:"
    )

    print(
        "data/clustered_hospitality_operations_kmeans.csv"
    )

    kmeans.save()


if __name__ == "__main__":

    main()