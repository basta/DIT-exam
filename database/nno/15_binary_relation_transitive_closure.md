---
id: nno_015
course: Nonsmooth Nonconvex Optimization
tags: [binary-relations, definability, set-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a **binary relation** and the properties **reflexive / symmetric / transitive**, and the **transitive closure** $A^{\mathrm{tr}}$. (HW2 Ex 0.5)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A **binary relation** on $\mathbb{R}$ is a subset $A \subseteq \mathbb{R}\times\mathbb{R}$. It is **reflexive** if $(x,x)\in A$ for all $x$; **symmetric** if $(x,y)\in A \Rightarrow (y,x)\in A$; **transitive** if $(x,y),(y,z)\in A \Rightarrow (x,z)\in A$. The **transitive closure** $A^{\mathrm{tr}}$ is the smallest transitive relation containing $A$.

## Explanation
📖 Wiki: [Binary relations](https://basta.github.io/nno-wiki/concepts/binary-relations)

Explicitly, the transitive closure is the union over all finite chains:

$$A^{\mathrm{tr}} = \bigcup_{k\ge 1} A^{\circ k}, \qquad A^{\circ k} = \{(x,z) : \exists\, y_1,\dots,y_{k-1},\ (x,y_1),\dots,(y_{k-1},z)\in A\}.$$

**The key subtlety (HW2 Ex 0.5):** $A^{\mathrm{tr}}$ is an *infinite* union of definable sets (one per chain length $k$), and definability is only closed under **finite** boolean operations. So transitive closure is **not** definable in general — there is a definable symmetric reflexive $A$ whose transitive closure is not definable. This is precisely how one defines $\mathbb{Z}$ or $\mathbb{N}$ (chains of unit steps), which o-minimality forbids.

This illustrates the contrast with first-order definability: $A^{\mathrm{tr}}$ is the canonical example of something expressible in *second-order* / least-fixed-point logic but not first-order, hence generally not definable in a structure.

## Related Concepts
- [[definable_set]]
- [[o_minimal_structure]]
- [[universe_of_structures]]
