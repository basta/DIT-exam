---
id: drs_072
course: Dynamics and Control of Networks
tags: [community-detection, centrality-measures, girvan-newman, edge-betweenness]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the algorithm using betweenness centrality for community detection. How does the Radicci algorithm differ from it?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The Girvan-Newman algorithm uses edge betweenness to iteratively remove bridges between communities, while the Radicci algorithm uses a local metric (clustering coefficient/triangles) to identify and remove edges.

## Explanation
The algorithm using betweenness centrality for community detection is formally known as the **Girvan-Newman algorithm**. Unlike traditional agglomerative clustering methods that build communities from the bottom up, this is a **divisive hierarchical approach**. It is based on the intuition that edges connecting different communities act as "bridges." These bridge edges will have high **edge betweenness centrality**, defined as the number of shortest paths between all pairs of nodes that pass through that specific edge. By iteratively removing the edge with the highest betweenness, the network structure is gradually broken down into disconnected components, which represent the communities.

The **Radicci algorithm** (or the Radicci et al. approach) was proposed as a computationally more efficient alternative to Girvan-Newman. The fundamental difference lies in the **edge metric** used for removal. While Girvan-Newman relies on a global property (shortest paths across the whole network), Radicci uses a **local property** based on the cycle structure, specifically the **edge clustering coefficient**. The logic is that edges within a community tend to belong to many triangles (short cycles), whereas edges connecting communities (bridges) rarely belong to triangles. 

The Radicci algorithm calculates the fraction of possible triangles an edge belongs to. Edges with a low clustering coefficient are considered "inter-community" edges and are targeted for removal. Because calculating local cycles is much faster than computing all-pairs shortest paths, the Radicci algorithm scales significantly better to large networks than the $O(m^2n)$ or $O(mn^2)$ complexity of Girvan-Newman.

### Steps / Derivation
1. **Girvan-Newman Process:**
   - Calculate the edge betweenness for all edges in the current graph.
   - Find the edge with the highest betweenness score.
   - Remove this edge from the graph.
   - Recalculate betweenness for the remaining edges (crucial, as path distributions change).
   - Repeat until no edges remain or a stopping criterion (like maximum Modularity $Q$) is met.

2. **Radicci Algorithm Difference:**
   - Instead of betweenness, calculate the edge clustering coefficient $C_{i,j}^{(g)}$ for an edge $(i,j)$ involving cycles of length $g$:
$$
C_{i,j}^{(g)} = \frac{z_{i,j}^{(g)} + 1}{s_{i,j}^{(g)}}
$$
   - Where $z_{i,j}^{(g)}$ is the number of cycles of length $g$ containing the edge, and $s_{i,j}^{(g)}$ is the maximum possible number of such cycles.
   - Remove the edge with the **lowest** coefficient, as it is least likely to be part of a densely connected local cluster.

## Related Concepts
- [[edge_betweenness_centrality]]
- [[modularity_optimization]]
- [[hierarchical_clustering]]