---
id: efd_009
course: Estimation, Filtration, and Detection
tags: [likelihood-function, maximum-likelihood-estimation, probability-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
Explain the concept of the Likelihood Function. How does it differ from a Probability Density Function?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The Likelihood Function $L(\theta | x)$ evaluates how well a parameter $\theta$ explains the observed data $x$, treating the data as fixed and the parameter as variable, whereas a PDF $f(x | \theta)$ describes the distribution of data $x$ for a fixed parameter $\theta$.

## Explanation
In statistical signal processing and estimation theory, the distinction between a Likelihood Function and a Probability Density Function (PDF) is fundamental, though they are algebraically represented by the same functional form. 

A **Probability Density Function**, denoted as $f(x; \theta)$ or $f(x | \theta)$, is a function of the random variable $x$ given a known set of parameters $\theta$. It is used *before* data is collected to predict the outcomes of an experiment. The area under a PDF must integrate to 1 over the domain of $x$, as it represents the distribution of total probability.

The **Likelihood Function**, denoted as $L(\theta | x)$, is used *after* the data $x$ has been observed. In this context, the data $x$ is fixed, and the function is treated as a function of the unknown parameter $\theta$. The primary purpose of the likelihood is to quantify the "support" provided by the observed data for various possible values of $\theta$. Unlike a PDF, the Likelihood Function does not necessarily integrate to 1 over the parameter space and is not a probability distribution. It is the core component of Maximum Likelihood Estimation (MLE), where we seek the value $\hat{\theta}$ that maximizes $L(\theta | x)$.

### Steps / Derivation
1. Define the joint density of the observed data $x$ given parameter $\theta$:
$$
f(x_1, x_2, ..., x_n | \theta)
$$
2. After observation, fix $x$ and treat the expression as a function of $\theta$ to obtain the Likelihood:
$$
L(\theta | x) = \prod_{i=1}^{n} f(x_i | \theta)
$$
3. To simplify maximization, compute the Log-Likelihood:
$$
\ell(\theta) = \ln L(\theta | x) = \sum_{i=1}^{n} \ln f(x_i | \theta)
$$

## Related Concepts
- [[maximum_likelihood_estimation]]
- [[sufficient_statistics]]
- [[bayesian_inference]]