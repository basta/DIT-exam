---
id: mpv_012
course: Methods of Computer Vision
tags: [matching, ratio-test, mutual-nn, ransac, correspondences]
difficulty: 3
type: open
status: to_learn
---

# Question
How are local descriptors matched? What are the ways of filtering out **unreliable correspondences**?

---
# Solution

## Step 1: Nearest-Neighbor Matching
For each descriptor $\mathbf{x}_i$ in image A, find the most similar descriptor in image B (nearest neighbor under Euclidean / Hamming distance):
$$
j^*(i) = \arg\min_j \|\mathbf{x}_i - \mathbf{y}_j\|.
$$
Done with:
- **Brute force** ($O(N M)$, fine for small sets).
- **Approximate nearest neighbors:** KD-trees / FLANN (low dims), product quantization, HNSW for high-dim/large scale.

## Step 2: Filtering Unreliable Correspondences

### 2.1 Distance Threshold
Reject matches with $\|\mathbf{x}_i - \mathbf{y}_{j^*}\| > \tau$. Simple but a global $\tau$ is hard to tune and depends on the data.

### 2.2 Lowe's Ratio Test (Most Important)
Let $d_1, d_2$ be the distances to the 1st and 2nd nearest neighbor. Keep the match only if
$$
\frac{d_1}{d_2} < r, \quad r \approx 0.7\text{-}0.8.
$$
**Idea:** a *correct* match is much closer than the second-best one in descriptor space; an *ambiguous* match has $d_1 \approx d_2$. This filter alone removes most false matches (typical: 80–90 % of all tentative matches are dropped, but the surviving ones are highly reliable).

### 2.3 Mutual Nearest Neighbors (Cross-Check)
$i$ and $j$ are kept only if $j = \text{NN}(i)$ in B and $i = \text{NN}(j)$ in A. Symmetric and parameter-free; often combined with the ratio test.

### 2.4 First/Second Region Verification
Use the ratio test but require the 2nd-nearest neighbor to come from a *different image* than the 1st (for retrieval pipelines where many DB images are searched).

### 2.5 Geometric (Spatial) Verification
After descriptor-only matching, fit a geometric model with **RANSAC**:
- Homography $H$ (planar / rotation-only),
- Fundamental $F$ or essential $E$ matrix (general 3D scene),
- Affine model.

Inliers are the final correspondences; everything else is discarded. Robust variants: LO-RANSAC, MAGSAC, DEGENSAC, PROSAC (uses match quality as prior).

### 2.6 Learned Outlier Rejection
- **PointCN / OANet / SuperGlue / LightGlue**: learn to classify tentative correspondences as inliers/outliers using context (positions, descriptors).
- Replaces or augments the ratio test and pre-RANSAC filtering.

### 2.7 Domain-Specific Filters
- **Scale and orientation consistency:** require matches to share a consistent global scale ratio / rotation (in SIFT each match comes with $(\sigma, \theta)$).
- **Spatial reciprocity:** matches whose 4 nearest neighbors in the image plane also match → "spatial coherence" filters.

## Final Pipeline
$$
\underbrace{\text{NN search}}_{\text{tentative matches}} \;\to\; \underbrace{\text{ratio test + mutual NN}}_{\text{good matches}} \;\to\; \underbrace{\text{RANSAC}}_{\text{geometrically verified inliers}}.
$$

## Related Concepts
- [[ratio-test]]
- [[RANSAC]]
- [[FLANN]]
- [[SuperGlue]]
