---
id: nno_008
course: Nonsmooth Nonconvex Optimization
tags: [definability, structures, model-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
What is a **definable set** in a structure $\mathcal{R}$? Describe strategies for showing a set is definable. (HW3/4 Ex 0.2)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A set $A \subseteq \mathbb{R}^n$ is **definable in $\mathcal{R}$** if $A \in \mathcal{R}_n$. Equivalently, $A$ is definable iff it can be described by a first-order formula in the language of $\mathcal{R}$ (boolean combinations of the basic relations, with quantifiers).

## Explanation
"Definable" just means "is a member of the structure". Because a structure is closed under the boolean operations, products, projections, diagonals, and contains the field operations and order, definability is preserved by all first-order constructions.

📖 Wiki: [Definable sets](https://basta.github.io/nno-wiki/concepts/definable-sets)

**Strategies to prove a set $A$ is definable** (HW3/4 Ex 0.2 explicitly asks for these):

1. **Boolean combinations** — finite $\cap, \cup, {}^c$ of definable sets are definable (S1).
2. **Adding/permuting variables** — cylinders $A\times\mathbb{R}$ and diagonals are definable (S2, S3).
3. **Projection = existential quantifier** — if $\{(x,y): \varphi(x,y)\}$ is definable, so is $\{x : \exists y\,\varphi(x,y)\}$ (S4). Universal $\forall$ comes via $\neg\exists\neg$.
4. **Polynomial / field operations and order** are available (S5, S6), so any semialgebraic condition is definable.
5. **Composition** — preimages/images under definable functions are definable.
6. **Reduce to a known definable function** — show $A$ is built from $\exp$, $\sin|_{[a,b]}$, a Pfaffian function, etc., that is already known to be definable in $\mathcal{R}$.

Example (HW1 Ex 0.15): the set $\{a : F(a) \text{ is nowhere dense}\}$ for a definable set-valued map $F$ is definable, by writing "nowhere dense" as a first-order condition about the closure and interior.

## Related Concepts
- [[definable_function]]
- [[definable_set_valued_map]]
- [[structure_axioms_s1_s6]]
- [[o_minimal_structure]]
