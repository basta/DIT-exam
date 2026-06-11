---
id: nno_031
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, dimension, manifolds, o-minimal]
difficulty: 4
type: derivation
status: to_learn
---

# Question
**Proof technique.** Show that for a definable $C^1$-manifold $M$ of dimension $d$ in an o-minimal structure, the dimension function gives $\mathrm{d}(M)=d$, and that $\dim(\mathrm{bd}\,A)<\dim A$. (HW3/4 Ex 0.8–0.9)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Cell-decompose $M$; locally $M$ is the graph of a $C^1$ map over a $d$-plane, a $d$-cell, so its max cell dimension (= the dimension function) is $d$. For boundaries, $\mathrm{cl}(A)\setminus A$ is a definable set containing no relatively-open piece of $\dim A$, so by cell decomposition it sits in strictly lower-dimensional cells.

## Explanation
📖 Wiki: [Dimension theorem](https://basta.github.io/nno-wiki/concepts/dimension-theorem) · [Cells](https://basta.github.io/nno-wiki/concepts/cells)

### Steps / Derivation
1. **Dimension = top cell dimension.** In an o-minimal structure define $\mathrm{d}(A)$ as the maximal dimension of a cell in a cell decomposition of $A$; this is well-defined (independent of decomposition) and invariant under definable bijections.
2. **$\mathrm{d}(M)=d$ (Ex 0.9).** Each point of the $C^1$-manifold $M$ has a neighborhood where $M$ is the graph of a $C^1$ function over an open subset of a $d$-dimensional coordinate plane (since $\dim_{\mathbb{R}}T_M(x)=d$). A graph over a $d$-cell is a $d$-cell, so $M$ is covered by $d$-cells and contains no $(d{+}1)$-cell $\Rightarrow \mathrm{d}(M)=d$. **Without o-minimality** dimension is not well-defined (a definable bijection $\mathbb{R}\to\mathbb{R}^2$ could exist), so the equality can fail.
3. **$\mathrm{d}(V)=\dim_{\mathbb{R}}V$ (Ex 0.8).** A linear subspace is an affine cell of linear dimension $\dim_{\mathbb{R}}V$; the two notions coincide.
4. **$\dim(\mathrm{bd}\,A)<\dim A$ (the "frontier" inequality).** $\mathrm{cl}(A)\setminus A$ is definable; if it contained a cell of dimension $\dim A$, that cell would be a relatively-open subset accumulating on $A$, contradicting that $A$ already realizes its own dimension on an open-in-$A$ cell. So the frontier lives in cells of dimension $<\dim A$. This is the tame analog of "boundaries are nowhere dense."

**Techniques to name:** *cell decomposition*, *graphs of $C^1$ maps are cells*, *frontier inequality*.

## Related Concepts
- [[dimension_function]]
- [[c1_manifold_tangent_space]]
- [[topological_boundary_nowhere_dense]]
- [[cells]]
