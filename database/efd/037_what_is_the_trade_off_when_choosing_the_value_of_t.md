---
id: efd_037
course: Estimation, Filtration, and Detection
tags: [recursive-least-squares, parameter-estimation, adaptive-filtering]
difficulty: 3
type: open
status: to_learn
---

# Question
What is the trade-off when choosing the value of the forgetting factor lambda (e.g., lambda = 0.99 vs lambda = 0.90)?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The trade-off is between tracking capability (adaptability) and estimation precision (noise sensitivity).

## Explanation
The forgetting factor $\lambda$ (typically $0 < \lambda \leq 1$) is a hyperparameter used in Recursive Least Squares (RLS) and other adaptive filtering algorithms to weigh recent data more heavily than past observations. This is crucial when the system being modeled is non-stationary, meaning its internal parameters change over time.

Choosing a larger value, such as $\lambda = 0.99$, assigns a long "memory" to the algorithm. This results in higher estimation precision because the estimate is averaged over a larger window of data points, effectively filtering out more measurement noise. However, this comes at the cost of sluggishness; the filter will be slow to react if the true system parameters undergo a sudden change (a step change).

Conversely, choosing a smaller value, such as $\lambda = 0.90$, results in a shorter memory. This enhances the algorithm's tracking capability, allowing it to adapt rapidly to time-varying dynamics. The downside is increased sensitivity to noise (increased variance of the estimate). Because the algorithm relies on fewer data points to form its estimate, random fluctuations in the signal are more likely to be misinterpreted as parameter changes, leading to "noisy" or "jittery" estimates.

In summary, $\lambda$ defines the effective window size $N_{eff} \approx \frac{1}{1-\lambda}$. A $\lambda$ closer to 1 provides stability and noise rejection (good for stationary systems), while a smaller $\lambda$ provides agility and fast convergence (good for highly dynamic systems).

### Steps / Derivation
1. Define the exponentially weighted cost function to be minimized:
$$
J(n) = \sum_{i=1}^{n} \lambda^{n-i} [y(i) - \mathbf{x}^T(i)\hat{\boldsymbol{\theta}}(n)]^2
$$
2. Identify the effective memory depth $N_{eff}$ which represents the number of samples that significantly contribute to the current estimate:
$$
N_{eff} = \frac{1}{1-\lambda}
$$
3. Compare $\lambda = 0.99$ ($N_{eff} \approx 100$ samples) vs $\lambda = 0.90$ ($N_{eff} \approx 10$ samples).
4. Conclude that the choice is a compromise between the bias introduced by slow tracking and the variance introduced by measurement noise.

## Related Concepts
- [[recursive_least_squares]]
- [[non_stationary_processes]]
- [[bias_variance_tradeoff]]