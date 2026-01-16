---
id: drs_060
course: Dynamics and Control of Networks
tags: [centrality-measures, graph-algorithms, betweenness, shortest-paths]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain how to find the betweenness centrality of a given vertex using either the breadth-first search or Dijkstra's algorithm.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The algorithm involves calculating the number of shortest paths between all pairs of nodes that pass through the target vertex, typically using Brandes' Algorithm.

## Explanation
Betweenness centrality quantifies the degree to which a node acts as a bridge or "broker" between other nodes in a network. Formally, for a vertex $v$, it is defined as the sum of the fractions of all-pairs shortest paths that pass through $v$. To compute this efficiently, we utilize the concept of "dependency" of a source node $s$ on a vertex $v$.

The choice between Breadth-First Search (BFS) and Dijkstra’s algorithm depends on whether the network is weighted. For unweighted graphs, BFS is used to find shortest paths in $O(E)$ time. For graphs with positive edge weights, Dijkstra’s algorithm is required, typically running in $O(E + V \log V)$ using a priority queue.

The modern standard for this calculation is Brandes' Algorithm. Instead of explicitly enumerating all shortest paths (which could be exponential), the algorithm works in two phases for each source node $s$:
1. **The Forward Phase**: Perform a BFS/Dijkstra search starting from $s$ to compute the distance $d(s, w)$ to all other nodes $w$ and identify the set of predecessors $P_s(w)$ (nodes that immediately precede $w$ on a shortest path from $s$).
2. **The Backward Phase**: Process nodes in non-increasing order of their distance from $s$. We accumulate "dependencies" $\delta_{s\bullet}(v)$ by summing contributions from children in the shortest-path tree. This recursive accumulation allows us to determine how much of the flow from $s$ passes through $v$ without checking every path individually.

### Steps / Derivation
1. **Initialize Centrality**: For all $v \in V$, set $C_B(v) = 0$.
2. **Iterate per Source**: For each node $s \in V$, perform the following:
   - Initialize a stack $S$, empty predecessor lists $P[w]$, and distances $d(s, w) = \infty$.
   - Execute BFS (unweighted) or Dijkstra (weighted) to find distances and predecessor sets. Use $P[w]$ to store all $u$ such that $d(s, w) = d(s, u) + \text{weight}(u, w)$.
   - During the search, also count the number of shortest paths $\sigma_{sw}$ from $s$ to each $w$.
3. **Accumulate Dependency**: While the stack $S$ is not empty:
   - Pop node $w$. For each predecessor $u \in P[w]$, update the dependency:
$$
\delta_{s\bullet}(u) = \delta_{s\bullet}(u) + \frac{\sigma_{su}}{\sigma_{sw}} (1 + \delta_{s\bullet}(w))
$$
   - If $w \neq s$, add $\delta_{s\bullet}(w)$ to the running total $C_B(w)$.
4. **Result**: The final $C_B(v)$ value represents the betweenness centrality of vertex $v$.

## Related Concepts
- [[brandes_algorithm]]
- [[shortest_path_problem]]
- [[network_topology]]