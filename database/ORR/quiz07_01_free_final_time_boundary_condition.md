---
id: orr_quiz07_01
course: Optimal and Robust Control
tags: [free-final-time, transversality, Hamiltonian, boundary-conditions]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
Consider a general continuous-time optimal control problem with a **free final time** $t_f$ and **fixed final state** (the initial state is, as usual, given). Choose a valid boundary condition for the boundary value problem.

## Options
A) Hamiltonian vanishes at the end of the control interval, that is, $H(\mathbf{x}(t),\mathbf{u}(t),\boldsymbol{\lambda}(t),t) = 0$ for $t = t_f$.
B) There is a linear relationship between the state and the costate at the final time, that is, $\mathbf{S}\mathbf{x}(t_f) = \boldsymbol{\lambda}(t_f)$.
C) —
D) —

---
# Solution
**Correct Answer:** A

## Explanation
When the final time $t_f$ is **free**, the variation of the cost must also vanish with respect to the variation $dt_f$. The general transversality condition is
$$
\Big(H(t_f) + \frac{\partial \phi}{\partial t}\Big)dt_f + \big(\nabla_{\mathbf{x}}\phi - \boldsymbol{\lambda}(t_f)\big)^T d\mathbf{x}(t_f) = 0 .
$$
Because $dt_f$ is now a free variation, its coefficient must vanish, giving (for a time-invariant problem with no explicit terminal time cost) the condition
$$
H(\mathbf{x}(t_f),\mathbf{u}(t_f),\boldsymbol{\lambda}(t_f),t_f) = 0 .
$$
This is the **extra boundary condition** that compensates for the extra unknown $t_f$.

- **B ($\boldsymbol{\lambda}(t_f)=\mathbf{S}\mathbf{x}(t_f)$)** is the transversality condition for a **free final state**, which contradicts the given assumption of a **fixed** final state ($d\mathbf{x}(t_f)=0$, so that term drops out automatically). It is not the condition that handles the free final *time*.

## Related Concepts
- [[free-final-time]]
- [[transversality-condition]]
- [[Hamiltonian]]
