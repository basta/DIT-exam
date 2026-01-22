---
id: efd_052
course: Estimation, Filtration, and Detection
tags: [kalman-filter, linearized-systems, state-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe the fundamental difference between the Linear Kalman Filter and the Extended Kalman Filter (EKF).

## Options
A) N/A (Open-ended question)
B) 
C) 
D) 

---
# Solution
**Correct Answer:** The fundamental difference lies in the linearity of the system models and how the probability distribution is propagated: the LKF assumes linear transitions and measurement functions, while the EKF handles non-linearities via local linearization using Jacobian matrices.

## Explanation
The **Linear Kalman Filter (LKF)** is the optimal estimator for systems governed by linear stochastic difference equations. It assumes that the next state is a linear combination of the previous state and control inputs, and that the measurements are linear combinations of the state. Because linear transformations of Gaussian random variables remain Gaussian, the LKF can perfectly track the mean and covariance of the state distribution using simple matrix algebra.

The **Extended Kalman Filter (EKF)**, on the other hand, is designed for non-linear systems where the state transition function $f(x)$ or the measurement function $h(x)$ are non-linear. In such cases, passing a Gaussian distribution through a non-linear function results in a non-Gaussian distribution, which makes the standard LKF equations invalid. 

To solve this, the EKF performs a first-order Taylor series expansion (linearization) around the current mean estimate. By calculating the **Jacobian** matrices (partial derivatives) of the non-linear functions at each time step, the EKF approximates the system as "locally linear." While the LKF is optimal for linear Gaussian systems, the EKF is an approximation and can diverge if the non-linearities are too severe or if the initial estimate is poor. Unlike the LKF, where the filter gain $K_k$ and covariance $P_k$ can be pre-calculated, the EKF's gain depends on the current state estimate, requiring real-time computation of Jacobians.

### Steps / Derivation
1. Define the system models. LKF: $x_k = Ax_{k-1} + w_k$. EKF: $x_k = f(x_{k-1}) + w_k$.
2. Compute the Jacobians for EKF linearization at each step:
$$
F_k = \frac{\partial f}{\partial x} \bigg|_{\hat{x}_{k-1|k-1}}, \quad H_k = \frac{\partial h}{\partial x} \bigg|_{\hat{x}_{k|k-1}}
$$
3. Propagate the covariance using these linearized matrices:
$$
P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q
$$

## Related Concepts
- [[taylor_series_expansion]]
- [[jacobian_matrix]]
- [[unscented_kalman_filter]]