---
id: efd_068
course: Estimation, Filtration, and Detection
tags: [kalman-filter, fault-detection, stochastic-processes]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain how the Kalman Filter innovations (residuals) can be used for fault detection. What statistical property of the innovations is violated if a fault occurs?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The innovations sequence is used to construct a Chi-square ($\chi^2$) test statistic; the property of whiteness (zero-mean and lack of autocorrelation) is violated during a fault.

## Explanation
In the context of a Kalman Filter (KF), the innovation (or residual) is defined as the difference between the actual measurement and the predicted measurement at time $k$: $\tilde{y}_k = z_k - H_k \hat{x}_{k|k-1}$. Under nominal operating conditions (where the model matches the physical system and the noise is Gaussian), the Kalman Filter is the optimal linear estimator. In this ideal state, the innovations sequence $\{\tilde{y}_k\}$ possesses three critical statistical properties: it is a Gaussian white noise process, it has a mean of zero, and its covariance is given by $S_k = H_k P_{k|k-1} H_k^T + R_k$.

Fault detection leverages these properties by monitoring the behavior of $\tilde{y}_k$. When a sensor failure, actuator bias, or sudden change in system dynamics occurs, the filter's internal model no longer accurately reflects the physical reality. This causes the innovations to deviate from their expected behavior. Specifically, the innovations may exhibit a non-zero mean (shifting away from the origin) or an increased variance that exceeds the predicted $S_k$. 

The most common method for detection is the **Chi-square ($\chi^2$) test**. A normalized squared innovation (Mahalanobis distance) is calculated: $\epsilon_k = \tilde{y}_k^T S_k^{-1} \tilde{y}_k$. Under healthy conditions, $\epsilon_k$ follows a $\chi^2$ distribution with degrees of freedom equal to the dimension of the measurement vector. If $\epsilon_k$ exceeds a predefined threshold (determined by a desired false alarm rate), a fault is declared.

## Steps / Derivation
1. Define the innovation $\tilde{y}_k$ and its theoretical covariance $S_k$ based on the Kalman Filter equations.
2. Establish the null hypothesis $H_0$: The system is healthy, implying $\tilde{y}_k \sim \mathcal{N}(0, S_k)$.
3. Construct the scalar test statistic $\epsilon_k$ to monitor for deviations.
$$
\epsilon_k = \tilde{y}_k^T (H_k P_{k|k-1} H_k^T + R_k)^{-1} \tilde{y}_k
$$
4. Compare $\epsilon_k$ against a threshold $\lambda$ derived from the $\chi^2$ distribution tables for a specific significance level $\alpha$.

## Related Concepts
- [[chi_square_test]]
- [[innovation_whiteness_test]]
- [[analytical_redundancy]]