---
id: orr_quiz07_02
course: Optimal and Robust Control
tags: [Pontryagin, maximum-principle, Hamiltonian]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Choose the correct interpretation of Pontryagin's principle of maximum.

## Options
A) Time of regulation is minimized.
B) The Hamiltonian is maximized by the optimal control.
C) Optimal control always takes its extreme values.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
Pontryagin's principle states that the optimal control $\mathbf{u}^\star(t)$, at every instant, **extremizes the Hamiltonian** over the set of admissible controls — in the *maximum* principle convention (with $H = -L + \boldsymbol\lambda^T f$ or equivalently a sign choice), the optimal control **maximizes $H$**:
$$
\mathbf{u}^\star(t) = \arg\max_{\mathbf{u}\in\mathcal{U}} H(\mathbf{x}^\star,\mathbf{u},\boldsymbol{\lambda}^\star,t).
$$
(With the alternative sign convention $H = L + \boldsymbol\lambda^T f$ this is the *minimum* principle — the substance is the same: the control optimizes $H$ pointwise.)

- **A** confuses the principle with a specific objective (time-optimal control is just one application).
- **C** is only true in special cases — for instance **bang-bang** control of systems with a control-affine $H$ — but it is **not** the general statement. The general principle is the optimization of $H$; extremal-value control is a *consequence* in particular structures.

## Related Concepts
- [[Pontryagin-maximum-principle]]
- [[Hamiltonian]]
- [[bang-bang-control]]
