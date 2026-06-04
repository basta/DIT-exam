---
id: orr_quiz03_04
course: Optimal and Robust Control
tags: [LQ-control, free-final-state, state-feedback, Riccati]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
When the state at the final time is free in the popular LQ-optimal control design (on a finite horizon), the control design based on Riccati equations gives

## Options
A) a state-feedback controller.
B) a precomputed control sequence.
C) an output-feedback controller.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
With a **free final state**, the terminal costate condition is $\boldsymbol{\lambda}_N = \mathbf{S}_N\mathbf{x}_N$. Assuming the linear relation $\boldsymbol{\lambda}_k = \mathbf{S}_k\mathbf{x}_k$ holds at every step and substituting into the necessary conditions yields the **difference Riccati equation** for $\mathbf{S}_k$. The optimal control then takes the **state-feedback** form
$$
\mathbf{u}_k = -\mathbf{K}_k \mathbf{x}_k, \qquad \mathbf{K}_k = (\mathbf{R}+\mathbf{B}^T\mathbf{S}_{k+1}\mathbf{B})^{-1}\mathbf{B}^T\mathbf{S}_{k+1}\mathbf{A}.
$$
This is the celebrated **LQR** result: a (time-varying on a finite horizon) **state-feedback** gain, not an open-loop sequence (B) and not output feedback (C — full state is assumed measurable; output feedback would require an observer, i.e., LQG).

## Related Concepts
- [[Riccati-equation]]
- [[LQR]]
- [[state-feedback]]
