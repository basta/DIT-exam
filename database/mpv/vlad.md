---
id: mpv_017
course: Methods of Computer Vision
tags: [VLAD, aggregation, residuals, descriptor, retrieval]
difficulty: 3
type: open
status: to_learn
---

# Question
How is the **VLAD descriptor** computed and how does it differ from BoW?

---
# Solution

## VLAD = Vector of Locally Aggregated Descriptors (Jégou et al., 2010)

### Construction
1. Train a small codebook of $K$ centroids $\{\mathbf{c}_1, \dots, \mathbf{c}_K\}$ by $k$-means on local descriptors (typically $K = 64$–$256$, far smaller than BoW vocabularies).
2. For an image with local descriptors $\mathbf{x}_1, \dots, \mathbf{x}_F$:
   - Assign each $\mathbf{x}_t$ to its nearest centroid $\mathbf{c}_{q(t)}$.
   - For each centroid $i$, **sum the residuals** of all descriptors assigned to it:
   $$
   \mathbf{v}_i = \sum_{t : q(t) = i} (\mathbf{x}_t - \mathbf{c}_i) \in \mathbb{R}^D.
   $$
3. Concatenate: $\mathbf{V} = [\mathbf{v}_1; \dots; \mathbf{v}_K] \in \mathbb{R}^{K D}$ (e.g., $K = 64, D = 128 \Rightarrow$ 8192-dim).
4. **Normalization (crucial):**
   a. **Intra-normalization** — $L_2$-normalize each block $\mathbf{v}_i$ separately (Arandjelović & Zisserman). Counters bursty features that dominate one cell.
   b. **Power-law normalization** — $v \to \text{sign}(v) |v|^\alpha$ with $\alpha \approx 0.5$ (a.k.a. **SSR** / signed square root). Reduces the effect of large components.
   c. **Global $L_2$-normalization** — final unit vector.

### Matching
Cosine similarity (dot product of $L_2$-normalized VLADs).

## Differences from BoW
| Aspect | BoW | VLAD |
|---|---|---|
| What is aggregated? | counts (0-th order) | residual vectors (1st order) |
| Vocabulary size $K$ | $10^4$–$10^6$ | $10$–$10^3$ |
| Descriptor dim | $K$ | $K D$ |
| Sparsity | very sparse | dense |
| Inverted file? | yes — efficient | usually no (dense vectors) |
| Storage per image | a few kB with index | typically compressed (PQ) to a few hundred bytes |
| Info captured | which words present | which words + how descriptors deviate from each centroid |
| Discriminability per dim | low (just counts) | high (rich residual statistics) |

## Why It Works
A BoW histogram throws away all information about *where* in the cell a descriptor landed; VLAD keeps the *mean shift* of the descriptors within each cell. Two images with similar word frequencies but different fine-grained appearance differ in VLAD but not in BoW.

## Practical Notes
- VLAD pairs naturally with **Product Quantization (PQ)** for compression to short codes (e.g., 128 bytes per image), enabling retrieval at the scale of $10^8$ images on a single machine.
- The **Fisher Vector** is a generalization: replace hard $k$-means assignment with a GMM, aggregate first **and** second order statistics relative to the GMM.
- **NetVLAD** is the differentiable, learnable counterpart used in CNN-based retrieval.

## Related Concepts
- [[BoW]]
- [[fisher-vector]]
- [[product-quantization]]
- [[NetVLAD]]
