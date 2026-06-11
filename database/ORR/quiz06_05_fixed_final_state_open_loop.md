---
id: orr_quiz06_05
course: Optimal and Robust Control
tags: [LQ-control, fixed-final-state, open-loop]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
If we consider an LQ-optimal control on a fixed time interval with the value of the final state **fixed**, the optimal control is

## Options
A) time-varying state feedback control.
B) time-invariant state feedback control.
C) open-loop control, that is, a precomputed signal (or function of time).
D) —

---
# Solution
**Correct Answer:** C

## Explanation
When the final state is **fixed**, the problem becomes a point-to-point transfer determined by *both* endpoints. Solving the two-point boundary value problem yields a trajectory-specific solution: an **open-loop control signal** (a precomputed function of time) that drives the given initial state exactly to the required final state.

The clean **state-feedback** structure $\mathbf{u}=-\mathbf{K}(t)\mathbf{x}$ arises only when the final state is *free* (terminal cost $\mathbf{S}\mathbf{x}(t_f)$), because then $\boldsymbol{\lambda}(t)=\mathbf{S}(t)\mathbf{x}(t)$ and the control becomes a function of the current state. Fixing the endpoint breaks that and gives open-loop control. (See also the continuous-time analogue of quiz #3 Q3.)

## Related Concepts
- [[open-loop-control]]
- [[fixed-final-state]]
- [[boundary-value-problem]]
