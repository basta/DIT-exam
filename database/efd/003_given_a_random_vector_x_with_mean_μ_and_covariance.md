---
id: efd_003
course: Estimation, Filtration, and Detection
tags: [linear-transformation, stochastic-processes, moment-propagation]
difficulty: 2
type: open
status: to_learn
---

# Question
Given a random vector x with mean μ and covariance matrix P, what is the mean and covariance of the linear transformation y = Ax + b?

## Options
A) Mean: $A\mu$, Covariance: $APA^T$
B) Mean: $A\mu + b$, Covariance: $APA^T$
C) Mean: $A\mu + b$, Covariance: $AP$
D) Mean: $A\mu + b$, Covariance: $A^2 P$

---
# Solution
**Correct Answer:** B) Mean: $E[y] = A\mu + b$, Covariance: $Cov(y) = APA^T$

## Explanation
In the study of estimation and signal processing, understanding how the statistics of a random variable propagate through a linear system is fundamental. This process is often referred to as the propagation of moments. For any linear transformation $y = Ax + b$, the first and second moments (mean and covariance) are transformed in a predictable, linear, and quadratic fashion, respectively.

The mean, or expected value, is a linear operator. This means that the expectation of a sum is the sum of the expectations, and constant matrices can be pulled out of the operator. Therefore, when we apply the expectation operator to $y$, the matrix $A$ and the vector $b$ (which are deterministic) behave predictably, shifting the original mean $\mu$ by the transformation $A$ and the offset $b$.

The covariance matrix describes the dispersion of the random vector around its mean. By definition, the covariance of $y$ is the expected value of the outer product of the deviation of $y$ from its own mean. When substituting the linear equation into this definition, the constant offset $b$ cancels out, as it affects both the variable and its mean equally. The resulting expression demonstrates that the covariance is scaled quadratically by the transformation matrix $A$. Specifically, the transformation results in $APA^T$. This result is a cornerstone of the Kalman Filter's prediction step, where the state covariance is propagated forward in time using the state transition matrix.

### Steps / Derivation
1. **Derive the Mean:** Apply the expectation operator $E[\cdot]$ to the linear equation.
2. **Derive the Covariance:** Use the definition $Cov(y) = E[(y - E[y])(y - E[y])^T]$.
$$
E[y] = E[Ax + b] = AE[x] + b = A\mu + b
$$
$$
Cov(y) = E[(Ax + b - (A\mu + b))(Ax + b - (A\mu + b))^T]
$$
$$
Cov(y) = E[(A(x - \mu))(A(x - \mu))^T] = E[A(x - \mu)(x - \mu)^T A^T]
$$
$$
Cov(y) = A E[(x - \mu)(x - \mu)^T] A^T = APA^T
$$

## Related Concepts
- [[kalman_filter_prediction]]
- [[multivariate_gaussian_distribution]]
- [[linear_minimum_mean_square_error]]