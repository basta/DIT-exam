---
id: drs_075
course: Dynamics and Control of Networks
tags: [community-detection, modularity, k-means, hierarchical-clustering]
difficulty: 2
type: open
status: to_learn

---
# Question
Comment on which of the algorithms detect a fixed number vs. an unspecified number of communities.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Community detection algorithms vary in their requirement for the parameter $k$ (the number of clusters). Algorithms like $k$-means and Spectral Clustering typically require a pre-specified number of communities, while algorithms based on Modularity Optimization (e.g., Louvain, Girvan-Newman) or Hierarchical Clustering determine the number of communities endogenously.

## Explanation
In the study of network dynamics and topology, community detection is the process of partitioning nodes into sets that are more densely connected internally than externally. A fundamental distinction between these algorithms is whether the user must provide the number of communities ($k$) as an input parameter or if the algorithm discovers the "natural" number of communities based on the network's structural properties.

**Fixed Number of Communities:**
Centroid-based algorithms, such as **k-means**, require the number of clusters to be defined beforehand. In the context of networks, **Spectral Clustering** is a prominent example. While spectral methods provide powerful insights into the graph Laplacian, the standard approach involves selecting the $k$ smallest non-zero eigenvalues and their corresponding eigenvectors to project nodes into a $k$-dimensional space, implying that the number of communities is a fixed constraint of the model.

**Unspecified Number of Communities:**
Many network-specific algorithms aim to find the globally optimal partition without prior knowledge of $k$. **Modularity Optimization** is the most common technique here. The modularity score $Q$ measures the density of edges inside communities compared to edges in a null model (random graph). Algorithms like the **Louvain Method** or **Leiden Algorithm** greedily move nodes to maximize $Q$, naturally stopping when no further increase is possible, thus identifying an unspecified number of communities. Similarly, **Divisive Hierarchical Clustering** (like Girvan-Newman) removes edges based on edge-betweenness; one can observe the entire dendrogram and use metrics like the maximum modularity to "cut" the tree, effectively letting the data dictate the optimal number of communities.

### Steps / Derivation
1. **Identify the Objective Function:** Determine if the algorithm optimizes a global quality metric (like Modularity $Q$) or minimizes a distance-to-centroid metric.
2. **Evaluate Input Parameters:** Check if the algorithm requires $k$ as a hyperparameter.
3. **Analyze Stopping Criteria:**
   - If the algorithm stops only when a specific partition size is reached: **Fixed.**
   - If the algorithm stops when an optimization metric is maximized: **Unspecified.**
$$
Q = \frac{1}{2m} \sum_{ij} \left( A_{ij} - \frac{k_i k_j}{2m} \right) \delta(c_i, c_j)
$$

## Related Concepts
- [[modularity_optimization]]
- [[spectral_clustering]]
- [[graph_partitioning]]