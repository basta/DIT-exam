---
id: orr_quiz11_02
course: Optimal and Robust Control
tags: [H-infinity-control, generalized-plant, LFT, controller-synthesis]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The general control design methodology based on minimization of the $\mathcal{H}_\infty$ norm is formulated as
$$
\operatorname{minimize}_K \lVert \mathcal{F}_{\text{lower}}(P, K) \rVert_\infty,
$$
where $\mathcal{F}_{\text{lower}}()$ is the lower linear fractional transformation and $K$ is a controller. What is the role of $P$?

## Options
A) Weighting filter on closed-loop performance.
B) Model of the generalized system — interconnection of the original physical system and various weighting filters and summation blocks.
C) Model of the physical system.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
$P$ is the **generalized plant** (also "augmented plant"). It is **not** just the physical system, and **not** just a weight — it is the **entire interconnection** that bundles together:
- the model of the original physical system,
- all the **weighting filters** ($W_1, W_2, W_3, \dots$) that encode the performance and robustness specifications, and
- the **summation/junction blocks** that form the error and performance signals.

$P$ has two sets of inputs (exogenous $w$, control $u$) and two sets of outputs (performance $z$, measured $y$). Closing the lower loop with the controller $K$ (from $y$ to $u$) gives the closed-loop map $z = \mathcal{F}_{\text{lower}}(P,K)\,w$, whose $\mathcal{H}_\infty$ norm is minimized over stabilizing $K$.

- **A** describes just the weights (a part of $P$).
- **C** describes only the bare physical model (also just a part of $P$).

## Related Concepts
- [[generalized-plant]]
- [[lower-LFT]]
- [[H-infinity-synthesis]]
