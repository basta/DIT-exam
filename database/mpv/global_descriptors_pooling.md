---
id: mpv_023
course: Methods of Computer Vision
tags: [SPoC, MAC, GeM, global-descriptor, CNN, pooling]
difficulty: 4
type: open
status: to_learn
---

# Question
How are global image descriptors obtained using CNNs and **SPoC, MAC, GeM**? What is the relation between **GeM** and the others? Which of these representations are **translation invariant** and why? Describe one CNN architecture for extracting global descriptors that is **not** translation invariant. Why isn't it?

---
# Solution

## Setup
A CNN backbone (e.g., ResNet-50 truncated before the FC layer) produces a feature map
$$
\mathbf{X} \in \mathbb{R}^{H \times W \times D},
$$
i.e., $D$ channels, each a $H \times W$ activation map. Each channel $k$ is a 2D map $\mathbf{X}_k$. We pool over the spatial dimensions to obtain a $D$-dim global descriptor $\mathbf{f}$ with $f_k = \text{pool}(\mathbf{X}_k)$.

## SPoC — Sum-Pooled Convolutional Features (Babenko & Lempitsky, 2015)
$$
f_k^{\text{SPoC}} = \sum_{h, w} \mathbf{X}_k(h, w).
$$
Plain spatial sum. Often followed by a center-prior weighting (Gaussian-weighted sum to upweight central pixels) and $L_2$ + PCA-whitening.

## MAC — Maximum Activations of Convolutions (Razavian / Tolias et al.)
$$
f_k^{\text{MAC}} = \max_{h, w} \mathbf{X}_k(h, w).
$$
The most active spatial location per channel. Captures "the strongest evidence" for each filter's pattern anywhere in the image.

## GeM — Generalized Mean Pooling (Radenović, Tolias, Chum, 2018)
$$
f_k^{\text{GeM}} = \left( \frac{1}{HW} \sum_{h, w} \mathbf{X}_k(h, w)^{p} \right)^{1/p}, \quad p \ge 1.
$$
A *generalized mean* with exponent $p$. $p$ is a learnable scalar (often per-channel or shared). After pooling: $L_2$-normalize + (optional) PCA whitening.

## Relation Between Them
GeM **interpolates** the other two:
- $p = 1$ ⇒ arithmetic mean → equivalent to SPoC (up to a constant $\frac{1}{HW}$).
- $p \to \infty$ ⇒ max → MAC.
- $p \approx 3$ (typical learned value) is a soft-max that emphasises strong responses but does not collapse to a single one.

So SPoC and MAC are the two **endpoints** and GeM is the smooth one-parameter family connecting them. Because $p$ is trainable, GeM adapts the trade-off per task.

## Translation Invariance
"Translation invariance" here means: if we shift the input image, the global descriptor does not change (as long as the relevant content stays in the field of view; we ignore border effects).

The CNN feature map $\mathbf{X}$ is **translation equivariant** (a shift in input ⇒ a shift in $\mathbf{X}$). A pooling operation that is invariant to spatial permutation makes the descriptor translation invariant:
- **MAC** — max over spatial positions is invariant to any permutation, hence translation invariant.
- **SPoC** — sum over spatial positions, also permutation invariant ⇒ translation invariant. **However**, if SPoC is used with center-prior weighting, the center weights destroy translation invariance (positions are weighted differently).
- **GeM** — $\left(\sum_{h, w} \mathbf{X}_k(h, w)^p\right)^{1/p}$ is a symmetric function of the positions ⇒ translation invariant. The learnable $p$ does not affect this.

All three are translation invariant (modulo boundary effects from convolution and pooling stride).

## A Global Descriptor That Is **Not** Translation Invariant
**R-MAC** (Regional MAC) without aggregation, or any descriptor based on a **fixed spatial grid** of pooling, e.g., **GeM with spatial pyramid (e.g., 2×2 cells) where the per-cell descriptors are concatenated**. Concretely, a CNN that ends with a **fully connected layer over a flattened feature map** (e.g., AlexNet's `fc6`, or the "Neural Codes" of Babenko et al. 2014):
$$
\mathbf{f} = W \cdot \text{vec}(\mathbf{X}) + \mathbf{b}.
$$
This is **not translation invariant** because:
- $\text{vec}(\mathbf{X})$ uses the *position* of each feature explicitly.
- A horizontal shift of the input shifts the feature map, but $W$ multiplies positions by different weights — so the resulting descriptor changes.

The same applies to NetVLAD if the soft-assignment is followed by **spatial weighting**, and to **R-MAC** with regional sums concatenated (the order/position of regions is part of the representation).

## Summary
- SPoC / MAC / GeM all pool spatially → translation invariant (subject to boundary effects).
- GeM unifies them via a learnable exponent $p$.
- Any descriptor that keeps spatial position (FC layers over flattened features, R-MAC concatenation) is **not** translation invariant.

## Related Concepts
- [[GeM]]
- [[MAC]]
- [[R-MAC]]
- [[translation-equivariance]]
- [[PCA-whitening]]
