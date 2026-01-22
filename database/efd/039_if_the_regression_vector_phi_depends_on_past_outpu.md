---
id: efd_039
course: Estimation, Filtration, and Detection
tags: [least-squares, consistency, colored-noise, arx-models]
difficulty: 4
type: open
status: to_learn
---

# Question
If the regression vector phi depends on past outputs (e.g., in an ARX model) and the noise is colored, is the LS estimator consistent? Explain why or why not.

## Options
A) Yes, LS is always consistent for linear models.
B) Yes, provided the noise is zero-mean.
C) No, because the regression vector and the noise term become correlated.
D) No, because colored noise violates the Gauss-Markov theorem.

---
# Solution
**Correct Answer:** C) No, because the regression vector and the noise term become correlated.

## Explanation
In the context of system identification, the Least Squares (LS) estimator $\hat{\theta}_{LS}$ is consistent if it converges in probability to the true parameter vector $\theta_0$ as the number of samples $N \to \infty$. Mathematically, this requires that the term $\frac{1}{N} \sum_{t=1}^{N} \phi(t) e(t)$ converges to zero, where $\phi(t)$ is the regression vector and $e(t)$ is the noise.

When dealing with an ARX (Auto-Regressive with Extra inputs) model, the regression vector $\phi(t)$ contains lagged output values, such as $y(t-1), y(t-2), \dots$. If the noise $e(t)$ is white, it is uncorrelated with past outputs, and the LS estimator remains consistent. However, if the noise is **colored** (i.e., it is auto-correlated, often represented as $e(t) = H(q)v(t)$ where $v(t)$ is white noise), a critical problem arises. 

Because $y(t-1)$ depends on the noise at time $t-1$ (i.e., $e(t-1)$), and because $e(t)$ is correlated with $e(t-1)$ due to its "colored" nature, the regression vector $\phi(t)$ becomes correlated with the current noise $e(t)$. Specifically, $E[\phi(t)e(t)] \neq 0$. In the LS error equation $\hat{\theta}_{LS} = \theta_0 + [\sum \phi \phi^T]^{-1} \sum \phi e$, this non-zero correlation prevents the second term from vanishing even as $N$ approaches infinity. This result is a permanent bias in the estimate, meaning the LS estimator is inconsistent. To rectify this, one would typically use an Instrumental Variable (IV) method or an Extended Least Squares (ELS) approach.

### Steps / Derivation
1. Write the system model in regression form:
$$
y(t) = \phi^T(t)\theta_0 + e(t)
$$
2. Express the LS estimator error:
$$
\hat{\theta}_{LS} - \theta_0 = \left( \frac{1}{N} \sum_{t=1}^N \phi(t)\phi^T(t) \right)^{-1} \left( \frac{1}{N} \sum_{t=1}^N \phi(t)e(t) \right)
$$
3. Analyze the expectation of the cross-product term under colored noise $e(t)$:
$$
E[\phi(t)e(t)] = E \begin{bmatrix} -y(t-1) \\ \vdots \\ u(t-1) \end{bmatrix} e(t) \neq 0
$$
4. Since $y(t-1)$ contains components of $e(t-1)$ and $E[e(t-1)e(t)] \neq 0$ for colored noise, the term does not vanish.

## Related Concepts
- [[instrumental_variables]]
- [[arx_models]]
- [[consistency_of_estimators]]