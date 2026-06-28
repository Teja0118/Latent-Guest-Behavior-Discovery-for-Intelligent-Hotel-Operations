# PCA Clustering Model Comparison

Pipeline: Feature Engineering -> StandardScaler -> PCA(85% variance) -> Clustering Model

| Model | Silhouette | DB Index | CH Score | Notes |
| --- | --- | --- | --- | --- |
| KMeans | 0.2341 | 1.4100 | 23832.6696 | Current baseline: centroid model, supports predict. Confidence: distance-margin or calibrated soft assignment from centroid distances; not a true probability. Clusters=6, size range=12751-20586 |
| MiniBatch KMeans | 0.1858 | 1.7575 | 19745.4036 | Fast centroid baseline variant; supports predict. Confidence: distance-margin or calibrated soft assignment from centroid distances; not a true probability. Clusters=6, size range=7325-29316 |
| Agglomerative Clustering | 0.1669 | 1.6781 | 18116.9030 | Hierarchical structure; no native predict/probability. Confidence: no native probability/predict interface for new guests. Clusters=6, size range=8993-23983 |
| HDBSCAN | 0.0328 | 2.5742 | 2577.8438 | Density model; reports membership strength for fitted samples. Confidence: native membership strength available for fitted samples, median=0.734. Noise=11.35% Clusters=4, size range=239-72420 |
| Spectral Clustering | N/A | N/A | N/A | Skipped for full 102k-row dataset: graph-based model is computationally expensive and has no native predict method. Evaluate separately on a fixed sample only if required. |
| Birch | N/A | N/A | N/A | Incremental CF-tree model; supports predict after fitting. Evaluation failed on full dataset: MemoryError: unable to allocate array data. |

## Confidence Score Recommendation

Use clustering confidence as an honest assignment-strength score, not as supervised prediction probability. For KMeans-style models, the most defensible production score is a centroid distance margin: `second_nearest_distance / (nearest_distance + second_nearest_distance)`, optionally reported with a clear label such as `cluster_assignment_strength`. Do not rescale it into 90-99% confidence. If HDBSCAN wins on metrics and cluster stability, its native `probabilities_` value is more meaningful for fitted-sample membership strength, but sklearn HDBSCAN does not provide the same simple new-sample prediction workflow as KMeans. Based on the current metric sort, the leading offline model is KMeans.
