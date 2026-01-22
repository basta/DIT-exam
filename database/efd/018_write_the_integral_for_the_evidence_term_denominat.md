---
id: efd_018
course: Estimation, Filtration, and Detection
tags: [bayesian-inference, map-estimation, model-selection, marginal-likelihood]
difficulty: 2
type: open
status: to_learn
---

# Question
Write the integral for the Evidence term (denominator) in Bayes' rule. Why is this term often ignored for MAP estimation but crucial for model comparison?

---
# Solution
**Correct Answer:** $p(y) = \int p(y|\theta)p(\theta) d\theta$

## Explanation
In the context of Bayesian inference, Bayes' Rule is expressed as $p(\theta|y) = \frac{p(y|\theta)p(\theta)}{p(y)}$, where $\theta$ represents the parameters and $y$ represents the observed data. The denominator $p(y)$, also known as the **Evidence** or **Marginal Likelihood**, represents the probability of observing the data $y$ under all possible parameter values weighted by their prior probability.

**Why it is ignored for MAP estimation:**
Maximum A Posteriori (MAP) estimation seeks to find the specific value of $\theta$ that maximizes the posterior distribution $p(\theta|y)$. Since the evidence term $p(y)$ is an integral over the entire parameter space $\Theta$, it results in a constant value that does not depend on any specific realization of $\theta$. When performing optimization (differentiation or searching for a mode) with respect to $\theta$, a constant divisor does not change the location of the maximum. Therefore, we can state $p(\theta|y) \propto p(y|\theta)p(\theta)$ and find $\hat{\theta}_{MAP} = \arg\max_{\theta} [p(y|\theta)p(\theta)]$, significantly simplifying the computation by avoiding a potentially high-dimensional integral.

**Why it is crucial for model comparison:**
When comparing two different models $M_1$ and $M_2$, we are evaluating which model structure more likely generated the data. The evidence term is no longer a shared constant; rather, it is specific to the model: $p(y|M_i) = \int p(y|\theta_i, M_i) p(\theta_i|M_i) d\theta_i$. This term naturally penalizes over-complex models (an expression of Occam’s Razor). A complex model with many parameters spreads its prior probability mass thin over a large space, whereas a simpler model concentrates its probability. Comparing the "Bayes Factor" (the ratio of the evidence for two models) allows us to select the model that provides the best trade-off between fit and complexity.

### Steps / Derivation
1. Write the definition of the Marginal Likelihood (Evidence) using the law of total probability:
$$
p(y) = \int_{\Theta} p(y, \theta) d\theta
$$
2. Apply the product rule of probability ($p(y, \theta) = p(y|\theta)p(\theta)$) to express the evidence in terms of the likelihood and the prior:
$$
p(y) = \int_{\Theta} p(y|\theta)p(\theta) d\theta
$$

## Related Concepts
- [[maximum_a_posteriori_estimation]]
- [[bayesian_model_selection]]
- [[marginal_likelihood]]