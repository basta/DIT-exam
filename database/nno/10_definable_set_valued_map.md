---
id: nno_010
course: Nonsmooth Nonconvex Optimization
tags: [definability, set-valued-maps, variational-analysis]
difficulty: 3
type: open
status: to_learn
---

# Question
What is a **definable set-valued map** $F : \mathbb{R}^m \rightrightarrows \mathbb{R}^n$? (HW1 Ex 0.15, HW2 Ex 0.7)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A set-valued map $F : \mathbb{R}^m \rightrightarrows \mathbb{R}^n$ assigns to each $x$ a set $F(x) \subseteq \mathbb{R}^n$. It is **definable in $\mathcal{R}$** if its graph $\mathrm{gph}\,F = \{(x,y) : y \in F(x)\} \subseteq \mathbb{R}^{m+n}$ is a definable set.

## Explanation
Set-valued maps (multifunctions) are the natural language of nonsmooth analysis — subdifferentials, tangent cones, and limit maps are all set-valued. As with ordinary functions, **definability is defined through the graph**.

📖 Wiki: [Definable functions](https://basta.github.io/nno-wiki/concepts/definable-functions) · [Variational analysis (Lecture 2)](https://basta.github.io/nno-wiki/lectures/02-variational-analysis)

Because the graph is just a definable subset of $\mathbb{R}^{m+n}$, all definable operations apply to $F$:

- $F(x)$ for fixed $x$ (a fiber/section) is definable;
- the **domain** $\{x : F(x)\ne\varnothing\}$ and **range** are definable (projections);
- pointwise topological constructions — $\mathrm{cl}\,F(x)$, $\mathrm{int}\,F(x)$ — are definable uniformly in $x$.

HW1 Ex 0.15: if $F$ is definable in a structure satisfying (S1)–(S4) and (O1), then $\{a : F(a)\text{ is nowhere dense in }\mathbb{R}^n\}$ is definable, because "nowhere dense" unwinds to a first-order formula over $\mathrm{gph}\,F$.

This is the framework behind the **outer/inner limits** and the **tangent cone**, which are themselves definable set-valued maps when $C$ is definable (HW2 Ex 0.7–0.9).

## Related Concepts
- [[definable_function]]
- [[set_valued_map_inner_outer_limit]]
- [[tangent_cone]]
- [[clarke_subdifferential]]
