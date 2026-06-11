---
id: orr_quiz02_01
course: Optimal and Robust Control
tags: [LQ-control, cost-function, weighting-matrices, positive-semidefinite]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
One of the most popular (mainly because of its mathematical tractability) optimal control cost functions is the following quadratic function
$$
J = \tfrac{1}{2}\mathbf{x}_N^T \mathbf{S}\mathbf{x}_N + \tfrac{1}{2}\sum_{k=0}^{N-1}\left[\mathbf{x}_k^T \mathbf{Q}\mathbf{x}_k + \mathbf{u}_k^T \mathbf{R}\mathbf{u}_k\right],
$$
where $\mathbf{S}, \mathbf{Q}$ and $\mathbf{R}$ are given constant weighting matrices. They are typically symmetric. But what are the other commonly imposed conditions on these matrices?

## Options
A) They must all be nonsingular.
B) There are no other conditions.
C) They are all positive semidefinite, that is, $\mathbf{S} \ge 0, \mathbf{Q} \ge 0, \mathbf{R} \ge 0$.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
The quadratic cost penalizes the "energy" of the states and the control. For these penalties to make physical sense (a cost that is never negative, so that minimization is well posed), the weighting matrices must be **positive semidefinite**:
$$
\mathbf{S} \ge 0, \quad \mathbf{Q} \ge 0, \quad \mathbf{R} \ge 0 .
$$
This guarantees $\mathbf{x}^T\mathbf{Q}\mathbf{x} \ge 0$ and $\mathbf{u}^T\mathbf{R}\mathbf{u} \ge 0$ for every $\mathbf{x}, \mathbf{u}$, so $J \ge 0$ and the optimization is convex.

**Important nuance:** In practice the control weight $\mathbf{R}$ is required to be *positive definite* ($\mathbf{R} > 0$, hence nonsingular) so that the stationarity condition $\mathbf{R}\mathbf{u}_k + \mathbf{B}^T\boldsymbol{\lambda}_{k+1} = 0$ can be solved for a *unique* optimal control $\mathbf{u}_k$. Definiteness of $\mathbf{Q}$ (or $\mathbf{S}$) is only needed for stability/uniqueness guarantees (via detectability of $(\mathbf{A}, \sqrt{\mathbf{Q}})$). The "commonly imposed minimal condition" asked here is semidefiniteness — option A is wrong because semidefinite matrices may be singular, and B is wrong because definiteness *is* a condition.

## Related Concepts
- [[LQ-optimal-control]]
- [[positive-semidefinite-matrix]]
- [[quadratic-cost-function]]
