---
id: efd_020
course: Estimation, Filtration, and Detection
tags: [bayesian-estimation, mse-minimization, posterior-distribution, mmse]
difficulty: 3
type: derivation
status: to_learn
---

# Question
Show that the estimator that minimizes the Mean Squared Error in a Bayesian framework is the Conditional Mean of the posterior distribution.

## Options
N/A (Open Derivation)

---
# Solution
**Correct Answer:** $\hat{x}_{MSE}(y) = E[x|y]$

## Explanation
In Bayesian estimation, we treat the parameter to be estimated, $x$, as a random variable with a known prior distribution $p(x)$. Given an observation $y$, our goal is to find an estimator $\hat{x} = g(y)$ that minimizes the Risk Function associated with a specific cost function. For the Mean Squared Error (MSE), the cost function is defined as the squared difference between the true value and the estimate: $L(x, \hat{x}) = (x - \hat{x})^2$.

The Bayesian MSE is defined as the expected value of this cost function over the joint distribution of $x$ and $y$:
$MSE = E[(x - \hat{x})^2] = \int \int (x - g(y))^2 p(x, y) dx dy$.

Using the property of joint densities $p(x, y) = p(x|y)p(y)$, we can rewrite the double integral. Since the marginal density $p(y)$ is always non-negative, minimizing the total MSE is equivalent to minimizing the inner integral (the conditional MSE) for every possible realization of $y$. This inner integral represents the posterior mean squared error.

By taking the derivative of this conditional expectation with respect to the estimate $\hat{x}$ and setting it to zero, we find the point that minimizes the variance of the error. This mathematical framework demonstrates that the "best" estimate in a squared-error sense is the center of mass of the posterior distribution, $p(x|y)$. This result is fundamental in signal processing, as it forms the basis for the Wiener filter and the Kalman filter under Gaussian assumptions.

### Steps / Derivation
1. Define the Mean Squared Error (MSE) objective function using the law of iterated expectations:
$$
MSE = E_{y} [ E_{x|y} [ (x - \hat{x})^2 | y ] ] = \int p(y) \left[ \int (x - \hat{x})^2 p(x|y) dx \right] dy
$$

2. To minimize the total MSE, minimize the inner term (the conditional risk) for a fixed $y$:
$$
\frac{d}{d\hat{x}} \int (x - \hat{x})^2 p(x|y) dx = 0
$$

3. Pass the derivative through the integral and solve for $\hat{x}$:
$$
\int \frac{\partial}{\partial \hat{x}} (x^2 - 2x\hat{x} + \hat{x}^2) p(x|y) dx = \int (-2x + 2\hat{x}) p(x|y) dx = 0
$$

4. Distribute the integral and pull out the constant $\hat{x}$:
$$
-\int x p(x|y) dx + \hat{x} \int p(x|y) dx = 0
$$

5. Since the posterior density integrates to 1 ($\int p(x|y) dx = 1$), we obtain:
$$
\hat{x} = \int x p(x|y) dx = E[x|y]
$$

## Related Concepts
- [[minimum_mean_square_error]]
- [[posterior_density]]
- [[orthogonality_principle]]