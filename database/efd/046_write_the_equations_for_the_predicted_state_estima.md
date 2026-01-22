---
id: efd_046
course: Estimation, Filtration, and Detection
tags: [kalman-filter, state-estimation, stochastic-processes]
difficulty: 2
type: open
status: to_learn
---

# Question
Write the equations for the predicted state estimate and its error covariance ($P_{k|k-1}$) based on the previous estimate.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
The predicted state estimate is $\hat{x}_{k|k-1} = F_k \hat{x}_{k-1|k-1} + B_k u_k$ and the predicted error covariance is $P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q_k$.

## Explanation
In the context of the Discrete-Time Kalman Filter, the estimation process is divided into two distinct phases: **Prediction** (Time Update) and **Correction** (Measurement Update). The equations requested represent the Prediction phase, where the filter projects the current state estimate and uncertainty forward in time to the next time step before a new observation is incorporated.

The state of a linear dynamical system is typically modeled by the stochastic difference equation $x_k = F_k x_{k-1} + B_k u_k + w_{k-1}$, where $F_k$ is the state transition model, $B_k$ is the control-input model, and $w_{k-1}$ is zero-mean Gaussian process noise with covariance $Q_k$. Because the expected value of the noise is zero, the best a priori estimate of the state, denoted as $\hat{x}_{k|k-1}$, is simply the transformation of the previous a posteriori estimate $\hat{x}_{k-1|k-1}$ through the system dynamics.

The error covariance $P_{k|k-1}$ represents the uncertainty in this prediction. It is derived from the expectation of the outer product of the estimation error. When we project the state forward, the uncertainty grows due to two factors: the propagation of existing uncertainty through the transition matrix $F_k$ (represented by $F_k P_{k-1|k-1} F_k^T$) and the addition of new uncertainty from the process noise $Q_k$. Accurately calculating $P_{k|k-1}$ is crucial because it determines the optimal Kalman Gain in the subsequent correction step, effectively deciding how much the filter should "trust" the model versus the new noisy measurement.

### Steps / Derivation
1. **Predicted State Estimate:** Applying the expectation operator $E[\cdot]$ to the state equation, assuming $E[w_{k-1}] = 0$:
$$
\hat{x}_{k|k-1} = F_k \hat{x}_{k-1|k-1} + B_k u_k
$$
2. **Prediction Error:** Define the error as $e_{k|k-1} = x_k - \hat{x}_{k|k-1}$. Substituting the dynamics:
$$
e_{k|k-1} = F_k(x_{k-1} - \hat{x}_{k-1|k-1}) + w_{k-1}
$$
3. **Predicted Covariance:** Calculate $P_{k|k-1} = E[e_{k|k-1} e_{k|k-1}^T]$. Assuming the state error and process noise are uncorrelated:
$$
P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q_k
$$

## Related Concepts
- [[linear_quadratic_estimation]]
- [[state_transition_matrix]]
- [[gaussian_noise_modeling]]