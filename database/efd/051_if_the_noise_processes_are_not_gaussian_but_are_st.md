---
id: efd_051
course: Estimation, Filtration, and Detection
tags: [kalman-filter, non-gaussian-noise, blue, minimum-mean-square-error]
difficulty: 2
type: open
status: to_learn
---

# Question
If the noise processes are NOT Gaussian (but are still white and zero-mean), is the Kalman Filter still the absolute best estimator? If not, what property does it retain (BLUE)?

## Options
A) Yes, it remains the MVUE (Minimum Variance Unbiased Estimator) for all distributions.
B) No, it is no longer the absolute best, but it remains the Best Linear Unbiased Estimator (BLUE).
C) No, it becomes biased and loses all optimality properties.
D) Yes, as long as the noise is white, the distribution type does not affect optimality.

---
# Solution
**Correct Answer:** B) No, it is no longer the absolute best, but it remains the Best Linear Unbiased Estimator (BLUE).

## Explanation
The Kalman Filter is derived based on the first two moments (mean and covariance) of the noise processes. Under the assumption that the process noise $w_k$ and measurement noise $v_k$ are Gaussian, the Kalman Filter is the **Minimum Mean Square Error (MMSE)** estimator. In the Gaussian case, the conditional mean $E[x | z]$ is a linear function of the measurements, meaning no non-linear estimator can perform better.

However, when the noise processes are **non-Gaussian**, the optimal MMSE estimator (the conditional mean) is generally a **nonlinear** function of the observations. In this scenario, the Kalman Filter is no longer the "absolute best" (it is not the MVUE) because a nonlinear filter (such as a Particle Filter or a specific Bayesian filter) could potentially achieve a lower mean square error.

Despite losing its absolute optimality, the Kalman Filter retains a very important property: it remains the **Best Linear Unbiased Estimator (BLUE)**. This means that among the class of all possible **linear** estimators, the Kalman Filter still minimizes the estimation error covariance. It is "best" in the sense of minimizing variance, "linear" because the update is a linear combination of the previous estimate and the innovation, and "unbiased" because the expected value of the error remains zero.

### Steps / Derivation
1. **Define Optimality in Gaussian Case:** 
   If $w_k \sim N(0, Q)$ and $v_k \sim N(0, R)$, then:
   $$ \hat{x}_{k|k} = E[x_k | z_1, \dots, z_k] $$
   This is the absolute minimum variance estimator.

2. **Contrast with Non-Gaussian Case:**
   If the distributions are non-Gaussian, $E[x_k | z_1, \dots, z_k]$ is typically non-linear. The Kalman Filter, which is constrained to a linear structure:
   $$ \hat{x}_{k|k} = L_{k} \hat{x}_{k-1|k-1} + K_k z_k $$
   cannot match the performance of the true conditional mean.

3. **Establish BLUE Property:**
   The Kalman Filter equations only require the mean $E[\cdot]$ and covariance $Var(\cdot)$. By minimizing the cost function $J = E[\|x - \hat{x}\|^2]$ subject to the constraint that $\hat{x}$ is a linear function of $z$, we arrive at the Kalman Gain $K$. Thus, it is the best within the linear class.

## Related Concepts
- [[minimum_mean_square_error]]
- [[best_linear_unbiased_estimator]]
- [[orthogonality_principle]]