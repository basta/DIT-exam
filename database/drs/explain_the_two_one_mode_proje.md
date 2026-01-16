---
id: drs_010
course: Dynamics and Control of Networks
tags: [bipartite-graphs, network-topology, one-mode-projection]
difficulty: 2
type: open
status: to_learn
---

# Question
Explain the two one-mode projections of a bipartite network.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The two one-mode projections are the "Top" projection and the "Bottom" projection, where nodes from one set are connected if they share a common neighbor in the opposite set.

## Explanation
A bipartite network (or bigraph) is a specific type of network $G = (U, V, E)$ where the set of nodes is partitioned into two disjoint sets, $U$ and $V$, such that every edge $e \in E$ connects a node in $U$ to a node in $V$. There are no intra-set edges (no $U-U$ or $V-V$ connections). Common examples include authors and scientific papers, or actors and movies.

Because many analytical tools are designed for unipartite (one-mode) graphs, we often perform a "one-mode projection" to simplify the network. This process creates two distinct unipartite graphs:

1.  **The $U$-projection (Top Projection):** In this graph, the nodes consist only of the set $U$. Two nodes $u_i, u_j \in U$ are connected by an edge if and only if they share at least one common neighbor in the set $V$. For example, in an author-paper network, two authors are connected if they have co-authored at least one paper.
2.  **The $V$-projection (Bottom Projection):** Conversely, this graph consists only of the set $V$. Two nodes $v_i, v_j \in V$ are connected if they share a common neighbor in the set $U$. In the same example, two papers are connected if they share at least one common author.

While projections make the network easier to analyze using standard centrality measures or community detection algorithms, they result in a loss of information. Specifically, the exact structure of the original bipartite connections is obscured, often leading to large cliques in the projection that may overstate the density of the relationships.

### Steps / Derivation
1. Define the bipartite adjacency matrix $\mathbf{B}$ of size $n_U \times n_V$, where $B_{iv} = 1$ if node $u_i$ is connected to node $v$, and $0$ otherwise.
2. To find the $U$-projection (nodes in $U$), calculate the product of the adjacency matrix and its transpose:
$$
\mathbf{P^U} = \mathbf{B}\mathbf{B}^T
$$
3. To find the $V$-projection (nodes in $V$), calculate the product of the transpose and the original matrix:
$$
\mathbf{P^V} = \mathbf{B}^T\mathbf{B}
$$
4. In these projection matrices, the diagonal elements $P_{ii}$ represent the degree of node $i$ in the bipartite graph, while off-diagonal elements $P_{ij}$ represent the number of common neighbors shared by nodes $i$ and $j$.

## Related Concepts
- [[adjacency_matrix]]
- [[affiliation_networks]]
- [[incidence_matrix]]