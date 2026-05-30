import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class ClusteringTrainer:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def elbow_method(self):

        try:
            inertia_values = []

            cluster_range = range(2,11)

            for cluster_count in cluster_range:

                model = KMeans(
                    n_clusters = cluster_count,
                    random_state=42,
                    n_init=10
                )

                model.fit(self.dataframe)

                inertia_values.append(model.inertia_)
            
            plt.figure(figsize=(8,5))

            plt.plot(
                cluster_range,
                inertia_values,
                marker="o"
            )
            plt.xlabel("Number of Clusters")
            plt.ylabel("Inertia")
            plt.title("Elbow Method")
            plt.show()

        except Exception as error:
            print(f"Error during elbow method: {error}")
    
    def silhouette_method(self):
        try:
            print("\nSilhouette Scores:\n")

            for cluster_count in range(2, 11):
                model = KMeans(
                    n_clusters=cluster_count,
                    random_state=42,
                    n_init=10
                )
                cluster_labels = model.fit_predict(
                    self.dataframe
                )

                score = silhouette_score(
                    self.dataframe,
                    cluster_labels
                )

                print(
                    f"K = {cluster_count} "
                    f"| Silhouette Score = {score:.4f}"
                )
        except Exception as error:
            print(f"Error during silhouette method: {error}")