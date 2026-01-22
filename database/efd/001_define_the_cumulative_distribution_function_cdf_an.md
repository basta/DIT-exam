---
id: efd_001
course: Estimation, Filtration, and Detection
tags: [probability-basics, stochastic-processes, detection-fundamentals]
difficulty: 1
type: open
status: to_learn
---

# Question
Define the Cumulative Distribution Function (CDF) and the Probability Density Function (PDF). How are they mathematically related?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The CDF $F_X(x)$ is the probability that a random variable $X$ takes a value less than or equal to $x$, while the PDF $f_X(x)$ describes the relative likelihood of $X$ taking a specific value. They are related through integration and differentiation.

## Explanation
In the context of Signal Processing and Control Theory, characterizing random variables is fundamental for noise modeling and decision-making. 

The **Cumulative Distribution Function (CDF)**, denoted as $F_X(x)$, is defined for any random variable $X$ (discrete or continuous) as the probability that the realization of $X$ is less than or equal to a threshold $x$. Mathematically, $F_X(x) = P(X \leq x)$. The CDF is a non-decreasing function that ranges from 0 (at $-\infty$) to 1 (at $+\infty$). It provides a complete probabilistic description of the random variable.

The **Probability Density Function (PDF)**, denoted as $f_X(x)$, is used for continuous random variables. Unlike the CDF, the PDF does not represent a probability directly; rather, the area under the PDF curve over an interval $[a, b]$ represents the probability that the random variable falls within that interval. For an infinitesimal interval $dx$, the probability is $f_X(x)dx$.

The mathematical relationship between the two is governed by the Fundamental Theorem of Calculus. The PDF is the derivative of the CDF with respect to $x$. Conversely, the CDF is the integral of the PDF from $-\infty$ to the point $x$. In detection theory, these functions are critical for calculating the Probability of False Alarm ($P_{FA}$) and Probability of Detection ($P_D$), where we often integrate the PDF over specific decision regions.

### Steps / Derivation
1. **From PDF to CDF:** The CDF is obtained by accumulating (integrating) the probability density from the lowest possible value up to $x$.
$$
F_X(x) = \int_{-\infty}^{x} f_X(u) \, du
$$
2. **From CDF to PDF:** If the CDF is differentiable, the PDF is its rate of change at point $x$.
$$
f_X(x) = \frac{d}{dx} F_X(x)
$$

## Related Concepts
- [[random_variables]]
- [[likelihood_ratio_testing]]
- [[gaussian_distribution]]