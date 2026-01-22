---
id: efd_086
course: Estimation, Filtration, and Detection
tags: [particle-filters, sequential-monte-carlo, importance-sampling]
difficulty: 4
type: open
status: to_learn
---

# Question
What characterizes the Optimal Proposal Distribution? Which variance does it minimize?

## Options
A) It is the distribution that maximizes the likelihood of the measurements; it minimizes the state error variance.
B) It is defined as $p(x_k | x_{k-1}^i, z_k)$; it minimizes the variance of the true posterior distribution.
C) It is the distribution $p(x_k | x_{k-1}^i, z_k)$; it minimizes the variance of the importance weights conditioned on the previous state and current measurement.
D) It is the transition prior $p(x_k | x_{k-1})$; it minimizes the computational complexity of the resampling step.

---
# Solution
**Correct Answer:** C

## Explanation
In the context of Particle Filtering (Sequential Monte Carlo methods), the choice of the proposal distribution (also known as the importance density), $q(x_k | x_{k-1}^i, z_{k})$, is critical for the efficiency of the filter. The "Optimal Proposal Distribution" is defined as the distribution that minimizes the variance of the importance weights $w_k^i$ conditioned on the state trajectory $x_{k-1}^i$ and the latest measurement $z_k$. 

When we use the transition prior $p(x_k | x_{k-1}^i)$ as the proposal (the Bootstrap Filter approach), we often ignore the most recent information contained in $z_k$. This can lead to "weight degeneracy," where most particles have negligible weights because they are sampled in regions where the likelihood $p(z_k | x_k)$ is very low. By contrast, the optimal distribution incorporates the current observation $z_k$ into the sampling process. 

Mathematically, the optimal distribution is given by the conditional posterior of the state at time $k$ given the previous state and the current observation: $q(x_k | x_{k-1}^i, z_k) = p(x_k | x_{k-1}^i, z_k)$. By utilizing this specific density, the incremental weight becomes independent of the current state $x_k$, which dramatically reduces the variation in particle weights across the ensemble, thereby maintaining a high "effective sample size" and reducing the frequency of required resampling steps.

### Steps / Derivation
1. The importance weight update equation is defined as:
$$
w_k^i \propto w_{k-1}^i \frac{p(z_k | x_k^i) p(x_k^i | x_{k-1}^i)}{q(x_k^i | x_{k-1}^i, z_k)}
$$
2. To minimize the variance of $w_k^i$ (conditioned on $x_{k-1}^i$ and $z_k$), we set the proposal distribution to the conditional state distribution:
$$
q(x_k | x_{k-1}^i, z_k) = p(x_k | x_{k-1}^i, z_k) = \frac{p(z_k | x_k) p(x_k | x_{k-1}^i)}{p(z_k | x_{k-1}^i)}
$$
3. Substituting this back into the weight equation, we find that the terms involving $x_k$ cancel out:
$$
w_k^i \propto w_{k-1}^i p(z_k | x_{k-1}^i) = w_{k-1}^i \int p(z_k | x_k) p(x_k | x_{k-1}^i) dx_k
$$
4. Since the new weight $w_k^i$ no longer depends on the specific sample $x_k^i$ drawn, the conditional variance of the weights is zero.

## Related Concepts
- [[importance_sampling]]
- [[weight_degeneracy]]
- [[sequential_monte_carlo]]