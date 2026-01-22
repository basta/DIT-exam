---
id: efd_031
course: Estimation, Filtration, and Detection
tags: [least-squares, unbiasedness, Gauss-Markov]
difficulty: 2
type: open
status: to_learn
---

# Question
Under what specific assumptions regarding the noise term 'e' is the Least Squares estimator unbiased?

## Options
A) The noise must be Gaussian and Independent and Identically Distributed (IID).
B) The noise must have a zero mean $E[e] = 0$ and be uncorrelated with the regressors $X$.
C) The noise must have constant variance (homoscedasticity) $\text{Var}(e) = \sigma^2 I$.
D) The noise must be strictly smaller than the signal-to-noise ratio.

---
# Solution
**Correct Answer:** B) The noise must have a zero mean $E[e] = 0$ and be uncorrelated with the regressors $X$.

## Explanation
In the context of the Linear Least Squares (LLS) model $y = X\theta + e$, the estimator is defined as $\hat{\theta} = (X^T X)^{-1} X^T y$. For an estimator to be unbiased, the expected value of the estimate must equal the true parameter value, i.e., $E[\hat{\theta}] = \theta$. 

There are two primary conditions required for this property to hold:
1. **Zero Mean Error:** The expected value of the noise term must be zero ($E[e] = 0$). If the noise has a non-zero mean, this "offset" will be absorbed into the parameter estimates (specifically the intercept), causing a bias.
2. **Exogeneity/Uncorrelatedness:** The noise term must be uncorrelated with the regressor matrix $X$. Mathematically, this is expressed as $E[X^T e] = 0$ or $E[e|X] = 0$. If the noise is correlated with the predictors, the estimator will attribute variations caused by the noise to the parameters $\theta$, leading to "endogeneity bias."

It is a common misconception that noise must be Gaussian or homoscedastic (constant variance) for the estimator to be unbiased. While those assumptions are required for the Gauss-Markov theorem (to prove that LS is the *Best* Linear Unbiased Estimator or BLUE) and for hypothesis testing, they are not strictly necessary for the proof of unbiasedness itself. Even with heteroscedastic or non-Gaussian noise, $\hat{\theta}$ remains unbiased as long as the noise is centered at zero and independent of the input data.

### Steps / Derivation
1. Substitute the model $y = X\theta + e$ into the Least Squares formula:
$$
\hat{\theta} = (X^T X)^{-1} X^T (X\theta + e)
$$
2. Distribute the terms:
$$
\hat{\theta} = (X^T X)^{-1} X^T X\theta + (X^T X)^{-1} X^T e = \theta + (X^T X)^{-1} X^T e
$$
3. Take the expectation of $\hat{\theta}$ conditioned on $X$:
$$
E[\hat{\theta} | X] = \theta + (X^T X)^{-1} X^T E[e | X]
$$
4. For $E[\hat{\theta}] = \theta$, the term $(X^T X)^{-1} X^T E[e | X]$ must vanish, which occurs if $E[e | X] = 0$.

## Related Concepts
- [[gauss_markov_theorem]]
- [[linear_regression_assumptions]]
- [[bias_variance_tradeoff]]