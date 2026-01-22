---
id: efd_011
course: Estimation, Filtration, and Detection
tags: [least-squares, maximum-likelihood, gaussian-noise, parameter-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Under what specific conditions is the Least Squares (LS) estimator equivalent to the Maximum Likelihood (MLE) estimator?

## Options
A) When the measurement noise is zero-mean and uncorrelated.
B) When the measurement noise is Additive White Gaussian Noise (AWGN).
C) When the system model is strictly linear and the noise is Laplacian.
D) When the prior distribution of the parameters is a known Gaussian.

---
# Solution
**Correct Answer:** B

## Explanation
The equivalence between the Least Squares (LS) estimator and the Maximum Likelihood Estimator (MLE) is a fundamental result in estimation theory that hinges on the distribution of the measurement error. 

The Least Squares approach is a deterministic geometric optimization method; it seeks to minimize the sum of the squares of the residuals (the differences between observed and predicted values) without necessarily making assumptions about the underlying probability density function (PDF). Mathematically, it minimizes $J(\theta) = \|y - H\theta\|^2$.

Conversely, the MLE is a statistical approach that chooses the parameter value $\theta$ that maximizes the likelihood function $L(\theta) = p(y | \theta)$. For the two estimators to yield the identical analytical solution, the log-likelihood function must take a quadratic form that mirrors the LS cost function. 

This specific condition occurs when the measurement noise is assumed to be **Additive White Gaussian Noise (AWGN)**. If the noise $v$ is Gaussian with $v \sim \mathcal{N}(0, \sigma^2 I)$, the likelihood function involves an exponential term $e^{-\frac{1}{2\sigma^2}(y-H\theta)^T(y-H\theta)}$. Taking the natural logarithm reveals that maximizing the likelihood is mathematically identical to minimizing the squared Euclidean norm of the residual vector. If the noise is non-Gaussian (e.g., Laplacian or Uniform), the MLE will result in a different estimator (such as Least Absolute Deviations for Laplacian noise). Furthermore, if the noise is colored (correlated), the MLE corresponds to the Weighted Least Squares (WLS) estimator rather than the Ordinary Least Squares (OLS) estimator.

### Steps / Derivation
1. Write the linear observation model with Gaussian noise $v \sim \mathcal{N}(0, \sigma^2 I)$:
$$
y = H\theta + v
$$
2. Express the Likelihood Function $p(y|\theta)$:
$$
p(y|\theta) = \frac{1}{(2\pi)^{n/2} \sigma^n} \exp\left( -\frac{1}{2\sigma^2} (y - H\theta)^T (y - H\theta) \right)
$$
3. Take the log-likelihood to simplify the maximization:
$$
\ln L(\theta) = -\frac{n}{2}\ln(2\pi) - n\ln(\sigma) - \frac{1}{2\sigma^2} \|y - H\theta\|^2
$$
4. Observe that maximizing $\ln L(\theta)$ is equivalent to minimizing the residual sum of squares, which is the LS objective:
$$
\hat{\theta}_{MLE} = \arg\min_{\theta} \|y - H\theta\|^2 = \hat{\theta}_{LS}
$$

## Related Concepts
- [[gauss_markov_theorem]]
- [[maximum_likelihood_estimation]]
- [[weighted_least_squares]]