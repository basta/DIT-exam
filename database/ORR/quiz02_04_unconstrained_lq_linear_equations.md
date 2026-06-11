---
id: orr_quiz02_04
course: Optimal and Robust Control
tags: [LQ-control, unconstrained, linear-equations, KKT]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Consider a linear discrete-time system and the standard quadratic cost function. If there are no constraints on the states and the controls, the task of finding the optimal control sequence can be solved by invoking a numerical solver for

## Options
A) a set of linear equations.
B) a set of nonlinear equations.
C) quadratic optimization with inequality constraints.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
With **linear dynamics** and a **quadratic cost**, the optimization is an unconstrained **convex quadratic program (QP)**. The first-order optimality (stationarity) condition of a quadratic function is **linear** in the decision variables:
$$
\nabla J = \mathbf{H}\mathbf{z} + \mathbf{f} = \mathbf{0} \;\Rightarrow\; \mathbf{H}\mathbf{z} = -\mathbf{f},
$$
where $\mathbf{H}$ is the (positive (semi)definite) Hessian. Equivalently, the discrete-time necessary conditions form a linear two-point boundary value problem (state, costate, stationarity all linear). Hence the optimum is obtained by solving a **set of linear equations** — no iterative nonlinear solver needed.

- **B** would apply to a nonlinear system or nonquadratic cost.
- **C** would apply only if inequality constraints on states/controls were present (then it becomes a constrained QP, the MPC case).

## Related Concepts
- [[quadratic-program]]
- [[unconstrained-LQ]]
- [[two-point-boundary-value-problem]]
