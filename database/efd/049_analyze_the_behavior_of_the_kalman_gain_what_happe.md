---
id: efd_049
course: Estimation, Filtration, and Detection
tags: [kalman-filter, state-estimation, measurement-noise]
difficulty: 2
type: open
status: to_learn
---

# Question
Analyze the behavior of the Kalman Gain: What happens to $K$ if the measurement noise covariance $R$ approaches infinity? What if $R$ approaches zero?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** As $R \to \infty$, $K \to 0$. As $R \to 0$, $K \to H^{-1}$ (or more generally $K$ weights the measurement fully).

## Explanation
The Kalman Gain, $K_k$, acts as a weighting factor that determines how much the filter should trust the new measurement $z_k$ versus the a priori state estimate $\hat{x}_k^-$. This relationship is fundamentally governed by the ratio of the uncertainty in the model (represented by the project error covariance $P_k^-$) and the uncertainty in the sensors (represented by the measurement noise covariance $R$).

**Case 1: $R \to \infty$ (Extremely Noisy Measurements)**
When the measurement noise covariance $R$ becomes very large, it implies that the sensor data is highly unreliable or carries little to no useful information. Mathematically, as $R$ dominates the denominator of the Kalman Gain equation, the gain $K$ drops toward zero. In this scenario, the filter effectively ignores the measurement and relies almost entirely on the internal dynamic model to update the state. The state update equation $\hat{x}_k = \hat{x}_k^- + K(z_k - H\hat{x}_k^-)$ simplifies to $\hat{x}_k \approx \hat{x}_k^-$.

**Case 2: $R \to 0$ (Perfect Measurements)**
Conversely, as $R$ approaches zero, the sensor is perceived as being perfectly accurate. In this limit, the Kalman Gain increases to provide maximum weighting to the "innovation" (the difference between the actual and predicted measurement). If we assume for simplicity that $H$ is square and invertible, $K$ approaches $H^{-1}$. The state update then weights the measurement so heavily that the previous estimate is discarded in favor of the value indicated by the sensor: $\hat{x}_k \approx H^{-1}z_k$. This represents a "deadbeat" update where the filter immediately jumps to the measured state.

### Steps / Derivation
1. Write the discrete-time Kalman Gain formula:
$$
K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}
$$
2. Analyze the limit as $R \to \infty$:
$$
\lim_{R \to \infty} P_k^- H^T (H P_k^- H^T + R)^{-1} = 0
$$
3. Analyze the limit as $R \to 0$:
$$
\lim_{R \to 0} K_k = P_k^- H^T (H P_k^- H^T)^{-1} = P_k^- H^T (H^T)^{-1} (P_k^-)^{-1} H^{-1} = H^{-1}
$$

## Related Concepts
- [[optimal_estimation]]
- [[innovation_sequence]]
- [[sensor_fusion]]