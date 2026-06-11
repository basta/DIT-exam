---
id: nno_005
course: Nonsmooth Nonconvex Optimization
tags: [semialgebraic, tame-geometry]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a **basic closed semialgebraic** subset of $\mathbb{R}^n$. (HW1, stated definition)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A **basic closed semialgebraic** set is a set of the form
$$\bigcap_{i=1}^{r} \{x \in \mathbb{R}^n : g_i(x) \ge 0\}, \qquad g_i \in \mathbb{R}[X_1,\dots,X_n].$$

## Explanation
A basic closed semialgebraic set is a finite intersection of polynomial "$\ge 0$" sublevel-type sets — the closed building blocks of semialgebraic geometry.

📖 Wiki: [Semialgebraic sets](https://basta.github.io/nno-wiki/concepts/semialgebraic)

Contrast with the general semialgebraic sets (which also allow strict inequalities and complements). Important subtleties from HW1:

- Every basic closed semialgebraic set **is topologically closed** (finite intersection of closed sets), and more generally the collection $\mathcal{D}_n$ of finite unions of basic closed semialgebraic sets equals the **closed** semialgebraic sets (HW1 Ex 0.12–0.13).
- Not every closed semialgebraic set is *basic* closed: $\{x \ge 0\} \cup \{y \ge 0\} \subseteq \mathbb{R}^2$ is closed semialgebraic but **not** basic closed (HW1 Ex 0.11) — you cannot cut it out by a single conjunction of polynomial inequalities.
- The family $\mathcal{D} = (\mathcal{D}_n)$ satisfies axioms (S2),(S3),(S5),(S6) but fails (S1),(S4),(O1),(O2): it is not closed under complement or projection, showing why "closed sets only" is *not* a structure.

## Related Concepts
- [[semialgebraic_set]]
- [[structure_axioms_s1_s6]]
- [[boolean_algebra_of_subsets]]
