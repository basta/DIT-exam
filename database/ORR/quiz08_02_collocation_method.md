---
id: orr_quiz08_02
course: Optimal and Robust Control
tags: [numerical-methods, collocation, direct-methods, discretization]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The numerical method for optimal control based on *collocation* is based on

## Options
A) Discretization of the states both with respect to time and with respect to the values (quantization).
B) Time-discretization of the control signal only, the state variables are solved for numerically using ODE solvers.
C) Time-discretization of both the control signal and the state variables. During the discretization intervals they are both approximated by some polynomials.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
**Collocation** is a *direct transcription* method. It discretizes **both** the control and the state in time and approximates each of them by **polynomials** (e.g., piecewise polynomials / splines) over the discretization intervals. The dynamics $\dot{\mathbf{x}}=f(\mathbf{x},\mathbf{u})$ are then enforced only at selected **collocation points** by requiring the polynomial's derivative to match $f$ there. This converts the optimal control problem into a large but **sparse nonlinear program (NLP)** over the polynomial coefficients (the discretized states and controls).

- **B** describes **(single) shooting**, where only the control is parameterized and the state is obtained by ODE integration — that is *not* collocation.
- **A** describes **quantization of values** (as in dynamic programming on a discretized state grid), not collocation, which discretizes in *time* and keeps continuous values.

## Related Concepts
- [[collocation]]
- [[direct-transcription]]
- [[nonlinear-programming]]
- [[simultaneous-formulation]]
