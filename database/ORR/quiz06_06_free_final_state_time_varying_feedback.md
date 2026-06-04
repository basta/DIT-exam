---
id: orr_quiz06_06
course: Optimal and Robust Control
tags: [LQ-control, free-final-state, time-varying-feedback, Riccati]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
The LQ-optimal controller for a **free final state** and a **fixed final time** is

## Options
A) a time-invariant state feedback controller.
B) open-loop control, that is, a precomputed signal (or a function of time).
C) a time-varying state feedback controller.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
With a **free final state** the optimal control is a **state feedback** $\mathbf{u}(t) = -\mathbf{K}(t)\mathbf{x}(t)$, where the gain comes from the solution $\mathbf{S}(t)$ of the **differential Riccati equation** integrated backward from the terminal weight $\mathbf{S}(t_f)$. Because the horizon is **finite** ($t_f$ fixed and approaching), $\mathbf{S}(t)$ — and hence the gain $\mathbf{K}(t)$ — is **time-varying**.

- **A (time-invariant feedback)** is the **infinite-horizon** result, where $\mathbf{S}$ reaches the constant stabilizing solution of the *algebraic* Riccati equation and $\mathbf{K}$ is constant.
- **B (open-loop)** is the *fixed* final-state case.

So: free final state + finite horizon $\Rightarrow$ **time-varying state feedback**.

## Related Concepts
- [[differential-Riccati-equation]]
- [[finite-horizon-LQR]]
- [[time-varying-gain]]
