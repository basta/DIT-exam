---
id: efd_078
course: Estimation, Filtration, and Detection
tags: [particle-filtering, sequential-importance-sampling, bayesian-estimation, monte-carlo]
difficulty: 4
type: open
status: to_learn
---

# Question
Describe the Sequential Importance Sampling (SIS) algorithm. How are the weights updated recursively as new data arrives?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The SIS algorithm approximates the posterior distribution using a set of weighted particles. The weights are updated recursively by multiplying the previous weight by the ratio of the likelihood and transition density over the importance proposal distribution.

## Explanation
The Sequential Importance Sampling (SIS) algorithm is a Monte Carlo method used to estimate the state of a dynamical system in a non-linear or non-Gaussian environment. It forms the foundation for Particle Filtering. The core idea is to represent the posterior distribution $p(x_{0:k} | z_{1:k})$ using a set of $N$ random samples (particles) $\{x_{0:k}^i\}_{i=1}^N$ with associated weights $\{w_k^i\}_{i=1}^N$.

Because it is often impossible to sample directly from the posterior (the target distribution), we sample from a known **importance density** $q(x_{0:k} | z_{1:k})$. To correct for the discrepancy between the target and the proposal, each particle is assigned an importance weight. In the sequential context, we choose the importance density such that it can be factorized:
$$q(x_{0:k} | z_{1:k}) = q(x_k | x_{0:k-1}, z_{1:k}) q(x_{0:k-1} | z_{1:k-1})$$

By applying Bayes' Rule to the target posterior and utilizing this factorization, we derive a recursive update for the weights. This allows the algorithm to process data online without re-processing all previous observations. However, a major challenge in SIS is the **degeneracy phenomenon**, where after a few iterations, all but one particle have negligible weights, which is typically addressed by adding a resampling step (resulting in the Sequential Importance Resampling or SIR filter).

### Steps / Derivation
1. **Selection of Importance Density:** We define a proposal distribution that satisfies the Markov property: $q(x_k | x_{0:k-1}, z_{1:k}) = q(x_k | x_{k-1}, z_k)$.
2. **Weight Definition:** The weight at time $k$ is defined by the ratio of the posterior to the proposal:
$$
w_k^i \propto \frac{p(z_k | x_k^i) p(x_k^i | x_{k-1}^i) p(x_{0:k-1}^i | z_{1:k-1})}{q(x_k^i | x_{k-1}^i, z_k) q(x_{0:k-1}^i | z_{1:k-1})}
$$
3. **Recursive Update:** By cancelling terms from the previous time step $w_{k-1}^i$, the weight update equation becomes:
$$
w_k^i = w_{k-1}^i \frac{p(z_k | x_k^i) p(x_k^i | x_{k-1}^i)}{q(x_k^i | x_{k-1}^i, z_k)}
$$
4. **Normalization:** The weights are normalized such that $\sum_{i=1}^N w_k^i = 1$.

## Related Concepts
- [[particle_filter_degeneracy]]
- [[importance_sampling]]
- [[sequential_monte_carlo]]