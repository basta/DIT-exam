---
id: nno_026
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, definability, o-minimal, transitive-closure]
difficulty: 3
type: derivation
status: to_learn
---

# Question
**Proof technique.** Show $\mathbb{N}$ (or $\mathbb{Z}$) is **not definable** in any o-minimal structure, and that **transitive closure** is not definable in general. (HW1 Ex 0.4, HW2 Ex 0.5)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $\mathbb{N}\subseteq\mathbb{R}$ is infinite and discrete, so it is *not* a finite union of points and intervals — it violates axiom (O2). Transitive closure $A^{\mathrm{tr}}=\bigcup_{k\ge1}A^{\circ k}$ is an infinite union (one term per chain length), outside the finite first-order toolkit; a definable $A$ whose closure encodes $\mathbb{N}$ shows it can fail to be definable.

## Explanation
📖 Wiki: [o-minimal structures](https://basta.github.io/nno-wiki/concepts/o-minimal-structures) · [Binary relations](https://basta.github.io/nno-wiki/concepts/binary-relations)

### Steps / Derivation
1. **$\mathbb{N}$ not definable (o-minimal case):** by (O2) every definable subset of $\mathbb{R}$ is a finite union of points and open intervals. $\mathbb{N}$ is infinite with empty interior, so not such a union. Done.
2. **$\mathbb{N}$ not definable (topological route, HW1 Ex 0.4):** $\mathrm{bd}(\mathbb{N})=\mathbb{N}$ is infinite, so $\mathbb{N}\notin\mathcal{FBP}(\mathbb{R})$; in an o-minimal structure definable subsets of $\mathbb{R}$ do have finite boundary, contradiction.
3. **Transitive closure (HW2 Ex 0.5):** take $A = \{(x,y): y = x+1\}\cup\{(x,y): y=x-1\}$ (or restrict suitably) — symmetric, definable. Its transitive closure $A^{\mathrm{tr}}$ relates $x$ to $x+k$ for all $k\in\mathbb{Z}$; the fiber $\{y:(0,y)\in A^{\mathrm{tr}}\}=\mathbb{Z}$ is infinite discrete. If $A^{\mathrm{tr}}$ were definable, $\mathbb{Z}$ would be too — impossible in an o-minimal structure.
4. **Moral / technique:** definability is closed only under **finite** boolean ops + **single** quantifiers. Transitive closure is a **least-fixed-point** (second-order) operation; exhibiting that it would define an infinite discrete set is the standard refutation.

**Contrast:** in *some* non-o-minimal structures (e.g. $\mathbb{R}_{\mathrm{PH}}=(\mathbb{R}_{\mathrm{alg}},\sin)$) you *can* define $\mathbb{Z}=\sin^{-1}(0)/\pi$ — which is exactly why they fail o-minimality.

## Related Concepts
- [[binary_relation_transitive_closure]]
- [[finite_boundary_property]]
- [[o_minimal_structure]]
- [[universe_of_structures]]
