---
id: efd_079
course: Estimation, Filtration, and Detection
tags: [particle-filters, sequential-importance-sampling, bayesian-estimation]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain the Degeneracy Phenomenon in Sequential Importance Sampling. What happens to the variance of the importance weights over time?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Degeneracy refers to the concentration of importance weights on a single particle. The variance of the importance weights increases monotonically over time.

## Explanation
The Degeneracy Phenomenon is a fundamental challenge in Sequential Importance Sampling (SIS), which is a Monte Carlo method used to estimate the state of a dynamical system. In SIS, a set of random samples (particles) represents the posterior distribution. Since we cannot sample from the true posterior directly, we sample from a proposal distribution and assign an importance weight to each particle to account for the difference.

Degeneracy occurs because, as the number of iterations increases, the variance of the importance weights can only increase. Mathematically, it has been shown by Kong et al. (1994) that for a fixed number of particles, the variance of the weights $w_k^i$ increases over time, regardless of the choice of the proposal distribution. Consequently, after a few iterations, all but one particle will have negligible (near-zero) normalized weights. This means that a large amount of computational effort is wasted on updating particles that contribute almost nothing to the final estimate of the posterior distribution.

The "Effective Sample Size" ($N_{eff}$) is typically used to monitor this phenomenon. When the weights are highly skewed, $N_{eff}$ drops significantly, indicating that the sample set no longer provides a reliable representation of the probability density function. To combat this, researchers introduced the "Resampling" step, leading to the development of the Sampling Importance Resampling (SIR) filter or the standard Particle Filter.

### Steps / Derivation
1. Define the unnormalized importance weight at time $k$:
$$
w_k^i = w_{k-1}^i \frac{p(y_k | x_k^i) p(x_k^i | x_{k-1}^i)}{q(x_k^i | x_{k-1}^i, y_k)}
$$
2. Observe that the normalized weights $\tilde{w}_k^i = \frac{w_k^i}{\sum w_k^i}$ eventually satisfy:
$$
\text{Var}[\tilde{w}_k] \to \infty \text{ as } k \to \infty
$$
3. Calculate the Effective Sample Size to quantify degeneracy:
$$
\hat{N}_{eff} = \frac{1}{\sum_{i=1}^N (\tilde{w}_k^i)^2}
$$
where $1 \le \hat{N}_{eff} \le N$. A low $\hat{N}_{eff}$ indicates severe degeneracy.

## Related Concepts
- [[particle_filtering]]
- [[importance_resampling]]
- [[monte_carlo_methods]]