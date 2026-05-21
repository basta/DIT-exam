---
id: mpv_024
course: Methods of Computer Vision
tags: [contrastive-loss, triplet-loss, hard-negatives, metric-learning]
difficulty: 3
type: open
status: to_learn
---

# Question
How do the **contrastive** and **triplet** loss work? What is the role of the **margin**? What are **hard negatives** and why are they so important?

---
# Solution

## Contrastive Loss (Pair-wise)
For a pair $(\mathbf{x}_i, \mathbf{x}_j)$ with label $y_{ij} \in \{0, 1\}$ (1 = positive / same identity, 0 = negative / different):
$$
\mathcal{L}_{\text{contr}} = y_{ij} \, d_{ij}^2 + (1 - y_{ij}) \, \max(0, m - d_{ij})^2,
$$
where $d_{ij} = \|\mathbf{f}(\mathbf{x}_i) - \mathbf{f}(\mathbf{x}_j)\|_2$ and $m > 0$ is the **margin**.

- Positive pairs are pulled together (distance → 0).
- Negative pairs are pushed apart **only if** their distance is below the margin $m$. Negatives already at distance $\ge m$ contribute zero loss and are ignored.

## Triplet Loss (Anchor / Positive / Negative)
For a triplet $(a, p, n)$ where $a$ and $p$ are same-class, $a$ and $n$ are different-class:
$$
\mathcal{L}_{\text{tri}} = \max\big(0, \; d_{ap}^2 - d_{an}^2 + m\big).
$$
The loss is zero when the **negative is farther than the positive by at least margin $m$**:
$$
d_{an} \ge d_{ap} + m.
$$
Otherwise it pushes negatives away from the anchor and pulls positives in.

Triplet loss compares **relative distances**: it does not enforce any absolute scale (a uniform stretching of the embedding does not change the loss until the margin is hit). This is one reason it is often used together with $L_2$-normalization of the embedding (placing everything on the unit hypersphere).

## Role of the Margin $m$
- Without a margin, the loss could be minimized by making all features identical (collapse) — the trivial solution would already satisfy the inequalities.
- The margin enforces a **strict separation** between positive and negative pairs and creates a "buffer zone": once a negative is far enough, no further gradient is wasted on it.
- Too small $m$ → loss is satisfied too easily → underfitting, embeddings collapse close together.
- Too large $m$ → loss is almost never zero → gradients become noisy / hard to train; possible divergence.
- For normalized embeddings, common values are $m \in [0.1, 0.5]$.

## Hard Negatives
A **hard negative** is one whose embedding is *closer to the anchor* than the positive (or barely outside the margin):
$$
d_{an} < d_{ap} + m.
$$
"Hard" = currently violating the margin = currently producing a non-zero gradient.

Other categories:
- **Easy negative:** already far enough ($d_{an} \gg d_{ap} + m$). Contributes zero loss → useless gradient.
- **Semi-hard negative:** $d_{ap} < d_{an} < d_{ap} + m$. Inside margin band but still farther than the positive. FaceNet uses these.
- **Hard negative:** $d_{an} < d_{ap}$ — closer than the positive; very informative but risky (may cause training instability).

### Why Hard Negatives Matter
- **Random** sampling gives mostly easy negatives, so most triplets are loss-zero. Training stalls because gradients are dominated by trivial cases.
- Mining hard or semi-hard negatives focuses gradient updates on the **decision boundary** of the embedding, where learning actually happens.
- A few hundred hard examples can have larger effect than tens of thousands of random triplets — vastly improves convergence and final quality.
- For retrieval / metric learning, **hard negative mining** is what separates working triplet pipelines from collapsed ones.

### Mining Strategies
- **Batch hard:** within a mini-batch, for each anchor pick the hardest positive and hardest negative (Hermans et al.).
- **Semi-hard mining:** FaceNet — choose the hardest negative still farther than the positive.
- **Cached / global mining:** maintain a memory bank of recent embeddings; mine hard negatives from there (XBM, MoCo-style).
- **Class-aware mining:** sample triplets to balance classes.

## Practical Notes
- Always $L_2$-normalize embeddings to keep distances bounded; this stabilizes the margin choice.
- Cross-batch memory and large batches help by enlarging the pool of candidate hard negatives.
- Modern variants: **InfoNCE / NT-Xent** (SimCLR) — softmax over many negatives, generalizes contrastive loss to many negatives at once, with built-in implicit hard-negative weighting.

## Related Concepts
- [[metric-learning]]
- [[hard-negative-mining]]
- [[FaceNet]]
- [[InfoNCE]]
