---
id: efd_032
course: Estimation, Filtration, and Detection
tags: [least-squares, maximum-likelihood, gaussian-noise, parameter-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Under what assumption is the Least Squares estimator also the Maximum Likelihood Estimator (MLE)?

## Options
A) When the measurement noise follows a Poisson distribution.
B) When the measurement noise is Additive White Gaussian Noise (AWGN).
C) When the system is non-linear and the noise is multiplicative.
D) When the prior distribution of the parameters is Uniform.

---
# Solution
**Correct Answer:** B) When the measurement noise is Additive White Gaussian Noise (AWGN).

## Explanation
The equivalence between the Least Squares (LS) estimator and the Maximum Likelihood Estimator (MLE) is a fundamental result in estimation theory. The Least Squares method is a deterministic approach that seeks to minimize the sum of the squared residuals (the difference between observed and predicted values) without necessarily assuming a specific probability distribution for the errors. 

In contrast, the Maximum Likelihood approach is a probabilistic method that selects parameter values that maximize the likelihood function, which represents the probability density of the observed data given the parameters. When the measurement noise is assumed to be Independent and Identically Distributed (i.i.d.) with a Gaussian distribution (specifically, Zero-mean Additive White Gaussian Noise), the likelihood function takes the form of an exponential of a negative quadratic term.

Specifically, for a model $y = H\theta + w$, where $w \sim \mathcal{N}(0, \sigma^2 I)$, maximizing the likelihood is mathematically equivalent to minimizing the exponent. Since the exponent in a Gaussian PDF is the squared Euclidean norm of the error vector, the parameter $\theta$ that maximizes the probability of the data is the same $\theta$ that minimizes the squared error. If the noise is not Gaussian (e.g., Laplace or Uniform), the MLE will result in a different estimator (such as Mean Absolute Error for Laplace noise).

### Steps / Derivation
1. Define the linear model with Gaussian noise:
$$
y = H\theta + w, \quad w \sim \mathcal{N}(0, \sigma^2 I)
$$
2. Write the Likelihood function $L(\theta)$ based on the PDF of $w$:
$$
L(\theta) = p(y|\theta) = \frac{1}{(2\pi\sigma^2)^{n/2}} \exp\left( -\frac{1}{2\sigma^2} (y - H\theta)^T (y - H\theta) \right)
$$
3. To find the MLE, take the natural logarithm (Log-Likelihood) and remove constants that do not depend on $\theta$:
$$
\ln L(\theta) \propto -(y - H\theta)^T (y - H\theta)
$$
4. Observe that maximizing the negative quadratic form is equivalent to minimizing the Least Squares objective function:
$$
J(\theta) = \|y - H\theta\|^2
$$

## Related Concepts
- [[linear_regression]]
- [[gaussian_distribution]]
- [[blue_estimator]]