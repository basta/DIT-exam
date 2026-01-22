---
id: efd_070
course: Estimation, Filtration, and Detection
tags: [mmae, fault-detection, kalman-filter, bayesian-estimation]
difficulty: 4
type: open
status: to_learn
---

# Question
Describe the Multiple Model (MMAE) approach to Fault Detection and Isolation. How do we determine which model (faulty or healthy) is currently active?

---
# Solution
**Correct Answer:** MMAE uses a parallel bank of Kalman Filters, each representing a specific system hypothesis, and determines the active model by calculating conditional posterior probabilities based on the innovations of each filter.

## Explanation
The Multiple Model Adaptive Estimation (MMAE) approach is a sophisticated framework used in stochastic control and signal processing for simultaneous state estimation and system identification. In the context of Fault Detection and Isolation (FDI), MMAE operates under the assumption that the system's behavior can be characterized by one of a finite set of $K$ candidate models. These models typically include one "healthy" model representing nominal operation and several "faulty" models, each corresponding to a specific failure mode (e.g., sensor bias, actuator stuck, or loss of effectiveness).

The architecture consists of a bank of $K$ filters (usually Kalman Filters) running in parallel. Each filter is matched to one of the hypotheses $H_k$. Every filter processes the same measurement stream $z_k$ and input $u_k$, producing its own state estimate $\hat{x}_k$ and, crucially, its own innovation sequence (residual) $v_k = z_k - H\hat{x}_{k|k-1}$ and innovation covariance $S_k$.

The core mechanism for determining the active model is a recursive Bayesian update. MMAE assigns a weight $p_k(t)$, representing the posterior probability that model $k$ is the true model given the observed data. If a particular model matches the physical reality of the system, its innovations $v_k$ will be near-zero and white (zero-mean Gaussian). Filters that do not match the system state will produce large, biased residuals. By monitoring these residuals, the MMAE algorithm "identifies" the fault by shifting the probability weight toward the filter with the smallest normalized residual.

## Steps / Derivation
1. **Parallel Filtering**: Run $K$ Kalman filters simultaneously. For each model $k$, compute the innovation $v_k(t)$ and its covariance $S_k(t)$.
2. **Likelihood Calculation**: Compute the likelihood of the current measurement $z(t)$ given model $k$ using the Gaussian probability density function:
$$
L_k(t) = \frac{1}{\sqrt{(2\pi)^m |S_k(t)|}} \exp\left(-\frac{1}{2} v_k^T(t) S_k^{-1}(t) v_k(t)\right)
$$
3. **Recursive Probability Update**: Update the posterior probability $p_k(t)$ for each model using Bayes' Rule:
$$
p_k(t) = \frac{L_k(t) p_k(t-1)}{\sum_{j=1}^{K} L_j(t) p_j(t-1)}
$$
4. **Decision Rule (FDI)**: The active model or fault is identified by selecting the index $k$ that maximizes $p_k(t)$, or by comparing $p_k(t)$ against a predefined threshold.

## Related Concepts
- [[kalman_filter_innovations]]
- [[bayesian_model_averaging]]
- [[interactive_multiple_model_imm]]