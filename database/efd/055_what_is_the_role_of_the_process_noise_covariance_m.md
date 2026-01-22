---
id: efd_055
course: Estimation, Filtration, and Detection
tags: [kalman-filter, stochastic-processes, state-estimation]
difficulty: 3
type: open
status: to_learn
---

# Question
What is the role of the process noise covariance matrix Q? How does increasing the values in Q affect the filter's "bandwidth" or responsiveness to changes?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The matrix $Q$ represents the uncertainty in the system's physical model. Increasing $Q$ makes the filter more responsive (higher bandwidth) by trusting new measurements more than the internal model.

## Explanation
The process noise covariance matrix, denoted as $Q$, represents the uncertainty or "randomness" in the evolution of the state vector. In a discrete-time Kalman Filter, the state transition is modeled as $x_k = F x_{k-1} + B u_{k-1} + w_{k-1}$, where $w_k \sim \mathcal{N}(0, Q)$. The role of $Q$ is to account for unmodeled dynamics, disturbances, or inaccuracies in the state transition matrix $F$. 

In the context of the Kalman Gain, $K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}$, the matrix $Q$ directly influences the "prior" error covariance $P_k^- = F P_{k-1} F^T + Q$. 

When you increase the values in $Q$, you are effectively telling the filter that the physical model is unreliable or that the system is subject to high-frequency erratic movements. This leads to a larger $P_k^-$, which in turn increases the Kalman Gain $K$. A larger Gain means the filter places more weight on the innovation (the difference between the actual measurement and the predicted measurement) and less weight on the model's prediction. 

In signal processing terms, this increases the "bandwidth" of the filter. A high-bandwidth filter reacts quickly to changes in the signal (low lag) but is also more susceptible to passing through high-frequency measurement noise. Conversely, a small $Q$ results in a heavily smoothed output that ignores sudden changes, viewing them as noise rather than true state transitions.

### Steps / Derivation
1. Define the relationship between $Q$ and the predicted covariance:
$$
P_k^- = F P_{k-1} F^T + Q
$$
2. Observe that the Kalman Gain $K_k$ is proportional to $P_k^-$:
$$
K_k \propto P_k^- (H P_k^- H^T + R)^{-1}
$$
3. Analyze the weight of the measurement $z_k$ in the state update:
$$
\hat{x}_k = \hat{x}_k^- + K_k (z_k - H \hat{x}_k^-)
$$
4. Conclude that $Q \uparrow \implies P_k^- \uparrow \implies K_k \uparrow$, which increases responsiveness to $z_k$.

## Related Concepts
- [[kalman_gain]]
- [[measurement_noise_covariance]]
- [[state_space_modeling]]