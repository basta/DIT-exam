---
id: efd_084
course: Estimation, Filtration, and Detection
tags: [particle-filter, extended-kalman-filter, non-linear-estimation, non-gaussian-noise]
difficulty: 3
type: open
status: to_learn
---

# Question
Compare the Particle Filter to the Extended Kalman Filter (EKF). In what specific scenarios (type of non-linearity, type of noise) does the Particle Filter significantly outperform the EKF?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** The Particle Filter outperforms the EKF in scenarios involving highly non-linear dynamics/measurements and non-Gaussian (especially multi-modal or heavy-tailed) noise distributions.

## Explanation
The **Extended Kalman Filter (EKF)** is the standard recursive filter for non-linear systems. It operates by linearizing the state transition and observation models using a first-order Taylor series expansion (Jacobians) around the current mean estimate. This approach assumes that the posterior distribution can be sufficiently approximated by a single Gaussian. Consequently, the EKF fails when the linearity assumption is violated over the range of the uncertainty or when the true distribution is non-Gaussian.

The **Particle Filter (PF)**, or Sequential Monte Carlo (SMC) method, represents the posterior probability density function (PDF) using a set of discrete, weighted samples (particles) rather than a parametric form. This allows it to track arbitrary distributions.

The Particle Filter significantly outperforms the EKF in the following scenarios:

1.  **Highly Non-linear Dynamics:** When the functions $f(x)$ or $h(x)$ have high curvature (e.g., sharp turns, trigonometric oscillations), the linear approximation used in the EKF introduces significant bias and can lead to filter divergence.
2.  **Non-Gaussian Noise:** If the process noise $w_k$ or measurement noise $v_k$ is non-Gaussian—such as Bi-modal (representing two distinct hypotheses), Cauchy, or Uniform distributions—the EKF’s mean-covariance representation cannot capture the true statistics.
3.  **Multi-modal Distributions:** In "Global Localization" problems where the system might be in one of several discrete locations, the PF can maintain multiple clusters of particles, whereas the EKF will attempt to average them into a single (often incorrect) Gaussian mean.

## Steps / Derivation
1. **Linearization vs. Sampling:** EKF uses a Taylor expansion:
$$
\hat{x}_{k|k} \approx f(\hat{x}_{k-1|k-1}) + \mathbf{F}_k (x_{k-1} - \hat{x}_{k-1|k-1})
$$
where $\mathbf{F}_k$ is the Jacobian. Particle filters avoid this by passing $N$ samples directly through the non-linear function:
$$
x_k^{(i)} = f(x_{k-1}^{(i)}, w_{k-1}^{(i)})
$$

2. **Density Representation:** EKF assumes:
$$
p(x_k | z_{1:k}) \sim \mathcal{N}(\hat{x}_k, P_k)
$$
Particle Filter approximates:
$$
p(x_k | z_{1:k}) \approx \sum_{i=1}^{N} w_k^{(i)} \delta(x_k - x_k^{(i)})
$$

3. **Computational Trade-off:** While PF is more robust, its computational cost scales linearly with the number of particles $N$, whereas EKF is computationally efficient but fragile.

## Related Concepts
- [[sequential_monte_carlo]]
- [[recursive_bayesian_estimation]]
- [[linearization_errors]]