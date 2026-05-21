---
id: mpv_020
course: Methods of Computer Vision
tags: [retrieval, RANSAC, zoom-in, sub-image-search]
difficulty: 4
type: open
status: to_learn
---

# Question
How can retrieval and RANSAC be used to perform **zoom-in** operation given a query image and a large dataset of images? How does the first retrieval stage (before re-ranking with RANSAC) differ from the standard retrieval with BoW? Why is this modification necessary?

---
# Solution

## Zoom-in Problem
Given a query image $q$ depicting (possibly) a small detail of a scene, find database images that contain the same scene but at *higher resolution* / closer view. The matching region in the database image is small compared with the full image — most of the database image is irrelevant to the query.

## Why Standard BoW Retrieval Fails
- Standard BoW similarity uses the **global** descriptor of the database image: counts of all visual words in $d$.
- If the relevant region in $d$ is only e.g. 5 % of the image, its visual words are diluted by the visual words of the rest of $d$, and the cosine similarity is dominated by the noisy / non-matching majority.
- Consequence: the relevant database images get **low scores** and are missed in the top-$k$.

## Modified First Stage (BoW Retrieval Adapted for Zoom-in)
The fix is to bias the retrieval toward images where the **query's** visual words concentrate, not where the *database* image's visual words match. Concretely:

- **Use a similarity that does not penalize "extra" words in the database image.**
- One common form (Mikulík / Chum / Matas): score by the **intersection / asymmetric** measure
$$
s(q, d) = \sum_i \min(h_q^{(i)}, h_d^{(i)}) \cdot \text{idf}(i)^2,
$$
or the asymmetric dot product without re-normalizing $d$ by $\|h_d\|$:
$$
s(q, d) = \sum_i h_q^{(i)} \, h_d^{(i)} \, \text{idf}(i)^2 / \|h_q\|,
$$
- Effectively this is an **asymmetric similarity** that normalizes only by the query, not the candidate. The database image is allowed to be much larger — its extra content does not subtract from the score.
- Equivalent intuition: we are asking "*how well does the query appear inside $d$?*", not "*how similar is the global content of $q$ and $d$?*".

## Re-ranking with RANSAC
After getting a short list of candidates, run RANSAC (or fast spatial verification) on tentative correspondences (BoW + same-word matches; HE optional). The model fit is typically a **similarity** or **affine** transform. The inlier set yields:
1. A **localized region** in $d$ corresponding to $q$ (the bounding box of the inlier database keypoints).
2. A **transform** (scale ratio + translation + rotation) — which is essentially the zoom factor and position.

The re-ranked score is the number of geometrically consistent inliers.

## Why the Modification is Necessary
- BoW cosine **penalizes** images for having content beyond the matched region (denominator $\|h_d\|$ grows). This makes images that contain the query as a *sub-region* score poorly compared to small images depicting only that region.
- The asymmetric / intersection score makes the retrieval *partial-matching aware*: a database image is rewarded for **containing** the query, regardless of how much extra content it has.
- Without this modification, the relevant images would not even survive into the short list — RANSAC re-ranking cannot recover what was already filtered out.

## Pipeline Summary
1. **BoW asymmetric / intersection retrieval** → top-$N$ candidates (containing the query's words).
2. **Spatial verification (RANSAC)** on each candidate to localize and confirm.
3. **Output:** ranked list with bounding boxes / cropped close-ups.

## Related Concepts
- [[spatial-verification]]
- [[query-expansion]]
- [[asymmetric-similarity]]
- [[BoW]]
