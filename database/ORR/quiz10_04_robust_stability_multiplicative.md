---
id: orr_quiz10_04
course: Optimal and Robust Control
tags: [robust-stability, multiplicative-uncertainty, complementary-sensitivity]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Choose the correct condition for robust stability in the presence of multiplicative uncertainty.

## Options
A) $\lVert W_1 S\rVert_\infty + \lVert W_2 T\rVert_\infty < 1$
B) $\lVert WS\rVert_\infty < 1$
C) $\lVert WT\rVert_\infty < 1$
D) —

---
# Solution
**Correct Answer:** C

## Explanation
For a plant with **(output) multiplicative uncertainty** $G_p = (I + W\Delta)G$, $\|\Delta\|_\infty \le 1$, the small-gain theorem applied to the loop seen by $\Delta$ gives the robust-stability condition
$$
\boxed{\;\lVert W T\rVert_\infty < 1\;}
$$
where $T = L(I+L)^{-1}$ is the **complementary sensitivity** function and $W$ is the uncertainty weight. The $\Delta$ block "sees" the loop transfer $WT$, so the loop is robustly stable for all admissible $\Delta$ iff $\|WT\|_\infty<1$.

- **B ($\|WS\|_\infty<1$)** involves the **sensitivity** $S=(I+L)^{-1}$ — that is a *performance* (disturbance-attenuation) specification, not multiplicative robust stability.
- **A** is the **robust performance** condition combining both $S$ and $T$ weights — more than is needed for stability alone (see quiz #10 Q6).

## Related Concepts
- [[robust-stability]]
- [[complementary-sensitivity]]
- [[small-gain-theorem]]
- [[multiplicative-uncertainty]]
