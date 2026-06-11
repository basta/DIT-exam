---
id: nno_012
course: Nonsmooth Nonconvex Optimization
tags: [o-minimal, growth, structures, field-of-exponents]
difficulty: 4
type: open
status: to_learn
---

# Question
Define the **field of exponents** of a (polynomially bounded) o-minimal structure. (HW3/4 Ex 0.3)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The **field of exponents** of an o-minimal structure $\mathcal{R}$ is the set of all $\lambda \in \mathbb{R}$ such that the power function $x \mapsto x^{\lambda}$ (on $(0,\infty)$) is definable in $\mathcal{R}$. By the Growth Dichotomy this set is a subfield of $\mathbb{R}$.

## Explanation
The field of exponents measures *which real powers* a polynomially bounded structure can "see".

📖 Wiki: [Universe of structures](https://basta.github.io/nno-wiki/concepts/universe-of-structures)

Key facts:

- For a **polynomially bounded** o-minimal $\mathcal{R}$, Miller's theorem says the set $K = \{\lambda : x^\lambda \text{ definable}\}$ is a **field** $\subseteq \mathbb{R}$, and every definable $f:\mathbb{R}\to\mathbb{R}$ has a Puiseux-like leading term $c\,x^\lambda$ with $\lambda \in K$.
- $\mathbb{R}_{\mathrm{alg}}$ has field of exponents $\mathbb{Q}$ (only rational powers via roots of polynomials).
- $\mathbb{R}_{\mathrm{an}}$ also has field of exponents $\mathbb{Q}$.
- A structure can be engineered to have any given real-closed subfield (or even all of $\mathbb{R}$) as its field of exponents while remaining polynomially bounded.
- Once $\exp$ is definable (e.g. $\mathbb{R}_{\exp}$), the structure is **not** polynomially bounded and "field of exponents" in this sense is no longer the right invariant.

This is exactly the data HW3/4 Ex 0.3 asks you to annotate on the "universe of structures" picture: for each structure, mark o-minimal / polynomially bounded / exponentially bounded and its field of exponents.

## Related Concepts
- [[polynomially_exponentially_bounded]]
- [[universe_of_structures]]
- [[o_minimal_structure]]
