---
id: efd_069
course: Estimation, Filtration, and Detection
tags: [kalman-filter, innovation-monitoring, fault-detection]
difficulty: 3
type: open
status: to_learn
---

# Question
What is the $\chi^2$ (Chi-square) test on the innovations? What specific type of fault or anomaly does it primarily detect?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The $\chi^2$ test on innovations is a statistical hypothesis test used to verify if the residual (innovation) sequence of a filter (typically a Kalman Filter) is consistent with its predicted covariance. It primarily detects **sensor outliers**, **model mismatches**, and **sudden jumps (biases)** in the measurement process.

## Explanation
In the context of optimal estimation, specifically the Kalman Filter, the **innovation** (or residual) is defined as the difference between the actual measurement $z_k$ and the predicted measurement $\hat{z}_{k|k-1}$. Under the assumption of a correctly modeled linear Gaussian system, the innovations sequence is white noise with a zero mean and a known covariance matrix $S_k$.

The $\chi^2$ test utilizes the normalized squared innovation, also known as the **Mahalanobis distance**. The scalar test statistic is defined as:
$$ \epsilon_k = \nu_k^T S_k^{-1} \nu_k $$
where $\nu_k$ is the innovation vector and $S_k$ is the innovation covariance calculated by the filter. Under the null hypothesis $H_0$ (the filter is performing optimally/no fault), this statistic follows a Chi-square distribution with $n_z$ degrees of freedom, where $n_z$ is the dimension of the measurement vector.

The primary goal of this test is **Statistical Consistency Monitoring**. By setting a threshold based on a desired confidence level (e.g., $P < 0.05$), we can determine if the current measurement is "statistically likely." If $\epsilon_k$ exceeds the threshold, the measurement is flagged as an anomaly. This is particularly effective at detecting **sensor faults**, such as sudden spikes or biases, because these events cause the innovation to move significantly away from zero, resulting in a test statistic that is highly improbable under the normal distribution model. It also identifies **unmodeled dynamics** or **maneuvers** where the system state deviates from the predictive model.

### Steps / Derivation
1. **Define the Innovation:**
Calculate the difference between the measurement and the prediction.
$$ \nu_k = z_k - H_k \hat{x}_{k|k-1} $$

2. **Compute the Innovation Covariance:**
Obtained from the Kalman gain equations.
$$ S_k = H_k P_{k|k-1} H_k^T + R_k $$

3. **Calculate the Scalar Test Statistic:**
Compute the quadratic form (Mahalanobis distance).
$$ \epsilon_k = \nu_k^T S_k^{-1} \nu_k $$

4. **Hypothesis Testing:**
Compare $\epsilon_k$ against a threshold $\gamma$ from the $\chi^2$ table for $n_z$ degrees of freedom.
$$ \epsilon_k > \gamma \implies \text{Fault Detected} $$

## Related Concepts
- [[kalman_filter_residuals]]
- [[mahalanobis_distance]]
- [[integrity_monitoring]]