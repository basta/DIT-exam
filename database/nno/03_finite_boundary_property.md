---
id: nno_003
course: Nonsmooth Nonconvex Optimization
tags: [prerequisites, topology, boolean-algebra, definability]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the **finite boundary property** of a subset of a topological space, and the collection $\mathcal{FBP}(X)$. (HW1 Ex 0.3–0.4)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Let $X = (X,\tau)$ be a topological space. A subset $A \subseteq X$ has the **finite boundary property** if its boundary $\mathrm{bd}(A) = \mathrm{cl}(A) \setminus \mathrm{int}(A)$ is a finite set. Then $\mathcal{FBP}(X) := \{A \subseteq X : A \text{ has the finite boundary property}\}$.

## Explanation
This is a toy model for o-minimality on $\mathbb{R}$: sets with finite boundary behave like the one-dimensional definable sets (finite unions of points and intervals).

Using $\mathrm{bd}(A) = \mathrm{bd}(A^c)$ and $\mathrm{bd}(A\cup B) \subseteq \mathrm{bd}(A)\cup\mathrm{bd}(B)$ (HW1 Ex 0.3), one shows $\mathcal{FBP}(X)$ is a **boolean algebra of subsets** of $X$:

- complements: $\mathrm{bd}(A^c) = \mathrm{bd}(A)$ finite $\Rightarrow A^c \in \mathcal{FBP}(X)$;
- unions: $\mathrm{bd}(A\cup B) \subseteq \mathrm{bd}(A)\cup\mathrm{bd}(B)$, a finite union of finite sets.

On $X = \mathbb{R}$ with the euclidean topology, every open interval $(a,b)$ lies in $\mathcal{FBP}(\mathbb{R})$ (boundary $= \{a,b\}$), and the semialgebraic subsets of $\mathbb{R}^1$ form a sub-boolean-algebra. But $\mathbb{N}$ does **not** have the finite boundary property ($\mathrm{bd}(\mathbb{N}) = \mathbb{N}$ is infinite), which is the HW1 Ex 0.4 route to showing $\mathbb{N}$ is **not definable** in any o-minimal structure on $\mathbb{R}$.

## Related Concepts
- [[boolean_algebra_of_subsets]]
- [[topological_boundary_nowhere_dense]]
- [[o_minimal_structure]]
