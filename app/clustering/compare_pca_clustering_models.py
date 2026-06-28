from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import (
    AgglomerativeClustering,
    Birch,
    HDBSCAN,
    KMeans,
    MiniBatchKMeans,
)
from sklearn.decomposition import PCA
from sklearn.metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler


class PCAClusteringComparison:

    def __init__(
        self,
        dataframe: pd.DataFrame,
        n_clusters: int = 6,
        pca_variance: float = 0.85,
        random_state: int = 42,
    ):

        self.dataframe = dataframe
        self.n_clusters = n_clusters
        self.pca_variance = pca_variance
        self.random_state = random_state

        self.scaler = StandardScaler()
        self.pca = PCA(
            n_components=pca_variance,
            random_state=random_state,
        )

    def _prepare_features(self):

        scaled_data = self.scaler.fit_transform(
            self.dataframe
        )

        pca_data = self.pca.fit_transform(
            scaled_data
        )

        self.connectivity = kneighbors_graph(
            pca_data,
            n_neighbors=20,
            include_self=False,
        )

        print(
            f"\nPCA Components Retained: "
            f"{self.pca.n_components_}"
        )

        print(
            f"Explained Variance: "
            f"{self.pca.explained_variance_ratio_.sum():.4f}"
        )

        return pca_data

    def _build_models(self):

        return [
            (
                "KMeans",
                KMeans(
                    n_clusters=self.n_clusters,
                    random_state=self.random_state,
                    n_init=20,
                ),
                "Current baseline: centroid model, supports predict.",
            ),
            (
                "Agglomerative Clustering",
                AgglomerativeClustering(
                    n_clusters=self.n_clusters,
                    connectivity=self.connectivity,
                    compute_full_tree=False,
                    linkage="ward",
                ),
                "Hierarchical structure; no native predict/probability.",
            ),
            (
                "HDBSCAN",
                HDBSCAN(
                    min_cluster_size=100,
                    min_samples=20,
                    store_centers="centroid",
                ),
                "Density model; reports membership strength for fitted samples.",
            ),
            (
                "Spectral Clustering",
                None,
                (
                    "Skipped for full 102k-row dataset: graph-based model is "
                    "computationally expensive and has no native predict method. "
                    "Evaluate separately on a fixed sample only if required."
                ),
            ),
            (
                "Birch",
                Birch(
                    n_clusters=self.n_clusters,
                    threshold=0.5,
                ),
                "Incremental CF-tree model; supports predict after fitting.",
            ),
            (
                "MiniBatch KMeans",
                MiniBatchKMeans(
                    n_clusters=self.n_clusters,
                    random_state=self.random_state,
                    n_init=20,
                    batch_size=4096,
                ),
                "Fast centroid baseline variant; supports predict.",
            ),
        ]

    def _valid_metric_data(
        self,
        pca_data,
        labels,
        model_name,
    ):

        labels = np.asarray(labels)
        notes = []

        if model_name == "HDBSCAN":
            noise_mask = labels == -1
            noise_count = int(noise_mask.sum())
            noise_pct = (noise_count / len(labels)) * 100
            notes.append(f"Noise={noise_pct:.2f}%")

            if noise_count:
                pca_data = pca_data[~noise_mask]
                labels = labels[~noise_mask]

        unique_labels = np.unique(labels)

        if len(unique_labels) < 2:
            return None, None, notes + ["Metrics unavailable: fewer than 2 clusters."]

        if len(unique_labels) >= len(labels):
            return None, None, notes + ["Metrics unavailable: every sample is isolated."]

        cluster_sizes = pd.Series(labels).value_counts().sort_index()
        smallest_cluster = int(cluster_sizes.min())
        largest_cluster = int(cluster_sizes.max())

        notes.append(
            f"Clusters={len(unique_labels)}, size range={smallest_cluster}-{largest_cluster}"
        )

        return pca_data, labels, notes

    def _evaluate_model(
        self,
        model_name,
        model,
        model_note,
        pca_data,
    ):

        print(
            f"\nTraining {model_name}...",
            flush=True,
        )

        if model is None:
            print(
                f"{model_name}: skipped.",
                flush=True,
            )

            return {
                "Model": model_name,
                "Silhouette": np.nan,
                "DB Index": np.nan,
                "CH Score": np.nan,
                "Notes": model_note,
            }

        try:
            labels = model.fit_predict(
                pca_data
            )
        except Exception as error:
            error_name = type(error).__name__
            print(
                f"{model_name} failed: {error_name}: {error}",
                flush=True,
            )

            return {
                "Model": model_name,
                "Silhouette": np.nan,
                "DB Index": np.nan,
                "CH Score": np.nan,
                "Notes": (
                    f"{model_note} Evaluation failed on full dataset: "
                    f"{error_name}: {error}"
                ),
            }

        metric_data, metric_labels, notes = self._valid_metric_data(
            pca_data,
            labels,
            model_name,
        )

        if metric_data is None:
            silhouette = np.nan
            davies_bouldin = np.nan
            calinski_harabasz = np.nan
        else:
            silhouette = silhouette_score(
                metric_data,
                metric_labels,
            )

            davies_bouldin = davies_bouldin_score(
                metric_data,
                metric_labels,
            )

            calinski_harabasz = calinski_harabasz_score(
                metric_data,
                metric_labels,
            )

        confidence_note = self._confidence_note(
            model_name,
            model,
        )

        result = {
            "Model": model_name,
            "Silhouette": silhouette,
            "DB Index": davies_bouldin,
            "CH Score": calinski_harabasz,
            "Notes": " ".join([model_note, confidence_note] + notes),
        }

        print(
            f"{model_name}: "
            f"Silhouette={silhouette:.4f}, "
            f"DB={davies_bouldin:.4f}, "
            f"CH={calinski_harabasz:.2f}",
            flush=True,
        )

        return result

    def _confidence_note(
        self,
        model_name,
        model,
    ):

        if model_name in {
            "KMeans",
            "MiniBatch KMeans",
        }:
            return (
                "Confidence: distance-margin or calibrated soft assignment "
                "from centroid distances; not a true probability."
            )

        if model_name == "Birch":
            return (
                "Confidence: nearest-subcluster distance can be used as a "
                "relative confidence; not a probability."
            )

        if model_name == "HDBSCAN" and hasattr(model, "probabilities_"):
            probabilities = model.probabilities_
            assigned_probabilities = probabilities[probabilities > 0]

            if len(assigned_probabilities):
                median_probability = float(
                    np.median(assigned_probabilities)
                )
                return (
                    "Confidence: native membership strength available for "
                    f"fitted samples, median={median_probability:.3f}."
                )

            return (
                "Confidence: native membership strength available, but no "
                "assigned non-noise samples were found."
            )

        return (
            "Confidence: no native probability/predict interface for new guests."
        )

    def run(self):

        pca_data = self._prepare_features()

        results = []

        for model_name, model, model_note in self._build_models():
            result = self._evaluate_model(
                model_name,
                model,
                model_note,
                pca_data,
            )
            results.append(result)

        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values(
            by=["Silhouette", "DB Index", "CH Score"],
            ascending=[False, True, False],
            na_position="last",
        )

        return results_df

    @staticmethod
    def save_report(
        results_df,
        output_dir,
    ):

        output_dir = Path(output_dir)
        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        csv_path = output_dir / "pca_clustering_model_comparison.csv"
        markdown_path = output_dir / "pca_clustering_model_comparison.md"

        results_df.to_csv(
            csv_path,
            index=False,
        )

        markdown_table = PCAClusteringComparison._to_markdown_table(
            results_df
        )

        recommendation = PCAClusteringComparison._build_recommendation(
            results_df
        )

        markdown_path.write_text(
            "# PCA Clustering Model Comparison\n\n"
            "Pipeline: Feature Engineering -> StandardScaler -> "
            "PCA(85% variance) -> Clustering Model\n\n"
            f"{markdown_table}\n\n"
            "## Confidence Score Recommendation\n\n"
            f"{recommendation}\n",
            encoding="utf-8",
        )

        print(
            "\nSaved comparison outputs:\n"
            f"{csv_path}\n"
            f"{markdown_path}",
            flush=True,
        )

    @staticmethod
    def _build_recommendation(results_df):

        best_row = results_df.iloc[0]

        return (
            "Use clustering confidence as an honest assignment-strength score, "
            "not as supervised prediction probability. For KMeans-style models, "
            "the most defensible production score is a centroid distance margin: "
            "`second_nearest_distance / (nearest_distance + second_nearest_distance)`, "
            "optionally reported with a clear label such as `cluster_assignment_strength`. "
            "Do not rescale it into 90-99% confidence. If HDBSCAN wins on metrics "
            "and cluster stability, its native `probabilities_` value is more "
            "meaningful for fitted-sample membership strength, but sklearn HDBSCAN "
            "does not provide the same simple new-sample prediction workflow as "
            "KMeans. Based on the current metric sort, the leading offline model is "
            f"{best_row['Model']}."
        )

    @staticmethod
    def _to_markdown_table(results_df):

        columns = [
            "Model",
            "Silhouette",
            "DB Index",
            "CH Score",
            "Notes",
        ]

        rows = []

        for _, row in results_df[columns].iterrows():
            rendered_row = []

            for column in columns:
                value = row[column]

                if isinstance(value, float):
                    if np.isnan(value):
                        rendered_row.append("N/A")
                    else:
                        rendered_row.append(f"{value:.4f}")
                else:
                    rendered_row.append(str(value).replace("|", "/"))

            rows.append(rendered_row)

        header = "| " + " | ".join(columns) + " |"
        separator = "| " + " | ".join(["---"] * len(columns)) + " |"
        body = [
            "| " + " | ".join(row) + " |"
            for row in rows
        ]

        return "\n".join(
            [header, separator] + body
        )
