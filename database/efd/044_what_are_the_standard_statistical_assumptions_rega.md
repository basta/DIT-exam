---
id: efd_044
course: Estimation, Filtration, and Detection
tags: [stochastic-processes, kalman-filter, noise-modeling]
difficulty: 2
type: open
status: to_learn
---

# Question
What are the standard statistical assumptions regarding the process noise w(k) and measurement noise v(k)?

## Options
A) They are assumed to be colored noise with a non-zero mean and high correlation with the state $x(k)$.
B) They are assumed to be zero-mean, white, Gaussian, and uncorrelated with each other and the initial state.
C) They must follow a Uniform distribution and be linearly dependent on the control input $u(k)$.
D) They are assumed to be deterministic signals with a known period and amplitude.

---
# Solution
**Correct Answer:** B

## Explanation
In the context of classical Estimation Theory (specifically the discrete-time Kalman Filter), the process noise $w(k)$ and measurement noise $v(k)$ are typically characterized by a set of idealized statistical assumptions to ensure the optimality of the estimator. 

1. **Zero-Mean:** It is assumed that $E[w(k)] = 0$ and $E[v(k)] = 0$. If the noise had a known non-zero mean (bias), it could be modeled as a deterministic input and subtracted out, so the zero-mean assumption simplifies the derivation without loss of generality.
2. **White Noise:** The noise vectors are temporally uncorrelated. This means the value of the noise at time $k$ provides no information about the value at time $j$ ($k \neq j$). Mathematically, the autocovariance is zero for all non-zero lags.
3. **Gaussian (Normal) Distribution:** While the Kalman filter is the best *linear* estimator for any distribution, it is the absolute *optimal* estimator (Minimum Mean Square Error) if the noise is Gaussian. This allows the state PDF to be completely characterized by its mean and covariance.
4. **Uncorrelatedness:** It is standard to assume that the process noise $w(k)$ and measurement noise $v(k)$ are mutually uncorrelated, and both are uncorrelated with the initial state $x(0)$. Specifically, $E[w(k)v(j)^T] = 0$ for all $k, j$.

### Steps / Derivation
The statistical properties can be summarized by the following expectations:

1. The noise processes are white and zero-mean:
$$
E[w(k)] = 0, \quad E[v(k)] = 0
$$

2. The covariance matrices are defined as:
$$
E[w(k)w(j)^T] = Q_k \delta_{kj}, \quad E[v(k)v(j)^T] = R_k \delta_{kj}
$$
where $\delta_{kj}$ is the Kronecker delta.

3. Cross-correlation between noise sources is zero:
$$
E[w(k)v(j)^T] = 0
$$

## Related Concepts
- [[kalman_filter]]
- [[white_gaussian_noise]]
- [[orthogonality_principle]]