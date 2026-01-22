---
id: efd_025
course: Estimation, Filtration, and Detection
tags: [kalman-filter, bayesian-inference, gaussian-likelihood, posterior-covariance]
difficulty: 3
type: open
status: to_learn
---

# Question
If the prior is Gaussian and the likelihood is linear-Gaussian, what happens to the posterior covariance matrix as we process more data, and does it depend on the measurement values?

## Options
A) The covariance increases; it depends on the measurement values.
B) The covariance decreases; it depends on the measurement values.
C) The covariance decreases or stays the same; it is independent of the measurement values.
D) The covariance stays constant; it is independent of the measurement values.

---
# Solution
**Correct Answer:** C

## Explanation
In the context of Bayesian estimation with a Gaussian prior and a linear-Gaussian likelihood, the resulting posterior distribution is also Gaussian. A fundamental property of this conjugate pair is that the update equations for the mean and the covariance are decoupled. 

The posterior covariance represents our uncertainty about the state estimate. As more data is processed (assuming the measurements provide some information about the state), the information content increases, which mathematically results in a non-increasing covariance matrix. Specifically, in a static estimation problem, the covariance monotonically decreases (in the sense of the Loewner partial ordering) or converges to a steady state if the system is dynamic (like a Kalman Filter).

Crucially, the formula for the posterior covariance—often expressed via the Joseph form or the standard Kalman update—depends solely on the prior covariance, the measurement matrix ($H$), and the measurement noise covariance ($R$). It does not contain the actual measurement vector $y$. This implies that we can pre-compute the "certainty" or "error budget" of our estimator before we ever receive a single data point. This property is a unique characteristic of the linear-Gaussian case; if the measurement model were non-linear or the noise were non-Gaussian (e.g., Poisson), the posterior uncertainty would typically depend on the specific values of the observations received.

### Steps / Derivation
1. Define the prior $\mathbf{x} \sim \mathcal{N}(\hat{\mathbf{x}}_0, P_0)$ and the measurement model $\mathbf{y} = H\mathbf{x} + \mathbf{v}$, where $\mathbf{v} \sim \mathcal{N}(0, R)$.
2. Use the Bayes' Rule for Gaussian variables to find the posterior covariance $P_1$.
3. Observe the Information Form of the covariance update:
$$
P_{post}^{-1} = P_{prior}^{-1} + H^T R^{-1} H
$$
4. Alternatively, using the Kalman Gain $K = P_{prior}H^T(HP_{prior}H^T + R)^{-1}$:
$$
P_{post} = (I - KH)P_{prior}
$$
5. Note that neither $P_{post}^{-1}$ nor $P_{post}$ involve the measurement vector $\mathbf{y}$.

## Related Concepts
- [[kalman_filter]]
- [[conjugate_prior]]
- [[minimum_mean_square_error]]