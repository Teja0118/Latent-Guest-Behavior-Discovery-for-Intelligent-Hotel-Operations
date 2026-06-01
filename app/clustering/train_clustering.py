import joblib
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class ClusteringTrainer:

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.model = None

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
    
    def silhouette_analysis(self):
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
        
    def train_final_model(self, n_clusters=5):
        try:
            self.model = KMeans(
                n_clusters=n_clusters,
                random_state=42,
                n_init=10
            )

            cluster_labels = self.model.fit_predict(
                self.dataframe
            )

            print(
                f"\nFinal KMeans model trained "
                f"successfully with K = {n_clusters}"
            )

            return cluster_labels
        
        except Exception as error:
            print(f"Error while training final model: {error}")

    def save_model(self, output_path):
        try:
            joblib.dump(
                self.model,
                output_path
            )

            print(
                f"\nClustering model saved successfully at: \n"
                f"{output_path}"
            )
        
        except Exception as error:
            print(f"Error while saving model: {error}")
