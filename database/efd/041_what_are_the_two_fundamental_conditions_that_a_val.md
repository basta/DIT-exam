---
id: efd_041
course: Estimation, Filtration, and Detection
tags: [instrumental-variables, parameter-estimation, system-identification, consistency]
difficulty: 3
type: open
status: to_learn
---

# Question
What are the two fundamental conditions that a valid Instrumental Variable vector 'z' must satisfy?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 1. Orthogonality (Exogeneity) condition: $E[z_k v_k] = 0$; 2. Rank (Relevance) condition: $E[z_k \phi_k^T]$ must be non-singular (full rank).

## Explanation
In the context of system identification and parameter estimation, the Least Squares (LS) estimator becomes biased and inconsistent if the regressors $\phi_k$ are correlated with the noise $v_k$. This often occurs in closed-loop systems or when there is colored noise (output error models, ARMAX models). To overcome this, the Instrumental Variable (IV) method is introduced.

A valid instrumental variable (or instrument) $z_k$ is a vector that serves as a proxy for the regressors. To ensure that the resulting IV estimator $\hat{\theta}_{IV}$ is consistent (i.e., converges to the true parameter value as the sample size $N \to \infty$), the instruments must satisfy two core properties:

1. **Instrument Exogeneity (Orthogonality):** The instrument must be uncorrelated with the noise term $v_k$. Mathematically, this is expressed as $E[z_k v_k] = 0$. This ensures that the "noise" component of the estimate vanishes in the limit, eliminating the bias found in standard LS.

2. **Instrument Relevance (Non-Singularity):** The instrument must be sufficiently correlated with the original regressors $\phi_k$. Formally, the cross-covariance matrix $R_{z\phi} = E[z_k \phi_k^T]$ must be non-singular (invertible). If the instruments are not correlated with the regressors, the estimation process fails because the "signal" cannot be recovered, leading to extremely high variance or an undefined estimator.

### Steps / Derivation
1. Consider the linear model $y_k = \phi_k^T \theta + v_k$. The IV estimator is defined by solving the normal equations involving the instrument $z_k$:
$$
\hat{\theta}_{IV} = \left( \sum_{k=1}^{N} z_k \phi_k^T \right)^{-1} \sum_{k=1}^{N} z_k y_k
$$
2. Substitute the model equation into the estimator formula to analyze consistency:
$$
\hat{\theta}_{IV} = \theta + \left( \frac{1}{N} \sum_{k=1}^{N} z_k \phi_k^T \right)^{-1} \left( \frac{1}{N} \sum_{k=1}^{N} z_k v_k \right)
$$
3. For $\hat{\theta}_{IV} \xrightarrow{p} \theta$, the term $E[z_k v_k]$ must be 0, and $E[z_k \phi_k^T]$ must be invertible.

## Related Concepts
- [[least_squares_estimation]]
- [[consistency_of_estimators]]
- [[system_identification]]