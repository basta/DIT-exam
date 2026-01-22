---
id: efd_027
course: Estimation, Filtration, and Detection
tags: [bayesian-inference, non-linear-estimation, posterior-distribution, recursive-filtering]
difficulty: 3
type: open
status: to_learn
---

# Question
Why is calculating the exact Bayesian posterior often analytically intractable for non-Gaussian, non-linear problems?

## Options
A) Integration in the denominator (evidence term) lacks a closed-form solution.
B) The product of non-conjugate prior and likelihood functions does not yield a standard distribution.
C) The dimensionality of the state space leads to exponential growth in computational requirement for grid-based methods.
D) All of the above.

---
# Solution
**Correct Answer:** D) All of the above.

## Explanation
In Bayesian estimation, the goal is to determine the posterior density $p(x_k | y_{1:k})$, which represents our belief about the state $x_k$ given a sequence of measurements $y_{1:k}$. While the Kalman Filter provides an optimal closed-form solution for linear-Gaussian systems, non-linear and non-Gaussian problems break the mathematical "symmetry" that allows for such simplicity.

The primary hurdle lies in the normalization constant, often called the **Evidence** or **Marginal Likelihood**. According to Bayes' rule:
$$ p(x|y) = \frac{p(y|x)p(x)}{\int p(y|x)p(x) dx} $$
For non-linear systems, the transition or measurement mappings (e.g., $h(x) = \sin(x)$) transform the probability densities in ways that do not preserve their functional form. Even if we start with a Gaussian prior, passing it through a non-linear function results in a non-Gaussian posterior. Unlike Gaussian distributions, which are fully described by just two moments (mean and covariance), non-Gaussian distributions may require an infinite number of moments to describe perfectly.

Furthermore, if the likelihood and prior are not **conjugate pairs**, the numerator does not simplify into a known distribution family. To solve the denominator, one must perform high-dimensional integration over the entire state space. For complex, high-dimensional models, these integrals have no analytical solution, necessitating numerical approximations like Sequential Monte Carlo (Particle Filters) or Variational Inference.

### Steps / Derivation
1. **Analyze the Bayes Update Rule:**
Identify the components: Prior $p(x_{k}|y_{1:k-1})$, Likelihood $p(y_k|x_k)$, and Posterior $p(x_k|y_{1:k})$.
2. **Observe the Propagation of Uncertainty:**
In a non-linear system $x_k = f(x_{k-1}) + w_k$, the Chapman-Kolmogorov equation requires:
$$
p(x_k | y_{1:k-1}) = \int p(x_k | x_{k-1}) p(x_{k-1} | y_{1:k-1}) dx_{k-1}
$$
3. **Identify the Intractability:**
If $f(\cdot)$ or $h(\cdot)$ are non-linear, the resulting integral reflects a convolution that usually cannot be solved symbolically.

## Related Concepts
- [[curse_of_dimensionality]]
- [[conjugate_priors]]
- [[particle_filtering]]