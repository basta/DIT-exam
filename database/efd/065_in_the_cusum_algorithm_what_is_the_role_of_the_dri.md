---
id: efd_065
course: Estimation, Filtration, and Detection
tags: [sequential-analysis, change-point-detection, hypothesis-testing]
difficulty: 3
type: open
status: to_learn
---

# Question
In the CUSUM (Cumulative Sum) algorithm, what is the role of the drift parameter (often denoted as $\nu$) and the threshold ($h$)?

## Options
A) $\nu$ determines the filter gain and $h$ determines the signal-to-noise ratio.
B) $\nu$ represents the expected log-likelihood ratio under the alternative hypothesis, acts as a "leak" to prevent false alarms, and $h$ determines the sensitivity/delay tradeoff.
C) Both parameters are used to minimize the Mean Square Error of the state estimate.
D) $\nu$ is the measurement noise covariance and $h$ is the process noise covariance.

---
# Solution
**Correct Answer:** B

## Explanation
The CUSUM (Cumulative Sum) algorithm is a sequential analysis technique used for change-point detection. Its primary goal is to identify a change in the probability distribution of a stochastic process as quickly as possible while maintaining a low rate of false alarms.

The **drift parameter** ($\nu$), sometimes called the "offset" or "allowable slack," is conceptually tied to the sensitivity of the detector. In the context of detecting a shift in the mean of a process, $\nu$ is typically chosen as half the magnitude of the shift one intends to detect (i.e., $\nu = \frac{|\mu_1 - \mu_0|}{2}$). Mathematically, it is subtracted from the log-likelihood ratio (or the raw measurements) in each step. This ensures that when the system is in its "normal" state (under hypothesis $H_0$), the cumulative sum has a negative drift and remains clamped at zero due to the $\max(0, \cdot)$ operator. If the drift $\nu$ is set too low, the algorithm becomes overly sensitive to small fluctuations or noise, increasing false alarms. If set too high, the algorithm may fail to detect subtle changes.

The **threshold** ($h$) is the decision boundary. The cumulative sum $S_k$ grows when the observed data supports the alternative hypothesis ($H_1$). A change is declared at time $k$ if $S_k \geq h$. There is an inherent tradeoff managed by $h$: a lower threshold results in a shorter **Average Run Length** (ARL) until detection (lower latency) but significantly increases the probability of false alarms. Conversely, a higher threshold provides robustness against noise but increases the detection delay.

### Steps / Derivation
1. The recursive form of the CUSUM algorithm for detecting an increase in mean is given by:
$$
S_k = \max(0, S_{k-1} + x_k - \mu_0 - \nu)
$$
2. The drift parameter $\nu$ ensures that under the null hypothesis $E[x_k - \mu_0 - \nu] < 0$, keeping the test statistic near zero.
3. The stopping time $\tau$ (the moment a change is detected) is defined as:
$$
\tau = \inf \{ k : S_k \geq h \}
$$

## Related Concepts
- [[sequential_probability_ratio_test]]
- [[change_point_detection]]
- [[average_run_length]]