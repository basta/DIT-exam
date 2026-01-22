---
id: efd_024
course: Estimation, Filtration, and Detection
tags: [recursive-bayes, posterior-estimation, stochastic-processes, kalman-filtering]
difficulty: 3
type: open
status: to_learn
---

# Question
Derive or state the recursive form of Bayes' rule. How do we use the posterior from time step k-1 to calculate the posterior at time step k?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The recursive Bayesian estimation consists of two main steps: the Prediction step and the Update step. The posterior at $k-1$, $p(x_{k-1} | z_{1:k-1})$, is propagated through the system dynamics to form a prior for step $k$, which is then updated using the new measurement $z_k$.

## Explanation
Recursive Bayesian estimation is the foundation for optimal filtering in dynamic systems. The goal is to estimate the state $x_k$ of a system at time $k$ given a sequence of noisy measurements $z_{1:k} = \{z_1, z_2, \dots, z_k\}$. To do this recursively, we assume the system follows a Markovian process, where the current state $x_k$ depends only on the previous state $x_{k-1}$, and the measurement $z_k$ depends only on the current state $x_k$.

The process begins with the **Prediction Step**. Here, we take the posterior distribution from the previous time step, $p(x_{k-1} | z_{1:k-1})$, and project it forward in time using the transition probability $p(x_k | x_{k-1})$, which describes the system dynamics. This results in the "prior" or "predictive" density $p(x_k | z_{1:k-1})$. Mathematically, this is an application of the Total Probability Theorem (Chapman-Kolmogorov equation).

The second stage is the **Update Step**. Once a new measurement $z_k$ becomes available, we use Bayes' rule to update our prediction. The predictive density becomes the new prior, and it is multiplied by the likelihood $p(z_k | x_k)$, which describes how likely the measurement is given a specific state. The product is then normalized by the evidence $p(z_k | z_{1:k-1})$ to ensure the resulting posterior $p(x_k | z_{1:k})$ integrates to one. This recursive cycle allows the filter to process data sequentially without needing to store the entire history of measurements.

### Steps / Derivation
1. **Prediction Step (Chapman-Kolmogorov):** Calculate the predictive density $p(x_k | z_{1:k-1})$ using the posterior from $k-1$.
$$
p(x_k | z_{1:k-1}) = \int p(x_k | x_{k-1}) p(x_{k-1} | z_{1:k-1}) dx_{k-1}
$$
2. **Update Step (Bayes' Rule):** Incorporate the new measurement $z_k$ to obtain the new posterior.
$$
p(x_k | z_{1:k}) = \frac{p(z_k | x_k) p(x_k | z_{1:k-1})}{p(z_k | z_{1:k-1})}
$$
3. **Normalization Constant:** The denominator is calculated by marginalizing the numerator over $x_k$.
$$
p(z_k | z_{1:k-1}) = \int p(z_k | x_k) p(x_k | z_{1:k-1}) dx_k
$$

## Related Concepts
- [[chapman_kolmogorov_equation]]
- [[hidden_markov_models]]
- [[kalman_filter_derivation]]