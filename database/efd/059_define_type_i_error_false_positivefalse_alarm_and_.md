---
id: efd_059
course: Estimation, Filtration, and Detection
tags: [binary-hypothesis-testing, detection-theory, error-probabilities]
difficulty: 2
type: open
status: to_learn
---

# Question
Define Type I Error (False Positive/False Alarm) and Type II Error (False Negative/Missed Detection). Which probabilities represent these errors?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Type I Error is represented by the False Alarm Probability ($P_{FA}$), and Type II Error is represented by the Miss Probability ($P_M$).

## Explanation
In the context of Detection Theory and Signal Processing, we often deal with Binary Hypothesis Testing. We define two states of nature: the Null Hypothesis ($H_0$), usually representing the absence of a signal (noise only), and the Alternative Hypothesis ($H_1$), representing the presence of a signal (signal plus noise).

A **Type I Error**, commonly referred to as a **False Alarm** or **False Positive**, occurs when the detector decides that the signal is present ($\hat{H} = H_1$) given that the signal was actually absent ($H_0$ is true). In statistical terms, this is rejecting a true null hypothesis. The probability associated with this error is denoted as $P_{FA}$ or $\alpha$. It represents the area under the probability density function of the observation $y$ under $H_0$ that falls within the decision region assigned to $H_1$.

A **Type II Error**, commonly referred to as a **Missed Detection**, **Miss**, or **False Negative**, occurs when the detector decides the signal is absent ($\hat{H} = H_0$) given that the signal was actually present ($H_1$ is true). This corresponds to failing to reject a false null hypothesis. The probability of this error is denoted as $P_M$ or $\beta$.

In detection system design, there is an inherent trade-off between these two errors. Reducing the threshold to make the system more sensitive increases the Probability of Detection ($P_D = 1 - P_M$) but simultaneously increases the Probability of False Alarm ($P_{FA}$). This relationship is often visualized using a Receiver Operating Characteristic (ROC) curve.

### Steps / Derivation
1. Define the decision rule based on the observation $y$ and a threshold $\gamma$:
$$
\text{Decide } H_1 \text{ if } L(y) > \gamma, \text{ else decide } H_0
$$
2. Express the Probability of Type I Error (False Alarm):
$$
P_{FA} = P(\hat{H}=H_1 | H_0) = \int_{\gamma}^{\infty} f(y|H_0) dy
$$
3. Express the Probability of Type II Error (Miss):
$$
P_{M} = P(\hat{H}=H_0 | H_1) = \int_{-\infty}^{\gamma} f(y|H_1) dy
$$
4. Note the relationship to Detection Probability (Power):
$$
P_D = 1 - P_M = \int_{\gamma}^{\infty} f(y|H_1) dy
$$

## Related Concepts
- [[binary_hypothesis_testing]]
- [[receiver_operating_characteristic]]
- [[neyman_pearson_criterion]]