---
id: orr_quiz04_02
course: Optimal and Robust Control
tags: [dynamic-programming, LQ-control, cost-to-go, Riccati]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
While solving the discrete-time LQ-optimal control problem using Bellman's principle of optimality, we learnt that

## Options
A) The optimal cost-to-go at a given discrete time $k$ is given as $J^*_k = \tfrac{1}{2}\mathbf{x}_k^T \mathbf{Q}\mathbf{x}_k$, where $\mathbf{Q}$ is the (matrix) that penalizes the states in the quadratic criterion.
B) Dynamic programming is not applicable to the problem of LQ-optimal control.
C) The optimal cost-to-go at a given discrete time $k$ is given as $J^*_k = \tfrac{1}{2}\mathbf{x}_k^T \mathbf{S}_k\mathbf{x}_k$, where $\mathbf{S}_k$ is the (matrix) solution to the difference Riccati equation.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
For the LQ problem the optimal **cost-to-go (value function)** is **quadratic in the state**:
$$
J^*_k(\mathbf{x}_k) = \tfrac{1}{2}\mathbf{x}_k^T \mathbf{S}_k \mathbf{x}_k,
$$
where $\mathbf{S}_k$ is **not** the state-penalty $\mathbf{Q}$ but the **solution of the difference Riccati equation**, computed backward from the terminal condition $\mathbf{S}_N$:
$$
\mathbf{S}_k = \mathbf{Q} + \mathbf{A}^T\mathbf{S}_{k+1}\mathbf{A} - \mathbf{A}^T\mathbf{S}_{k+1}\mathbf{B}(\mathbf{R}+\mathbf{B}^T\mathbf{S}_{k+1}\mathbf{B})^{-1}\mathbf{B}^T\mathbf{S}_{k+1}\mathbf{A}.
$$
$\mathbf{S}_k$ accumulates the cost of all *future* steps under optimal control, so it generally differs from $\mathbf{Q}$ (which only weights the *current* stage). 
- **A** confuses the value-function matrix with the stage weight $\mathbf{Q}$.
- **B** is plainly false — LQ is the textbook success story of dynamic programming.

## Related Concepts
- [[difference-Riccati-equation]]
- [[value-function]]
- [[backward-recursion]]
