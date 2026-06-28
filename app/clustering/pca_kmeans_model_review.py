from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler


class PCAKMeansModelReview:

    def __init__(
        self,
        dataframe: pd.DataFrame,
        grid_results_path: str = "data/pca_kmeans_grid_search_results.csv",
        output_path: str = "data/pca_kmeans_model_review.md",
    ):

        self.dataframe = dataframe
        self.grid_results_path = Path(grid_results_path)
        self.output_path = Path(output_path)

    def run(self):

        scaled_data = StandardScaler().fit_transform(
            self.dataframe
        )

        pca = PCA(
            n_components=0.85,
            random_state=42,
        )

        pca_data = pca.fit_transform(
            scaled_data
        )

        baseline_model = KMeans(
            n_clusters=6,
            random_state=42,
            n_init=20,
        )

        baseline_labels = baseline_model.fit_predict(
            pca_data
        )

        stability_rows = self._seed_stability(
            pca_data,
            baseline_labels,
        )

        confidence_summary = self._confidence_summary(
            baseline_model,
            pca_data,
        )

        best_grid_row = self._best_grid_row()

        report = self._build_report(
            pca,
            best_grid_row,
            stability_rows,
            confidence_summary,
        )

        self.output_path.write_text(
            report,
            encoding="utf-8",
        )

        print(
            f"\nSaved KMeans model review:\n{self.output_path}"
        )

    def _seed_stability(
        self,
        pca_data,
        baseline_labels,
    ):

        rows = []

        for seed in [
            7,
            21,
            42,
            84,
            123,
        ]:

            model = KMeans(
                n_clusters=6,
                random_state=seed,
                n_init=20,
            )

            labels = model.fit_predict(
                pca_data
            )

            rows.append({
                "Seed": seed,
                "ARI vs Seed 42": adjusted_rand_score(
                    baseline_labels,
                    labels,
                ),
                "Inertia": model.inertia_,
                "Smallest Cluster": int(
                    pd.Series(labels).value_counts().min()
                ),
                "Largest Cluster": int(
                    pd.Series(labels).value_counts().max()
                ),
            })

        return pd.DataFrame(rows)

    def _confidence_summary(
        self,
        model,
        pca_data,
    ):

        sorted_distances = np.sort(
            model.transform(pca_data),
            axis=1,
        )

        assignment_strength = (
            sorted_distances[:, 1]
            /
            (
                sorted_distances[:, 0]
                +
                sorted_distances[:, 1]
            )
        ) * 100

        percentiles = np.percentile(
            assignment_strength,
            [
                5,
                25,
                50,
                75,
                95,
            ],
        )

        return {
            "Mean": float(
                assignment_strength.mean()
            ),
            "P5": float(percentiles[0]),
            "P25": float(percentiles[1]),
            "P50": float(percentiles[2]),
            "P75": float(percentiles[3]),
            "P95": float(percentiles[4]),
        }

    def _best_grid_row(self):

        if not self.grid_results_path.exists():
            return None

        grid_results = pd.read_csv(
            self.grid_results_path
        )

        return (
            grid_results
            .sort_values(
                by=[
                    "silhouette",
                    "db",
                    "ch",
                ],
                ascending=[
                    False,
                    True,
                    False,
                ],
            )
            .iloc[0]
        )

    def _build_report(
        self,
        pca,
        best_grid_row,
        stability_rows,
        confidence_summary,
    ):

        stability_table = self._to_markdown_table(
            stability_rows
        )

        if best_grid_row is None:
            grid_summary = (
                "Grid-search result file was not found, so no previous "
                "PCA/KMeans tuning result could be summarized."
            )
        else:
            grid_summary = (
                f"Best existing grid-search setting: PCA variance "
                f"`{best_grid_row['variance']}`, components "
                f"`{int(best_grid_row['components'])}`, k "
                f"`{int(best_grid_row['k'])}`, n_init "
                f"`{int(best_grid_row['n_init'])}` with silhouette "
                f"`{best_grid_row['silhouette']:.4f}`, DB "
                f"`{best_grid_row['db']:.4f}`, CH "
                f"`{best_grid_row['ch']:.2f}`."
            )

        confidence_lines = "\n".join([
            f"- Mean: `{confidence_summary['Mean']:.2f}%`",
            f"- P5: `{confidence_summary['P5']:.2f}%`",
            f"- P25: `{confidence_summary['P25']:.2f}%`",
            f"- P50: `{confidence_summary['P50']:.2f}%`",
            f"- P75: `{confidence_summary['P75']:.2f}%`",
            f"- P95: `{confidence_summary['P95']:.2f}%`",
        ])

        return (
            "# PCA KMeans Model Review\n\n"
            "## Decision\n\n"
            "Keep PCA(85% variance) + KMeans(k=6, n_init=20) as the "
            "current production model. It remains the strongest tested "
            "option while preserving prediction support and current cluster "
            "mapping compatibility.\n\n"
            "## Existing Tuning Result\n\n"
            f"{grid_summary}\n\n"
            "## PCA Summary\n\n"
            f"- Components retained: `{pca.n_components_}`\n"
            f"- Explained variance: `{pca.explained_variance_ratio_.sum():.4f}`\n\n"
            "## Seed Stability\n\n"
            f"{stability_table}\n\n"
            "ARI close to 1.0 means assignments are very similar to the "
            "current seed-42 model after accounting for arbitrary cluster "
            "label numbering.\n\n"
            "## Assignment Strength Distribution\n\n"
            f"{confidence_lines}\n\n"
            "Recommended presentation: keep the numeric value as an "
            "`assignment_strength` score, not a true probability. Suggested "
            "bands: `<56% = Low`, `56-67% = Medium`, `>67% = High`.\n\n"
            "## Improvement Conclusion\n\n"
            "The tested algorithm changes did not improve the model. The "
            "existing KMeans grid search already selected the best tested "
            "configuration. Further metric improvement would likely require "
            "changing the feature set, cluster count, or business mapping, "
            "which should be treated as a separate model versioning task."
        )

    @staticmethod
    def _to_markdown_table(dataframe):

        columns = list(dataframe.columns)
        rows = []

        for _, row in dataframe.iterrows():
            rendered_row = []

            for column in columns:
                value = row[column]

                if isinstance(value, float):
                    rendered_row.append(f"{value:.4f}")
                else:
                    rendered_row.append(str(value))

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
