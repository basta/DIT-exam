---
id: mpv_018
course: Methods of Computer Vision
tags: [SMK, selective-match-kernel, BoW, retrieval]
difficulty: 4
type: open
status: to_learn
---

# Question
How does the **SMK** approach work and how does it extend the BoW approach? How does SMK differ from the BoW approach? Discuss advantages, drawbacks, memory, speed, performance.

---
# Solution

## Selective Match Kernels (Tolias, Avrithis, Jégou, 2013)
SMK unifies and extends BoW, VLAD and **Hamming Embedding** as instances of a **match kernel**:
$$
K(\mathcal{X}, \mathcal{Y}) = \gamma(\mathcal{X}) \gamma(\mathcal{Y}) \sum_{c=1}^{K} \sum_{\substack{x \in \mathcal{X}_c \\ y \in \mathcal{Y}_c}} k(\hat r(x), \hat r(y)),
$$
where the descriptors are first quantized into cells indexed by $c$ (the visual word), $\hat r(\cdot)$ is the **residual** $\mathbf{x} - \mathbf{c}_c$ normalized to unit length within the cell, and $k(\cdot, \cdot)$ is a *selective* kernel.

### Selectivity
$$
k(a, b) = \sigma_\alpha\!\big( \langle a, b \rangle \big), \quad \sigma_\alpha(u) = \begin{cases} \text{sign}(u) |u|^\alpha, & u \ge \tau, \\ 0, & u < \tau. \end{cases}
$$
- Pairs of features whose **normalized residuals** have cosine similarity below threshold $\tau$ contribute **zero** (down-weighting weakly matching pairs).
- For pairs above threshold, the contribution is raised to a power $\alpha$ — strongly emphasizing close matches and damping borderline ones.

This is the *selective* part: only "good" feature-to-feature similarities count.

### Aggregated SMK (ASMK)
Replace the cell-wise *sum* of residuals by the **mean** (or normalized sum) of residuals **before** computing the kernel:
$$
R_c(\mathcal{X}) = \widehat{\sum_{x \in \mathcal{X}_c} \hat r(x)}.
$$
Then $K \propto \sum_c \sigma_\alpha(\langle R_c(\mathcal X), R_c(\mathcal Y) \rangle)$. This corresponds to a per-cell VLAD-like signature with a selective kernel on top, and dramatically reduces memory (one residual per (image, cell) instead of one per feature).

## Relation to BoW
- **BoW** corresponds to $k \equiv 1$ inside each cell and no residual information — it just counts co-occurrences.
- **SMK** keeps an inverted-file-like structure indexed by visual word but, inside each cell, scores feature pairs by their normalized residual similarity, **selectively** discarding low-quality pairs.
- **VLAD/Fisher** is a special case with $\alpha = 1$ and no selectivity ($\tau = -\infty$).

## Differences and Trade-offs
| Aspect | BoW | SMK | ASMK |
|---|---|---|---|
| Per-feature cost in index | small | descriptor residual stored per feature | aggregated residual per cell, per image |
| Memory | small | high (each feature carries its residual) | moderate |
| Selectivity | none | yes | yes |
| Retrieval quality | baseline | best | nearly as good as SMK, far less memory |
| Compatible with inverted file | yes | yes | yes |
| Compatible with Hamming Embedding | possible | yes — natural fit | yes |

## Advantages
- **Significantly better mAP** than BoW at the same codebook size, because individual feature-to-feature similarities (not just co-occurrence) are used.
- Unified framework: BoW, HE, VLAD all derived as special cases.
- ASMK has BoW-like storage cost but matches the quality of dense aggregation.

## Drawbacks
- Plain SMK is **memory-heavy**: each indexed feature carries a residual vector (or its binary code). Mitigated by ASMK and by binary residual codes.
- More parameters to tune ($\alpha, \tau$, codebook size, residual normalization).
- Implementation more complex than vanilla BoW.

## Speed
- Same asymptotic structure as BoW with inverted file (touch only posting lists of query words).
- ASMK is essentially as fast as BoW; SMK is somewhat slower due to per-pair kernel evaluation but still suitable for large-scale retrieval.

## Performance
- On Oxford / Paris benchmarks SMK / ASMK improved mAP by ~10 points over plain BoW (e.g., from ~0.6 to ~0.7+), and were the leading approach for SIFT-based retrieval before the CNN era.

## Related Concepts
- [[hamming-embedding]]
- [[VLAD]]
- [[ASMK]]
- [[inverted-file]]
