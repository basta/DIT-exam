---
id: efd_021
course: Estimation, Filtration, and Detection
tags: [map-estimation, maximum-likelihood, bayesian-inference, point-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the MAP estimator. How does it relate to the Maximum Likelihood Estimator (MLE) and under what condition are they identical?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The MAP estimator chooses the parameter value that maximizes the posterior distribution. It reduces to the MLE when the prior distribution of the parameter is uniform or non-informative.

## Explanation
The Maximum A Posteriori (MAP) estimator is a Bayesian point estimation technique. Unlike frequentist approaches, Bayesian estimation treats the unknown parameter $\theta$ as a random variable with a known prior probability density function (PDF), denoted $p(\theta)$. The MAP estimate is the mode of the posterior distribution, representing the most likely value of $\theta$ given the observed data $y$.

The relationship between MAP and Maximum Likelihood Estimation (MLE) is rooted in Bayes' Rule. While MLE seeks to maximize the likelihood function $p(y|\theta)$—asking "which parameter makes these observations most probable?"—MAP seeks to maximize $p(\theta|y)$—asking "which parameter is most probable given these observations?". 

Mathematically, the posterior is proportional to the product of the likelihood and the prior. If the prior $p(\theta)$ is a flat (uniform) distribution over the parameter space, it acts as a constant in the optimization process. In this specific case, the location of the maximum of the posterior becomes identical to the location of the maximum of the likelihood. Consequently, the MLE can be viewed as a special case of the MAP estimator where no prior knowledge is assumed (or the prior is uninformative).

## Steps / Derivation
1. Start with Bayes' Rule for the posterior distribution:
$$
p(\theta|y) = \frac{p(y|\theta)p(\theta)}{p(y)}
$$
2. Define the MAP estimator as the argument that maximizes the posterior. Since the evidence $p(y)$ does not depend on $\theta$, it is ignored during optimization:
$$
\hat{\theta}_{MAP} = \arg \max_{\theta} [p(y|\theta) p(\theta)]
$$
3. Apply the natural logarithm to simplify the optimization (log-MAP):
$$
\hat{\theta}_{MAP} = \arg \max_{\theta} [\ln p(y|\theta) + \ln p(\theta)]
$$
4. Observe that if $p(\theta) = C$ (a uniform prior), then $\ln p(\theta)$ is a constant. The expression reduces to the MLE:
$$
\hat{\theta}_{ML} = \arg \max_{\theta} \ln p(y|\theta)
$$

## Related Concepts
- [[bayesean_parameter_estimation]]
- [[posterior_probability]]
- [[uniform_prior]]