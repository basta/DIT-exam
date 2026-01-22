---
id: efd_066
course: Estimation, Filtration, and Detection
tags: [sequential-analysis, change-point-detection, hypothesis-testing]
difficulty: 3
type: open
status: to_learn
---

# Question
How does the CUSUM stopping rule function? When is an alarm triggered?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The CUSUM (Cumulative Sum) stopping rule functions by accumulating the log-likelihood ratio of incoming observations and resetting to zero whenever the sum becomes negative. An alarm is triggered at the first time step $n$ where this accumulated value exceeds a predefined positive threshold $h$.

## Explanation
The CUSUM (Cumulative Sum) algorithm is a sequential analysis technique developed by E.S. Page for change-point detection. Its primary goal is to detect a transition in the underlying distribution of a stochastic process (from a "nominal" state $P_0$ to an "anomalous" state $P_1$) as quickly as possible while maintaining a low rate of false alarms.

The rule functions by maintaining a running statistic $S_n$. This statistic is based on the log-likelihood ratio (LLR) of the observations. Under normal conditions (the null hypothesis $H_0$), the expected value of the LLR is negative, meaning the cumulative sum tends to drift downward. However, when a change occurs (the alternative hypothesis $H_1$), the expected value of the LLR becomes positive, causing the sum to drift upward. 

To prevent the algorithm from drifting too far negative (which would delay the detection of a change), CUSUM employs a "reset" mechanism. The statistic is defined as $S_n = \max(0, S_{n-1} + z_n)$, where $z_n$ is the log-likelihood ratio of the current observation. This effectively restarts the integration of evidence every time the evidence suggests no change has occurred. An alarm is triggered at the stopping time $T = \inf \{n : S_n \ge h\}$, where $h$ is a threshold chosen based on the desired mean time between false alarms (MTBFA) and the required sensitivity.

### Steps / Derivation
1. Define the log-likelihood ratio $z_i$ for an observation $x_i$ given the pre-change density $f_0$ and post-change density $f_1$:
$$
z_i = \ln \frac{f_1(x_i)}{f_0(x_i)}
$$
2. Initialize the CUSUM statistic at $S_0 = 0$.
3. Update the cumulative sum recursively at each time step $n$, ensuring the value never drops below zero:
$$
S_n = \max(0, S_{n-1} + z_n)
$$
4. Define the stopping rule (alarm trigger) based on a positive threshold $h$:
$$
T_{CUSUM} = \min \{ n \geq 1 : S_n \geq h \}
$$

## Related Concepts
- [[sequential_probability_ratio_test]]
- [[change_point_detection]]
- [[likelihood_ratio_test]]