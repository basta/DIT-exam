---
id: efd_022
course: Estimation, Filtration, and Detection
tags: [bayesian-inference, conjugate-prior, recursive-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
What is a conjugate prior? Why are they computationally useful in recursive Bayesian estimation?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A conjugate prior is a distribution for the prior probability such that the resulting posterior distribution belongs to the same family of distributions as the prior, given the likelihood function. They are useful because they allow for closed-form recursive updates of distribution parameters without the need for complex numerical integration.

## Explanation
In Bayesian statistics, the goal is to update our belief about a parameter $\theta$ after observing data $y$. This is governed by Bayes' Theorem:
$$p(\theta | y) = \frac{p(y | \theta) p(\theta)}{p(y)}$$
The term $p(\theta)$ is the **prior**, $p(y | \theta)$ is the **likelihood**, and $p(\theta | y)$ is the **posterior**. Generally, calculating the posterior is difficult because the denominator $p(y) = \int p(y | \theta) p(\theta) d\theta$ often lacks an analytical solution, requiring computationally expensive methods like Markov Chain Monte Carlo (MCMC).

A **conjugate prior** is specifically chosen such that the functional form of the posterior $p(\theta | y)$ is identical to that of the prior $p(\theta)$. For example, if the likelihood is Gaussian and the prior is Gaussian, the posterior is guaranteed to be Gaussian. This relationship implies that the "update" from prior to posterior involves only updating a finite set of parameters (hyperparameters) rather than re-calculating the entire distribution shape.

In **recursive Bayesian estimation**, measurements arrive sequentially. The posterior from time step $k-1$ becomes the prior for time step $k$. If conjugate priors are used, the estimator only needs to track a few variables (such as the mean $\mu$ and variance $\sigma^2$ in the Kalman Filter case) to perfectly represent the state of knowledge. This avoids the "curse of dimensionality" and ensures that the computational cost per update remains constant and efficient for real-time applications.

### Steps / Derivation
1. **Identify the Likelihood**: Determine the distribution $p(y | \theta)$ of the observed data.
2. **Select the Conjugate Prior**: Choose $p(\theta)$ from the family conjugate to the likelihood (e.g., Beta prior for Binomial likelihood).
3. **Compute Hyperparameter Updates**: Instead of integration, apply the algebraic update rules:
$$
\text{Posterior Parameters} = f(\text{Prior Parameters}, \text{New Data})
$$

## Related Concepts
- [[recursive_least_squares]]
- [[exponential_family]]
- [[kalman_filter]]