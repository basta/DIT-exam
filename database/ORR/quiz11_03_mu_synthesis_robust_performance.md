---
id: orr_quiz11_03
course: Optimal and Robust Control
tags: [mu-synthesis, robust-performance, structured-uncertainty, DK-iteration]
difficulty: 5
type: multiple_choice
status: to_learn
---

# Question
A computational procedure called *$\mu$-synthesis* provides a feedback controller that makes the closed-loop system robustly stable with respect to structured uncertainty. However, robust stability is not enough for a realistic project — robust performance is also needed. Can $\mu$-synthesis be used for designing such a controller? If yes, how?

## Options
A) No, $\mu$-synthesis is a procedure for designing a robustly stabilizing controller only; it does not have the capability to take performance requirements into consideration.
B) Yes, $\mu$-synthesis can be used to design a feedback controller that guarantees robust performance. The way to do it is to include in the description of uncertainty an artificial uncertainty term that corresponds to the performance requirements expressed in the form of a bound on the $\mathcal{H}_\infty$ norm.
C) Yes, $\mu$-synthesis can be used to "robustify" a performance-guaranteeing controller already designed by some other method (LQG, ...). In particular, $\mu$-synthesis provides another component plugged in series with the original controller.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
A key theoretical result of robust control is that **robust performance can be recast as robust stability against an enlarged, structured uncertainty**. One appends a **fictitious "performance" uncertainty block** $\Delta_P$ (full, norm-bounded, $\|\Delta_P\|_\infty\le 1$) that connects the performance output $z$ back to the exogenous input $w$. Then:
$$
\text{robust performance} \iff \mu_{\hat\Delta}\big(\mathcal{F}_u(\cdot)\big) < 1, \quad \hat\Delta = \operatorname{diag}(\Delta,\ \Delta_P).
$$
With this augmented block structure, the **structured singular value $\mu$** test for robust *stability* against $\hat\Delta$ is equivalent to robust *performance* against the real uncertainty $\Delta$. $\mu$-synthesis (e.g. **D–K iteration**, alternating $\mathcal{H}_\infty$ controller synthesis with $D$-scale fitting) then directly designs a single controller achieving robust performance.

- **A is wrong:** $\mu$-synthesis explicitly *does* handle performance, via the artificial performance block.
- **C is wrong:** $\mu$-synthesis designs **one** controller from the augmented problem; it is not a series add-on that "robustifies" a pre-existing LQG controller.

## Related Concepts
- [[mu-synthesis]]
- [[structured-singular-value]]
- [[robust-performance]]
- [[DK-iteration]]
