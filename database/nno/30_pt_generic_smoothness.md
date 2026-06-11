---
id: nno_030
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, cell-decomposition, dimension, generic-smoothness]
difficulty: 4
type: derivation
status: to_learn
---

# Question
**Proof technique.** For a definable $F:\mathbb{R}^n\to\mathbb{R}^n$ and nonempty definable open $C$, show there is a nonempty definable open $C'\subseteq C$ such that **either** $F|_{C'}$ is a homeomorphism onto its image **or** $\dim F[C']<n$. (HW3/4 Ex 0.10)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Apply **cell decomposition** to $F$ so it is $C^1$ on each cell; on a top-dimensional cell the Jacobian rank is constant. If rank $=n$ somewhere, the **inverse function theorem** gives an open $C'$ on which $F$ is a diffeomorphism (homeomorphism onto image); if rank $<n$ everywhere on the cell, $F[C']$ has dimension $<n$.

## Explanation
📖 Wiki: [Cell decomposition](https://basta.github.io/nno-wiki/concepts/cell-decomposition) · [Dimension theorem](https://basta.github.io/nno-wiki/concepts/dimension-theorem) · [Stratifications](https://basta.github.io/nno-wiki/concepts/stratifications)

### Steps / Derivation
1. **$C^k$ cell decomposition.** In an o-minimal structure, $\mathbb{R}^n$ (and the definable map $F$) admit a finite partition into definable $C^1$ **cells** on each of which $F$ is $C^1$. Pick a cell $D$ that is open (top-dimensional) and contained in $C$ — exists because $C$ is open and the open cells cover a dense definable subset.
2. **Constant rank.** Shrinking $D$ to a definable open $C'$, the Jacobian rank $r=\mathrm{rank}\,DF$ is **constant** (the rank-drop locus is definable and lower-dimensional, so avoid it).
3. **Case $r=n$.** $DF(x)$ invertible on $C'$ $\Rightarrow$ by the inverse function theorem $F$ is locally a $C^1$-diffeomorphism; shrinking to where it is injective (again a definable open set), $F|_{C'}$ is a **homeomorphism onto its image**.
4. **Case $r<n$.** Constant rank $r<n$ $\Rightarrow$ (rank theorem) $F[C']$ is locally a $C^1$-manifold of dimension $r<n$, so $\dim F[C']\le r<n$.
5. **Conclude** the dichotomy.

This is the o-minimal **generic smoothness / Sard-type** statement: definable maps are piecewise diffeomorphisms up to a lower-dimensional exceptional set. **Techniques to name:** *cell decomposition + constant-rank/inverse-function theorem + dimension of image.*

## Related Concepts
- [[c1_manifold_tangent_space]]
- [[dimension_function]]
- [[cell_decomposition]]
- [[cells]]
