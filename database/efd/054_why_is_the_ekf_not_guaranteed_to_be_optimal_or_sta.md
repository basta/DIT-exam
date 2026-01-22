---
id: efd_054
course: Estimation, Filtration, and Detection
tags: [extended-kalman-filter, linearization, stability, non-linear-estimation]
difficulty: 3
type: open
status: to_learn
---

# Question
Why is the EKF not guaranteed to be optimal or stable, unlike the linear Kalman Filter?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The EKF relies on local linearization via Taylor Series expansion, which introduces truncation errors, loses the property of preserving Gaussianity, and ignores higher-order moments.

## Explanation
The optimality and stability of the standard Kalman Filter (KF) are rooted in the properties of linear systems and Gaussian distributions. In a linear-Gaussian system, the KF is the Minimum Mean Square Error (MMSE) estimator because the propagation of a Gaussian distribution through a linear transformation remains Gaussian. Furthermore, under certain conditions of controllability and observability, the KF error covariance is guaranteed to converge to a unique steady-state value.

The Extended Kalman Filter (EKF) breaks these guarantees for several reasons:

1.  **Linearization Errors (Truncation):** The EKF uses a first-order Taylor Series expansion to linearize the nonlinear functions $f(x)$ and $h(x)$ around the current estimate. By discarding higher-order terms (the Hessian and beyond), the EKF introduces an approximation error. If the nonlinearity is severe or the initial estimate is far from the true state, these "linearization residuals" can lead to significant estimation bias.
2.  **Non-Gaussianity:** When a Gaussian distribution passes through a nonlinear function, the resulting distribution is generally no longer Gaussian. The EKF, however, forcedly approximates the posterior as a Gaussian by only tracking the mean and covariance. This loss of information regarding higher-order moments means the EKF is no longer the true MMSE estimator.
3.  **Divergence and Stability:** In the linear KF, the calculation of the Covariance Matrix $P_k$ is independent of the actual measurements $z_k$. In the EKF, the Jacobian matrices $F_k$ and $H_k$ are evaluated at the current state estimate $\hat{x}_{k|k}$. This creates a feedback loop: if the state estimate is poor, the Jacobian is inaccurate; if the Jacobian is inaccurate, the covariance and gain calculations are wrong, further degrading the estimate. This positive feedback can lead to filter divergence where the error grows unboundedly.

### Steps / Derivation
1. Consider the nonlinear state transition:
$$
x_{k} = f(x_{k-1}) + w_{k-1}
$$
2. The EKF linearizes this using the Jacobian $F$:
$$
F_{k-1} = \left. \frac{\partial f}{\partial x} \right|_{\hat{x}_{k-1|k-1}}
$$
3. The approximation ignores the remainder $R$ in the Taylor expansion:
$$
f(x) \approx f(\hat{x}) + F(x - \hat{x}) + R(x, \hat{x})
$$
If $R$ is large, the covariance update $P_{k|k-1} = F_{k-1} P_{k-1|k-1} F_{k-1}^T + Q$ becomes an unreliable representation of the actual uncertainty.

## Related Concepts
- [[linearization_errors]]
- [[jacobian_matrices]]
- [[unscented_kalman_filter]]