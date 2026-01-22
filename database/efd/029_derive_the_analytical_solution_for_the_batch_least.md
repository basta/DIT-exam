---
id: efd_029
course: Estimation, Filtration, and Detection
tags: [least-squares, point-estimation, linear-models]
difficulty: 2
type: derivation
status: to_learn
---

# Question
Derive the analytical solution for the Batch Least Squares (LS) estimator.

## Options
N/A (Open Derivation)

---
# Solution
**Correct Answer:** $\hat{\theta}_{LS} = (H^T H)^{-1} H^T y$

## Explanation
The Batch Least Squares (LS) estimator is a fundamental technique in estimation theory used to find the best-fitting parameters for an overdetermined system of linear equations. In this context, we assume a linear observation model of the form $y = H\theta + v$, where $y \in \mathbb{R}^m$ is the vector of observed measurements, $H \in \mathbb{R}^{m \times n}$ is the observation matrix (or regressor), $\theta \in \mathbb{R}^n$ is the vector of unknown parameters to be estimated, and $v$ represents measurement noise or modeling errors.

The "Batch" approach implies that we process all available data points $m$ simultaneously to produce a single estimate $\hat{\theta}$. The objective of the LS estimator is to minimize the sum of the squares of the residuals. A residual is defined as the difference between the actual observed value and the value predicted by the model: $r = y - H\hat{\theta}$. By minimizing the squared Euclidean norm of this residual vector, $\|r\|^2$, we ensure that the resulting estimate provides the closest possible fit to the data in a geometric sense.

Mathematically, this is framed as an optimization problem where we seek to minimize a cost function $J(\theta)$. Because $J(\theta)$ is a convex quadratic function of $\theta$, its global minimum can be found by setting the gradient with respect to $\theta$ to zero. This leads to the "Normal Equations." The resulting estimator is unbiased if the noise has zero mean and is the Best Linear Unbiased Estimator (BLUE) if the noise is white and homoscedastic (Gauss-Markov Theorem).

### Steps / Derivation
1. Define the linear measurement model and the scalar cost function $J(\theta)$ using the squared $L_2$ norm:
$$
J(\theta) = \|y - H\theta\|^2 = (y - H\theta)^T(y - H\theta)
$$

2. Expand the quadratic form:
$$
J(\theta) = y^T y - \theta^T H^T y - y^T H \theta + \theta^T H^T H \theta
$$
Note that since $\theta^T H^T y$ is a scalar, it is equal to its transpose $(y^T H \theta)$. Thus:
$$
J(\theta) = y^T y - 2\theta^T H^T y + \theta^T H^T H \theta
$$

3. Take the gradient of $J(\theta)$ with respect to the vector $\theta$:
$$
\frac{\partial J(\theta)}{\partial \theta} = -2H^T y + 2H^T H \theta
$$

4. Set the gradient to zero to find the extremum (the Normal Equations):
$$
2H^T H \hat{\theta} = 2H^T y \implies H^T H \hat{\theta} = H^T y
$$

5. Solve for $\hat{\theta}$, assuming $H^T H$ is non-singular (full column rank):
$$
\hat{\theta}_{LS} = (H^T H)^{-1} H^T y
$$

## Related Concepts
- [[gauss_markov_theorem]]
- [[weighted_least_squares]]
- [[moore_penrose_pseudoinverse]]