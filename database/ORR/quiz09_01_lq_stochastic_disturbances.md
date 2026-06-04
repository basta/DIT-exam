---
id: orr_quiz09_01
course: Optimal and Robust Control
tags: [LQ-control, stochastic, certainty-equivalence, Riccati]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
How does the computational procedure for LQ-optimal state feedback change when stochastic disturbances acting on the system are taken into consideration?

## Options
A) It does not change at all.
B) The Riccati equation now has to incorporate the values of the initial state variables.
C) The Riccati equation now has to be accompanied by a Lyapunov equation that captures the evolution of the covariance matrix in time.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
This is the **certainty-equivalence** property of the LQ regulator. If a linear system is driven by **additive zero-mean (Gaussian) process noise** and we still have full state measurement, the optimal state-feedback gain is **exactly the same** as in the deterministic (noise-free) LQR problem:
$$
\mathbf{u}_k = -\mathbf{K}_k\mathbf{x}_k, \quad \text{with the same Riccati-based } \mathbf{K}_k.
$$
The optimal controller acts on the *current measured state* and does not need to change because of the noise — the feedback gain computation (the Riccati equation) is unaffected. The noise increases the *value* of the cost but not the *form* of the optimal law.

- **B** is false — the Riccati equation never depends on the initial state.
- **C** describes computing the **covariance/performance** (which does use a Lyapunov equation), but that is *analysis* of the closed loop, not part of computing the optimal feedback gain.

## Related Concepts
- [[certainty-equivalence]]
- [[LQG]]
- [[separation-principle]]
