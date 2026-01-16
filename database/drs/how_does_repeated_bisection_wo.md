---
id: drs_070
course: Dynamics and Control of Networks
tags: [modularity-maximization, spectral-clustering, graph-partitioning, community-detection]
difficulty: 3
type: open
status: to_learn
---

# Question
How does repeated bisection work for modularity maximization? Compare it with the same approach in graph partitioning.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Repeated bisection involves recursively splitting a network into two communities by maximizing the modularity change $\Delta Q$ at each step, stopping when no further increase is possible. Unlike graph partitioning, which uses a fixed number of partitions and seeks to minimize edge cuts, modularity bisection is self-terminating and accounts for the expected number of edges in a null model.

## Explanation
Spectral bisection is a fundamental technique for community detection. In the context of modularity ($Q$), the goal is to divide nodes into two groups such that the density of edges within groups is significantly higher than what would be expected by random chance (the null model).

For a network with adjacency matrix $A_{ij}$, the modularity matrix $B$ is defined as $B_{ij} = A_{ij} - \frac{k_i k_j}{2m}$, where $k_i$ is the degree of node $i$ and $m$ is the total number of edges. The change in modularity resulting from a division into two groups (represented by a vector $s$ where $s_i \in \{+1, -1\}$) is:
$$ \Delta Q = \frac{1}{4m} s^T B s $$
To maximize $\Delta Q$, we find the leading eigenvector of $B$ and assign nodes to groups based on the signs of its components. This process is then repeated on the resulting subgraphs. However, a crucial modification is required: when subdividing a subgraph, the modularity matrix must be adjusted to account for the degrees within the global network, ensuring the contribution to the total modularity is calculated correctly.

### Comparison with Graph Partitioning
While the "repeated bisection" algorithm looks similar to the Kernighan-Lin or spectral bisection methods used in traditional graph partitioning (like Min-Cut), there are two core differences:

1. **Fixed vs. Variable Clusters**: In graph partitioning, the number of clusters $k$ is usually predefined (e.g., bisection into two equal halves). In modularity maximization, the algorithm naturally discovers the number of communities. If the maximum eigenvalue of the modularity matrix for a subgraph is non-positive (or if the best split yields $\Delta Q \leq 0$), the subdivision stops.
2. **The Null Model**: Graph partitioning typically tries to minimize the cut size (number of edges between groups). Modularity maximization subtracts a penalty $\frac{k_i k_j}{2m}$, meaning it rewards "better than random" connections rather than just "few" connections. This makes modularity less sensitive to the total number of nodes and more sensitive to the statistical significance of the link density.

### Steps / Derivation
1. **Construct the Modularity Matrix**: Compute $B_{ij} = A_{ij} - \frac{k_i k_j}{2m}$.
2. **Spectral Decomposition**: Find the eigenvector $u_1$ corresponding to the largest positive eigenvalue of $B$.
3. **Partition nodes**: Assign node $i$ to group 1 if $u_{1,i} > 0$ and group 2 if $u_{1,i} < 0$.
4. **Iterate and Refine**: For each resulting subgraph, construct the generalized modularity matrix $B^{(sub)}_{ij} = B_{ij} - \delta_{ij} \sum_{l \in G} B_{il}$.
5. **Termination**: Stop splitting a community if the largest eigenvalue of the local modularity matrix is $\leq 0$ or if the split does not increase the total modularity.

## Related Concepts
- [[modularity_matrix]]
- [[spectral_clustering]]
- [[community_detection]]
- [[null_models]]