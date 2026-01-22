---
id: efd_083
course: Estimation, Filtration, and Detection
tags: [particle-filter, sequential-monte-carlo, resampling]
difficulty: 3
type: open
status: to_learn
---

# Question
What is Sample Impoverishment (or Loss of Diversity) caused by resampling? Why is it dangerous for the filter?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Sample impoverishment is the phenomenon where a particle filter's population becomes concentrated on a very small number of unique states due to repeated resampling of high-weight particles, leading to a loss of statistical diversity and potential filter divergence.

## Explanation
In Particle Filtering (Sequential Monte Carlo), we represent the posterior distribution $p(x_k | z_{1:k})$ using a set of weighted particles. A common issue arises where, after several iterations, most particles have negligible weights. To address this, we use **resampling**, which eliminates particles with low weights and replicates those with high weights.

**Sample Impoverishment** occurs when the resampling process is applied repeatedly, especially in scenarios with low process noise ($Q \approx 0$). Because the resampling step chooses particles with replacement based on their importance weights, a single particle with a very high weight might be selected dozens or hundreds of times. This results in a new particle set where many individuals are identical copies of one ancestor.

This is dangerous for the filter for several reasons:
1. **Loss of Diversity:** The particles no longer span the state space effectively. Instead of a cloud representing a probability density, the filter collapses into a few discrete points.
2. **Inaccurate Uncertainty Estimation:** The filter may report a very low covariance (appearing "confident") while being significantly far from the true state because it has discarded the "correct" trajectory earlier in the process.
3. **Filter Divergence:** If the true state moves into a region not covered by the remaining unique particles, the filter becomes "blind" and cannot recover, leading to a total failure in tracking.
4. **Degeneracy of the PDF:** The discrete approximation of the posterior becomes so sparse that it no longer serves as a valid representation of the continuous underlying distribution.

### Steps / Derivation
1. **Weight Update:** Calculate importance weights based on the likelihood:
$$
w_k^i \propto w_{k-1}^i \frac{p(z_k|x_k^i)p(x_k^i|x_{k-1}^i)}{q(x_k^i|x_{k-1}^i, z_k)}
$$
2. **Resampling:** Draw $N$ samples from the current set with probability $P(x_k^i) = w_k^i$. 
3. **Diversity Metric:** The Effective Sample Size $N_{eff}$ is often used to monitor this:
$$
\hat{N}_{eff} = \frac{1}{\sum_{i=1}^N (w_k^i)^2}
$$
4. **Impoverishment:** When $N_{eff}$ is low, resampling is triggered. If process noise is small, the particles $x_k^i$ do not "spread out" after resampling, leading to:
$$
x_k^i = x_k^j \text{ for many } i, j
$$

## Related Concepts
- [[sequential_importance_sampling]]
- [[effective_sample_size]]
- [[monte_carlo_localization]]