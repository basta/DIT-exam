---
id: efd_082
course: Estimation, Filtration, and Detection
tags: [particle-filters, sequential-monte-carlo, resampling]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the basic Systematic Resampling algorithm. How does it select which particles to keep and which to discard?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Systematic resampling uses a single random number $u \sim \mathcal{U}[0, 1/N]$ to generate $N$ equally spaced points across the cumulative sum of weights, ensuring that particles with weights larger than $1/N$ are selected at least once.

## Explanation
Systematic Resampling is a key step in the Particle Filter (Sequential Monte Carlo) framework, specifically designed to combat the problem of **weight degeneracy**. In a standard particle filter, the variance of the importance weights increases over time, leading to a situation where all but one particle have negligible weights. Resampling addresses this by replicating particles with high weights and discarding those with low weights.

Unlike Multinomial Resampling, which draws $N$ independent samples, Systematic Resampling is more computationally efficient and typically yields lower variance in the particle set. The algorithm operates on the Cumulative Distribution Function (CDF) of the normalized weights $w_k^i$. Instead of picking $N$ independent random numbers, it picks a single starting point $u_1 \sim \mathcal{U}[0, 1/N]$ and then generates a deterministic grid of points $u_j = u_1 + \frac{j-1}{N}$ for $j=1, \dots, N$.

A particle $i$ is selected for the new population if any of the points $\{u_j\}$ fall within the interval defined by its cumulative weight: $[\sum_{m=1}^{i-1} w^m, \sum_{m=1}^{i} w^m)$. Because the distance between the points $u_j$ is exactly $1/N$, any particle with a normalized weight $w^i > 1/N$ is guaranteed to be picked at least once. Particles with very small weights may be skipped entirely if no $u_j$ falls within their respective narrow interval. After selection, all new particles are assigned an equal weight of $1/N$.

### Steps / Derivation
1. Compute the cumulative sum of the normalized weights (CDF):
$$
C_i = \sum_{m=1}^{i} w^m \quad \text{for } i=1, \dots, N
$$
2. Draw a single starting point from a uniform distribution:
$$
u_1 \sim \mathcal{U}\left[0, \frac{1}{N}\right]
$$
3. Generate the sequence of $N$ selection points:
$$
u_j = u_1 + \frac{j-1}{N}, \quad j = 1, \dots, N
$$
4. Iterate through the selection points $u_j$ and find the index $i$ such that:
$$
C_{i-1} < u_j \le C_i
$$
5. Replicate the particle $x^{i}$ as $x^{j}_{new}$ and reset the weight to $1/N$.

## Related Concepts
- [[sequential_importance_sampling]]
- [[weight_degeneracy]]
- [[monte_carlo_methods]]