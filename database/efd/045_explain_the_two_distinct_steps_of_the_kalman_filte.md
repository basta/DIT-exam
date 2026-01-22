---
id: efd_045
course: Estimation, Filtration, and Detection
tags: [kalman-filter, state-estimation, recursive-least-squares, stochastic-processes]
difficulty: 2
type: open
status: to_learn
---

# Question
Explain the two distinct steps of the Kalman Filter cycle: Time Update (Prediction) and Measurement Update (Correction).

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** The Kalman Filter operates as a recursive feedback control loop consisting of "Predict" equations (projecting the state forward) and "Correct" equations (incorporating noisy observations).

## Explanation
The Kalman Filter is an optimal recursive estimator for linear systems subject to Gaussian noise. It minimizes the mean squared error (MSE) of the state estimate by splitting the computational burden into two primary phases:

1. **Time Update (Prediction):** This step projects the current state estimate ($\hat{x}_{k-1}$) and the error covariance ($P_{k-1}$) forward in time to the next time step $k$. It acts as the "look ahead" mechanism based on the physical model of the system. Because this step involves moving through the transition matrix $A$ and adding process noise $Q$, the uncertainty (covariance) typically increases during this phase. This provides an *a-priori* estimate.

2. **Measurement Update (Correction):** In this step, the filter "corrects" the predicted *a-priori* estimate by incorporating a real-world measurement $z_k$. First, it calculates the **Innovation** (the difference between the actual measurement and the predicted measurement). Then, it calculates the **Kalman Gain** ($K_k$), which determines how much to trust the measurement versus the prediction. If the measurement noise $R$ is very low, the gain is high, and the filter trusts the measurement more. The result is the *a-posteriori* estimate, and the error covariance is "shrunk" or updated to reflect the new information.

The beauty of this cycle is its recursive nature: the *a-posteriori* estimate of step $k$ becomes the starting point for the *a-priori* estimate of step $k+1$.

### Steps / Derivation
1. **Time Update (Predict):** Project the state and covariance forward.
$$
\hat{x}_{k}^{-} = A \hat{x}_{k-1} + B u_{k-1}
$$
$$
P_{k}^{-} = A P_{k-1} A^T + Q
$$
2. **Measurement Update (Correct):** Compute Kalman Gain and update state estimate with measurement $z_k$.
$$
K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}
$$
$$
\hat{x}_k = \hat{x}_k^- + K_k (z_k - H \hat{x}_k^-)
$$
$$
P_k = (I - K_k H) P_k^-
$$

## Related Concepts
- [[recursive_bayesian_estimation]]
- [[linear_quadratic_estimator]]
- [[white_noise_processes]]