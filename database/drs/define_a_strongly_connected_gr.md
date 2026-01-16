---
id: drs_025
course: Dynamics and Control of Networks
tags: [graph-theory, connectivity, directed-graphs]
difficulty: 2
type: open
status: to_learn
---

# Question
Define a strongly connected graph.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A directed graph is strongly connected if, for every pair of vertices $(u, v)$, there exists a directed path from $u$ to $v$ and a directed path from $v$ to $u$.

## Explanation
In the study of Network Dynamics and Control, the connectivity of a graph is a fundamental property that dictates how information, influence, or physical quantities propagate through a system. Connectivity is generally categorized based on whether the graph is undirected or directed. For undirected graphs, we simply speak of "connectedness." However, for directed graphs (digraphs), where edges possess a specific orientation, the definition becomes more nuanced.

A directed graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ consists of a set of vertices $\mathcal{V}$ and a set of ordered pairs $\mathcal{E}$ representing directed edges. We define the graph as being **strongly connected** if it is possible to reach any vertex starting from any other vertex by following the direction of the edges. Formally, this means that for any distinct vertices $i, j \in \mathcal{V}$, there exists a sequence of edges $(i, k_1), (k_1, k_2), \dots, (k_n, j)$ that forms a directed path.

This property is significantly stronger than **weak connectivity**, which only requires that the underlying undirected graph (the graph formed by replacing all directed edges with undirected ones) be connected. In the context of control theory, strong connectivity is often a prerequisite for reaching a consensus in multi-agent systems or for ensuring that a network is irreducible. If a graph is not strongly connected, it can be decomposed into "strongly connected components" (SCCs), which are maximal subgraphs that satisfy the strong connectivity criteria.

### Steps / Derivation
1. **Identify the Graph Type:** Strong connectivity applies specifically to directed graphs (digraphs).
2. **Path Existence:** Verify that for any arbitrary pair of nodes $i$ and $j$, a directed path exists $i \to \dots \to j$.
3. **Mutual Reachability:** Verify the converse, that a directed path exists $j \to \dots \to i$.
$$
\forall i, j \in \mathcal{V}, \exists \text{ path } \mathcal{P}_{i \to j} \text{ and } \mathcal{P}_{j \to i}
$$

## Related Concepts
- [[strongly_connected_components]]
- [[irreducible_matrices]]
- [[consensus_dynamics]]