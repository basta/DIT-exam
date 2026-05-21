---
id: mpv_026
course: Methods of Computer Vision
tags: [SimCLR, self-supervised, contrastive, augmentation]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the **SimCLR** approach for self-supervised learning. What happens if you train it only using **positive pairs**?

---
# Solution

## SimCLR (Chen et al., 2020)

### Pipeline
1. **Image augmentations.** Pick a data-augmentation distribution $\mathcal{T}$ (random crop + resize, color jitter, random Gaussian blur, random horizontal flip, sometimes random gray-scale). The two strongest "ingredients" are random cropping and color jitter.
2. **Two views.** For each image $\mathbf{x}_i$ in a batch of $N$, sample two augmentations $t, t' \sim \mathcal{T}$ to obtain $\tilde{\mathbf{x}}_i = t(\mathbf{x}_i)$ and $\tilde{\mathbf{x}}_i' = t'(\mathbf{x}_i)$. The batch becomes $2N$ images.
3. **Encoder.** A backbone CNN $f$ (e.g., ResNet-50) maps each augmented view to a feature $\mathbf{h}_i = f(\tilde{\mathbf{x}}_i)$.
4. **Projection head.** A small MLP $g$ (e.g., 2 layers + ReLU) maps $\mathbf{h}_i$ to $\mathbf{z}_i = g(\mathbf{h}_i)$, $L_2$-normalized. The projection head is **only used during pretraining** — downstream tasks use $\mathbf{h}$.
5. **Contrastive loss (NT-Xent).** Treat the two views of the same image as **positives** and all other views in the batch as **negatives**:
$$
\ell_{i, j} = -\log \frac{\exp(\langle \mathbf{z}_i, \mathbf{z}_j \rangle / \tau)}{\sum_{k=1, k \ne i}^{2N} \exp(\langle \mathbf{z}_i, \mathbf{z}_k \rangle / \tau)},
$$
where $(i, j)$ is a positive pair. The total loss is the average over all positive pairs:
$$
\mathcal{L} = \frac{1}{2N} \sum_{(i, j) \text{ pos}} \ell_{i, j} + \ell_{j, i}.
$$
Temperature $\tau$ (e.g., 0.1) sharpens the softmax.

### Why It Works
- The encoder learns features that are **invariant** to the chosen augmentations (because positive pairs are forced together) but **discriminative** between different images (because of the negative term).
- Large batches (1024–8192) provide many negatives → strong contrastive signal.
- The projection head decouples the *training objective* representation from the *downstream* representation, which empirically helps.

### Key Design Choices
- Strong color augmentation is essential — without it, the network solves the task by color statistics alone.
- Long training (hundreds of epochs).
- High learning rate (LARS optimizer).
- The non-linear projection head improves linear-probe accuracy by ~10 points vs. no head.

## What If Only Positive Pairs Are Used?
Drop the contrastive (negative) term:
$$
\mathcal{L}_{\text{pos-only}} = -\sum_{(i, j) \text{ pos}} \langle \mathbf{z}_i, \mathbf{z}_j \rangle, \quad \text{or} \quad \|\mathbf{z}_i - \mathbf{z}_j\|_2^2.
$$
This is minimized trivially by making **all features identical** — the **representation collapse** problem. Encoder maps every input to the same point in feature space; the loss is 0 but the representation is useless.

Negative pairs (or some other repulsion mechanism) are **essential** to prevent this trivial minimum.

### Workarounds That Use Only Positives
Several self-supervised methods *do* train only on positives but avoid collapse through architectural / algorithmic tricks:
- **BYOL** (Grill et al., 2020): two networks (online + EMA target) and a predictor head; the target is detached, breaking the symmetry that would allow collapse. Empirically does not collapse.
- **SimSiam** (Chen & He, 2021): like BYOL but without the EMA target — a predictor + `stop-gradient` is enough.
- **Barlow Twins / VICReg:** add explicit **variance / decorrelation** regularizers across feature dimensions to force the network to use all dimensions and prevent collapse.

So: in plain SimCLR (no extra tricks), removing negatives causes **trivial collapse** to a constant representation. Modern positive-only methods avoid this only because of carefully designed asymmetries or variance regularizers.

## Related Concepts
- [[NT-Xent]]
- [[BYOL]]
- [[SimSiam]]
- [[representation-collapse]]
- [[InfoNCE]]
