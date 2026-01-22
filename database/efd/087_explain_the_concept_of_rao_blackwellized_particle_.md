---
id: efd_087
course: Estimation, Filtration, and Detection
tags: [particle-filter, kalman-filter, sequential-monte-carlo, marginalization]
difficulty: 4
type: open
status: to_learn
---

# Question
Explain the concept of Rao-Blackwellized Particle Filters. How does it combine the Kalman Filter and Particle Filter to improve efficiency?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The Rao-Blackwellized Particle Filter (RBPF) reduces the dimensionality of the state space used in Monte Carlo sampling by analytically marginalizing out variables that exhibit linear-Gaussian dependencies, typically using Kalman Filters.

## Explanation
The Rao-Blackwellized Particle Filter (RBPF), also known as the Marginalized Particle Filter, is a hybrid estimation technique designed to address the "curse of dimensionality" prevalent in standard Particle Filters (PF). In high-dimensional state spaces, a PF requires an exponentially increasing number of particles to represent the posterior distribution accurately. The RBPF mitigates this by applying the Rao-Blackwell theorem: if a subset of the state variables is conditionally linear and Gaussian given the remaining variables, those variables can be integrated out (marginalized) analytically.

Specifically, the state vector $x_t$ is partitioned into two parts: $x_t = [x_t^p, x_t^k]^T$. Here, $x_t^p$ represents the "nonlinear" or "non-Gaussian" part of the state, which is tracked using a standard Particle Filter. The second part, $x_t^k$, represents the "linear-Gaussian" part. Given a trajectory of the nonlinear states $x_{0:t}^p$, the conditional posterior $p(x_t^k | y_{1:t}, x_{0:t}^p)$ can be computed exactly using a Kalman Filter (KF).

This combination improves efficiency in two ways:
1. **Variance Reduction:** Analytical integration (the KF part) always results in a lower variance estimator compared to Monte Carlo sampling for the same variables.
2. **Dimension Reduction:** By only sampling in the lower-dimensional space of $x_t^p$, the RBPF requires significantly fewer particles to achieve the same level of accuracy as a standard PF acting on the full state $x_t$.

## Steps / Derivation
1. Partition the state vector into a nonlinear part $x_t^p$ and a linear part $x_t^k$. Factorize the posterior distribution using the chain rule:
$$
p(x_{0:t}^p, x_t^k | y_{1:t}) = p(x_t^k | y_{1:t}, x_{0:t}^p) p(x_{0:t}^p | y_{1:t})
$$
2. Represent the marginalized posterior $p(x_{0:t}^p | y_{1:t})$ using a set of $N$ particles $\{x_{0:t}^{p,(i)}\}_{i=1}^N$ and weights $w_t^{(i)}$.
3. For each particle $(i)$, maintain a unique Kalman Filter (mean $\hat{x}_t^{k,(i)}$ and covariance $P_t^{(i)}$) to compute the conditional distribution:
$$
p(x_t^k | y_{1:t}, x_{0:t}^{p,(i)}) \sim \mathcal{N}(\hat{x}_t^{k,(i)}, P_t^{(i)})
$$
4. Update the importance weights $w_t^{(i)}$ by evaluating the likelihood of the observation $y_t$, which now involves the predictive mean and covariance from the Kalman Filter step.

## Related Concepts
- [[marginalized_particle_filter]]
- [[sequential_importance_sampling]]
- [[linear_quadratic_estimation]]