---
id: efd_015
course: Estimation, Filtration, and Detection
tags: [unbiased-estimation, sample-variance, statistical-moments, bessels-correction]
difficulty: 2
type: open
status: to_learn
---

# Question
Consider a set of independent and identically distributed (i.i.d.) samples. Is the standard sample variance formula $S^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2$ an unbiased estimator? If not, how do you correct it?

## Options
A) Yes, it is unbiased.
B) No, it is biased; correct it by multiplying by $\frac{N}{N+1}$.
C) No, it is biased; correct it by using the divisor $(N-1)$ instead of $N$.
D) No, it is biased; correct it by subtracting the square of the mean.

---
# Solution
**Correct Answer:** C

## Explanation
In estimation theory, an estimator is considered **unbiased** if its expected value is equal to the true parameter being estimated. For a population with mean $\mu$ and variance $\sigma^2$, the estimator $S^2_{ML} = \frac{1}{N} \sum (x_i - \bar{x})^2$ (often associated with Maximum Likelihood Estimation for Gaussian distributions) consistently underestimates the true population variance. 

The source of this bias lies in the fact that the sample mean $\bar{x}$ is used in place of the true population mean $\mu$. Because $\bar{x}$ is calculated from the same data used to estimate variance, the residuals $(x_i - \bar{x})$ are not independent; they are "drawn" toward $\bar{x}$, which is the value that minimizes the sum of squared deviations. This results in a loss of one **degree of freedom**. 

Mathematically, it can be shown that $E[S^2_{ML}] = \frac{N-1}{N}\sigma^2$. Since the expected value is not $\sigma^2$, the estimator is biased. To correct this, we apply **Bessel's Correction**, which involves multiplying the biased estimator by $\frac{N}{N-1}$. This leads to the unbiased sample variance formula:
$$ S^2_{unbiased} = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2 $$
As $N \to \infty$, the bias disappears, making the original formula asymptotically unbiased.

### Steps / Derivation
1. Expand the summation term $(x_i - \bar{x})^2$ by introducing $\mu$:
$$
\sum (x_i - \bar{x})^2 = \sum ((x_i - \mu) - (\bar{x} - \mu))^2 = \sum (x_i - \mu)^2 - N(\bar{x} - \mu)^2
$$
2. Apply the expectation operator $E[\cdot]$ recognizing that $E[(x_i - \mu)^2] = \sigma^2$ and $E[(\bar{x} - \mu)^2] = \text{Var}(\bar{x}) = \frac{\sigma^2}{N}$:
$$
E\left[ \sum (x_i - \bar{x})^2 \right] = \sum \sigma^2 - N \left( \frac{\sigma^2}{N} \right) = N\sigma^2 - \sigma^2 = (N-1)\sigma^2
$$
3. Solve for $E[S^2]$ where $S^2 = \frac{1}{N} \sum (x_i - \bar{x})^2$:
$$
E[S^2] = \frac{N-1}{N}\sigma^2
$$

## Related Concepts
- [[maximum_likelihood_estimation]]
- [[degrees_of_freedom]]
- [[expected_value_properties]]