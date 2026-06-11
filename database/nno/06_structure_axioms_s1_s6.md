---
id: nno_006
course: Nonsmooth Nonconvex Optimization
tags: [structures, model-theory, axioms, definability]
difficulty: 3
type: open
status: to_learn
---

# Question
State the axioms **(S1)–(S6)** defining a **structure on $\mathbb{R}$**. (HW3/4 Ex 0.1)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A structure on $\mathbb{R}$ is a sequence $\mathcal{R} = (\mathcal{R}_n)_{n\ge 0}$ where each $\mathcal{R}_n \subseteq \mathcal{P}(\mathbb{R}^n)$, such that the $\mathcal{R}_n$ form boolean algebras containing the diagonals, are stable under products and coordinate projection, and contain the order and the graphs of $+$ and $\cdot$.

## Explanation
A **structure** is a system of collections of subsets ("definable sets") of each $\mathbb{R}^n$, closed under the logical operations. The standard axiomatization:

- **(S1)** Each $\mathcal{R}_n$ is a **boolean algebra** of subsets of $\mathbb{R}^n$ (closed under $\cap, \cup, {}^c$).
- **(S2)** If $A \in \mathcal{R}_n$ then $A \times \mathbb{R} \in \mathcal{R}_{n+1}$ and $\mathbb{R} \times A \in \mathcal{R}_{n+1}$ (stable under **products / cylinders**).
- **(S3)** Each diagonal $\Delta_{ij} = \{x \in \mathbb{R}^n : x_i = x_j\} \in \mathcal{R}_n$.
- **(S4)** $\mathcal{R}$ is stable under **projection** $\pi : \mathbb{R}^{n+1} \to \mathbb{R}^n$ (dropping a coordinate) — the model-theoretic $\exists$, i.e. Tarski–Seidenberg.
- **(S5)** The order $\{(x,y) : x < y\} \in \mathcal{R}_2$.
- **(S6)** The graphs of addition $\{(x,y,z): x+y=z\}$ and multiplication $\{(x,y,z): x\cdot y = z\}$ are in $\mathcal{R}_3$.

📖 Wiki: [Structures](https://basta.github.io/nno-wiki/concepts/structures) · [Definable sets](https://basta.github.io/nno-wiki/concepts/definable-sets)

(S1)–(S4) make $\mathcal{R}$ a structure in the bare logical sense; (S5)–(S6) say it **expands the real ordered field** $\mathbb{R}_{\mathrm{alg}}$, so every semialgebraic set is definable. The smallest structure satisfying all of (S1)–(S6) is $\mathbb{R}_{\mathrm{alg}}$ itself.

**Proof technique** for "this set is definable": build it from definable pieces using exactly these closure operations — boolean combinations (S1), adding dummy variables (S2), equalities (S3), existential quantifiers = projections (S4), inequalities (S5), polynomial arithmetic (S6).

## Related Concepts
- [[o_minimal_structure]]
- [[definable_set]]
- [[semialgebraic_set]]
- [[universe_of_structures]]
