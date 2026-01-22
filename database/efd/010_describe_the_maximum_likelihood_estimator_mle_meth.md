---
id: efd_010
course: Estimation, Filtration, and Detection
tags: [parameter-estimation, maximum-likelihood, statistics]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe the Maximum Likelihood Estimator (MLE) method. What is the objective function being maximized?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The Likelihood Function or the Log-Likelihood Function.

## Explanation
The Maximum Likelihood Estimator (MLE) is a fundamental point estimation method used in signal processing and statistics to find the parameter values that make the observed data "most probable." Unlike Bayesian estimation, which treats parameters as random variables with prior distributions, MLE treats the parameter vector $\theta$ as a deterministic but unknown constant.

The core philosophy of MLE is that, given a set of measurements or observations $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$, the best estimate $\hat{\theta}_{ML}$ is the value that maximizes the probability density function (PDF) of the observed data. When we view this PDF as a function of the parameters $\theta$ rather than the data $\mathbf{x}$, it is called the Likelihood Function, denoted as $L(\theta; \mathbf{x})$.

In practice, because many probability distributions (like the Gaussian distribution) involve exponential terms, it is computationally and analytically easier to maximize the natural logarithm of the likelihood function, known as the Log-Likelihood Function $\ell(\theta)$. Since the logarithm is a monotonically increasing function, the value of $\theta$ that maximizes the log-likelihood is identical to the value that maximizes the likelihood. MLE is favored in many engineering applications because it is asymptotically unbiased, consistent, and achieves the Cramér-Rao Lower Bound (CRLB) as the number of samples approaches infinity (asymptotic efficiency).

### Steps / Derivation
1. Define the joint PDF of the observed data given the parameter $\theta$: $p(\mathbf{x} | \theta)$.
2. Construct the Likelihood Function $L(\theta)$ or the Log-Likelihood Function $\ell(\theta)$.
3. Find the maximum by taking the derivative with respect to $\theta$ (the score function) and setting it to zero.
$$
\hat{\theta}_{ML} = \arg \max_{\theta} \ln p(\mathbf{x} | \theta)
$$

## Related Concepts
- [[cramer_rao_lower_bound]]
- [[sufficient_statistics]]
- [[bayesian_estimation]]