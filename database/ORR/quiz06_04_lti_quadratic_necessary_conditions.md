---
id: orr_quiz06_04
course: Optimal and Robust Control
tags: [LQ-control, necessary-conditions, boundary-conditions, continuous-time]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
Consider an LTI system described by a standard state-space model. We want to minimize the standard quadratic criterion $J = \tfrac{1}{2}(\mathbf{x}^T\mathbf{Q}\mathbf{x} + \mathbf{u}^T\mathbf{R}\mathbf{u})$ and we assume $\mathbf{Q} \ge 0$ and $\mathbf{R} > 0$. Choose the correct form of the first-order necessary conditions of optimality.

## Options
A) $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{R}^{-1}\mathbf{B}^T\boldsymbol{\lambda},\;\; \dot{\boldsymbol{\lambda}} = \mathbf{Q}\mathbf{x} - \mathbf{A}^T\boldsymbol{\lambda}.$
B) $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{R}^{-1}\mathbf{B}^T\boldsymbol{\lambda},\;\; \dot{\boldsymbol{\lambda}} = \mathbf{Q}\mathbf{x} - \mathbf{A}^T\boldsymbol{\lambda},\;\; \mathbf{x}(0)=\mathbf{r}_0.$
C) $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{R}^{-1}\mathbf{B}^T\boldsymbol{\lambda},\;\; \dot{\boldsymbol{\lambda}} = \mathbf{Q}\mathbf{x} - \mathbf{A}^T\boldsymbol{\lambda},\;\; \mathbf{x}(0)=\mathbf{r}_0,\;\; \mathbf{h}(\mathbf{x}(t_f),\boldsymbol{\lambda}(t_f))=0.$
D) —

---
# Solution
**Correct Answer:** C

## Explanation
Eliminating the optimal control via stationarity ($\mathbf{R}\mathbf{u} + \mathbf{B}^T\boldsymbol{\lambda} = 0 \Rightarrow \mathbf{u} = -\mathbf{R}^{-1}\mathbf{B}^T\boldsymbol{\lambda}$, possible because $\mathbf{R}>0$) gives the coupled **Hamiltonian (canonical) system** in $\mathbf{x}$ and $\boldsymbol{\lambda}$. But a system of ODEs is not a well-posed problem without **boundary conditions**:
- the **initial condition** $\mathbf{x}(0) = \mathbf{r}_0$, and
- a **terminal/transversality condition** $\mathbf{h}(\mathbf{x}(t_f),\boldsymbol{\lambda}(t_f)) = 0$ (e.g. $\boldsymbol{\lambda}(t_f) = \mathbf{S}\mathbf{x}(t_f)$ for free final state, or $\mathbf{x}(t_f)=\mathbf{r}_f$ for fixed final state).

Only option **C** is complete: it specifies the differential equations **and both boundary conditions**, forming the full two-point BVP. A lacks any boundary conditions; B lacks the terminal condition.

## Related Concepts
- [[two-point-boundary-value-problem]]
- [[transversality-condition]]
- [[Hamiltonian-system]]
