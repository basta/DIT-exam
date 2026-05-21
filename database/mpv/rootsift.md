---
id: mpv_010
course: Methods of Computer Vision
tags: [RootSIFT, descriptor, hellinger-kernel, normalization]
difficulty: 2
type: open
status: to_learn
---

# Question
**RootSIFT descriptor.** Describe the algorithm.

---
# Solution

## Motivation
SIFT descriptors are non-negative histograms. Comparing histograms with Euclidean distance can be suboptimal — the **Hellinger / Bhattacharyya** kernel is empirically better suited to histograms (Arandjelović & Zisserman, 2012). RootSIFT is a *post-processing* of SIFT such that **Euclidean distance on RootSIFT equals Hellinger distance on SIFT**, at zero implementation cost.

## Derivation
Let $\mathbf{x}, \mathbf{y}$ be SIFT vectors that are $L_1$-normalized: $\sum_i x_i = 1$, $x_i \ge 0$. The Hellinger kernel between them is
$$
H(\mathbf{x}, \mathbf{y}) = \sum_i \sqrt{x_i y_i}.
$$
Define $\tilde{x}_i = \sqrt{x_i}$. Then
$$
H(\mathbf{x}, \mathbf{y}) = \langle \tilde{\mathbf{x}}, \tilde{\mathbf{y}} \rangle, \qquad \|\tilde{\mathbf{x}}\|_2 = 1.
$$
So squaring is a feature map that turns Hellinger into a linear (dot-product) kernel; equivalently, Euclidean distance on $\tilde{\mathbf{x}}$ becomes
$$
\|\tilde{\mathbf{x}} - \tilde{\mathbf{y}}\|_2^2 = 2 - 2 \langle \tilde{\mathbf{x}}, \tilde{\mathbf{y}} \rangle = 2 - 2 H(\mathbf{x}, \mathbf{y}).
$$

## Algorithm
Given a SIFT descriptor $\mathbf{d}$:
1. **$L_1$-normalize:** $\mathbf{d} \leftarrow \mathbf{d} / \|\mathbf{d}\|_1$.
2. **Element-wise square root:** $\mathbf{d}_i \leftarrow \sqrt{\mathbf{d}_i}$ (the result is automatically $L_2$-normalized: $\sum_i d_i = 1$ implies $\sum_i (\sqrt{d_i})^2 = 1$).

The result is the **RootSIFT** descriptor. It is the same dimension (128) as SIFT, can be substituted everywhere SIFT is used, and can be matched with standard Euclidean nearest neighbor / FLANN / ANN structures.

## Notes
- Two extra lines of code; consistently improves matching and retrieval ($1$–$5$ mAP points) over plain SIFT.
- The same idea applies to other histogram-like descriptors (e.g., HOG, BoW vectors → Hellinger normalization is common in retrieval).
- Sign issue does not arise because SIFT entries are non-negative.

## Related Concepts
- [[SIFT]]
- [[hellinger-kernel]]
- [[bhattacharyya]]
- [[descriptor-normalization]]
