---
id: orr_quiz04_03
course: Optimal and Robust Control
tags: [HJB, dynamic-programming, continuous-time, value-function]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
The Hamilton-Jacobi-Bellman (HJB) equation gives the principle of optimality for continuous-time systems. Pick among the equations below the correct HJB equation for the system described by $\dot{x}(t) = f(x,u,t)$ and the cost function $J = \phi(x(t_f),t_f) + \int_{t_i}^{t_f} L(x,u,t)\,dt$.

## Options
A) $-\dot{S}(t) = A^T S(t) + S(t)A - S(t)BR^{-1}B^T S(t)$
B) $J^*_k(x_k) = \min_{u_k}\left(L_k(x_k,u_k) + J^*_{k+1}(x_{k+1})\right)$
C) $-\dfrac{\partial J^*}{\partial t} = \min_{u(t)}\left(L(x,u) + (\nabla_x J^*)^T f(x,u)\right)$
D) —

---
# Solution
**Correct Answer:** C

## Explanation
The **HJB equation** is the continuous-time counterpart of the Bellman recursion. Defining the optimal cost-to-go $J^*(x,t)$, it reads
$$
-\frac{\partial J^*}{\partial t} = \min_{u(t)}\left(L(x,u) + (\nabla_x J^*)^T f(x,u)\right),
$$
with boundary condition $J^*(x,t_f) = \phi(x(t_f), t_f)$. It is a **first-order nonlinear PDE** in the value function; the minimizing $u$ gives the optimal feedback law.

- **A** is the (continuous-time differential) **Riccati equation** — a *special case* result for the LQ problem, not the general HJB.
- **B** is the **discrete-time** Bellman recursion, not the continuous-time HJB (the question asks for the continuous-time system).

## Related Concepts
- [[Hamilton-Jacobi-Bellman-equation]]
- [[dynamic-programming]]
- [[continuous-time-optimal-control]]
