---
id: nno_017
course: Nonsmooth Nonconvex Optimization
tags: [variational-analysis, tangent-cone, set-valued-maps]
difficulty: 3
type: open
status: to_learn
---

# Question
Define the **tangent cone** $T_C(x)$ (tangent bundle) and the **derivable tangent cone** $T_C^{\mathrm{der}}(x)$ of a set $C\subseteq\mathbb{R}^n$. (HW2 Ex 0.8; Rockafellar–Wets Ch. 6)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:**
$$T_C(x) := \limsup_{\tau\downarrow 0} \tau^{-1}(C - x), \qquad T_C^{\mathrm{der}}(x) := \liminf_{\tau\downarrow 0} \tau^{-1}(C - x).$$
$T_C(x)$ is the **tangent cone** (outer limit of difference quotients of the set), $T_C^{\mathrm{der}}(x)$ the **derivable tangent cone** (inner limit).

## Explanation
📖 Wiki: [Variational analysis (Lecture 2)](https://basta.github.io/nno-wiki/lectures/02-variational-analysis) · [Variational analysis revisited (Lecture 9)](https://basta.github.io/nno-wiki/lectures/09-variational-revisited)

Unwinding the outer limit: $v \in T_C(x)$ iff there exist $\tau_k\downarrow 0$ and $x_k\in C$ with $(x_k - x)/\tau_k \to v$. The derivable cone requires this for *every* sequence $\tau\downarrow 0$. Both are **cones** (closed under nonnegative scaling), and $T_C^{\mathrm{der}}(x) \subseteq T_C(x)$ always.

The **tangent/derivable tangent bundles** are the set-valued maps $x \mapsto T_C(x)$, $x \mapsto T_C^{\mathrm{der}}(x)$.

HW2 Ex 0.9:

1. If $C$ is definable in a structure satisfying (S1)–(S4),(O1),(S5)–(S6), then $T_C$ and $T_C^{\mathrm{der}}$ are **definable**.
2. If $\mathcal{R}$ is **o-minimal** ((O2)), then $T_C(x) = T_C^{\mathrm{der}}(x)$ for every $x$ — the two cones coincide, because definable difference quotients have a genuine PK-limit (no oscillation: Curve Selection / Monotonicity).
3. A *non*-o-minimal counterexample where $T_C(x) \ne T_C^{\mathrm{der}}(x)$ (a spiraling/oscillating $C$).

This is the geometric payoff of o-minimality for optimization: tame sets have well-defined tangent geometry everywhere.

## Related Concepts
- [[set_valued_map_inner_outer_limit]]
- [[c1_manifold_tangent_space]]
- [[clarke_subdifferential]]
- [[o_minimal_structure]]
