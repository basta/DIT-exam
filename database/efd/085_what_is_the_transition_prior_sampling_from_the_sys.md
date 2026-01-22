---
id: efd_085
course: Estimation, Filtration, and Detection
tags: [particle-filters, sequential-monte-carlo, importance-sampling, proporsal-distribution]
difficulty: 3
type: open
status: to_learn
---

# Question
What is the "Transition Prior" (sampling from the system dynamics) when used as a proposal distribution? Why is it the most common choice, even if not optimal?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The Transition Prior is the distribution $p(x_k | x_{k-1})$, representing the state evolution model. It is common because it simplifies weight updates and is easy to sample from, despite ignoring the current measurement $z_k$.

## Explanation
In the context of Particle Filtering (Sequential Monte Carlo), the goal is to estimate the posterior distribution $p(x_{0:k} | z_{1:k})$. Since we cannot usually sample from this directly, we use Importance Sampling with a proposal distribution (or importance density) $q(x_k | x_{0:k-1}, z_{1:k})$.

The **Transition Prior** refers to choosing the system's own stochastic dynamics as the proposal:
$$q(x_k | x_{0:k-1}, z_{1:k}) = p(x_k | x_{k-1})$$

### Why it is the most common choice:
1. **Mathematical Simplicity:** When the transition prior is used, the importance weight update equation simplifies significantly. The weight update is typically $\frac{\text{target}}{\text{proposal}}$. By substituting the transition prior, the transition terms in the numerator and denominator cancel out, leaving the weight update as simply the likelihood of the current measurement: $w_{k} \propto w_{k-1} \cdot p(z_k | x_k)$.
2. **Ease of Implementation:** In most engineering applications, we already have a generative model for how the system evolves (e.g., $x_k = f(x_{k-1}) + v_k$). Sampling from $p(x_k | x_{k-1})$ is as simple as propagating the previous particles through the state equation and adding process noise. 
3. **No Analytical Requirement:** Unlike the "Optimal Importance Distribution," it does not require integrating over the state space or knowing the functional form of the product of the likelihood and transition density.

### Why it is not optimal:
It is suboptimal because it is "blind" to the current measurement $z_k$. If the measurement is highly accurate (low measurement noise) but the process noise is high, the particles will be spread out according to the dynamics, and many will land in regions where the likelihood $p(z_k | x_k)$ is near zero. This leads to **particle deprivation** and high variance in the weights.

### Steps / Derivation
1. General weight update equation for Importance Sampling:
$$
w_k = \frac{p(z_k|x_k)p(x_k|x_{k-1})}{q(x_k | x_{0:k-1}, z_{1:k})} w_{k-1}
$$
2. Substitute the Transition Prior $q(x_k | \dots) = p(x_k | x_{k-1})$:
$$
w_k = \frac{p(z_k|x_k)p(x_k|x_{k-1})}{p(x_k|x_{k-1})} w_{k-1} = p(z_k | x_k) w_{k-1}
$$

## Related Concepts
- [[importance_sampling]]
- [[particle_filter_degeneracy]]
- [[optimal_importance_density]]