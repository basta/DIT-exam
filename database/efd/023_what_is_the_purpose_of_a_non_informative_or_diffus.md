---
id: efd_023
course: Estimation, Filtration, and Detection
tags: [bayesian-estimation, prior-distributions, maximum-likelihood, information-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
What is the purpose of a non-informative or diffuse prior? How does a flat prior influence the posterior distribution compared to the likelihood?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** The purpose of a non-informative prior is to allow the observed data (the likelihood) to dominate the inference process, ensuring that subjective prior beliefs do not bias the parameter estimation. When a flat prior is used, the posterior distribution becomes directly proportional to the likelihood function.

## Explanation
In Bayesian estimation, the posterior distribution $p(\theta | y)$ is determined by the product of the likelihood $p(y | \theta)$ and the prior $p(\theta)$, according to Bayes' Rule. The primary purpose of a **non-informative** (or diffuse/flat) prior is to represent a state of "total ignorance" regarding the parameter $\theta$ before any data is collected. This is particularly useful in scientific contexts where the goal is to provide an objective analysis based solely on the evidence provided by the current experiment, or when no historical data exists to formulate a "strong" prior.

A **flat prior** is a specific type of non-informative prior where $p(\theta) \propto C$ (a constant) over the parameter space. When this is applied, the prior term in the numerator of Bayes' Rule effectively drops out as a constant factor. Consequently, the shape of the posterior distribution becomes identical to the shape of the likelihood function. In this scenario, the Bayesian Maximum A Posteriori (MAP) estimate converges exactly to the Maximum Likelihood Estimate (MLE). 

However, one must be cautious with non-informative priors: if the parameter space is infinite (e.g., $(-\infty, \infty)$), a constant prior results in an "improper prior" because its integral does not converge to 1. While the resulting posterior is often still well-behaved (proper) once multiplied by the likelihood, this transition from prior to posterior highlights that the "information" in the final estimate is derived almost exclusively from the signal and noise characteristics of the observed data $y$.

### Steps / Derivation
1. Write the general form of Bayes' Theorem:
$$
p(\theta | y) = \frac{p(y | \theta) p(\theta)}{p(y)}
$$
2. Assume a flat prior where $p(\theta) = k$ for all $\theta$ in the support of the likelihood:
$$
p(\theta | y) = \frac{p(y | \theta) \cdot k}{\int p(y | \theta) \cdot k \, d\theta}
$$
3. Simplify the expression by canceling the constant $k$:
$$
p(\theta | y) = \frac{p(y | \theta)}{\int p(y | \theta) \, d\theta} \propto p(y | \theta)
$$
4. Observe that the mode of the posterior (MAP) now equals the mode of the likelihood (MLE):
$$
\hat{\theta}_{MAP} = \arg\max_{\theta} p(y | \theta) = \hat{\theta}_{MLE}
$$

## Related Concepts
- [[maximum_likelihood_estimation]]
- [[maximum_a_posteriori]]
- [[conjugate_priors]]