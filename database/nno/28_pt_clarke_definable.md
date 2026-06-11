---
id: nno_028
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, clarke-subdifferential, definability, nonsmooth-analysis]
difficulty: 4
type: derivation
status: to_learn
---

# Question
**Proof technique.** Sketch why the **Clarke subdifferential** $\partial_C f$ of a definable, locally Lipschitz $f:\mathbb{R}^n\to\mathbb{R}$ is **definable** in any structure satisfying (S1)–(S4),(S5)–(S6). (HW3/4 Ex 0.4)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Definable $+$ locally Lipschitz $\Rightarrow$ (Rademacher) the differentiability set $D_f$ and the gradient map $\nabla f$ on $D_f$ are definable; the limiting-gradient set is a definable **outer limit**; and **convex hull** is definable via Carathéodory (a projection). Composing definable operations stays in the structure.

## Explanation
📖 Wiki: [Clarke subdifferential](https://basta.github.io/nno-wiki/concepts/clarke-subdifferential) · [Rademacher's theorem](https://basta.github.io/nno-wiki/concepts/rademacher-theorem)

Recall $\displaystyle \partial_C f(x)=\mathrm{conv}\big\{\lim_k \nabla f(x_k): x_k\to x,\ x_k\in D_f\big\}$.

### Steps / Derivation
1. **$D_f$ and $\nabla f$ are definable.** "$f$ is differentiable at $x$ with gradient $g$" is a first-order ($\forall\varepsilon\exists\delta$) condition on $\Gamma(f)$. So $D_f=\{x:\exists g,\dots\}$ is definable and the map $x\mapsto\nabla f(x)$ on $D_f$ has definable graph. (Rademacher guarantees $D_f$ is full-measure; o-minimality even makes its complement lower-dimensional.)
2. **Limiting gradients = outer limit.** $G(x):=\{\lim \nabla f(x_k): x_k\to x,\ x_k\in D_f\}=\limsup_{y\to x,\,y\in D_f}\{\nabla f(y)\}$. This is the **outer limit of a definable set-valued map**, hence definable (same machinery as the tangent cone / inner-outer limits).
3. **Convex hull is definable.** By **Carathéodory**, in $\mathbb{R}^n$ every point of $\mathrm{conv}(S)$ is a convex combination of $\le n+1$ points of $S$. So $\mathrm{conv}(G(x))$ is the image of $G(x)^{n+1}\times\Delta_n$ under a definable (polynomial) map — a projection of a definable set, hence definable.
4. **Compose.** $\mathrm{gph}\,\partial_C f$ is built from steps 1–3 by definable operations $\Rightarrow$ definable. Local Lipschitzness keeps $\partial_C f(x)$ nonempty compact.

**Note on hypotheses:** mere (S1)–(S6) already give *definability*; **o-minimality** is what additionally makes $\partial_C f$ nicely **stratified** / generically single-valued (and underlies the chain rule / conservative-field theory).

## Related Concepts
- [[clarke_subdifferential]]
- [[locally_lipschitz_rademacher]]
- [[set_valued_map_inner_outer_limit]]
- [[pt_showing_definability]]
