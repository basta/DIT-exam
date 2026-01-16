---
id: drs_044
course: Dynamics and Control of Networks
tags: [community-detection, modularity, spectral-analysis, network-topology]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the modularity matrix for undirected networks.

## Options
A) N/A (Open question)
B) 
C) 
D) 

---
# Solution
**Correct Answer:** The modularity matrix $B$ is defined by the elements $B_{ij} = A_{ij} - \frac{k_i k_j}{2m}$.

## Explanation
The modularity matrix $B$ is a fundamental tool in the field of network science, specifically used for community detection. While the adjacency matrix $A$ describes the actual topology of a network, the modularity matrix represents the difference between the observed network and a randomized null model.

The most common null model used is the Configuration Model, which preserves the degree sequence of the original network but assumes edges are placed at random. For an undirected network with $n$ nodes and $m$ edges, the expected number of edges between node $i$ (with degree $k_i$) and node $j$ (with degree $k_j$) is given by $\frac{k_i k_j}{2m}$. The modularity matrix is thus formed by subtracting this expected value from the actual adjacency matrix entry $A_{ij}$.

This matrix is crucial because it allows us to quantify the "modularity" $Q$ of a specific network partition. If a partition places nodes in groups where there are more internal edges than expected by chance, $Q$ will be positive. Mathematically, $Q = \frac{1}{2m} \mathbf{s}^T B \mathbf{s}$ for a two-way division, where $\mathbf{s}$ is a vector representing group membership.

Because the rows and columns of $B$ sum to zero (the null model preserves the total degree), the matrix always has a trivial eigenvalue of 0 associated with a constant eigenvector. The structure of the remaining eigenvalues and eigenvectors, particularly the leading eigenvector, is used in spectral algorithms to find optimal community structures.

### Steps / Derivation
1. Identify the adjacency matrix $A_{ij}$ where $A_{ij}=1$ if an edge exists between nodes $i$ and $j$, and $0$ otherwise.
2. Calculate the degree of each node $k_i = \sum_j A_{ij}$ and the total number of edges $m = \frac{1}{2} \sum_i k_i$.
3. Define the null model term as the probability of an edge existing between $i$ and $j$ in a random graph with the same degree distribution: $P_{ij} = \frac{k_i k_j}{2m}$.
4. Subtract the null model from the adjacency matrix to get the modularity matrix $B$:
$$
B_{ij} = A_{ij} - \frac{k_i k_j}{2m}
$$

## Related Concepts
- [[community_detection]]
- [[configuration_model]]
- [[spectral_clustering]]