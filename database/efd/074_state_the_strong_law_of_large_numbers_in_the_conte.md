---
id: efd_074
course: Estimation, Filtration, and Detection
tags: [monte-carlo, stochastic-convergence, estimation-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
State the Strong Law of Large Numbers in the context of Monte Carlo approximation. What happens as the number of samples N approaches infinity?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** The sample mean converges almost surely to the true expected value.

## Explanation
In the context of Monte Carlo approximation, we seek to estimate an integral or an expectation of a function $g(X)$, where $X$ is a random variable with a probability density function $f(x)$. The Monte Carlo estimator is defined as the empirical average of the function evaluated at $N$ independent and identically distributed (i.i.d.) samples $\{x_i\}_{i=1}^N$ drawn from $f(x)$.

The Strong Law of Large Numbers (SLLN) provides the theoretical foundation for this approximation. It states that if the expected value $E[|g(X)|] < \infty$, then the empirical average (the estimator) converges to the theoretical mean "almost surely" (with probability 1). 

As $N \to \infty$, the Monte Carlo estimator becomes a consistent estimator. The "strength" of the SLLN specifically refers to the mode of convergence (almost sure convergence), which is stronger than the convergence in probability offered by the Weak Law of Large Numbers. In practical estimation and filtration tasks (such as Particle Filtering), this ensures that as computational resources increase, the approximation error vanishes and the estimate perfectly recovers the target statistical property.

### Steps / Derivation
1. Define the target expectation $I$:
$$
I = E[g(X)] = \int g(x)f(x)dx
$$
2. Define the Monte Carlo estimator $\hat{I}_N$ using $N$ i.i.d. samples:
$$
\hat{I}_N = \frac{1}{N} \sum_{i=1}^N g(x_i)
$$
3. Apply the Strong Law of Large Numbers:
$$
P\left( \lim_{N \to \infty} \hat{I}_N = I \right) = 1
$$

## Related Concepts
- [[monte_carlo_integration]]
- [[convergence_of_random_variables]]
- [[particle_filtering]]