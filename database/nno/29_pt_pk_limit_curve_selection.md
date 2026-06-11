---
id: nno_029
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, variational-analysis, curve-selection, tangent-cone]
difficulty: 4
type: derivation
status: to_learn
---

# Question
**Proof technique.** Show that for a **definable** set $C$ in an o-minimal structure, the inner and outer limits agree, so the **Painlevé–Kuratowski limit** exists and $T_C(x)=T_C^{\mathrm{der}}(x)$. (HW2 Ex 0.7, 0.9)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Definability makes both limits definable (first-order). For equality, use the **Curve Selection Lemma**: any point in the outer limit is reached along a *definable curve*; by the **Monotonicity Theorem** that curve cannot oscillate, so the approach works for *all* small $\tau$, placing the point in the inner limit. Hence inner $=$ outer.

## Explanation
📖 Wiki: [Curve selection](https://basta.github.io/nno-wiki/concepts/curve-selection) · [Monotonicity theorem](https://basta.github.io/nno-wiki/concepts/monotonicity-theorem) · [Variational analysis (Lecture 2)](https://basta.github.io/nno-wiki/lectures/02-variational-analysis)

### Steps / Derivation
1. **Definability of the limits (S1–S4, O1).** The defining formulas for $\limsup$ and $\liminf$ (nested $\forall U\,\exists/\forall t$) are first-order over $\mathrm{gph}\,C$, so both limit maps are definable. This already answers HW2 Ex 0.7(1)/0.9(1).
2. **Outer $\Rightarrow$ inner via Curve Selection.** Let $v\in\limsup$. Then there are $\tau_k\downarrow0$, $x_k\in C$ with $(x_k-x)/\tau_k\to v$. The set of "good" parameters is definable and has $0$ in its closure, so by **Curve Selection** there is a definable curve $\gamma:(0,\varepsilon)\to C$ with $(\gamma(\tau)-x)/\tau\to v$ as $\tau\downarrow0$ along the curve.
3. **No oscillation (Monotonicity).** The definable map $\tau\mapsto(\gamma(\tau)-x)/\tau$ is, near $0$, continuous and monotone in each coordinate (Monotonicity Theorem), so its limit as $\tau\downarrow0$ exists as an honest two-sided limit — it holds for **all** small $\tau$, not just a subsequence.
4. **Conclude.** Therefore $v\in\liminf$. Since $\liminf\subseteq\limsup$ always, the two coincide: the **PK-limit exists**, and applying this to $\tau^{-1}(C-x)$ gives $T_C(x)=T_C^{\mathrm{der}}(x)$ (HW2 Ex 0.9(2)).
5. **Non-o-minimal failure.** Without (O2) the curve can spiral (e.g. via $\sin(1/\tau)$), giving $\liminf\subsetneq\limsup$ and $T_C^{\mathrm{der}}\ne T_C$ (Ex 0.9(3)).

**Techniques to name:** *Curve Selection Lemma* + *Monotonicity Theorem* (= "definable curves have honest one-sided limits, no oscillation").

## Related Concepts
- [[set_valued_map_inner_outer_limit]]
- [[tangent_cone]]
- [[curve_selection]]
- [[monotonicity_theorem]]
