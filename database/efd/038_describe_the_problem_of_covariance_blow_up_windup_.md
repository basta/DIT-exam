---
id: efd_038
course: Estimation, Filtration, and Detection
tags: [recursive-least-squares, forgetting-factor, parameter-estimation]
difficulty: 4
type: open
status: to_learn
---

# Question
Describe the problem of "Covariance Blow-up" (Windup) in RLS with a forgetting factor. When does this typically occur?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** Covariance blow-up occurs in Recursive Least Squares (RLS) with a forgetting factor when there is insufficient excitation in the input signal, causing the covariance matrix to grow exponentially and making the estimator hyper-sensitive to noise.

## Explanation
In Recursive Least Squares (RLS) estimation, a **forgetting factor** $\lambda$ (where $0 < \lambda < 1$, typically $0.95 \le \lambda < 1$) is introduced to allow the algorithm to track time-varying parameters. This factor assigns more weight to recent data and exponentially discounts older observations. However, this creates a fundamental trade-off regarding the information content of the incoming signal.

The update rule for the inverse covariance matrix $P(k)$ in RLS is given by:
$$P(k) = \frac{1}{\lambda} \left[ P(k-1) - \frac{P(k-1) \phi(k) \phi^T(k) P(k-1)}{\lambda + \phi^T(k) P(k-1) \phi(k)} \right]$$

**Covariance Blow-up** (or Estimator Windup) occurs when the input signal $\phi(k)$ lacks **Persistent Excitation (PE)**. If the system enters a period of "quiescence" where $\phi(k) \approx 0$ or remains in a direction that does not span the parameter space, the subtractive term in the update equation becomes zero or negligible. Since the entire expression is divided by $\lambda < 1$, the eigenvalues of $P(k)$ grow exponentially. Essentially, the algorithm is "forgetting" old information without receiving new information to replace it.

The consequence is that the estimator becomes extremely sensitive. Even a small amount of measurement noise or a sudden minor change in the input can lead to massive, erratic jumps in the parameter estimates $\hat{\theta}(k)$, as the gain $K(k) = P(k)\phi(k)$ becomes excessively large.

## Steps / Derivation
1. **Identify the Information Matrix update:** The information matrix $P^{-1}(k)$ evolves as $P^{-1}(k) = \lambda P^{-1}(k-1) + \phi(k)\phi^T(k)$.
2. **Observe the Lack of Excitation:** If $\phi(k) = 0$ over a window of time, the equation simplifies to:
$$
P^{-1}(k) = \lambda P^{-1}(k-1) \implies P(k) = \lambda^{-1} P(k-1)
$$
3. **Exponential Growth:** Since $\lambda < 1$, the term $\lambda^{-k}$ grows exponentially.
4. **Conclusion:** After $N$ steps of no excitation, $P(k+N) = \lambda^{-N} P(k)$, leading to numerical instability and loss of robustness.

## Related Concepts
- [[persistent_excitation]]
- [[exponential_forgetting]]
- [[recursive_least_squares]]