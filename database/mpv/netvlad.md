---
id: mpv_022
course: Methods of Computer Vision
tags: [NetVLAD, learnable-pooling, CNN, retrieval]
difficulty: 4
type: open
status: to_learn
---

# Question
How does **NetVLAD** work and what is the difference with **VLAD**?

---
# Solution

## Recall: VLAD
For features $\{\mathbf{x}_t\}$ assigned hard to one of $K$ centroids:
$$
\mathbf{v}_i = \sum_{t : q(t) = i} (\mathbf{x}_t - \mathbf{c}_i), \qquad \mathbf{V} = [\mathbf{v}_1; \dots; \mathbf{v}_K] \in \mathbb{R}^{KD}.
$$
The hard assignment $q(t) = \arg\min_i \|\mathbf{x}_t - \mathbf{c}_i\|^2$ is **non-differentiable** — VLAD cannot be plugged into an end-to-end learnable model.

## NetVLAD (Arandjelović et al., 2016)
Replace the hard assignment by a **soft assignment**:
$$
\bar a_i(\mathbf{x}_t) = \frac{e^{-\alpha \|\mathbf{x}_t - \mathbf{c}_i\|^2}}{\sum_j e^{-\alpha \|\mathbf{x}_t - \mathbf{c}_j\|^2}}.
$$
Expanding the squared norms and cancelling common terms, this equals
$$
\bar a_i(\mathbf{x}_t) = \frac{e^{\mathbf{w}_i^\top \mathbf{x}_t + b_i}}{\sum_j e^{\mathbf{w}_j^\top \mathbf{x}_t + b_j}}, \quad \mathbf{w}_i = 2\alpha \mathbf{c}_i, \; b_i = -\alpha\|\mathbf{c}_i\|^2,
$$
i.e., a **softmax of a linear projection** of $\mathbf{x}_t$. The pooling becomes
$$
\mathbf{v}_i = \sum_t \bar a_i(\mathbf{x}_t) \cdot (\mathbf{x}_t - \mathbf{c}_i).
$$
Here $\{\mathbf{w}_i, b_i, \mathbf{c}_i\}$ are **free parameters** — decoupled from each other and trained end-to-end with the rest of the network. After pooling, the per-cell vectors are intra-normalized and the whole vector $L_2$-normalized exactly as in VLAD.

### Architecture
- A backbone CNN (VGG / ResNet) produces a $H \times W \times D$ feature map. Each spatial location $(h, w)$ is treated as a local descriptor $\mathbf{x}_t \in \mathbb{R}^D$.
- A **NetVLAD layer** applies a $1 \times 1$ conv (the $\mathbf{w}_i$ for soft assignment) followed by softmax, multiplies by per-location residuals, and sums spatially.
- Output: $KD$-dim global descriptor.

### Training
Trained for **place recognition / retrieval** using:
- **Weakly-supervised triplet loss** on Google Street View Time Machine: for an anchor query, positives are images taken near the same GPS within $\le 10$ m and similar viewpoint; negatives are images far away (> 25 m).
- Loss: triplet margin or **listwise (Average Precision)** loss.

## Differences from VLAD
| Aspect | VLAD | NetVLAD |
|---|---|---|
| Assignment | hard ($\arg\min$) | soft (softmax) |
| Differentiable? | no | yes |
| Centroids / weights | from $k$-means on local descriptors | learned by SGD |
| Local features | hand-crafted (SIFT / RootSIFT) | learned CNN feature map |
| Independence of $\mathbf{w}_i$ from $\mathbf{c}_i$ | tied | independent (more flexible) |
| Trainable end-to-end | no | yes (with backbone) |
| Performance | strong with hand-crafted features | state-of-the-art on place recognition |

## Variants & Successors
- **GhostVLAD:** adds "ghost" centroids that absorb noisy/uninformative features (image faces).
- **NetRVLAD:** drop residual subtraction (use $\mathbf{x}_t$ directly).
- **GeM, R-MAC, SOLAR, DELG**: alternative learnable global descriptors based on pooling rather than VLAD-style aggregation.

## Related Concepts
- [[VLAD]]
- [[soft-assignment]]
- [[triplet-loss]]
- [[place-recognition]]
