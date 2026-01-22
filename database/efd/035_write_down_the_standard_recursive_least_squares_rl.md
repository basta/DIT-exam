---
id: efd_035
course: Estimation, Filtration, and Detection
tags: [recursive-least-squares, adaptive-filtering, parameter-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Write down the standard Recursive Least Squares (RLS) update equations (Gain, Estimation update, Covariance update).

![[question_image.png]]

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
The standard RLS update equations for a system $y(n) = \mathbf{x}^T(n)\boldsymbol{\theta} + v(n)$ are:
1. Gain Vector: $\mathbf{k}(n) = \frac{\mathbf{P}(n-1)\mathbf{x}(n)}{\lambda + \mathbf{x}^T(n)\mathbf{P}(n-1)\mathbf{x}(n)}$
2. Parameter Update: $\hat{\boldsymbol{\theta}}(n) = \hat{\boldsymbol{\theta}}(n-1) + \mathbf{k}(n)[y(n) - \mathbf{x}^T(n)\hat{\boldsymbol{\theta}}(n-1)]$
3. Covariance Update: $\mathbf{P}(n) = \frac{1}{\lambda} [ \mathbf{P}(n-1) - \mathbf{k}(n)\mathbf{x}^T(n)\mathbf{P}(n-1) ]$

## Explanation
The Recursive Least Squares (RLS) algorithm is an iterative method used to find the coefficients that minimize a weighted linear least squares cost function relating to the input signals. Unlike the LMS (Least Mean Squares) algorithm, which uses a stochastic gradient descent approach, RLS aims to solve for the optimal parameters exactly at each time step based on all previous data.

The core objective is to minimize the cost function $J(n) = \sum_{i=1}^{n} \lambda^{n-i} |e(i)|^2$, where $e(i)$ is the estimation error and $\lambda$ is the "forgetting factor" (typically $0 < \lambda \le 1$). Small values of $\lambda$ allow the filter to track time-varying parameters by giving less weight to older data.

The algorithm relies on the Matrix Inversion Lemma (also known as the Woodbury Matrix Identity) to update the inverse of the correlation matrix $\mathbf{P}(n) = \mathbf{R}^{-1}(n)$ without performing a direct matrix inversion at every step. This reduces the computational complexity to $O(M^2)$, where $M$ is the number of parameters, compared to the $O(M^3)$ of a batch Least Squares approach. The gain vector $\mathbf{k}(n)$ acts as a weighting factor that determines how much the current prediction error $e(n) = y(n) - \hat{y}(n)$ should influence the update of the parameter estimate $\hat{\boldsymbol{\theta}}$.

### Steps / Derivation
1. Initialize $\hat{\boldsymbol{\theta}}(0) = \mathbf{0}$ and $\mathbf{P}(0) = \delta^{-1}\mathbf{I}$, where $\delta$ is a small positive constant.
2. For each time step $n=1, 2, \dots$, compute the gain vector:
$$
\mathbf{k}(n) = \frac{\mathbf{P}(n-1)\mathbf{x}(n)}{\lambda + \mathbf{x}^T(n)\mathbf{P}(n-1)\mathbf{x}(n)}
$$
3. Update the parameter estimate using the innovation (a-priori error):
$$
\hat{\boldsymbol{\theta}}(n) = \hat{\boldsymbol{\theta}}(n-1) + \mathbf{k}(n)[y(n) - \mathbf{x}^T(n)\hat{\boldsymbol{\theta}}(n-1)]
$$
4. Update the inverse correlation (covariance) matrix:
$$
\mathbf{P}(n) = \lambda^{-1} \left( \mathbf{P}(n-1) - \mathbf{k}(n)\mathbf{x}^T(n)\mathbf{P}(n-1) \right)
$$

## Related Concepts
- [[least_mean_squares_lms]]
- [[kalman_filter]]
- [[matrix_inversion_lemma]]