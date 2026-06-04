---
id: orr_quiz02_07
course: Optimal and Robust Control
tags: [MPC, tracking, control-increments, integral-action]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The need for replacing control signals by their increments in tracking MPC is due to the fact that

## Options
A) at steady state the tracking error is desired to be zero while control signal itself is nonzero.
B) the computational load is then reduced as only increments need to be considered in the optimization.
C) the increments in the control are what actually needs to be penalized, not the control signal itself.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
In a tracking problem, at steady state we want the **output error to be zero**, but the **control input is generally nonzero** (it must hold the plant at the desired operating point, e.g., a nonzero valve opening to maintain a setpoint). If the cost penalizes $\mathbf{u}$ directly toward zero, it fights against the nonzero steady-state input and produces a steady-state offset.

By reformulating in terms of **control increments** $\Delta\mathbf{u}_k = \mathbf{u}_k - \mathbf{u}_{k-1}$ (and augmenting the state with $\mathbf{u}_{k-1}$), the penalty pushes $\Delta\mathbf{u}\to 0$ at steady state — which is exactly what we want — while the actual control $\mathbf{u}$ can settle at whatever nonzero value is needed. This effectively introduces **integral action**, eliminating steady-state tracking error.

- **B is false:** it does not reduce computation (the state is augmented).
- **C is false:** penalizing increments is a means to remove offset, not a fundamental goal in itself.

## Related Concepts
- [[tracking-MPC]]
- [[integral-action]]
- [[velocity-form]]
