---
id: drs_006
course: Dynamics and Control of Networks
tags: [hypergraphs, bipartite-networks, higher-order-interactions, network-topology]
difficulty: 2
type: open
status: to_learn
---

# Question
Tell the difference between a graph and a hyper-graph. Depict a given hyper-graph by a bipartite network.

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** A graph represents binary relations (edges connect exactly two nodes), while a hypergraph represents multi-way relations (hyperedges connect any number of nodes). A hypergraph can be depicted as a bipartite network by treating nodes as one set and hyperedges as the second set of vertices, with edges connecting nodes to the hyperedges they belong to.

## Explanation
The fundamental difference between a graph and a hypergraph lies in the cardinality of the relationship between entities. In a standard **Graph $G = (V, E)$**, each edge $e \in E$ is a set of exactly two vertices $\{u, v\}$, where $u, v \in V$. This structure is ideal for modeling pairwise interactions, such as a physical cable between two computers or a friendship between two individuals. 

In contrast, a **Hypergraph $H = (V, E)$** consists of a set of vertices $V$ and a set of hyperedges $E$, where each hyperedge $e \in E$ is a non-empty subset of $V$ of any size. That is, $e \subseteq V$. This allows for the representation of "higher-order" interactions. For example, a research paper (hyperedge) can be authored by five scientists (nodes), or a chemical reaction (hyperedge) can involve three different molecules (nodes). A standard graph would lose the "group" information by breaking these down into individual pairs (cliques), whereas a hypergraph preserves the integrity of the group interaction.

To visualize or analyze a hypergraph using standard graph-theoretic tools, we often use a **Bipartite Representation** (also known as a König representation). A bipartite graph $B = (U, W, E_B)$ consists of two disjoint sets of vertices. To depict a hypergraph $H$:
1. Let the first set of vertices $U$ represent the original nodes of the hypergraph.
2. Let the second set of vertices $W$ represent the hyperedges of the hypergraph.
3. Draw an edge in $B$ between $u \in U$ and $w \in W$ if and only if the node $u$ is contained within the hyperedge $w$ in the original hypergraph $H$.

This transformation is lossless and allows the application of bipartite matching and flow algorithms to solve hypergraph problems.

### Steps / Derivation
1. **Identify Nodes and Hyperedges:** Define the set of nodes $V = \{v_1, v_2, \dots, v_n\}$ and the set of hyperedges $E = \{e_1, e_2, \dots, e_m\}$.
2. **Construct Bipartite Sets:** Create a bipartite graph with two distinct partitions. Partition A contains the original nodes; Partition B contains nodes representing each hyperedge.
3. **Map Connections:** For every $v_i \in e_j$, draw an incident link between node $i$ in Partition A and node $j$ in Partition B.
$$
\text{Incidence Matrix } A_{ij} = 
\begin{cases} 
1 & \text{if } v_i \in e_j \\
0 & \text{otherwise}
\end{cases}
$$

## Related Concepts
- [[higher_order_interactions]]
- [[incidence_matrix]]
- [[bipartite_graph_projection]]