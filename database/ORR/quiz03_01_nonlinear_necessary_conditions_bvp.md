---
id: orr_quiz03_01
course: Optimal and Robust Control
tags: [necessary-conditions, discrete-time, two-point-BVP, optimal-control]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The first-order necessary conditions of optimality for a general (nonlinear) optimal control problem
$$
\min \;\phi(\mathbf{x}_N, N) + \sum_{k=i}^{N-1} L(\mathbf{x}_k, \mathbf{u}_k)
$$
subject to
$$
\mathbf{x}_{k+1} = \mathbf{f}(\mathbf{x}_k, \mathbf{u}_k), \qquad \mathbf{x}_i = \mathbf{r}_i
$$
are in the form of

## Options
A) a set of difference equations with the boundary conditions defined only at the initial time — the so-called discrete-time *initial value problem (IVP)*.
B) a set of difference and algebraic equations with boundary conditions given at both the initial and the final time — the so-called discrete-time two-point boundary value problem (BVP).
C) a set of quadratic inequalities.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
Forming the discrete Hamiltonian $H_k = L(\mathbf{x}_k,\mathbf{u}_k) + \boldsymbol{\lambda}_{k+1}^T \mathbf{f}(\mathbf{x}_k,\mathbf{u}_k)$, the necessary conditions are:
- **State equation** (forward difference): $\mathbf{x}_{k+1} = \mathbf{f}(\mathbf{x}_k,\mathbf{u}_k)$,
- **Costate equation** (backward difference): $\boldsymbol{\lambda}_k = \nabla_{\mathbf{x}_k} H_k$,
- **Stationarity** (algebraic): $\mathbf{0} = \nabla_{\mathbf{u}_k} H_k$.

The crucial structural feature is the **split boundary conditions**: the **initial state** is fixed ($\mathbf{x}_i = \mathbf{r}_i$, given at $k=i$), while the **costate** condition (transversality) is set at the **final time** ($\boldsymbol{\lambda}_N = \nabla_{\mathbf{x}_N}\phi$). Conditions specified at *two* different time ends make this a **two-point boundary value problem (BVP)** — it cannot be integrated as a simple forward IVP (A is wrong). C is unrelated (this is an equality system, not inequalities).

## Related Concepts
- [[two-point-boundary-value-problem]]
- [[discrete-Hamiltonian]]
- [[transversality-condition]]
