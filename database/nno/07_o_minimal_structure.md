---
id: nno_007
course: Nonsmooth Nonconvex Optimization
tags: [o-minimal, structures, model-theory, axioms]
difficulty: 3
type: open
status: to_learn
---

# Question
State axioms **(O1)–(O2)** and give the full definition of an **o-minimal structure** on $\mathbb{R}$. (HW3/4 Ex 0.1)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** An **o-minimal structure** is a structure $\mathcal{R}$ on $\mathbb{R}$ (satisfying (S1)–(S6)) that additionally satisfies (O1): the singleton $\{a\} \in \mathcal{R}_1$ for some/any $a$ (or: every interval is definable), and (O2): every definable subset of $\mathbb{R}^1$ is a **finite union of points and open intervals**.

## Explanation
The "o" is for *order*: o-minimality says the definable subsets of the line are as simple as possible.

- **(O1)** $\{(x,y) : x < y\}$-style intervals / singletons are definable (often folded into (S5)); concretely each $\{a\} \in \mathcal{R}_1$.
- **(O2)** Every $A \in \mathcal{R}_1$ is a **finite union of points and open intervals** (equivalently: every definable subset of $\mathbb{R}$ has finitely many connected components).

📖 Wiki: [o-minimal structures](https://basta.github.io/nno-wiki/concepts/o-minimal-structures) · [Tame geometry](https://basta.github.io/nno-wiki/concepts/tame-geometry)

The miracle is that this one-dimensional tameness propagates to all dimensions (cell decomposition, monotonicity theorem, finiteness of components, dimension theory). Consequences you should be able to cite:

- **Monotonicity theorem:** a definable $f:(a,b)\to\mathbb{R}$ is piecewise continuous and monotone.
- **Cell decomposition:** every definable set partitions into finitely many cells.
- definable sets have a well-defined **dimension**, and $\dim(\mathrm{bd}\,A) < \dim A$.

The full hierarchy: (S1)–(S4) = structure; +(S5),(S6) = expands real field; +(O1),(O2) = **o-minimal**. $\mathbb{N}$ is not definable in any o-minimal structure (it would violate (O2)).

## Related Concepts
- [[structure_axioms_s1_s6]]
- [[finite_boundary_property]]
- [[dimension_function]]
- [[universe_of_structures]]
