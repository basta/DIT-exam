---
id: drs_027
course: Dynamics and Control of Networks
tags: [centrality-measures, spectral-analysis, node-importance]
difficulty: 3
type: open
status: to_learn
---

# Question
Motivate the eigenvector centrality.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Eigenvector centrality motivates the idea that a node's importance is determined not just by how many connections it has, but by the importance of the neighbors it is connected to.

## Explanation
Eigenvector centrality is an extension of degree centrality that addresses a fundamental limitation: in degree centrality, all neighbors contribute equally to a node's score. However, in many real-world networks (like citation networks or the World Wide Web), a connection to a highly influential node should arguably confer more status than a connection to an isolated or unimportant node. 

The core motivation is circular and recursive: a node is important if it is linked to by other important nodes. This creates a self-consistent scoring system. If we denote $x_i$ as the centrality of node $i$, we want $x_i$ to be proportional to the sum of the centralities of its neighbors. This leads to the mathematical formulation using the adjacency matrix $A$, where $A_{ij} = 1$ if there is an edge between $i$ and $j$, and $0$ otherwise. By requiring $x_i = \frac{1}{\lambda} \sum_{j} A_{ij} x_j$, we effectively transform a qualitative idea of "prestige" into a linear algebra problem.

This measure is particularly effective at identifying "influencers" within a network cluster. Unlike PageRank, which scales down influence by the out-degree of the source node, eigenvector centrality allows a single powerful node to pass its full "status" to all its neighbors, assuming the eigenvalue $\lambda$ is properly chosen (usually the spectral radius).

### Steps / Derivation
1. Assign a centrality score $x_i$ to each node $i$. Define $x_i$ such that it is proportional to the sum of the scores of its neighbors:
$$
x_i = \kappa^{-1} \sum_{j=1}^n A_{ij} x_j
$$
2. Rewrite the set of equations for all nodes in matrix-vector form:
$$
\mathbf{Ax} = \lambda \mathbf{x}
$$
3. By the Perron-Frobenius Theorem, for a connected graph (or more generally, an irreducible matrix), there exists a unique largest positive eigenvalue $\lambda_1$ with a corresponding eigenvector $\mathbf{x}$ having all positive components. This eigenvector $\mathbf{x}$ provides the centrality scores.

## Related Concepts
- [[degree_centrality]]
- [[perron_frobenius_theorem]]
- [[spectral_radius]]