---
id: efd_007
course: Estimation, Filtration, and Detection
tags: [mse, bias-variance-tradeoff, estimator-performance]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the Mean Squared Error (MSE) of an estimator. How can it be decomposed into variance and bias?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $MSE(\hat{\theta}) = Var(\hat{\theta}) + [Bias(\hat{\theta})]^2$

## Explanation
The Mean Squared Error (MSE) is a fundamental risk function used to measure the quality of an estimator. Given an unknown parameter $\theta$ and its estimator $\hat{\theta}$ (which is a random variable derived from observed data), the MSE measures the average squared difference between the estimated value and the true parameter value. Mathematically, it is defined as $E[(\hat{\theta} - \theta)^2]$. 

The significance of MSE lies in its ability to capture two distinct types of errors: precision and accuracy. Precision is represented by the **Variance**, which measures how much the estimate fluctuates around its own expected value. Accuracy is represented by the **Bias**, which measures the distance between the expected value of the estimator and the true parameter value. 

The bias-variance decomposition is a critical concept in signal processing and machine learning because it illustrates the inherent trade-off in model complexity. An unbiased estimator ($\text{Bias} = 0$) is not always preferable if it results in an extremely high variance. Conversely, a biased estimator might be chosen if it significantly reduces the variance, leading to a lower overall MSE. This decomposition is derived by adding and subtracting $E[\hat{\theta}]$ within the expectation of the squared error and expanding the quadratic term. The cross-product term vanishes due to the properties of expectation, leaving the sum of the variance and the square of the bias.

### Steps / Derivation
1. Start with the definition of MSE and subtract/add $E[\hat{\theta}]$ inside the square:
$$
MSE(\hat{\theta}) = E\left[ \left( \hat{\theta} - \theta \right)^2 \right] = E\left[ \left( (\hat{\theta} - E[\hat{\theta}]) + (E[\hat{\theta}] - \theta) \right)^2 \right]
$$
2. Expand the quadratic term $(a+b)^2 = a^2 + 2ab + b^2$:
$$
MSE(\hat{\theta}) = E\left[ (\hat{\theta} - E[\hat{\theta}])^2 \right] + 2E\left[ (\hat{\theta} - E[\hat{\theta}])(E[\hat{\theta}] - \theta) \right] + E\left[ (E[\hat{\theta}] - \theta)^2 \right]
$$
3. Note that $(E[\hat{\theta}] - \theta)$ is a constant, and $E[\hat{\theta} - E[\hat{\theta}]] = 0$, causing the middle term to vanish. Thus:
$$
MSE(\hat{\theta}) = Var(\hat{\theta}) + [Bias(\hat{\theta})]^2
$$

## Related Concepts
- [[cramer_rao_lower_bound]]
- [[minimum_mean_squared_error_estimation]]
- [[bias_variance_tradeoff]]