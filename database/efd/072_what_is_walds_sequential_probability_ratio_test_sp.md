---
id: efd_072
course: Estimation, Filtration, and Detection
tags: [sequential-analysis, hypothesis-testing, likelihood-ratio]
difficulty: 3
type: open
status: to_learn
---

# Question
What is Wald's Sequential Probability Ratio Test (SPRT)? How does it differ from a standard fixed-sample-size test?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Wald's SPRT is a statistical hypothesis test where the number of samples is not pre-determined but depends on the observed data. It differs from fixed-sample-size tests by potentially reaching a decision much earlier, leading to a smaller average sample number (ASN) for the same error probabilities.

## Explanation
Wald's Sequential Probability Ratio Test (SPRT) is a specific type of statistical test used for deciding between two hypotheses—typically a null hypothesis $H_0$ and an alternative hypothesis $H_1$. Unlike the Neyman-Pearson framework, which fixes the number of observations $N$ in advance to minimize the probability of error, the SPRT treats the sample size as a random variable.

In the SPRT, the Likelihood Ratio (LR) is updated iteratively as each new observation $x_i$ arrives. The test compares the cumulative LR against two constant thresholds, $A$ and $B$. These thresholds are directly related to the desired Type I error probability ($\alpha$) and Type II error probability ($\beta$). Specifically, Wald provided the approximations $A \approx \frac{1-\beta}{\alpha}$ and $B \approx \frac{\beta}{1-\alpha}$.

The primary advantage of the SPRT over fixed-sample-size tests is efficiency. On average, the SPRT requires significantly fewer observations to reach a conclusion with the same levels of confidence ($\alpha$ and $\beta$). This is particularly critical in signal processing and control applications where data acquisition is costly, time-sensitive, or where a rapid detection of a change in system state is required. However, while the Average Sample Number (ASN) is lower, the actual number of samples required for a specific trial can theoretically be very large, although the probability of the test continuing indefinitely is zero.

### Steps / Derivation
1. Calculate the Log-Likelihood Ratio (LLR) for the $n$-th observation:
$$
\Lambda_n = \ln \frac{P(x_1, \dots, x_n | H_1)}{P(x_1, \dots, x_n | H_0)} = \sum_{i=1}^{n} \ln \frac{p(x_i | H_1)}{p(x_i | H_0)}
$$
2. Define the decision boundaries based on desired error rates $\alpha$ and $\beta$:
$$
a = \ln \frac{\beta}{1-\alpha}, \quad b = \ln \frac{1-\beta}{\alpha}
$$
3. At each step $n$, evaluate the decision rule:
   - If $\Lambda_n \geq b$, accept $H_1$ and stop.
   - If $\Lambda_n \leq a$, accept $H_0$ and stop.
   - If $a < \Lambda_n < b$, continue to take observation $n+1$.

## Related Concepts
- [[neyman_pearson_lemma]]
- [[average_sample_number]]
- [[likelihood_ratio_test]]