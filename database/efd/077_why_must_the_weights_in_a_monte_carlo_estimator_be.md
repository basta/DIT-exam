---
id: efd_077
course: Estimation, Filtration, and Detection
tags: [monte-carlo-methods, importance-sampling, particle-filtering, bayesian-estimation]
difficulty: 3
type: open
status: to_learn
---

# Question
Why must the weights in a Monte Carlo estimator be normalized?

## Options
A) To ensure the variance of the estimator is reduced to zero.
B) To account for the unknown normalization constant of the target distribution and ensure the estimator remains unbiased or consistent.
C) To satisfy the requirements of the Central Limit Theorem for finite samples.
D) To convert the importance weights into a Gaussian distribution for easier processing.

---
# Solution
**Correct Answer:** B

## Explanation
In many practical Bayesian estimation problems—such as particle filtering—we wish to compute an expectation $E_p[f(x)] = \int f(x) p(x) dx$, where the target distribution $p(x)$ is difficult to sample from directly. However, we often only know $p(x)$ up to a normalization constant, i.e., $p(x) \propto \pi(x)$. To estimate the expectation, we use Importance Sampling by drawing samples from a proposal distribution $q(x)$.

The raw importance weight for a sample $i$ is defined as $w_i = \frac{\pi(x_i)}{q(x_i)}$. If we do not normalize these weights, the sum of the weights will not equal 1, and the resulting estimator will be biased by the unknown scaling factor of $\pi(x)$. By performing normalization, where $\tilde{w}_i = \frac{w_i}{\sum_{j=1}^N w_j}$, we ensure that the estimator $\hat{I} = \sum \tilde{w}_i f(x_i)$ represents a valid probability measure. This is specifically known as Self-Normalized Importance Sampling (SNIS). While normalization introduces a small $O(1/N)$ bias in finite samples, it makes the estimator consistent (converging to the true value as $N \to \infty$) even when the normalization constant of the posterior density is unknown, which is the standard case in complex filtering applications.

### Steps / Derivation
1. Define the expectation of $f(x)$ under target $p(x)$ using a proposal $q(x)$:
$$
E_p[f(x)] = \int f(x) \frac{p(x)}{q(x)} q(x) dx
$$
2. Substitute $p(x) = \frac{\pi(x)}{\int \pi(x) dx}$ to account for the unknown constant:
$$
E_p[f(x)] = \frac{\int f(x) \frac{\pi(x)}{q(x)} q(x) dx}{\int \frac{\pi(x)}{q(x)} q(x) dx}
$$
3. Replace integrals with Monte Carlo summations using $N$ samples from $q(x)$:
$$
\hat{I} = \frac{\frac{1}{N} \sum_{i=1}^N f(x_i) w_i}{\frac{1}{N} \sum_{j=1}^N w_j} = \sum_{i=1}^N f(x_i) \left( \frac{w_i}{\sum_{j=1}^N w_j} \right)
$$

## Related Concepts
- [[importance_sampling]]
- [[particle_filter_resampling]]
- [[bayesian_posterior_estimation]]