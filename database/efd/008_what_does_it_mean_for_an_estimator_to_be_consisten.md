---
id: efd_008
course: Estimation, Filtration, and Detection
tags: [point-estimation, asymptotic-properties, statistical-inference]
difficulty: 2
type: open
status: to_learn
---

# Question
What does it mean for an estimator to be consistent? How does this differ from being unbiased?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** An estimator is consistent if it converges in probability to the true parameter value as the sample size approaches infinity. It differs from unbiasedness because consistency is an asymptotic property (large sample limit), while unbiasedness is a finite-sample property.

## Explanation
In estimation theory, we evaluate the quality of an estimator $\hat{\theta}_n$ based on its sampling distribution. 

**Consistency** is an asymptotic property. An estimator is considered consistent if, as the number of observations $n$ increases, the estimate concentratedly "collapses" onto the true parameter value $\theta$. Formally, this is defined as convergence in probability: for any $\epsilon > 0$, $\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| > \epsilon) = 0$. In practical terms, a consistent estimator is guaranteed to provide the correct answer if we have an infinite amount of data. A common sufficient condition for consistency (in the mean-square sense) is that both the bias and the variance of the estimator must vanish as $n \to \infty$.

**Unbiasedness**, on the other hand, is a finite-sample property. An estimator is unbiased if its expected value is equal to the true parameter value for *any* sample size $n$. That is, $E[\hat{\theta}_n] = \theta$. 

The core differences are:
1. **Sample Size:** Unbiasedness must hold for $n=1, 2, \dots$, whereas consistency only cares about the limit as $n \to \infty$.
2. **Existence:** An estimator can be biased but consistent (e.g., the Maximum Likelihood Estimator of variance, which uses $1/n$ instead of $1/(n-1)$). Conversely, an estimator can be unbiased but inconsistent (e.g., using only the first observation $X_1$ to estimate a population mean; it is unbiased, but its variance never shrinks regardless of how many more samples are collected).

## Steps / Derivation
1. **Definition of Unbiasedness:**
$$
E[\hat{\theta}_n] = \theta, \quad \forall n
$$
2. **Definition of Consistency (Convergence in Probability):**
$$
\text{plim}_{n \to \infty} \hat{\theta}_n = \theta
$$
3. **Mean Square Error (MSE) Criterion for Consistency:**
If an estimator's bias $B(\hat{\theta}_n)$ and variance $\text{Var}(\hat{\theta}_n)$ satisfy the following, the estimator is consistent:
$$
\lim_{n \to \infty} B(\hat{\theta}_n) = 0 \quad \text{and} \quad \lim_{n \to \infty} \text{Var}(\hat{\theta}_n) = 0
$$

## Related Concepts
- [[mean_square_error]]
- [[maximum_likelihood_estimation]]
- [[asymptotic_normality]]