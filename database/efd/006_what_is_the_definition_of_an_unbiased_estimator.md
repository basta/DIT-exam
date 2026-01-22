---
id: efd_006
course: Estimation, Filtration, and Detection
tags: [point-estimation, bias, statistical-inference]
difficulty: 1
type: open
status: to_learn
---

# Question
What is the definition of an unbiased estimator?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** An estimator $\hat{\theta}$ is unbiased if its expected value is equal to the true value of the parameter $\theta$ being estimated, i.e., $E[\hat{\theta}] = \theta$.

## Explanation
In the field of signal processing and control theory, estimation involves determining the hidden state or parameters of a system based on noisy observations. An estimator is a rule or function (often denoted as $\hat{\theta}$) that maps a set of observed data to an estimate of a parameter $\theta$. Because the observations are stochastic, the estimate itself is a random variable.

The "bias" of an estimator is defined as the difference between the expected value of the estimator and the true underlying value of the parameter. Specifically, $B(\hat{\theta}) = E[\hat{\theta}] - \theta$. An estimator is considered "unbiased" if this difference is zero for all possible values of $\theta$. 

Intuitively, an unbiased estimator "centers" its probability distribution around the true value. If you were to repeat the experiment an infinite number of times and average the results of an unbiased estimator, you would converge to the exact true value. While being unbiased is a desirable property, it does not guarantee that a single realization of the estimate will be close to the truth; the variance of the estimator also plays a critical role in its performance. In many practical scenarios, such as in Minimum Mean Square Error (MMSE) estimation, a small amount of bias is sometimes accepted if it significantly reduces the variance, leading to a lower overall Mean Square Error (MSE).

### Steps / Derivation
1. Define the estimator $\hat{\theta}$ as a function of the observation vector $\mathbf{y}$.
2. Calculate the expected value of the estimator over the distribution of the data, conditioned on $\theta$.
$$
E[\hat{\theta}] = \int_{-\infty}^{\infty} \hat{\theta}(\mathbf{y}) p(\mathbf{y}; \theta) d\mathbf{y}
$$
3. Set the condition for unbiasedness:
$$
E[\hat{\theta}] - \theta = 0 \implies E[\hat{\theta}] = \theta
$$

## Related Concepts
- [[mean_square_error]]
- [[cramer_rao_lower_bound]]
- [[maximum_likelihood_estimation]]