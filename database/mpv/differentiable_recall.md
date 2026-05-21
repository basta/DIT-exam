---
id: mpv_025
course: Methods of Computer Vision
tags: [recall, differentiable-loss, smooth-rank, retrieval]
difficulty: 4
type: open
status: to_learn
---

# Question
How can you make **recall@k** to be differentiable and use it as a loss? Describe the loss in detail.

---
# Solution

## Why It Is Not Differentiable
For a query $q$, retrieve database items ranked by similarity score $s_d$. Let $\Omega^+$ be the set of positives. Recall@$k$:
$$
\text{R@}k = \frac{|\{d \in \Omega^+ : \text{rank}(d) \le k\}|}{|\Omega^+|}.
$$
The **rank** of $d$ is
$$
\text{rank}(d) = 1 + \sum_{d' \ne d} \mathbb{1}[s_{d'} > s_d],
$$
which uses an indicator (Heaviside) — non-differentiable. The set membership $\mathbb{1}[\text{rank}(d) \le k]$ is also a step.

So R@$k$ has gradient zero almost everywhere with respect to the scores → cannot be optimized directly with SGD.

## Idea: Smooth Surrogate
Replace the step $\mathbb{1}[u > 0]$ with a smooth approximation, typically the **sigmoid**:
$$
H_\tau(u) = \sigma(u / \tau) = \frac{1}{1 + e^{-u / \tau}},
$$
with temperature $\tau > 0$. As $\tau \to 0^+$ this converges to the step.

### Smooth Rank
$$
\tilde{\text{rank}}(d) = 1 + \sum_{d' \ne d} H_\tau(s_{d'} - s_d).
$$
Differentiable in all scores $s_{d'}, s_d$.

### Smooth Recall@k (Smooth-AP / SmoothRank / Recall@k Surrogate)
A second sigmoid implements the "rank ≤ k" check:
$$
\tilde{\text{R@}}k(q) = \frac{1}{|\Omega^+|} \sum_{d \in \Omega^+} H_\tau\!\big( k - \tilde{\text{rank}}(d) \big).
$$
- The outer sigmoid is 1 if $d$ is well above rank $k$ (small rank) and 0 otherwise.
- The inner sigmoid replaces the hard indicator of $s_{d'} > s_d$.

We then maximize the average over queries, i.e., minimize the loss
$$
\mathcal{L} = 1 - \frac{1}{|Q|} \sum_q \tilde{\text{R@}}k(q).
$$

This is the loss form used in the paper **"Recall@k Surrogate Loss with Large Batches and Similarity Mixup"** (Patel, Tolias, Matas, CVPR 2022).

## Practical Considerations
- **Large batches.** The sum over $d'$ is over the entire batch (or memory bank). The larger the batch, the better the rank approximation. Memory tricks like **gradient checkpointing**, cross-GPU all-gather, or external memory banks are used to scale beyond GPU memory.
- **Temperature schedule.** Start with a larger $\tau$ for smoother gradients, anneal $\tau \to 0$ for accuracy. Too small $\tau$ → vanishing gradient (back to the step); too large $\tau$ → ranks are confused.
- **Similarity Mixup.** Augment training pairs by linear interpolation of feature vectors / similarities; helps because positives become denser around the decision region.
- The same idea works for any rank-based metric: smooth approximations exist for **AP** (Smooth-AP, FastAP, Soft-Histogram-AP) and **NDCG**.

## Smooth-AP (Closely Related)
Smooth-AP (Brown et al., 2020) replaces the rank indicator in
$$
\text{AP}(q) = \frac{1}{|\Omega^+|} \sum_{d \in \Omega^+} \frac{\text{rank}^+(d)}{\text{rank}(d)}
$$
with the same sigmoid-based smooth rank. It is a strict generalization of the R@$k$ surrogate (which can be derived as a limit case).

## Why This Works
- The loss is **directly aligned** with the evaluation metric — no need to choose a proxy (triplet margin, contrastive margin) and tune it.
- Gradients pull each positive towards the top of the ranking and push negatives away — globally and listwise, not just pairwise.
- It implicitly performs hard-example mining: gradients are largest exactly where the smooth indicator is changing, i.e., for items near the rank boundary.

## Related Concepts
- [[AP-loss]]
- [[listwise-loss]]
- [[sigmoid-relaxation]]
- [[hard-negative-mining]]
