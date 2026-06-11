---
id: orr_quiz02_05
course: Optimal and Robust Control
tags: [MPC, receding-horizon, constraints]
difficulty: 1
type: multiple_choice
status: to_learn
---

# Question
The key advantage of the control strategy known as Model Predictive Control (MPC) or also as Receding Horizon Control (RHC) is

## Options
A) low computational requirements compared to majority of (classical) control strategies.
B) the capability to handle the constraints on the controls and states explicitly.
C) the optimization can be done in real-time and it does not need the mathematical model of the system.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
MPC's defining strength is that it **explicitly incorporates constraints** on inputs (actuator limits, slew rates) and states/outputs (safety/operating limits) directly into the optimization solved at each step. Classical controllers (PID, loop shaping) handle constraints only indirectly (e.g., anti-windup) and cannot anticipate them.

- **A is false:** MPC is *computationally expensive* — it solves an optimization problem (typically a QP) at every sampling instant.
- **C is false:** MPC is fundamentally **model-based** — it predicts the future response using a model of the system; without a model there is nothing to optimize over.

## Related Concepts
- [[model-predictive-control]]
- [[receding-horizon-control]]
- [[constraint-handling]]
