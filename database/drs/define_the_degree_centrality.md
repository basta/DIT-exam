---
id: drs_026
course: Dynamics and Control of Networks
tags: [centrality-measures, graph-theory, node-importance]
difficulty: 1
type: open
status: to_learn
---

# Question
Define the degree centrality.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Degree centrality is defined as the number of edges incident upon a node. In the context of a network, it represents the simplest measure of a node's importance or influence based purely on its direct connectivity.

## Explanation
Degree centrality is one of the most fundamental concepts in network analysis. It quantifies the importance of a node within a graph by looking at its immediate neighborhood. In an undirected graph, the degree centrality of a node $i$ is simply the count of the number of links (edges) connected to it. In directed graphs, this measure is refined into "in-degree centrality" (the number of incoming links) and "out-degree centrality" (the number of outgoing links), which can represent different dynamics such as popularity versus sociability.

From a structural perspective, a node with high degree centrality is often considered a "hub." In social networks, this might represent a person with many friends; in a communication network, it could represent a router or server that handles a large volume of direct traffic. While degree centrality is computationally efficient and easy to interpret, it has limitations: it only accounts for local connectivity. It does not distinguish between being connected to other highly influential nodes versus being connected to isolated nodes. Therefore, it is often used as a baseline before moving to more complex measures like Eigenvector centrality or Betweenness centrality.

### Steps / Derivation
1. Identify the adjacency matrix $A$ of the network, where $A_{ij} = 1$ if there is an edge between node $i$ and $j$, and $0$ otherwise.
2. Sum the entries of the row (or column) corresponding to node $i$ to find its degree $k_i$.
3. (Optional) Normalize the value by dividing by the maximum possible connections $(N-1)$ to allow for comparison across networks of different sizes.

$$
C_D(i) = k_i = \sum_{j=1}^{N} A_{ij}
$$

## Related Concepts
- [[adjacency_matrix]]
- [[eigenvector_centrality]]
- [[network_hubs]]