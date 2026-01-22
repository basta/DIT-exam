---
id: efd_081
course: Estimation, Filtration, and Detection
tags: [particle-filter, sequential-monte-carlo, importance-sampling]
difficulty: 3
type: open
status: to_learn
---

# Question
What is the purpose of the Resampling step in a Particle Filter (SIR algorithm)? How does it address the degeneracy problem?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The purpose of resampling is to eliminate particles with negligible weights and replicate particles with high weights, thereby refocusing computational effort on the more probable regions of the state space. It addresses the degeneracy problem by resetting the variance of the importance weights.

## Explanation
The Sequential Importance Resampling (SIR) algorithm is a non-linear, non-Gaussian filter that approximates the posterior distribution $p(x_k | z_{1:k})$ using a set of weighted particles $\{x_k^i, w_k^i\}_{i=1}^N$. Without a resampling step, the algorithm suffers from the **degeneracy problem**: after a few iterations, the variance of the importance weights increases significantly. Mathematically, it has been shown that the variance of the importance weights can only increase over time, leading to a situation where all but one particle have near-zero weights. This means the filter wastes computational resources on particles that do not effectively contribute to the approximation of the posterior.

Resampling addresses this by "resetting" the weights. When the Effective Sample Size (ESS), often approximated by $N_{eff} = \frac{1}{\sum_{i=1}^N (w_k^i)^2}$, falls below a certain threshold, the resampling step is triggered. In this step, a new set of particles is drawn from the current discrete approximation of the posterior. Particles with high weights are likely to be selected multiple times, while those with very low weights are discarded. After resampling, all new particles are assigned equal weights $w_k^i = 1/N$. This restores the diversity of the sample paths in regions of high likelihood, ensuring the filter remains a robust estimator of the state.

### Steps / Derivation
1. **Weight Normalization**: Ensure all importance weights sum to unity:
$$
\tilde{w}_k^i = \frac{w_k^i}{\sum_{j=1}^N w_k^j}
$$
2. **Calculate Effective Sample Size**: Determine if the degeneracy is significant enough to require resampling:
$$
\hat{N}_{eff} = \frac{1}{\sum_{i=1}^N (\tilde{w}_k^i)^2}
$$
3. **Selection**: Draw $N$ new samples $x_k^{i*}$ from the current set $\{x_k^i\}$ with probability $P(x_k^{i*} = x_k^j) = \tilde{w}_k^j$.
4. **Weight Reset**: Set the weights of the new particle set to $1/N$, effectively "forgetting" the past weight history while preserving the density information through the frequency of identical particles.

## Related Concepts
- [[importance_sampling]]
- [[sequential_monte_carlo]]
- [[effective_sample_size]]