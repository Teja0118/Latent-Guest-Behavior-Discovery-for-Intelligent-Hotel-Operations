from preprocessing.data_loader import DataLoader
from preprocessing.data_preprocessor import DataPreprocessor
from clustering.feature_selector import FeatureSelector

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)


def main():

    dataset_path = (
        "data/hospitality_operations_03.csv"
    )

    data_loader = DataLoader(
        dataset_path
    )

    dataframe = (
        data_loader.load_dataset()
    )

    preprocessor = DataPreprocessor(
        dataframe
    )

    preprocessor.drop_unnecessary_columns()

    original_dataframe = (
        preprocessor.get_original_dataframe()
    )

    feature_selector = FeatureSelector(
        original_dataframe
    )

    clustering_dataframe = (
        feature_selector.get_clustering_features()
    )

    scaler = StandardScaler()

    scaled_data = (
        scaler.fit_transform(
            clustering_dataframe
        )
    )

    pca = PCA(

        n_components=0.95,

        random_state=42
    )

    pca_data = (
        pca.fit_transform(
            scaled_data
        )
    )

    print(
        "\nPCA KMEANS K-SELECTION RESULTS\n"
    )

    print(
        f"PCA Components: "
        f"{pca.n_components_}"
    )

    print(
        f"Explained Variance: "
        f"{pca.explained_variance_ratio_.sum():.4f}\n"
    )

    for k in range(3, 11):

        model = KMeans(

            n_clusters=k,

            random_state=42,

            n_init=10
        )

        labels = (
            model.fit_predict(
                pca_data
            )
        )

        silhouette = (
            silhouette_score(
                pca_data,
                labels
            )
        )

        davies = (
            davies_bouldin_score(
                pca_data,
                labels
            )
        )

        calinski = (
            calinski_harabasz_score(
                pca_data,
                labels
            )
        )

        print(

            f"K={k}"

            f" | Silhouette="
            f"{silhouette:.4f}"

            f" | DB="
            f"{davies:.4f}"

            f" | CH="
            f"{calinski:.2f}"
        )


if __name__ == "__main__":

    main()