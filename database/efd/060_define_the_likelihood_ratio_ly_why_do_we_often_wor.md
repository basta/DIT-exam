---
id: efd_060
course: Estimation, Filtration, and Detection
tags: [hypothesis-testing, likelihood-ratio, signal-detection]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the Likelihood Ratio $L(y)$. Why do we often work with the Log-Likelihood Ratio $l(y)$ instead?

![[question_image.png]]

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
The Likelihood Ratio is the ratio of the conditional probability density functions (or mass functions) of the observation $y$ under two competing hypotheses, defined as $L(y) = \frac{p(y|H_1)}{p(y|H_0)}$. We use the log-likelihood ratio $l(y) = \ln L(y)$ primarily for mathematical simplification (converting products to sums) and numerical stability.

## Explanation
In the context of binary hypothesis testing, the Likelihood Ratio $L(y)$ serves as a sufficient statistic for deciding between a null hypothesis $H_0$ and an alternative hypothesis $H_1$. It quantifies how much more likely the observed data $y$ is under $H_1$ compared to $H_0$. According to the Neyman-Pearson lemma, the optimal decision rule consists of comparing $L(y)$ to a threshold $\eta$.

There are three primary reasons why engineers and statisticians prefer the Log-Likelihood Ratio (LLR), denoted as $l(y) = \ln[L(y)]$:

1. **Mathematical Simplification**: Many stochastic signals are modeled using the Exponential Family (e.g., Gaussian, Exponential, Poisson). These distributions involve exponential terms. Applying the natural logarithm linearizes the exponent, transforming complex multiplicative relationships into simple additive ones. When dealing with Independent and Identically Distributed (IID) samples $y = [y_1, y_2, ..., y_n]^T$, the joint PDF is a product of marginal PDFs. The log transform turns this product into a summation: $\sum \ln \frac{p(y_i|H_1)}{p(y_i|H_0)}$, which is much easier to differentiate when seeking Maximum Likelihood Estimates (MLE).

2. **Numerical Stability**: In practical signal processing, we often deal with large datasets. Multiplying many small probabilities can lead to "arithmetic underflow," where the values become smaller than the precision limits of a computer. Working in the log-domain keeps magnitudes within a manageable range.

3. **Monotonicity**: Since the logarithm is a strictly increasing (monotonic) function, applying it to $L(y)$ does not change the location of the maximum or the relative ordering of values. Therefore, comparing $l(y)$ to a new threshold $\ln(\eta)$ yields the exact same decision as comparing $L(y)$ to $\eta$.

### Steps / Derivation
1. Define the Likelihood Ratio for an observation vector $y$:
$$
L(y) = \frac{f_{Y|H_1}(y|H_1)}{f_{Y|H_0}(y|H_0)}
$$
2. Apply the natural logarithm to obtain the Log-Likelihood Ratio:
$$
l(y) = \ln \left( \frac{f_{Y|H_1}(y|H_1)}{f_{Y|H_0}(y|H_0)} \right) = \ln f_{Y|H_1}(y|H_1) - \ln f_{Y|H_0}(y|H_0)
$$

## Related Concepts
- [[neyman_pearson_lemma]]
- [[sufficient_statistics]]
- [[maximum_likelihood_estimation]]