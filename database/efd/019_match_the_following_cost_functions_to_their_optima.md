---
id: efd_019
course: Estimation, Filtration, and Detection
tags: [bayes-estimation, cost-functions, optimality-criteria, mmse]
difficulty: 2
type: open
status: to_learn
---

# Question
Match the following cost functions to their optimal estimators: Quadratic Error, Absolute Error, and Uniform Cost.

## Options
A) Quadratic: Mean; Absolute: Median; Uniform: Mode (MAP)
B) Quadratic: Mode; Absolute: Mean; Uniform: Median 
C) Quadratic: Median; Absolute: Mode; Uniform: Mean
D) Quadratic: Mean; Absolute: Mode; Uniform: Median

---
# Solution
**Correct Answer:** A

## Explanation
In Bayesian estimation, the optimal estimator $\hat{x}$ is the one that minimizes the expected cost (also known as the Bayes risk) based on the posterior distribution $p(x|y)$. The choice of a "cost function" $C(\epsilon)$, where $\epsilon = x - \hat{x}$, determines which statistical property of the posterior distribution is targeted as the optimal estimate.

1. **Quadratic Error (Mean Square Error - MSE):** The cost function is defined as $C(\epsilon) = \epsilon^2$. To minimize the expected value $E[(x - \hat{x})^2 | y]$, we take the derivative with respect to $\hat{x}$ and set it to zero. This leads to the **conditional mean** $\hat{x}_{MS} = E[x|y]$. This is the most common estimator used in Gaussian environments and Kalman filtering.

2. **Absolute Error (Mean Absolute Error - MAE):** The cost function is $C(\epsilon) = |\epsilon|$. Minimizing $E[|x - \hat{x}| | y]$ results in a value $\hat{x}$ where the probability of the true value being above the estimate is equal to the probability of it being below. This is the definition of the **conditional median**.

3. **Uniform Cost (Maximum A Posteriori - MAP):** The cost function is defined as $C(\epsilon) = 0$ if $|\epsilon| < \Delta$ and $1$ otherwise (as $\Delta \to 0$). Minimizing the expected cost in this scenario is equivalent to maximizing the probability that the estimate is "exactly" the true value. This occurs at the peak of the posterior density, making the optimal estimate the **conditional mode**.

### Steps / Derivation
1. **Quadratic:** Minimize $J = \int_{-\infty}^{\infty} (x - \hat{x})^2 p(x|y) dx$.
2. **Absolute:** Minimize $J = \int_{-\infty}^{\infty} |x - \hat{x}| p(x|y) dx$.
3. **Uniform:** Minimize $J = 1 - \int_{\hat{x}-\Delta}^{\hat{x}+\Delta} p(x|y) dx$.
$$
\frac{d}{d\hat{x}} E[(x - \hat{x})^2 | y] = 0 \implies \hat{x} = \int x p(x|y) dx
$$

## Related Concepts
- [[conditional_expectation]]
- [[bayesian_risk]]
- [[maximum_a_posteriori]]