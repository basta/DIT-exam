---
id: nno_023
course: Nonsmooth Nonconvex Optimization
tags: [manifolds, tangent-space, dimension, geometry]
difficulty: 4
type: open
status: to_learn
---

# Question
Define a **$C^1$-manifold** of dimension $d$ via its **tangent space** $T_M(x)$, and the notion of a **definable homeomorphism onto its image**. (HW3/4 Ex 0.9–0.10)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $M\subseteq\mathbb{R}^n$ is a **$C^1$-manifold of dimension $d$** if each $x\in M$ has a neighborhood in which $M$ is the graph of a $C^1$ map over a $d$-dimensional coordinate plane; equivalently the **tangent space** $T_M(x)$ is a $d$-dimensional linear subspace at every $x\in M$, i.e. $d=\dim_{\mathbb{R}} T_M(x)$. A map $F|_{C'}$ is a **homeomorphism onto its image** if it is a continuous bijection onto $F[C']$ with continuous inverse.

## Explanation
📖 Wiki: [Dimension theorem](https://basta.github.io/nno-wiki/concepts/dimension-theorem) · [Stratifications](https://basta.github.io/nno-wiki/concepts/stratifications) · [Cell decomposition](https://basta.github.io/nno-wiki/concepts/cell-decomposition)

The tangent space here is the *linear* tangent space of smooth geometry — for a manifold it is genuinely a $d$-dimensional subspace (unlike the general tangent **cone** $T_C(x)$ of an arbitrary set, which need not be linear).

HW3/4 Ex 0.9: if $M$ is definable in an o-minimal $\mathcal{R}$ and is a $C^1$-manifold of dimension $d$, then the structure's dimension function gives $\mathrm{d}(M)=d$. (Fails without o-minimality.)

HW3/4 Ex 0.10 (a generic-smoothness / Sard-type statement): for a definable $F:\mathbb{R}^n\to\mathbb{R}^n$ and a nonempty definable open $C$, there is a nonempty definable open $C'\subseteq C$ such that **either** $F|_{C'}$ is a homeomorphism onto its image, **or** $\dim F[C'] < n$. Proof technique: cell decomposition of the definable map $F$ into finitely many pieces on which it has constant rank; on full-rank cells it is a local homeomorphism, on the rest the image drops dimension.

This is the geometric capstone: o-minimality forces definable maps to be "tame" — piecewise diffeomorphisms up to lower-dimensional exceptional sets.

## Related Concepts
- [[dimension_function]]
- [[tangent_cone]]
- [[stratifications]]
- [[cell_decomposition]]
