---
id: orr_quiz10_02
course: Optimal and Robust Control
tags: [robust-control, LFT, linear-fractional-transformation, uncertainty]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
We introduced the mathematical framework of *linear fractional transformation* (LFT). What was our motivation for doing so?

## Options
A) We only wanted to convert continuous-time systems to discrete-time systems.
B) We use it as a computational tool for finding a robust controller.
C) LFT just generalizes the notion of feedback (not all the inputs and outputs are involved in the feedback) and we use it in the course to plug the uncertainty into the system in such a feedback manner.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
A **linear fractional transformation** is a generalized feedback interconnection: given a partitioned system $M=\begin{bmatrix}M_{11}&M_{12}\\M_{21}&M_{22}\end{bmatrix}$, closing a feedback loop around **only a subset** of its inputs/outputs with a block $\Delta$ (or controller $K$) yields the LFT
$$
\mathcal{F}_u(M,\Delta)=M_{22}+M_{21}\Delta(I-M_{11}\Delta)^{-1}M_{12}.
$$
This is the natural language for robust control because it lets us **"pull out the $\Delta$"**: any rational dependence on the uncertainty (or controller) can be rewritten as a fixed nominal system $M$ with $\Delta$ (or $K$) connected back in **feedback**. The standard $N$–$\Delta$ and $P$–$K$ forms are exactly upper/lower LFTs.

- **A** is unrelated (LFT is not about discretization).
- **B** is a downstream *use*, but the **motivation/role** is the structural one in C: generalizing feedback to insert uncertainty (or the controller) into a fixed interconnection.

## Related Concepts
- [[linear-fractional-transformation]]
- [[generalized-plant]]
- [[pull-out-the-delta]]
