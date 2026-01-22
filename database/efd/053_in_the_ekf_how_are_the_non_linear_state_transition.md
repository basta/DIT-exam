---
id: efd_053
course: Estimation, Filtration, and Detection
tags: [extended-kalman-filter, linearization, jacobian-matrices, non-linear-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
In the EKF, how are the non-linear state transition and measurement functions handled? (Mention Jacobians).

## Options
A) They are ignored, and a standard Linear Kalman Filter is used on the raw non-linear equations.
B) They are linearized at each time step using a first-order Taylor series expansion local to the current state estimate.
C) They are transformed using the Unscented Transform to capture higher-order moments.
D) They are replaced by Global Jacobians calculated only once at the initialization phase.

---
# Solution
**Correct Answer:** B) They are linearized at each time step using a first-order Taylor series expansion local to the current state estimate.

## Explanation
The Extended Kalman Filter (EKF) is the most widely used adaptation of the Kalman Filter for systems where the state transition model ($f$) or the observation model ($h$) are non-linear. Because the optimal Bayesian solution for non-linear systems is generally infinite-dimensional and computationally intractable, the EKF employs a "linearize-as-you-go" strategy.

The core mechanism involves approximating the non-linear functions using a first-order Taylor series expansion. This expansion is performed around the most recent state estimate: for the prediction step, it is performed around the previous estimate $\hat{x}_{k-1|k-1}$, and for the update step, it is performed around the predicted state $\hat{x}_{k|k-1}$. 

The "Jacobians" mentioned are matrices of first-order partial derivatives. The Jacobian matrix of the state transition function, $F_k$, represents how the state evolves locally, while the Jacobian of the measurement function, $H_k$, represents the local sensitivity of the sensors to changes in the state. By substituting these linear approximations into the standard Kalman Filter equations, the EKF can propagate the mean and covariance of the state estimate. However, because it neglects second-order and higher terms (Hessians, etc.), the EKF may diverge if the non-linearity is extreme or if the initial estimate is poor.

### Steps / Derivation
1. Define the non-linear system: $x_k = f(x_{k-1}, u_k) + w_k$ and $z_k = h(x_k) + v_k$.
2. Linearize the state transition function using the Jacobian evaluated at the previous estimate:
$$
F_k = \frac{\partial f}{\partial x} \bigg|_{\hat{x}_{k-1|k-1}, u_k}
$$
3. Linearize the measurement function using the Jacobian evaluated at the predicted state:
$$
H_k = \frac{\partial h}{\partial x} \bigg|_{\hat{x}_{k|k-1}}
$$
4. Use $F_k$ to project the covariance $P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q$, and use $H_k$ to calculate the Kalman Gain $K_k$.

## Related Concepts
- [[taylor_series_expansion]]
- [[linearization_methods]]
- [[unscented_kalman_filter]]