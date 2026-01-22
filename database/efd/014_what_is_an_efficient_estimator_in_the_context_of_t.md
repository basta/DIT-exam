---
id: efd_014
course: Estimation, Filtration, and Detection
tags: [cramer-rao-lower-bound, unbiased-estimators, fisher-information, efficiency]
difficulty: 2
type: open
status: to_learn
---

# Question
What is an efficient estimator in the context of the Cramér-Rao Lower Bound?

## Options
A) An estimator that has the smallest possible bias for a given sample size.
B) An unbiased estimator whose variance is equal to the Cramér-Rao Lower Bound (CRLB) for all values of the parameter.
C) An estimator that achieves the minimum mean square error (MMSE) among all possible estimators, including biased ones.
D) An estimator that converges to the true parameter value as the number of samples approaches infinity.

---
# Solution
**Correct Answer:** B

## Explanation
In the field of statistical signal processing and estimation theory, the performance of an unbiased estimator is often measured by its variance. The Cramér-Rao Lower Bound (CRLB) provides a fundamental lower limit on the variance of any unbiased estimator $\hat{\theta}$ of a deterministic parameter $\theta$. Specifically, if $p(x; \theta)$ is the likelihood function, the CRLB states that $Var(\hat{\theta}) \geq \frac{1}{I(\theta)}$, where $I(\theta)$ is the Fisher Information.

An **efficient estimator** is defined as an unbiased estimator that maintains a variance exactly equal to this theoretical floor. In other words, it is "efficient" because it extracts all possible information about the parameter from the data, achieving the highest possible precision allowed by the laws of probability for a given data model.

It is important to note that an efficient estimator does not always exist for every estimation problem. If the CRLB is not met with equality, one might look for a Minimum Variance Unbiased Estimator (MVUE), which is the best possible unbiased estimator even if it doesn't reach the CRLB. However, if an estimator is efficient, it is automatically the MVUE. Mathematically, an efficient estimator exists if and only if the score function (the derivative of the log-likelihood) can be expressed in a specific linear form.

### Steps / Derivation
1. Define the variance of an unbiased estimator $\hat{\theta}$:
$$
Var(\hat{\theta}) = E[(\hat{\theta} - E[\hat{\theta}])^2]
$$
2. State the Cramér-Rao Inequality for an unbiased estimator:
$$
Var(\hat{\theta}) \geq \frac{1}{-E\left[\frac{\partial^2 \ln p(x; \theta)}{\partial \theta^2}\right]} = \frac{1}{I(\theta)}
$$
3. Apply the condition for efficiency, where the equality holds:
$$
Var(\hat{\theta})_{eff} = \frac{1}{I(\theta)}
$$
4. Note the condition for the existence of an efficient estimator:
$$
\frac{\partial \ln p(x; \theta)}{\partial \theta} = I(\theta) (\hat{\theta}(x) - \theta)
$$

## Related Concepts
- [[fisher_information]]
- [[minimum_variance_unbiased_estimator]]
- [[maximum_likelihood_estimation]]