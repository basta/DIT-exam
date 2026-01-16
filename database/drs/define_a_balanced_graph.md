---
id: drs_024
course: Dynamics and Control of Networks
tags: [graph-theory, consensus-protocols, directed-graphs, balanced-graphs]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a balanced graph.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A directed graph (digraph) is called balanced if, for every node, the in-degree equals the out-degree.

## Explanation
In the study of Network Dynamics and Control, particularly when analyzing the convergence of multi-agent systems and consensus protocols, the structural properties of the communication topology are paramount. A balanced graph (often specifically referred to as a weight-balanced graph in weighted networks) is a directed graph where the inward influence on a node is exactly equal to the outward influence it exerts on its neighbors.

In an unweighted directed graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$, let $d_{in}(v_i)$ denote the in-degree of node $v_i$ (the number of incoming edges) and $d_{out}(v_i)$ denote the out-degree (the number of outgoing edges). The graph is balanced if:
$$d_{in}(v_i) = d_{out}(v_i), \quad \forall v_i \in \mathcal{V}$$

For a weighted graph with adjacency matrix $A = [a_{ij}]$, the graph is weight-balanced if:
$$\sum_{j=1}^{n} a_{ij} = \sum_{j=1}^{n} a_{ji}$$
This condition implies that the Laplacian matrix $L$ of the graph satisfies $1^T L = 0$. In dynamics, this property is critical because it ensures that the average state of the nodes in a consensus system $\dot{x} = -Lx$ is conserved over time. Specifically, if a graph is strongly connected and balanced, the network will reach a consensus value that is the simple average of the initial conditions.

### Steps / Derivation
1. Identify the in-degree of each node $i$:
$$d_{in}(i) = \sum_{j=1}^{n} a_{ij}$$
2. Identify the out-degree of each node $i$:
$$d_{out}(i) = \sum_{j=1}^{n} a_{ji}$$
3. Contrast the results to verify the balanced condition:
$$d_{in}(i) = d_{out}(i)$$

## Related Concepts
- [[consensus_algorithms]]
- [[laplacian_matrix]]
- [[strongly_connected_components]]