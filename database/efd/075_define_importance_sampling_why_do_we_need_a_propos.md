---
id: efd_075
course: Estimation, Filtration, and Detection
tags: [importance-sampling, monte-carlo-methods, bayesian-estimation]
difficulty: 3
type: open
status: to_learn
---

# Question
Define Importance Sampling. Why do we need a "proposal distribution" (or importance density) $q(x)$ instead of sampling directly from the target distribution $p(x)$?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Importance Sampling is a Monte Carlo technique used to estimate properties of a distribution by sampling from a different distribution. A proposal distribution is needed primarily because the target distribution may be complex to sample from directly, or because we need to focus samples on regions that contribute most to the variance of the estimate.

## Explanation
Importance Sampling (IS) is a variance reduction technique used in Monte Carlo integration. In signal processing and estimation theory—particularly in Particle Filtering—we often need to compute the expectation of a function $f(x)$ under a target probability density $p(x)$, defined as $I = E_p[f(x)] = \int f(x)p(x)dx$.

We use a "proposal distribution" $q(x)$ (also called an importance density) for several critical reasons:

1. **Analytical Intractability:** In many Bayesian estimation problems, the target distribution $p(x)$ (the posterior) is known only up to a normalization constant (i.e., $p(x) \propto p(y|x)p(x)$). Sampling directly from such a distribution is often impossible using standard transformation methods.
2. **Efficiency and Rare Events:** If we are interested in estimating the probability of a rare event (where $f(x)$ is non-zero only in the tails of $p(x)$), direct sampling from $p(x)$ would require an astronomical number of samples to yield any hits in the region of interest. By choosing $q(x)$ such that it has high mass where $f(x)p(x)$ is large, we can achieve an accurate estimate with far fewer samples.
3. **Hardware and Algorithmic Constraints:** In real-time systems, we need a distribution $q(x)$ that is easy and fast to sample from, such as a Gaussian or Uniform distribution, whereas the true state distribution might be highly non-linear or multimodal.

To correct for sampling from $q(x)$ instead of $p(x)$, we introduce "importance weights" $w(x) = p(x)/q(x)$, which represent the ratio of the target density to the proposal density.

### Steps / Derivation
1. Rewrite the expectation integral by multiplying and dividing by the proposal distribution $q(x)$:
$$
E_p[f(x)] = \int f(x) p(x) dx = \int f(x) \frac{p(x)}{q(x)} q(x) dx
$$
2. Define the importance weight $w(x) = \frac{p(x)}{q(x)}$ and express the integral as an expectation over $q(x)$:
$$
I = E_q[f(x)w(x)]
$$
3. Approximate the integral using $N$ independent samples $x^{(i)}$ drawn from $q(x)$:
$$
\hat{I} = \frac{1}{N} \sum_{i=1}^{N} f(x^{(i)}) w(x^{(i)})
$$

## Related Concepts
- [[particle_filtering]]
- [[monte_carlo_integration]]
- [[sequential_importance_resampling]]