---
id: efd_017
course: Estimation, Filtration, and Detection
tags: [bayesian-inference, parameter-estimation, probability-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
Write down Bayes' Rule for a parameter vector $\theta$ given data $D$ and identify the roles of the Prior, Likelihood, Posterior, and Evidence.

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** $p(\theta | D) = \frac{p(D | \theta) p(\theta)}{p(D)}$

## Explanation
In the context of Estimation, Filtration, and Detection, Bayes' Rule serves as the fundamental mechanism for updating our beliefs about a parameter vector $\theta$ based on observed data $D$. It bridges the gap between a forward model—which describes how data is generated—and an inverse problem—which involves estimating the underlying parameters from that data.

The components are defined as follows:
1. **The Posterior $p(\theta | D)$**: This represents our updated knowledge about $\theta$ after observing the data. It is a probability distribution that quantifies the uncertainty in our estimate.
2. **The Likelihood $p(D | \theta)$**: This is the probability of observing the specific data $D$ given a fixed value of $\theta$. In estimation theory, this is often derived from the sensor noise model or the system's measurement equation.
3. **The Prior $p(\theta)$**: This encapsulates all knowledge (or lack thereof) about $\theta$ before the data is collected. It can represent physical constraints, historical data, or a subjective belief (e.g., assuming a Gaussian distribution for a position).
4. **The Evidence $p(D)$**: Also known as the marginal likelihood, this is a normalization constant that ensures the posterior integrates to one. It is calculated by marginalizing the likelihood over the prior: $p(D) = \int p(D|\theta)p(\theta)d\theta$. In many detection tasks, this term is crucial for model selection.

### Steps / Derivation
1. Start with the definition of conditional probability for two events/variables:
$$
p(\theta | D) = \frac{p(\theta \cap D)}{p(D)}
$$
2. Apply the product rule to the joint distribution $p(\theta \cap D) = p(D | \theta)p(\theta)$:
$$
p(\theta | D) = \frac{p(D | \theta) p(\theta)}{p(D)}
$$

## Related Concepts
- [[maximum_a_posteriori_estimation]]
- [[bayesian_recursive_filtering]]
- [[minimum_mean_square_error]]