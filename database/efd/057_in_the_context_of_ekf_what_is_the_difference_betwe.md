---
id: efd_057
course: Estimation, Filtration, and Detection
tags: [extended-kalman-filter, linearization, state-estimation, non-linear-dynamics]
difficulty: 3
type: open
status: to_learn
---

# Question
In the context of EKF, what is the difference between linearizing around the "nominal trajectory" vs. linearizing around the "current estimate"?

## Options
A) Linearizing around the nominal trajectory results in the Extended Kalman Filter (EKF), while linearizing around the current estimate results in the Linearized Kalman Filter (LKF).
B) Linearizing around the nominal trajectory results in the Linearized Kalman Filter (LKF), while linearizing around the current estimate results in the Extended Kalman Filter (EKF).
C) Both methods result in the EKF, but linearizing around the nominal trajectory is always more accurate.
D) Linearizing around the current estimate requires pre-calculating the Kalman gains offline.

---
# Solution
**Correct Answer:** B) Linearizing around the nominal trajectory results in the Linearized Kalman Filter (LKF), while linearizing around the current estimate results in the Extended Kalman Filter (EKF).

## Explanation
The distinction between these two approaches is fundamental to non-linear estimation. When we have a non-linear system defined by $\dot{x} = f(x, u, w)$, we must linearize the dynamics to apply the recursive structure of the Kalman Filter.

1. **Linearized Kalman Filter (LKF):** This approach linearizes the non-linear equations around a pre-computed **nominal trajectory** ($x_{nom}$). This trajectory is typically determined ahead of time based on a known control input and the deterministic model (ignoring noise). Because the linearization point $x_{nom}(t)$ does not depend on the actual measurements received during runtime, the Jacobian matrices $F = \frac{\partial f}{\partial x}\vert_{x_{nom}}$ and the resulting Kalman Gains $K(t)$ can be computed **offline**. This makes LKF computationally efficient but prone to large errors if the actual state deviates significantly from the nominal path.

2. **Extended Kalman Filter (EKF):** The EKF linearizes around the **current best estimate**, which is the posterior estimate from the previous time step $\hat{x}_{k-1|k-1}$ (for the prediction step) and the prior estimate $\hat{x}_{k|k-1}$ (for the update step). Because the linearization point is updated using real-time measurement data, the filter "follows" the actual trajectory of the system more closely. However, this means the Jacobians and Kalman Gains must be computed **online**, increasing the computational load. The EKF is generally more robust than the LKF for systems where the trajectory is not strictly predictable.

### Steps / Derivation
1. **LKF Linearization:**
Expand $f(x)$ about the nominal state $x_{nom}$:
$$
f(x) \approx f(x_{nom}) + \left. \frac{\partial f}{\partial x} \right|_{x_{nom}} (x - x_{nom})
$$

2. **EKF Linearization:**
Expand $f(x)$ about the most recent estimate $\hat{x}_{k}$:
$$
f(x) \approx f(\hat{x}_{k}) + \left. \frac{\partial f}{\partial x} \right|_{\hat{x}_{k}} (x - \hat{x}_{k})
$$

## Related Concepts
- [[jacobian_matrix]]
- [[kalman_filter_stability]]
- [[taylor_series_expansion]]