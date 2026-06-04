---
id: orr_quiz07_03
course: Optimal and Robust Control
tags: [time-optimal-control, bang-bang, normality, singular-control]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
The time-optimal control of a linear system exhibits a switching character — so-called "bang-bang" control — it switches between the extreme (minimum and maximum) values of the control signal. A feedback therefore contains a *sign* function. Under which condition(s) is it guaranteed that the input to the sign function cannot be zero for some time interval (i.e., no singular arc)?

## Options
A) Observability of the system.
B) Normality of the system, that is, controllability from every input.
C) Controllability of the system.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
For a linear time-optimal problem, the optimal control is $u^\star(t) = -\operatorname{sign}(\mathbf{b}^T\boldsymbol{\lambda}(t))$. A **singular arc** would occur if the switching function $\mathbf{b}^T\boldsymbol{\lambda}(t)$ stayed **identically zero over a nonzero interval**, leaving the control undefined.

**Normality** of the system rules this out. A system is *normal* if it is **controllable from every individual input channel** (each single-input subsystem $(\mathbf{A},\mathbf{b}_i)$ is controllable). Under normality the switching function can have only **isolated zeros** (the switching instants), never a whole interval of zeros — so the bang-bang control is well defined throughout and switches a finite number of times.

- **Plain controllability (C)** of the multi-input system is necessary but **not sufficient** to forbid singular arcs — normality is the stronger, per-input notion required.
- **Observability (A)** concerns state estimation, unrelated to the switching structure.

## Related Concepts
- [[time-optimal-control]]
- [[bang-bang-control]]
- [[normality]]
- [[singular-arc]]
