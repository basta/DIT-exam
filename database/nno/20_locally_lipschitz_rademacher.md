---
id: nno_020
course: Nonsmooth Nonconvex Optimization
tags: [lipschitz, rademacher, nonsmooth-analysis]
difficulty: 3
type: open
status: to_learn
---

# Question
Define **locally Lipschitz** and state **Rademacher's Theorem**. (HW3/4 Ex 0.4)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $f:\mathbb{R}^n\to\mathbb{R}$ is **locally Lipschitz** if every point has a neighborhood $U$ and a constant $L$ with $|f(x)-f(y)|\le L\|x-y\|$ for all $x,y\in U$. **Rademacher's Theorem:** a locally Lipschitz function is **differentiable almost everywhere** (the set of non-differentiability points has Lebesgue measure zero).

## Explanation
📖 Wiki: [Rademacher's theorem](https://basta.github.io/nno-wiki/concepts/rademacher-theorem)

Local Lipschitz continuity is the natural regularity class for nonsmooth optimization: convex functions, max-of-smooth functions, ReLU networks, and norms are all locally Lipschitz but generally not differentiable everywhere.

**Rademacher** guarantees the gradient $\nabla f(x)$ exists for almost every $x$, on a full-measure set $D_f \subseteq \mathbb{R}^n$. This is the foundation that makes the **Clarke subdifferential** well-defined: you take limits of gradients sampled from $D_f$.

**Definability angle (HW3/4 Ex 0.4):** if $f$ is locally Lipschitz **and definable** in a structure satisfying (S1)–(S6), the set $D_f$ of differentiability points is definable and (by o-minimality) co-small — its complement is lower-dimensional, a definable strengthening of "measure zero". This is what lets you prove the Clarke subdifferential is itself **definable**.

**Proof technique to remember:** Rademacher is proved via absolute continuity on a.e. line + Fubini (directional derivatives exist a.e., then patch to full differentiability).

## Related Concepts
- [[clarke_subdifferential]]
- [[frechet_differentiable_c1]]
- [[definable_function]]
