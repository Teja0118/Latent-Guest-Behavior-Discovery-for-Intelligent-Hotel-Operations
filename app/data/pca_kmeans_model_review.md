# PCA KMeans Model Review

## Decision

Keep PCA(85% variance) + KMeans(k=6, n_init=20) as the current production model. It remains the strongest tested option while preserving prediction support and current cluster mapping compatibility.

## Existing Tuning Result

Best existing grid-search setting: PCA variance `0.85`, components `9`, k `6`, n_init `20` with silhouette `0.2341`, DB `1.4100`, CH `23832.67`.

## PCA Summary

- Components retained: `9`
- Explained variance: `0.8564`

## Seed Stability

| Seed | ARI vs Seed 42 | Inertia | Smallest Cluster | Largest Cluster |
| --- | --- | --- | --- | --- |
| 7.0000 | 0.9976 | 770448.2506 | 12728.0000 | 20562.0000 |
| 21.0000 | 0.9993 | 770448.4102 | 12744.0000 | 20589.0000 |
| 42.0000 | 1.0000 | 770448.6873 | 12751.0000 | 20586.0000 |
| 84.0000 | 0.9985 | 770449.4692 | 12739.0000 | 20595.0000 |
| 123.0000 | 0.9960 | 770448.6194 | 12695.0000 | 20528.0000 |

ARI close to 1.0 means assignments are very similar to the current seed-42 model after accounting for arbitrary cluster label numbering.

## Assignment Strength Distribution

- Mean: `61.87%`
- P5: `51.06%`
- P25: `55.84%`
- P50: `61.70%`
- P75: `67.24%`
- P95: `73.89%`

Recommended presentation: keep the numeric value as an `assignment_strength` score, not a true probability. Suggested bands: `<56% = Low`, `56-67% = Medium`, `>67% = High`.

## Improvement Conclusion

The tested algorithm changes did not improve the model. The existing KMeans grid search already selected the best tested configuration. Further metric improvement would likely require changing the feature set, cluster count, or business mapping, which should be treated as a separate model versioning task.