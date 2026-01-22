---
id: efd_080
course: Estimation, Filtration, and Detection
tags: [particle-filter, sequential-monte-carlo, importance-sampling]
difficulty: 3
type: open
status: to_learn
---

# Question
What is the Effective Sample Size ($N_{eff}$)? How is it approximated using the normalized weights?

---
# Solution
**Correct Answer:** The Effective Sample Size is a metric used in Particle Filtering to quantify the degeneracy of the particle set. It is approximated by $\hat{N}_{eff} = \frac{1}{\sum_{i=1}^N (w_t^i)^2}$.

## Explanation
In the context of Sequential Monte Carlo (SMC) methods, such as the Particle Filter, we represent a posterior probability distribution through a set of discrete particles and their associated importance weights. Ideally, each particle should contribute equally to the representation of the distribution. However, as the filter iterates through time, a phenomenon known as "weight degeneracy" occurs: the variance of the importance weights increases over time, eventually leading to a scenario where one particle has a weight near unity while all others have weights near zero.

The Effective Sample Size ($N_{eff}$) is a diagnostic tool used to measure this degeneracy. It represents the number of "equivalent" independent samples that the current weighted particle set represents. If $N_{eff}$ is close to the total number of particles $N$, the variance of the weights is low and the distribution is well-sampled. If $N_{eff}$ is small, it indicates that the filter is relying on only a few particles, making the estimate unreliable and necessitating a resampling step.

The mathematical approximation used in practice relies on the normalized importance weights $w_t^i$, where $\sum w_t^i = 1$. By squaring these weights and summing them, we capture the dispersion of the weight distribution. A uniform distribution of weights yields the maximum possible $N_{eff}$ ($N$), while a single dominant weight yields the minimum ($1$).

### Steps / Derivation
1. The theoretical $N_{eff}$ is defined relative to the variance of the importance weights:
$$
N_{eff} = \frac{N}{1 + Var(w_t^{*i})}
$$
where $w_t^{*i}$ is the "true" importance weight.
2. Since the true variance is unknown, we use the normalized weights $w_t^i$ to provide a practical estimate.
3. The approximation $\hat{N}_{eff}$ is derived from the reciprocal of the sum of squares of the normalized weights:
$$
\hat{N}_{eff} = \frac{1}{\sum_{i=1}^{N} (w_t^i)^2}
$$
4. When $\hat{N}_{eff}$ drops below a predefined threshold (e.g., $N/2$ or $2N/3$), a resampling step is usually triggered to replace low-weight particles with copies of high-weight particles.

## Related Concepts
- [[particle_filter_resampling]]
- [[importance_sampling]]
- [[weight_degeneracy]]