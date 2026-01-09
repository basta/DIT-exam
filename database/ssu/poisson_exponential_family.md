---
id: ssu_batch7_002
course: Statistical Machine Learning
tags: [exponential-family, poisson-distribution, maximum-likelihood, natural-parameter]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(4p) A discrete random variable $x \in \mathbb{N}$ is Poisson distributed with
$$ p(x = k) = \frac{\lambda^k e^{-\lambda}}{k!}, $$
where $\lambda$ is a positive parameter.

**a)** Show that Poisson distributions form an exponential family. Express the natural parameter as a function of $\lambda$.

**b)** Deduce the maximum likelihood estimate for the natural parameter of a Poisson distribution, given an i.i.d. training set $\mathcal{T}^m = \{k_i \in \mathbb{N} \mid i = 1, \dots, m\}$.

---
# Solution
## a) Exponential Family Form
The canonical form of the exponential family is:
$$ p(x) = h(x) \exp(\theta \cdot T(x) - A(\theta)) $$
Rewrite the Poisson PMF ($k$ is the random variable $x$):
$$ p(x) = \frac{1}{x!} \lambda^x e^{-\lambda} = \frac{1}{x!} \exp(x \ln \lambda - \lambda) $$
Comparing this to the canonical form:
-   $h(x) = \frac{1}{x!}$
-   $\theta \cdot T(x) = x \ln \lambda \implies T(x) = x$, Natural Parameter $\theta = \ln \lambda$.
-   $A(\theta) = \lambda = \exp(\theta)$.

**Natural Parameter:**
$$ \theta = \ln \lambda $$

## b) MLE for Natural Parameter
We want the MLE for $\theta$.
First, find MLE for $\lambda$ or directly for $\theta$.
The log-likelihood for $\theta$:
$$ L(\theta) = \sum_{i=1}^m \ln p(x_i) = \sum_{i=1}^m \left( x_i \theta - e^\theta - \ln(x_i!) \right) $$
Differentiate w.r.t $\theta$:
$$ \frac{\partial L}{\partial \theta} = \sum_{i=1}^m (x_i - e^\theta) = \sum x_i - m e^\theta $$
Set to 0:
$$ \sum x_i = m e^\theta $$
$$ e^{\hat{\theta}} = \frac{1}{m} \sum_{i=1}^m x_i = \bar{x} $$
$$ \hat{\theta} = \ln(\bar{x}) $$

So the Maximum Likelihood Estimate for the natural parameter $\theta$ is the natural logarithm of the sample mean.

## Related Concepts
- [[exponential-family]]
- [[poisson-distribution]]
- [[maximum-likelihood]]
