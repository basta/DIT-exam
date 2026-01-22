---
id: efd_056
course: Estimation, Filtration, and Detection
tags: [kalman-filter, state-estimation, statistical-testing]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain the concept of "Filter Consistency." What does it mean if the filter is inconsistent, and how can checking the innovation sequence help detect this?

## Options
N/A (Open-ended conceptual question)

---
# Solution
**Correct Answer:** A filter is consistent if its estimation error is zero-mean and its calculated covariance matches the actual error variance. Inconsistency implies the filter is overconfident or biased. Innovation sequence testing (whiteness and covariance tests) is the primary diagnostic tool.

## Explanation
Filter consistency is a fundamental property in optimal estimation, particularly for the Kalman Filter (KF). A filter is defined as consistent if it satisfies three primary criteria:
1. The estimation error $\tilde{x}(k) = x(k) - \hat{x}(k|k)$ is unbiased, meaning $E[\tilde{x}(k)] = 0$.
2. The state estimation error covariance $P(k|k)$ matches the actual mean square error (MSE), such that $E[\tilde{x}(k)\tilde{x}(k)^T] = P(k|k)$.
3. The innovation sequence (measurement residuals) is a zero-mean white noise process with a covariance $S(k)$ that matches the theoretical value calculated by the filter.

If a filter is **inconsistent**, it usually means the filter's internal estimate of its own uncertainty ($P$) does not reflect reality. Most commonly, filters become "optimistic" or overconfident, where $P$ is much smaller than the actual MSE. This leads to the filter ignoring new measurements in favor of its own (incorrect) state estimate, potentially causing the filter to diverge. Conversely, if $P$ is much larger than the actual error, the filter is "pessimistic" and sluggish.

The **innovation sequence** $\nu(k) = z(k) - H\hat{x}(k|k-1)$ is the "bread and butter" of consistency checking. In a well-tuned filter, the innovations represent the "new" information that cannot be predicted from previous states. If the filter is consistent, $\nu(k)$ should be a Gaussian white noise sequence. Analysts check this using:
- **Whiteness Tests:** Using autocorrelation to ensure $\nu(k)$ is uncorrelated over time.
- **Normalized Innovation Squared (NIS) Test:** We calculate $\epsilon_\nu = \nu(k)^T S(k)^{-1} \nu(k)$. Under the null hypothesis of consistency, this follows a $\chi^2$ distribution. If the values consistently fall outside the confidence bounds, the filter is deemed inconsistent.

### Steps / Derivation
1. **Define the Innovation:**
$$
\nu(k) = z(k) - H\hat{x}(k|k-1)
$$
2. **Calculate the Theoretical Innovation Covariance:**
$$
S(k) = H P(k|k-1) H^T + R
$$
3. **Perform the NIS test for a sample $k$:**
$$
\epsilon_\nu(k) = \nu(k)^T S(k)^{-1} \nu(k) \sim \chi^2_m
$$
where $m$ is the dimension of the measurement vector. If $\epsilon_\nu(k)$ is statistically larger than expected, $P$ or $R$ are likely under-modeled.

## Related Concepts
- [[kalman_filter_divergence]]
- [[chi_squared_test]]
- [[innovation_covariance]]