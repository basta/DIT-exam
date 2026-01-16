---
id: drs_071
course: Dynamics and Control of Networks
tags: [modularity-maximization, community-detection, optimization-algorithms]
difficulty: 3
type: open
status: to_learn
---

# Question
Briefly describe simulated annealing, genetic algorithm and greedy algorithm for modularity maximization.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Short description of the three heuristic optimization methods applied to the modularity $Q$ function.

## Explanation
Modularity maximization is a NP-hard problem used to detect community structures in networks by maximizing the objective function $Q$, which measures the density of edges inside communities compared to edges between communities. Because the search space of possible partitions is exhaustive, heuristic approaches are required.

1. **Greedy Algorithm (e.g., Clauset-Newman-Moore):** This is a bottom-up agglomerative approach. It starts with each node in its own community. At each step, the algorithm merges the two communities that result in the largest increase (or smallest decrease) in modularity $\Delta Q$. This process continues until no further merges can improve $Q$. While computationally efficient ($O(md \log n)$), it is prone to getting stuck in local optima and may suffer from a "resolution limit."

2. **Simulated Annealing (SA):** Inspired by metallurgy, SA is a stochastic global optimization technique. It explores the landscape of partitions by performing random node moves or community merges. A move that increases $Q$ is always accepted, while a move that decreases $Q$ is accepted with a probability $P = e^{\Delta Q / T}$, where $T$ is a "temperature" parameter that decreases over time. This allows the algorithm to escape local maxima early in the process, often leading to higher accuracy than greedy methods at the cost of significantly higher computational time.

3. **Genetic Algorithm (GA):** This is an evolutionary approach where a population of candidate partitions (chromosomes) undergoes selection, crossover, and mutation. The fitness function is the modularity $Q$. Through successive generations, the best partitions are combined to "breed" superior solutions. GA is effective at exploring diverse areas of the solution space simultaneously, though tuning parameters like mutation rate and population size is critical for performance.

### Steps / Derivation
1. **Define Objective Function:**
$$
Q = \frac{1}{2m} \sum_{i,j} \left( A_{ij} - \frac{k_i k_j}{2m} \right) \delta(c_i, c_j)
$$
2. **Greedy Step:** Find $\max(\Delta Q)$ for all possible merges of communities $i$ and $j$.
3. **SA Step:** Generate random partition $C'$, accept if $Q(C') > Q(C)$ or with probability $e^{\frac{Q(C') - Q(C)}{T}}$.
4. **GA Step:** Perform selection on population $P_t$ based on $Q$, apply crossover to create $P_{t+1}$.

## Related Concepts
- [[modularity_q]]
- [[community_detection]]
- [[heuristic_optimization]]