---
id: mpv_019
course: Methods of Computer Vision
tags: [spatial-verification, RANSAC, BoW, re-ranking, retrieval]
difficulty: 3
type: open
status: to_learn
---

# Question
How is **spatial verification** used to improve retrieval performance? How are tentative correspondences obtained with the BoW approach? What is the image-to-image similarity measure with spatial verification and why is this better than the BoW similarity?

---
# Solution

## Why Spatial Verification?
BoW similarity is **order-less**: it counts how many visual words appear, ignoring the geometric arrangement. Two images may share many visual words by accident (repetitive textures, common patterns), inflating their score. Spatial verification re-ranks the top BoW results by checking whether the matching features form a **geometrically consistent** configuration.

## Tentative Correspondences from BoW
With BoW, **features assigned to the same visual word** in the query and a database image become tentative correspondences:
- For each query feature $q$ in word $w$, every database feature $p$ in the same word (in a candidate image) yields a correspondence $(q, p)$.
- This can produce many spurious matches (especially for high-frequency words → idf-based pre-filtering or "stop-list" of the most frequent words is applied).
- Each feature has known position, scale, and orientation; this metadata enables fitting geometric models.

Optionally tightened by:
- **Hamming Embedding (HE):** within each visual word, accept the correspondence only if the (short) binary codes of the residuals are close in Hamming distance.
- **Single-link** within a word — keep only feature pairs whose descriptors are mutual nearest neighbors among features assigned to that word.

## Geometric Model Fitting
RANSAC (or a faster deterministic variant for retrieval — *Fast Spatial Verification* of Philbin et al., 2007) fits, typically:
- A **5-DOF affine** (or similarity) transformation between the two images from a *single* correspondence (since each feature carries scale + orientation a single match defines a similarity transform: 4 DOF).
- Or a homography with the usual 4-point RANSAC.

For each hypothesis, count inliers — correspondences whose predicted location is within $\epsilon$ of the actual.

## Re-Ranking
Re-rank the top $N$ (e.g., 200–1000) BoW candidates by their inlier count after RANSAC. The top of the new ranking is much cleaner. Often the inlier set is also used for **query expansion**: average the verified inlier descriptors with the query and re-issue the query.

## Spatially-Verified Similarity
The post-verification score can be:
$$
s_{\text{SV}}(q, d) = \#\{\text{inliers}(q, d)\},
$$
or a normalized variant:
$$
s_{\text{SV}}(q, d) = \frac{\#\text{inliers}(q, d)}{\sqrt{F_q F_d}},
$$
or the BoW cosine score evaluated only on inlier matches (tf-idf weighted).

## Why It Beats BoW
- **Suppresses random co-occurrences:** spatially inconsistent matches do not survive RANSAC, so common-but-random visual words contribute nothing.
- **Boosts true positives:** images of the same scene have many geometrically consistent matches → very high inlier counts dominate the score.
- Removes the impact of **repetitive textures and bursty features** which inflate BoW dot products without indicating a true match.
- Provides a **geometric transform** as a by-product, useful for downstream tasks (localization, zoom-in, mosaicking).

Limitations:
- Only feasible for a short list (RANSAC is expensive per image), hence it is a *re-ranking* stage, not a primary index.
- Needs per-feature metadata stored in the index → larger memory footprint than vanilla BoW.

## Related Concepts
- [[RANSAC]]
- [[fast-spatial-verification]]
- [[query-expansion]]
- [[hamming-embedding]]
