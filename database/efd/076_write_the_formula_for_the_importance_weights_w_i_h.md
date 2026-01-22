---
id: efd_076
course: Estimation, Filtration, and Detection
tags: [importance-sampling, particle-filtering, monte-carlo-methods]
difficulty: 2
type: open
status: to_learn
---

# Question
Write the formula for the Importance Weights $w_i$. How are they related to the target distribution and the proposal distribution?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $w_i = \frac{p(x_i)}{q(x_i)}$

## Explanation
Importance weights are a fundamental component of Importance Sampling and Particle Filtering. In many estimation problems, we wish to compute an expectation of a function $f(x)$ with respect to a "target" distribution $p(x)$, denoted as $E_p[f(x)] = \int f(x)p(x) dx$. However, it is often difficult or impossible to draw samples directly from $p(x)$ because it may be non-standard, truncated, or locally unknown (e.g., in Bayesian inference where we only know the unnormalized posterior).

To overcome this, we introduce a "proposal" distribution (also called an importance distribution or instrumental distribution) denoted as $q(x)$. We choose $q(x)$ such that it is easy to sample from and shares the same support as $p(x)$ (i.e., $q(x) > 0$ whenever $p(x) > 0$). By multiplying and dividing the integrand by $q(x)$, we rewrite the integral:
$\int f(x) \frac{p(x)}{q(x)} q(x) dx$.

This transformation allows us to evaluate the expectation using samples $x_i$ drawn from $q(x)$ rather than $p(x)$. The term $w_i = \frac{p(x_i)}{q(x_i)}$ acts as a correction factor. If $p(x_i) > q(x_i)$, the sample is more likely under the target distribution than the proposal, so it is given more "weight." Conversely, if $p(x_i) < q(x_i)$, the sample is over-represented by the proposal and its weight is reduced. In practical applications like Sequential Importance Resampling (SIR), these weights are often normalized so that $\sum w_i = 1$.

### Steps / Derivation
1. Define the expectation of $f(x)$ under the target distribution $p(x)$:
$$
E_p[f(x)] = \int f(x) p(x) dx
$$
2. Multiply and divide by the proposal distribution $q(x)$:
$$
E_p[f(x)] = \int f(x) \frac{p(x)}{q(x)} q(x) dx = E_q\left[ f(x) \frac{p(x)}{q(x)} \right]
$$
3. Identify the importance weight $w(x)$ as the ratio of the target density to the proposal density:
$$
w_i = \frac{p(x_i)}{q(x_i)}
$$

## Related Concepts
- [[sequential_monte_carlo]]
- [[monte_carlo_integration]]
- [[particle_filter_resampling]]