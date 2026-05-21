---
id: mpv_014
course: Methods of Computer Vision
tags: [mAP, precision, recall, evaluation, retrieval]
difficulty: 3
type: open
status: to_learn
---

# Question
How is **mAP** computed? Discuss relation to **precision@k**, **recall@k** for particular $k$.

---
# Solution

## Setup
We have a query and a *ranked* list of retrieved items. Each item is labeled as **relevant** (positive) or **non-relevant** (negative) for the query. Total number of relevant items in the database: $R$.

## Precision and Recall at $k$
After examining the top $k$ items:
- $\text{precision@}k = \dfrac{\#\{\text{relevant in top }k\}}{k}$,
- $\text{recall@}k = \dfrac{\#\{\text{relevant in top }k\}}{R}$.

These are scalar summaries — they describe only one operating point.

## Precision–Recall Curve
Sweep $k$ from 1 to $N$ (the database size). For every $k$, plot $(\text{recall@}k, \text{precision@}k)$. The curve generally moves rightward (recall is non-decreasing) but precision can fluctuate.

## Average Precision (AP)
**AP** is the area under the precision-recall curve. The most common discrete definition: average the precision at *every position where a relevant item appears*:
$$
\text{AP} = \frac{1}{R} \sum_{k=1}^{N} \text{precision@}k \cdot \text{rel}(k),
$$
where $\text{rel}(k) = 1$ if the $k$-th retrieved item is relevant, else 0. Equivalently,
$$
\text{AP} = \frac{1}{R} \sum_{i=1}^{R} \frac{i}{\text{rank}(i)},
$$
where $\text{rank}(i)$ is the position of the $i$-th retrieved positive in the ranked list. The optimum is $\text{AP} = 1$ when all $R$ positives rank at positions $1, \dots, R$.

## Mean Average Precision (mAP)
Average AP over a set of queries $Q$:
$$
\text{mAP} = \frac{1}{|Q|} \sum_{q \in Q} \text{AP}(q).
$$

## Relation to precision@$k$ and recall@$k$
- **AP is a weighted sum of precision values** evaluated at the recall steps. Each positive at rank $k$ contributes $\text{precision@}k$ to AP.
- **precision@$k$** alone is what AP measures when there is exactly one positive at rank $k$: AP averages these contributions.
- For a particular $k$:
  - If $k \le R$: $\text{recall@}k \le k/R$ and $\text{precision@}k \le 1$.
  - $\text{recall@}k = 1$ requires $k \ge R$.
- **precision@$k$ and recall@$k$ together describe one operating point**; AP captures the *whole* curve and so is a more complete summary, but is also harder to interpret intuitively.
- For datasets with few positives (e.g., 1 positive per query in re-identification), AP simplifies to $1/\text{rank}_{\text{first positive}}$, and mAP becomes the **mean reciprocal rank** (MRR).

## Practical Notes
- The Pascal VOC version of AP samples precision at 11 fixed recall levels and averages; the *all-points* version (used in image retrieval and detection benchmarks now) is the one defined above.
- In retrieval one often reports mAP@$k$ — AP truncated after the top-$k$ retrieved items, useful when only the top of the ranking matters.

## Related Concepts
- [[precision-recall-curve]]
- [[mean-reciprocal-rank]]
- [[information-retrieval]]
- [[evaluation-metrics]]
