---
id: nno_022
course: Nonsmooth Nonconvex Optimization
tags: [dimension, o-minimal, tame-geometry]
difficulty: 4
type: open
status: to_learn
---

# Question
Define a **dimension function** on a structure $\mathcal{R}$, and state its values on a linear subspace and a $C^1$-manifold. (HW3/4 Ex 0.8–0.9)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A **dimension function** $\mathrm{d}$ assigns to each nonempty definable set $A$ an integer $\mathrm{d}(A)\in\{0,\dots,n\}$ that is monotone ($A\subseteq B \Rightarrow \mathrm{d}(A)\le\mathrm{d}(B)$), additive under finite unions ($\mathrm{d}(A\cup B)=\max(\mathrm{d}(A),\mathrm{d}(B))$), invariant under definable bijections, and normalized so that $\mathrm{d}(\mathbb{R}^n)=n$ and $\dim\{pt\}=0$.

## Explanation
📖 Wiki: [Dimension theorem](https://basta.github.io/nno-wiki/concepts/dimension-theorem) · [Cells](https://basta.github.io/nno-wiki/concepts/cells) · [Cell decomposition](https://basta.github.io/nno-wiki/concepts/cell-decomposition)

In an o-minimal structure the dimension of a definable set is unambiguous (every reasonable definition — maximal coordinate projection, dimension of a cell decomposition, topological/manifold dimension — agrees). Core properties:

- $\dim(\mathrm{cl}\,A \setminus A) < \dim A$ and $\dim(\mathrm{bd}\,A) < \dim A$ (boundaries are lower-dimensional — the tame analog of "nowhere dense").
- $\dim(A\times B) = \dim A + \dim B$.

HW3/4 Ex 0.8: for an $\mathbb{R}$-linear subspace $V\subseteq\mathbb{R}^n$, $V$ is definable (it's the solution set of linear equations) and any dimension function gives
$$\mathrm{d}(V) = \dim_{\mathbb{R}} V,$$
the usual linear-algebra dimension.

HW3/4 Ex 0.9: for a definable $C^1$-manifold $M$ of dimension $d$ (i.e. $d=\dim_{\mathbb{R}} T_M(x)$ for all $x\in M$), $\mathrm{d}(M)=d$ — but this *requires* o-minimality; without it the manifold dimension and a structure's dimension function can disagree.

## Related Concepts
- [[c1_manifold_tangent_space]]
- [[cells]]
- [[topological_boundary_nowhere_dense]]
- [[o_minimal_structure]]
