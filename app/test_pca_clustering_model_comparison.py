from preprocessing.data_loader import DataLoader
from preprocessing.data_preprocessor import DataPreprocessor
from clustering.feature_selector import FeatureSelector
from clustering.compare_pca_clustering_models import PCAClusteringComparison


def main():

    dataset_path = "data/hospitality_operations_03.csv"
    output_dir = "data"

    data_loader = DataLoader(
        dataset_path
    )

    dataframe = data_loader.load_dataset()

    preprocessor = DataPreprocessor(
        dataframe
    )

    preprocessor.drop_unnecessary_columns()

    original_dataframe = preprocessor.get_original_dataframe()

    feature_selector = FeatureSelector(
        original_dataframe
    )

    clustering_dataframe = feature_selector.get_clustering_features()

    comparison = PCAClusteringComparison(
        clustering_dataframe,
        n_clusters=6,
        pca_variance=0.85,
        random_state=42,
    )

    results = comparison.run()

    print("\nPCA CLUSTERING MODEL COMPARISON\n")
    print(
        results.to_string(
            index=False
        )
    )

    comparison.save_report(
        results,
        output_dir,
    )


if __name__ == "__main__":

    main()
