---
id: orr_quiz10_03
course: Optimal and Robust Control
tags: [H-infinity-norm, MIMO, singular-values, system-norms]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Choose the correct definition of the $\mathcal{H}_\infty$ norm of a (linear model of a) dynamical system with multiple inputs and multiple outputs (MIMO).

## Options
A) The supremum of eigenvalues of the system's transfer function matrix over all frequencies.
B) The maximum of $\mathcal{H}_\infty$ norms of individual SISO transfer functions in the matrix of transfer functions.
C) The supremum of singular values of the system's transfer function matrix over all frequencies.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
For a MIMO transfer matrix $G(j\omega)$, the $\mathcal{H}_\infty$ norm is the **peak over frequency of the largest singular value**:
$$
\|G\|_\infty = \sup_{\omega}\ \bar{\sigma}\big(G(j\omega)\big),
$$
where $\bar{\sigma}$ denotes the **maximum singular value**. It equals the worst-case energy gain (induced 2-norm) of the system: the largest factor by which the input energy can be amplified, maximized over all directions and all frequencies.

- **A is wrong:** for MIMO systems one must use **singular values**, not eigenvalues — eigenvalues do not give the gain of a non-normal matrix and can be misleading (eigenvalues describe modal behaviour, singular values describe gain).
- **B is wrong:** the norm is **not** the max of the SISO entry norms; cross-coupling between channels means the directional (singular-value) gain can exceed any individual entry's peak.

## Related Concepts
- [[H-infinity-norm]]
- [[singular-value-decomposition]]
- [[induced-2-norm]]
