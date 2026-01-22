---
id: efd_033
course: Estimation, Filtration, and Detection
tags: [least-squares, parameter-estimation, gauss-markov]
difficulty: 2
type: open
status: to_learn
---

# Question
Explain the difference between Ordinary Least Squares (OLS) and Weighted Least Squares (WLS). When would you prefer WLS?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** OLS assumes homoscedasticity (equal variance of errors), while WLS accounts for heteroscedasticity by weighting observations inversely proportional to their error variance.

## Explanation
Ordinary Least Squares (OLS) is a fundamental estimation technique used to estimate the parameters $\theta$ in a linear model $y = H\theta + v$. The OLS estimator minimizes the sum of the squared residuals, expressed as $J(\theta) = (y - H\theta)^T(y - H\theta)$. A critical underlying assumption of OLS is that the measurement noise $v$ is white and homoscedastic, meaning $E[vv^T] = \sigma^2 I$. In this scenario, every observation is treated as equally reliable, and OLS provides the Best Linear Unbiased Estimator (BLUE) according to the Gauss-Markov theorem.

Weighted Least Squares (WLS) is a generalization of OLS designed to handle situations where the measurement errors are uncorrelated but have unequal variances (heteroscedasticity), or more generally, when the errors are correlated with a known covariance matrix $R$. The WLS objective function is $J(\theta) = (y - H\theta)^T W (y - H\theta)$, where $W$ is a weighting matrix, typically chosen as $W = R^{-1}$. By using the inverse of the covariance matrix as the weight, WLS gives more influence to "high-precision" measurements (those with small variance) and less influence to "low-precision" measurements (those with large variance).

One should prefer WLS over OLS whenever the assumption of constant variance is violated. In practical signal processing, this often occurs when sensors have different noise characteristics, or when measurements are taken under varying environmental conditions. Using OLS in the presence of heteroscedasticity results in estimators that are still unbiased but are no longer efficient, meaning they have unnecessarily large variances compared to the WLS estimator.

### Steps / Derivation
1. Define the linear measurement model with noise covariance $R$:
$$
y = H\theta + v, \quad E[v] = 0, \quad E[vv^T] = R
$$
2. The OLS solution assumes $R = \sigma^2 I$, yielding:
$$
\hat{\theta}_{OLS} = (H^T H)^{-1} H^T y
$$
3. The WLS solution incorporates the weighting matrix $W = R^{-1}$:
$$
\hat{\theta}_{WLS} = (H^T R^{-1} H)^{-1} H^T R^{-1} y
$$

## Related Concepts
- [[gauss_markov_theorem]]
- [[heteroscedasticity]]
- [[maximum_likelihood_estimation]]