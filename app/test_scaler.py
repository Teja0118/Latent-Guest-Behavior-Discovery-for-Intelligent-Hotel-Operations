# check_model_features.py

import joblib

scaler = joblib.load(
    "models/pca_kmeans_scaler.pkl"
)

print(
    scaler.feature_names_in_
)