---
id: nno_018
course: Nonsmooth Nonconvex Optimization
tags: [convexity, topology, variational-analysis]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a **convex set** and what it means for a set to be **semi-closed**. (HW2 Ex 0.12)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $C\subseteq\mathbb{R}^n$ is **convex** if for all $x,y\in C$ and $\lambda\in[0,1]$, $\lambda x + (1-\lambda)y \in C$. $C$ is **semi-closed** if $\mathrm{int}(C) = \mathrm{int}(\mathrm{cl}(C))$.

## Explanation
A convex set contains the whole segment between any two of its points.

HW2 Ex 0.12 asks you to prove:

1. Every convex $C$ is **semi-closed**: $\mathrm{int}(C) = \mathrm{int}(\mathrm{cl}(C))$. (Taking closure doesn't enlarge the interior — boundary points of a convex set are not interior to the closure, by a supporting-hyperplane / line-segment argument.)
2. The **boundary of a convex set is nowhere dense**: $\mathrm{int}(\mathrm{cl}(\mathrm{bd}\,C)) = \varnothing$.

The proof technique: for $x\in\mathrm{cl}(C)$ and $y\in\mathrm{int}(C)$, the half-open segment $[y,x)$ lies in $\mathrm{int}(C)$ (a standard convexity lemma); this forces $\mathrm{int}(\mathrm{cl}\,C)\subseteq \mathrm{int}(C)$, and the reverse inclusion is trivial.

This connects to the tame-geometry theme that *definable boundaries are nowhere dense / lower-dimensional* — convex sets are a clean special case requiring no o-minimality.

## Related Concepts
- [[topological_boundary_nowhere_dense]]
- [[clarke_subdifferential]]
- [[dimension_function]]
