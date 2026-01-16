---
id: drs_073
course: Dynamics and Control of Networks
tags: [community-detection, agglomerative-clustering, hierarchical-clustering]
difficulty: 3
type: open
status: to_learn

---
# Question
Explain how the agglomerative algorithms proceed in community detection.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Agglomerative algorithms follow a bottom-up hierarchical approach, starting with each node as a singleton community and iteratively merging the most similar pairs until a stopping criterion is met.

## Explanation
Agglomerative algorithms are a class of hierarchical clustering methods used in network science to uncover the meso-scale community structure of a graph. These algorithms are characterized by a "bottom-up" paradigm. Process-wise, the algorithm begins at the finest possible grain of the network: every individual node $i \in V$ is initially assigned to its own unique community.

The core mechanism of the algorithm involves the iterative fusion of communities. At each step, the algorithm evaluates all possible pairs of existing communities and selects the two that are "most similar" or "closest" based on a predefined affinity measure or objective function. A common metric used in this context is **Modularity ($Q$)**, where the pair whose merger results in the greatest increase (or least decrease) in the network's modularity is chosen. Another common metric is the **Linkage** (e.g., single, complete, or average linkage), which measures the topological distance between clusters.

As the algorithm progresses, a hierarchy is formed, which can be visualized as a **dendrogram** (a tree diagram). The leaves represent individual nodes, and the root represents a single community containing the entire network. To determine the "optimal" community structure, the algorithm must identify the horizontal slice of the dendrogram that maximizes a quality index, most frequently the Modularity score. Unlike divisive algorithms (which remove edges), agglomerative methods are generally more computationally efficient, especially when using heuristics like the Louvain Method or the Clauset-Newman-Moore (CNM) algorithm, making them suitable for large-scale network analysis.

### Steps / Derivation
1. **Initialization:** Assign each node $i$ in the network to its own community $C_i$. Calculate the initial similarity matrix or modularity score for the partition.
2. **Iterative Merging:** Identify the two communities $C_a$ and $C_b$ that, when merged, maximize the objective function (e.g., Modularity gain $\Delta Q$).
$$
\Delta Q = \left[ \frac{l_{ab}}{m} - 2\frac{k_a k_b}{(2m)^2} \right]
$$
3. **Update:** Merge $C_a$ and $C_b$ into a single community. Update the network topology representation (treating the new community as a single meta-node) and recalculate the similarities between the new community and all others.
4. **Termination:** Repeat steps 2 and 3 until all nodes are merged into a single community or the modularity $\Delta Q$ can no longer be improved.
5. **Selection:** Analyze the dendrogram or the modularity trace to select the partition that yields the highest quality score.

## Related Concepts
- [[modularity_optimization]]
- [[hierarchical_clustering]]
- [[louvain_method]]