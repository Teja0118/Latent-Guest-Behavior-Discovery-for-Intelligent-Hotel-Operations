# app/test_cluster_profiles.py

import pandas as pd

df = pd.read_csv(
    "data/clustered_hospitality_operations_pca_kmeans.csv"
)

print(

    df.groupby(
        "guest_cluster"
    ).mean(
        numeric_only=True
    )

)