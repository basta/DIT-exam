---
id: drs_031
course: Dynamics and Control of Networks
tags: [centrality-measures, network-topology, distance-metrics]
difficulty: 2
type: open
status: to_learn
---

# Question
Define closeness centrality and discuss different variants thereof.

## Options
A) N/A (Open Question)
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Closeness centrality measures how "close" a node is to all other nodes in a network based on geodesic distances. Standard definition: $C(u) = \frac{n-1}{\sum_{v \neq u} d(u, v)}$.

## Explanation
Closeness centrality is a fundamental measure in network analysis used to identify nodes that can efficiently spread information or influence throughout a graph. It is based on the intuition that a node is central if it has short paths to all other nodes in the network. Formally, for a node $u$ in a graph with $n$ nodes, it is defined as the reciprocal of the average shortest path distance between $u$ and all other reachable nodes $v$.

The primary limitation of the standard definition is its sensitivity to disconnected components. If a node cannot reach another node, the distance $d(u, v)$ is infinite, making the denominator infinite and the centrality zero, regardless of how central the node is within its own component.

To address this and other structural variations, several variants exist:

1. **Harmonic Centrality:** Instead of summing distances and then taking the reciprocal, this variant sums the reciprocals of the distances: $H(u) = \sum_{v \neq u} \frac{1}{d(u, v)}$. This naturally handles infinite distances (as $1/\infty = 0$) and works well for disconnected graphs.
2. **Decay Centrality:** This introduces a decay parameter $\delta \in (0, 1)$, where the influence of a node on another decreases exponentially with distance: $D(u) = \sum_{v \neq u} \delta^{d(u, v)}$.
3. **Information Centrality:** This generalizes closeness by considering all possible paths between nodes, not just the shortest ones, often utilizing the concept of effective resistance in electrical networks or random walks.

## Steps / Derivation
1. **Identify the Geodesic Distance:** Let $d(u, v)$ be the shortest path length between nodes $u$ and $v$.
2. **Sum distances:** Calculate the farness (or total distance) of node $u$: $\sum_{v \in V \setminus \{u\}} d(u, v)$.
3. **Normalize:** Divide the number of other nodes ($n-1$) by the total distance to obtain the average proximity.
$$
C(u) = \frac{n-1}{\sum_{v=1}^{n-1} d(u, v)}
$$

## Related Concepts
- [[betweenness_centrality]]
- [[shortest_path_algorithms]]
- [[graph_efficiency]]