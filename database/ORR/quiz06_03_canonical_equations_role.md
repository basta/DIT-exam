---
id: orr_quiz06_03
course: Optimal and Robust Control
tags: [Pontryagin, canonical-equations, Hamiltonian, necessary-conditions]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The role of the equations
$$
x' = \nabla_\lambda H, \qquad \lambda' = -\nabla_x H, \qquad 0 = \nabla_u H
$$
in optimal control is

## Options
A) they give first-order necessary conditions of optimality for a general nonlinear dynamical system and a general cost function.
B) they give a condition on closed-loop stability of the system.
C) these equations make no sense in optimal control.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
These are the **canonical (Hamiltonian) equations** — the first-order necessary conditions of optimality from Pontryagin's framework, where $H = L + \lambda^T f$ is the Hamiltonian:
- $x' = \nabla_\lambda H = f(x,u)$ — the **state equation** (recovers the dynamics),
- $\lambda' = -\nabla_x H$ — the **costate (adjoint) equation**, integrated backward,
- $0 = \nabla_u H$ — the **stationarity condition** for the control (in Pontryagin's general form replaced by minimization/maximization of $H$ over $u$).

Together with boundary/transversality conditions they form the two-point boundary value problem characterizing optimal trajectories of a **general nonlinear** system and cost. They are about **optimality**, not stability (B), and are central — not meaningless (C).

## Related Concepts
- [[Hamiltonian]]
- [[costate-equation]]
- [[Pontryagin-minimum-principle]]
