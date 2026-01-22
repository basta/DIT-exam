---
id: efd_067
course: Estimation, Filtration, and Detection
tags: [change-point-detection, cusum, sequential-analysis, signal-detection]
difficulty: 3
type: open
status: to_learn
---

# Question
Compare the CUSUM (Cumulative Sum) algorithm to a simple geometric moving average or a fixed-window detector. What advantage does CUSUM have regarding small, persistent changes?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** CUSUM acts as an integrator of the log-likelihood ratio, allowing it to accumulate evidence over time, which makes it significantly more sensitive to small, persistent mean shifts compared to memoryless or finite-window detectors.

## Explanation
In the field of statistical signal processing, detecting a change in the underlying distribution of a stochastic process is a fundamental task. A fixed-window detector (or a simple thresholding of raw data) only considers the current or very recent observations. Consequently, if a change is small (i.e., the shift in the mean is significantly smaller than the standard deviation of the noise, $\Delta\mu < \sigma$), the instantaneous signal-to-noise ratio is too low for reliable detection, leading to high false-negative rates.

The Geometric Moving Average (GMA) or Exponentially Weighted Moving Average (EWMA) improves upon this by providing "memory," but it discards older information exponentially. 

The **CUSUM (Cumulative Sum)** algorithm, based on Page’s trend test, is optimal for detecting a change in a parameter at an unknown time. Its primary advantage lies in its ability to **integrate evidence**. By summing the log-likelihood ratios of the observations, CUSUM effectively converts a small persistent shift in the mean into a linear drift in the cumulative sum statistic. While an individual observation might not cross a threshold, the "integration" of many such observations will eventually result in the sum exceeding a threshold. This makes CUSUM the Sequential Probability Ratio Test (SPRT) equivalent for change-point detection, minimizing the expected delay to detection for a fixed false-alarm rate (ARL - Average Run Length).

### Steps / Derivation
1. Define the log-likelihood ratio for an observation $x_i$ given a change from $\theta_0$ to $\theta_1$:
$$
s_i = \ln \frac{p(x_i | \theta_1)}{p(x_i | \theta_0)}
$$
2. The CUSUM recursive statistic $S_k$ is defined to "reset" when the evidence points towards the null hypothesis, effectively searching for the start of the change:
$$
S_k = \max(0, S_{k-1} + s_k)
$$
3. Because $E[s_i | \theta_1] > 0$, the value of $S_k$ will grow linearly after a change occurs, whereas for a fixed-window detector, the signal stays constant at $s_i$.
4. The stopping time $\tau$ is reached when $S_k$ exceeds a threshold $h$:
$$
\tau = \inf \{ k: S_k \ge h \}
$$

## Related Concepts
- [[sequential_probability_ratio_test]]
- [[average_run_length]]
- [[change_point_detection]]