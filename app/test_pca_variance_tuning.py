from preprocessing.data_loader import DataLoader
from preprocessing.data_preprocessor import DataPreprocessor

from clustering.feature_selector import (
    FeatureSelector
)

from clustering.test_pca_variance_tuning import (
    PCAVarianceTuner
)


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

tuner = PCAVarianceTuner(
    clustering_df
)

tuner.evaluate_variances()