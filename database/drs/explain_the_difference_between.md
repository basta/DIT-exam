---
id: drs_007
course: Dynamics and Control of Networks
tags: [graph-theory, network-topology, multi-graph, simple-graph]
difficulty: 1
type: open
status: to_learn
---

# Question
Explain the difference between a multi-graph and a simple graph.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A simple graph permits only one edge between any two distinct vertices and no self-loops, whereas a multi-graph allows multiple edges (parallel edges) between the same pair of vertices and potentially self-loops.

## Explanation
In the study of Network Dynamics and Control, the mathematical representation of a network—the graph—determines the constraints of the system's interactions. Both simple graphs and multi-graphs are defined by a set of vertices $V$ and a set of edges $E$. However, they differ significantly in their structural rules:

1. **Simple Graph:** A simple graph is an unweighted, undirected, or directed graph that adheres to two strict conditions. First, it contains no **self-loops**, meaning an edge cannot connect a vertex to itself (i.e., $(v_i, v_i) \notin E$). Second, it contains no **multiple edges**, meaning there is at most one edge between any two distinct vertices $v_i$ and $v_j$. Formally, the number of edges $|E|$ in a simple undirected graph is bounded by $\frac{|V|(|V|-1)}{2}$. Simple graphs are the standard model for social networks where "friendship" is a binary state.

2. **Multi-graph:** A multi-graph (or pseudograph if loops are explicitly included) relaxes these restrictions. It allows for multiple edges between the same pair of nodes, often used to represent different types of interactions or repeated occurrences of an event between two entities. For example, in a transportation network, two cities might be connected by both a highway and a railway line; a multi-graph can represent these as distinct edges $e_1, e_2$ between the same vertices $u$ and $v$. 

From a control perspective, the **Adjacency Matrix** $A$ reflects these differences. In a simple graph, $A_{ij} \in \{0, 1\}$. In a multi-graph, $A_{ij}$ can be any non-negative integer $k$, representing the number of edges between node $i$ and node $j$. This distinction is crucial when calculating the graph Laplacian $L = D - A$, as the multiple edges will increase the degree $D_{ii}$ of the nodes, directly impacting the synchronization and consensus speeds of the network.

### Steps / Derivation
1. Define the Graph $G = (V, E)$.
2. For a simple graph, ensure the mapping from $E$ to the set of pairs $\{\{u,v\} : u,v \in V, u \neq v\}$ is injective.
3. For a multi-graph, allow a multiset of edges where the multiplicity $m(u, v) > 1$.
$$
A_{ij} = \begin{cases} 1 & \text{if } (v_i, v_j) \in E \text{ (Simple)} \\ k & \text{if } k \text{ edges exist between } v_i, v_j \text{ (Multi)} \end{cases}
$$

## Related Concepts
- [[adjacency_matrix]]
- [[graph_laplacian]]
- [[network_topology]]