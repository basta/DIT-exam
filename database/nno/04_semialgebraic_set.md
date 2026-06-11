---
id: nno_004
course: Nonsmooth Nonconvex Optimization
tags: [semialgebraic, tame-geometry, definability]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a **semialgebraic set** in $\mathbb{R}^n$.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A set $X \subseteq \mathbb{R}^n$ is **semialgebraic** if it is a finite boolean combination (finite unions, intersections, complements) of sets of the form $\{x \in \mathbb{R}^n : g(x) > 0\}$ and $\{x \in \mathbb{R}^n : g(x) = 0\}$ with $g \in \mathbb{R}[X_1,\dots,X_n]$.

## Explanation
Equivalently, a semialgebraic set is a finite union of sets of the form

$$\{x : p(x)=0,\ q_1(x)>0,\dots,q_k(x)>0\}, \qquad p, q_i \in \mathbb{R}[X_1,\dots,X_n].$$

📖 Wiki: [Semialgebraic sets](https://basta.github.io/nno-wiki/concepts/semialgebraic)

Key facts established in HW1:

- the complement of a semialgebraic set is semialgebraic (Ex 0.6);
- in $\mathbb{R}^1$ a semialgebraic set is exactly a **finite union of intervals and points** (Ex 0.7) — this is the prototype for o-minimality;
- the semialgebraic sets form the smallest o-minimal structure, $\mathbb{R}_{\mathrm{alg}}$ (also generated as a boolean algebra by all the sets $\{g>0\}$).

The deep input is the **Tarski–Seidenberg theorem**: the projection of a semialgebraic set is semialgebraic (closure under $\exists$), which is the model-theoretic content of axiom (S4). This is why $\mathbb{R}_{\mathrm{alg}}$ is a *structure*.

**Why exp is not semialgebraic** (Ex 0.5): a semialgebraic function has finitely many zeros / is eventually monotone-polynomial in growth; $\exp$ has the functional equation and infinitely many intersection properties incompatible with a polynomial graph, e.g. $\Gamma(\exp)$ would have to be a curve $\{f=0\}$ that meets every line $\{y=c\}$ once but is not algebraic.

## Related Concepts
- [[basic_closed_semialgebraic_set]]
- [[structure_axioms_s1_s6]]
- [[universe_of_structures]]
