from preprocessing.data_loader import DataLoader
from preprocessing.data_preprocessor import DataPreprocessor
from clustering.feature_selector import FeatureSelector
from clustering.pca_kmeans_model_review import PCAKMeansModelReview


def main():

    data_loader = DataLoader(
        "data/hospitality_operations_03.csv"
    )

    dataframe = data_loader.load_dataset()

    preprocessor = DataPreprocessor(
        dataframe
    )

    preprocessor.drop_unnecessary_columns()

    feature_selector = FeatureSelector(
        preprocessor.get_original_dataframe()
    )

    clustering_dataframe = (
        feature_selector.get_clustering_features()
    )

    review = PCAKMeansModelReview(
        clustering_dataframe
    )

    review.run()


if __name__ == "__main__":

    main()
