---
id: orr_quiz10_05
course: Optimal and Robust Control
tags: [small-gain-theorem, robust-stability, LFT, structured-uncertainty]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
Choose the correct version of the *small gain theorem*, i.e., the condition of robust stability for a generalized plant $N$ interconnected with an uncertainty block $\Delta$, $\lVert\Delta\rVert_\infty \le 1$, using an upper LFT as in the figure below.

![[quiz10_05_small_gain_lft.png]]

*(Block diagram: $\Delta$ in the upper feedback path connected to $N$ via signals $u_\Delta, y_\Delta$; external signals $w$ in and $z$ out.)*

## Options
A) $\lVert N_{22}\rVert_\infty < 1$
B) $\lVert N_{11}\rVert_\infty < 1$
C) $\lVert N\rVert_\infty < 1$
D) —

---
# Solution
**Correct Answer:** B

## Explanation
Partition $N=\begin{bmatrix}N_{11}&N_{12}\\N_{21}&N_{22}\end{bmatrix}$ so that the **upper** loop $\Delta$ closes around the $N_{11}$ channel (the $u_\Delta\to y_\Delta$ path). The interconnection is the upper LFT $\mathcal{F}_u(N,\Delta)$, well-posed and internally stable iff $(I-N_{11}\Delta)^{-1}$ is stable. By the **small-gain theorem**, since $\|\Delta\|_\infty\le 1$, robust stability against *all* such $\Delta$ holds iff
$$
\boxed{\;\lVert N_{11}\rVert_\infty < 1.\;}
$$
Only the sub-block $N_{11}$ that is actually **in the loop with $\Delta$** matters.

- **A ($N_{22}$)** is the transfer from $w$ to $z$ (the external performance channel), not the loop seen by $\Delta$.
- **C ($\|N\|_\infty<1$)** is **overly conservative / incorrect** — it constrains the whole matrix including the external channels $N_{12},N_{21},N_{22}$, which are irrelevant to the stability of the $\Delta$-loop.

## Related Concepts
- [[small-gain-theorem]]
- [[upper-LFT]]
- [[robust-stability]]
