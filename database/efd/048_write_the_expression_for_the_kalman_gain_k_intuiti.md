---
id: efd_048
course: Estimation, Filtration, and Detection
tags: [kalman-filter, minimum-mean-square-error, optimal-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Write the expression for the Kalman Gain ($K_k$). Intuitively, how does it balance the trust between the model prediction and the actual measurement?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}$

## Explanation
The Kalman Gain ($K_k$) is the optimal weighting matrix used in the state update equation of a Kalman Filter: $\hat{x}_k = \hat{x}_k^- + K_k(z_k - H\hat{x}_k^-)$. It is derived to minimize the posterior error covariance, making the Kalman Filter a Minimum Mean Square Error (MMSE) estimator.

Intuitively, the Kalman Gain acts as a relative weighting factor between two sources of uncertainty: the **predicted state estimate** (from the system model) and the **innovation** (the difference between the actual measurement and the predicted measurement). This balance is governed by the ratio of the error covariances:

1. **Trusting the Measurement:** If the measurement noise covariance $R$ is very small (approaching zero), the measurement is highly reliable. In this case, the denominator of the gain expression decreases, and $K_k$ approaches $H^{-1}$. The filter "trusts" the measurement more, and the state update shifts significantly toward the observed data.
2. **Trusting the Model:** Conversely, if the predicted estimate error covariance $P_k^-$ is very small compared to $R$, it means the system model is very accurate and the measurement is noisy. In this scenario, $K_k$ decreases toward zero. The filter "trusts" the model prediction more, and the noisy measurement has a minimal impact on the updated state.

By continuously updating $K_k$ based on the evolving values of $P$ and $R$, the filter provides an optimal compromise that accounts for the reliability of both the physical dynamics and the sensor hardware at every time step.

### Steps / Derivation
1. Denote $P_k^-$ as the a priori error covariance and $R$ as the measurement noise covariance.
2. The Kalman Gain is defined as the matrix that minimizes the trace of the a posteriori error covariance $P_k$.
$$
K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}
$$

## Related Concepts
- [[optimal_operating_point]]
- [[innovation_covariance]]
- [[bayesian_filtering]]