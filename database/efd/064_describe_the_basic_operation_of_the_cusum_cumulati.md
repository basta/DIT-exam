---
id: efd_064
course: Estimation, Filtration, and Detection
tags: [change-point-detection, sequential-analysis, statistical-process-control]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the basic operation of the CUSUM (Cumulative Sum) algorithm. What is it designed to detect?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** CUSUM is a sequential analysis technique designed to detect a persistent shift in the mean of a process (a "change-point").

## Explanation
The Cumulative Sum (CUSUM) algorithm is a powerful tool in statistical signal processing and control theory, primarily used for **change-point detection**. Unlike simple thresholding or moving average filters that look at instantaneous values, CUSUM is designed to be sensitive to small, persistent shifts in the underlying distribution of a sequence of random variables.

The core intuition behind CUSUM is the integration of information over time. If a process is "in control" (operating at its nominal mean), the cumulative sum of the log-likelihood ratios of the observations should follow a random walk with a negative drift or remain near zero. However, once a change occurs (e.g., the mean shifts from $\mu_0$ to $\mu_1$), the cumulative sum begins to grow linearly. 

CUSUM is optimal in the sense of Lorden's criterion: it minimizes the expected delay to detection for a fixed rate of false alarms. It is widely used in industrial process control (to detect machine wear), intrusion detection in networks, and biomedical signal processing (to detect heart rate variability changes). In its "two-sided" form, it can monitor for both increases and decreases in the mean simultaneously by maintaining two separate running statistics.

### Steps / Derivation
1. Define the observations $x_n$ and the hypothesis: $H_0$ (nominal state with parameter $\theta_0$) and $H_1$ (changed state with parameter $\theta_1$).
2. Calculate the instantaneous log-likelihood ratio $s_n$ for each new sample:
$$
s_n = \ln \frac{p(x_n | \theta_1)}{p(x_n | \theta_0)}
$$
3. Update the cumulative test statistic $S_n$. To reset the algorithm when the sum becomes negative (indicating no change has occurred), we use the recursive form:
$$
S_n = \max(0, S_{n-1} + s_n)
$$
4. Compare the statistic $S_n$ to a pre-defined threshold $h$. If $S_n > h$, a change is declared at time $n$.

## Related Concepts
- [[sequential_probability_ratio_test]]
- [[change_point_detection]]
- [[statistical_process_control]]