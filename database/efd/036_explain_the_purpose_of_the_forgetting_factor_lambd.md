---
id: efd_036
course: Estimation, Filtration, and Detection
tags: [recursive-least-squares, rls, adaptive-filtering, parameter-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
Explain the purpose of the "Forgetting Factor" (lambda) in RLS. How does it affect the "memory" of the algorithm?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The forgetting factor $\lambda$ (typically $0 < \lambda \le 1$) is used to give more weight to recent data samples while exponentially de-emphasizing older data. It determines the "effective window length" of the algorithm, allowing it to track time-varying parameters.

## Explanation
In the standard Recursive Least Squares (RLS) algorithm, the objective is to minimize a cost function based on the sum of squared errors. Without a forgetting factor ($\lambda = 1$), the algorithm treats all historical data with equal importance. While this leads to excellent convergence for stationary systems, it renders the algorithm "blind" to changes in the underlying system parameters over time because the ever-growing accumulation of past data overwhelms new incoming information.

The forgetting factor $\lambda$ introduces an exponentially weighted moving average into the cost function:
$$J(n) = \sum_{i=1}^{n} \lambda^{n-i} [d(i) - w^T(n)x(i)]^2$$

When $\lambda < 1$, the influence of a data sample collected at time $i$ decreases geometrically as time $n$ increases. This gives the RLS algorithm "finite memory." A smaller $\lambda$ results in a shorter memory, making the filter more sensitive to recent changes and allowing it to track non-stationary signals or time-varying systems more effectively. However, there is a trade-off: a smaller $\lambda$ (shorter memory) increases the sensitivity to measurement noise, leading to higher steady-state fluctuations (larger excess mean-square error). Conversely, a $\lambda$ close to 1 provides better smoothing and higher accuracy in stationary environments but results in a slow tracking response to parameter drifts.

### Steps / Derivation
1. Define the weighted cost function where $e(i)$ is the error at time $i$:
$$
J(n) = \sum_{i=1}^{n} \lambda^{n-i} e^2(i)
$$
2. Identify the effective memory length (time constant) of the algorithm:
$$
N_{eff} \approx \frac{1}{1 - \lambda}
$$
3. Observe that if $\lambda = 0.99$, the algorithm effectively considers the last 100 samples. If $\lambda = 1$, the memory is infinite.

## Related Concepts
- [[recursive_least_squares]]
- [[adaptive_signal_processing]]
- [[non_stationary_estimation]]