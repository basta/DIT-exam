---
id: nno_016
course: Nonsmooth Nonconvex Optimization
tags: [variational-analysis, set-valued-maps, limits, painleve-kuratowski]
difficulty: 3
type: open
status: to_learn
---

# Question
Define the **outer limit** $\limsup_{t\downarrow 0} C_t$, the **inner limit** $\liminf_{t\downarrow 0} C_t$, and the **Painlevé–Kuratowski limit** of a set-valued map $C:(0,\infty)\rightrightarrows\mathbb{R}^n$. (HW2, stated; Rockafellar–Wets Ch. 4)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:**
$$\limsup_{t\downarrow 0} C_t := \{x : \forall\,U\ni x\ \text{nbhd},\ \forall\, t'>0,\ \exists\, 0<t''<t',\ C_{t''}\cap U \ne \varnothing\},$$
$$\liminf_{t\downarrow 0} C_t := \{x : \forall\,U\ni x\ \text{nbhd},\ \exists\, t'>0,\ \forall\, 0<t''<t',\ C_{t''}\cap U \ne \varnothing\}.$$
When they agree, the common set is the **Painlevé–Kuratowski limit** $\lim_{t\downarrow 0} C_t$.

## Explanation
📖 Wiki: [Variational analysis (Lecture 2)](https://basta.github.io/nno-wiki/lectures/02-variational-analysis)

Intuition:

- **Outer limit** = cluster points: $x$ is approached by points of $C_{t}$ along *some* sequence $t\downarrow 0$ ("$\exists$ a subsequence").
- **Inner limit** = limit points: every neighborhood of $x$ meets $C_t$ for *all* small $t$ ("for all sequences eventually"). Always $\liminf \subseteq \limsup$.
- **PK-limit** exists iff inner $=$ outer; both limit sets are automatically **closed**.

HW2 Ex 0.7: if $\mathcal{R}$ satisfies (S1)–(S4),(O1) and $C$ is definable, then both $\limsup$ and $\liminf$ are **definable** (the quantifier strings above are first-order over $\mathrm{gph}\,C$). If $\mathcal{R}$ is additionally **o-minimal** ((O2),(S5),(S6)), then **the PK-limit exists**, i.e. $\limsup = \liminf$ — definable curves cannot oscillate, by the Monotonicity Theorem / Curve Selection. Ex 0.7(3) asks for a *non*-o-minimal example where they differ (e.g. $C_t$ built from $\sin(1/t)$).

This is the engine behind the tangent cone (next card).

## Related Concepts
- [[definable_set_valued_map]]
- [[tangent_cone]]
- [[monotonicity_theorem]]
- [[curve_selection]]
