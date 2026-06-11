---
id: nno_021
course: Nonsmooth Nonconvex Optimization
tags: [clarke-subdifferential, nonsmooth-analysis, generalized-gradient]
difficulty: 4
type: open
status: to_learn
---

# Question
Define the **Clarke subdifferential** (generalized gradient) of a locally Lipschitz $f:\mathbb{R}^n\to\mathbb{R}$, and sketch why it is **definable** when $f$ is. (HW3/4 Ex 0.4)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Let $D_f$ be the full-measure set where $f$ is differentiable (Rademacher). The **Clarke subdifferential** is
$$\partial_C f(x) := \mathrm{conv}\Big\{ \lim_{k\to\infty} \nabla f(x_k) \ :\ x_k \to x,\ x_k \in D_f \Big\},$$
the convex hull of all limits of nearby gradients.

## Explanation
📖 Wiki: [Clarke subdifferential](https://basta.github.io/nno-wiki/concepts/clarke-subdifferential) · [Subgradients](https://basta.github.io/nno-wiki/concepts/subgradients) · [Clarke regularity](https://basta.github.io/nno-wiki/concepts/clarke-regularity)

$\partial_C f(x)$ is a nonempty, convex, compact set; when $f$ is $C^1$ it reduces to $\{\nabla f(x)\}$; for convex $f$ it equals the convex-analysis subdifferential. It is the standard stationarity object for nonsmooth nonconvex optimization: $0\in\partial_C f(x)$ defines a **Clarke-stationary** point.

**Why $\partial_C f$ is definable when $f$ is (HW3/4 Ex 0.4 — the key exam argument):** assume $\mathcal{R}$ satisfies (S1)–(S4) and (S5)–(S6) and $f$ is definable and locally Lipschitz.

1. $D_f$ and the gradient map $x\mapsto \nabla f(x)$ on $D_f$ are **definable** (differentiability and the limit defining $\nabla f$ are first-order conditions).
2. The **limiting gradients** set $\{\lim \nabla f(x_k) : x_k\to x,\ x_k\in D_f\}$ is an **outer limit** of a definable set-valued map, hence definable (same machinery as the tangent cone).
3. The **convex hull** of a definable set is definable: in $\mathbb{R}^n$, $\mathrm{conv}(S)$ needs only $n+1$ points (Carathéodory), so it is a projection of a definable set — a finite first-order construction.

Composing definable operations keeps you inside the structure, so $\mathrm{gph}\,\partial_C f$ is definable. (O-minimality is then what makes it *nicely* stratified, but mere (S1)–(S6) already give definability.)

## Related Concepts
- [[locally_lipschitz_rademacher]]
- [[subgradients]]
- [[set_valued_map_inner_outer_limit]]
- [[clarke_regularity]]
