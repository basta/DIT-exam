---
id: efd_002
course: Estimation, Filtration, and Detection
tags: [probability-theory, continuous-random-variable, statistical-moments]
difficulty: 1
type: open
status: to_learn
---

# Question
State the definition of the expected value (mean) and variance of a continuous random variable X.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
The expected value is $E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$ and the variance is $Var(X) = E[(X - E[X])^2] = \int_{-\infty}^{\infty} (x - \mu)^2 f_X(x) dx$.

## Explanation
In the field of signal processing and estimation theory, characterizing the statistical behavior of a continuous random variable $X$ is fundamental. This characterization is primarily achieved through its Probability Density Function (PDF), denoted as $f_X(x)$. The PDF describes the relative likelihood for this random variable to take on a given value.

The **expected value**, often referred to as the mean or the first moment ($\mu$), represents the "center of mass" of the distribution. For a continuous variable, it is calculated as the integral of all possible values heavily weighted by their respective probabilities. It acts as the best constant estimate of a random variable under the Minimum Mean Square Error (MMSE) criterion.

The **variance**, or the second central moment ($\sigma^2$), measures the "spread" or dispersion of the random variable around its mean. It quantifies the average squared deviation from the expected value. In detection and filtration contexts, variance is often associated with the power of the noise or the uncertainty of an estimate. A high variance indicates that values are widely distributed, whereas a low variance suggests that values are clustered closely around the mean. Together, these two parameters provide the most basic yet essential summary of a random process, forming the basis for more complex operations like Kalman filtering or Bayesian inference.

### Steps / Derivation
1. Define the Mean (Expected Value) as the first moment of the PDF:
$$
E[X] = \mu_X = \int_{-\infty}^{\infty} x f_X(x) dx
$$
2. Define the Variance as the expected value of the squared deviation from the mean:
$$
Var(X) = \sigma_X^2 = E[(X - \mu_X)^2] = \int_{-\infty}^{\infty} (x - \mu_X)^2 f_X(x) dx
$$
3. Note the alternative computational formula for variance (Parallel Axis Theorem):
$$
Var(X) = E[X^2] - (E[X])^2
$$

## Related Concepts
- [[probability_density_function]]
- [[statistical_moments]]
- [[minimum_mean_square_error]]