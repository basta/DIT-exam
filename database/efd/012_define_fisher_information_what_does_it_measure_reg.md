---
id: efd_012
course: Estimation, Filtration, and Detection
tags: [fisher-information, cramer-rao-lower-bound, parameter-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Define Fisher Information. What does it measure regarding the unknown parameter θ?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Fisher Information is the variance of the score function (the gradient of the log-likelihood). It measures the amount of information that an observable random variable $X$ carries about an unknown parameter $\theta$.

## Explanation
Fisher Information ($I(\theta)$) is a fundamental concept in estimation theory that quantifies how much "certainty" or "information" we can extract from data about a parameter we wish to estimate. Mathematically, it is defined as the variance of the **score**, where the score is the partial derivative of the log-likelihood function with respect to $\theta$. 

Intuitively, Fisher Information measures the **sensitivity** of the likelihood function to changes in the parameter $\theta$. If the likelihood function is very "sharp" or peaked around the true value of $\theta$, a small change in $\theta$ results in a large change in the log-likelihood. This implies that the data provides a high degree of certainty about the parameter's location. Conversely, a flat likelihood surface suggests that many different values of $\theta$ are almost equally likely given the data, resulting in low Fisher Information.

In the context of Signal Processing and Estimation, Fisher Information is most famous for its role in the **Cramér-Rao Lower Bound (CRLB)**. The CRLB states that the variance of any unbiased estimator $\hat{\theta}$ is bounded below by the reciprocal of the Fisher Information ($Var(\hat{\theta}) \geq 1/I(\theta)$). Therefore, Fisher Information effectively measures the best possible precision (minimum achievable variance) any unbiased estimation algorithm can attain. High Fisher information implies that a very precise estimate is possible, while low information implies inherent uncertainty regardless of the estimation technique used.

### Steps / Derivation
1. Define the Likelihood function $L(\theta; X) = f(X; \theta)$ and the Log-Likelihood $\ell(\theta; X) = \ln f(X; \theta)$.
2. Calculate the Score function, which is the first derivative: $s(\theta) = \frac{\partial}{\partial \theta} \ln f(X; \theta)$.
3. The Fisher Information is the second moment (variance) of the score:
$$
I(\theta) = E\left[ \left( \frac{\partial}{\partial \theta} \ln f(X; \theta) \right)^2 \right] = -E\left[ \frac{\partial^2}{\partial \theta^2} \ln f(X; \theta) \right]
$$

## Related Concepts
- [[cramer_rao_lower_bound]]
- [[maximum_likelihood_estimation]]
- [[sufficient_statistics]]