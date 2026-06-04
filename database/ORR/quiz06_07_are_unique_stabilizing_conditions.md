---
id: orr_quiz06_07
course: Optimal and Robust Control
tags: [ARE, stabilizability, detectability, LQR-existence]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
We can design an LQ-optimal controller by solving the Algebraic Riccati Equation (ARE). We are guaranteed that there will be a unique stabilizing controller derived from the solution of the ARE if and only if

## Options
A) $(\mathbf{A}, \mathbf{B})$ is stabilizable and $(\mathbf{A}, \sqrt{\mathbf{Q}})$ is detectable (could be strengthened to observability if a nonsingularity of the solution of ARE is required).
B) $\mathbf{A}$ is stable.
C) $(\mathbf{A}, \mathbf{B})$ is stabilizable.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
The standard existence/uniqueness result for the LQR / ARE requires **two** conditions:
1. **Stabilizability of $(\mathbf{A},\mathbf{B})$** — the unstable modes must be controllable, otherwise no feedback can stabilize the loop and the cost would be infinite.
2. **Detectability of $(\mathbf{A}, \sqrt{\mathbf{Q}})$** (where $\sqrt{\mathbf{Q}}$ is a factor with $\sqrt{\mathbf{Q}}^T\sqrt{\mathbf{Q}}=\mathbf{Q}$) — every unstable mode must be "seen" by the state penalty; otherwise an unstable mode could grow unboundedly without being penalized, and the stabilizing solution would not be unique.

Under both, the ARE has a **unique symmetric positive-semidefinite stabilizing solution** giving a stabilizing feedback. Strengthening detectability to **observability** of $(\mathbf{A},\sqrt{\mathbf{Q}})$ makes the solution **positive definite (nonsingular)**.

- **B** is far too strong (if $\mathbf{A}$ were already stable we'd hardly need control) and not required.
- **C** alone is insufficient — without detectability of $(\mathbf{A},\sqrt{\mathbf{Q}})$ uniqueness/stability of the solution is lost.

## Related Concepts
- [[algebraic-Riccati-equation]]
- [[stabilizability]]
- [[detectability]]
