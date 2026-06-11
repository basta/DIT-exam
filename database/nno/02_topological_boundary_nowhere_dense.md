---
id: nno_002
course: Nonsmooth Nonconvex Optimization
tags: [prerequisites, topology, boundary, nowhere-dense]
difficulty: 1
type: open
status: to_learn
---

# Question
Define the **topological boundary** $\mathrm{bd}(A)$ of a set, and state what it means for a set to be **nowhere dense**.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** In a topological space $(X,\tau)$, the boundary of $A$ is $\mathrm{bd}(A) := \mathrm{cl}(A) \setminus \mathrm{int}(A)$. A set $A$ is **nowhere dense** if $\mathrm{int}(\mathrm{cl}(A)) = \varnothing$, i.e. its closure has empty interior.

## Explanation
These topological notions recur throughout the course. The **closure** $\mathrm{cl}(A)$ is the smallest closed set containing $A$; the **interior** $\mathrm{int}(A)$ is the largest open set contained in $A$. The **boundary** is what remains:

$$\mathrm{bd}(A) := \mathrm{cl}(A) \setminus \mathrm{int}(A).$$

Basic identities used in HW1 Ex 0.3:

- $\mathrm{bd}(A) = \mathrm{bd}(A^c)$ (boundary of a set equals boundary of its complement);
- $\mathrm{bd}(A \cup B) \subseteq \mathrm{bd}(A) \cup \mathrm{bd}(B)$.

A set is **nowhere dense** when its closure contains no open ball. A central theme of tame geometry: the *boundary of a definable set is nowhere dense* (and lower-dimensional), which is exactly what makes definable sets well-behaved. HW2 Ex 0.12 uses this for convex sets (a convex set is "semi-closed" and its boundary is nowhere dense).

## Related Concepts
- [[finite_boundary_property]]
- [[convex_set_semi_closed]]
- [[dimension_function]]
