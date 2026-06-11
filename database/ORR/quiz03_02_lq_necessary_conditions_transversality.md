---
id: orr_quiz03_02
course: Optimal and Robust Control
tags: [LQ-control, necessary-conditions, transversality, costate]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
The first-order necessary conditions of optimality for the popular LQ-optimal control problem on a finite horizon $[0,N]$ which cover **both** the fixed and free final state cases are given by which set of equations?

## Options
A) $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k+\mathbf{B}\mathbf{u}_k,\; \boldsymbol{\lambda}_k=\mathbf{Q}\mathbf{x}_k+\mathbf{A}^T\boldsymbol{\lambda}_{k+1},\; \mathbf{0}=\mathbf{R}\mathbf{u}_k+\mathbf{B}^T\boldsymbol{\lambda}_{k+1},\; \mathbf{x}_N=\mathbf{r}_N,\; \mathbf{x}_0=\mathbf{r}_0.$
B) $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k+\mathbf{B}\mathbf{u}_k,\; \boldsymbol{\lambda}_k=\mathbf{Q}\mathbf{x}_k+\mathbf{A}^T\boldsymbol{\lambda}_{k+1},\; \mathbf{0}=\mathbf{R}\mathbf{u}_k+\mathbf{B}^T\boldsymbol{\lambda}_{k+1},\; 0=(\mathbf{S}_N\mathbf{x}_N-\boldsymbol{\lambda}_N)^T d\mathbf{x}_N,\; \mathbf{x}_0=\mathbf{r}_0.$
C) $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k+\mathbf{B}\mathbf{u}_k,\; \boldsymbol{\lambda}_k=\mathbf{Q}\mathbf{x}_k+\mathbf{A}^T\boldsymbol{\lambda}_{k+1},\; \mathbf{0}=\mathbf{R}\mathbf{u}_k+\mathbf{B}^T\boldsymbol{\lambda}_{k+1},\; 0=(\mathbf{S}_N\mathbf{x}_N-\boldsymbol{\lambda}_N)^T d\mathbf{x}_N.$
D) —

---
# Solution
**Correct Answer:** B

## Explanation
The state, costate and stationarity equations are identical in all options; the distinguishing element is the **terminal (transversality) condition** and the **initial condition**.

The general transversality condition is
$$
\big(\mathbf{S}_N\mathbf{x}_N - \boldsymbol{\lambda}_N\big)^T d\mathbf{x}_N = 0,
$$
which **elegantly covers both cases at once**:
- **Free final state:** $d\mathbf{x}_N$ is arbitrary $\Rightarrow$ $\boldsymbol{\lambda}_N = \mathbf{S}_N\mathbf{x}_N$ (the usual terminal costate condition).
- **Fixed final state:** $\mathbf{x}_N = \mathbf{r}_N$ is given $\Rightarrow$ $d\mathbf{x}_N = 0$, so the condition is satisfied automatically and $\boldsymbol{\lambda}_N$ is free.

Option B also correctly **keeps the initial condition** $\mathbf{x}_0=\mathbf{r}_0$ (always given). 
- **A** hard-codes $\mathbf{x}_N=\mathbf{r}_N$, so it only describes the *fixed* final state case.
- **C** has the right transversality term but **drops** $\mathbf{x}_0=\mathbf{r}_0$, so the boundary conditions are incomplete.

## Related Concepts
- [[transversality-condition]]
- [[LQ-optimal-control]]
- [[costate-boundary-condition]]
