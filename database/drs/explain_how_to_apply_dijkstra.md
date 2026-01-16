---
id: drs_059
course: Dynamics and Control of Networks
tags: [path-finding, shortest-path-tree, greedy-algorithms, graph-theory]
difficulty: 3
type: open
status: to_learn

---
# Question
Explain how to apply Dijkstra's algorithm to find the actual least weight path tree for a given starting vertex.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Shortest Path Tree (SPT) construction via greedy distance minimization and predecessor tracking.

## Explanation
Dijkstra’s algorithm is a greedy search heuristic used to solve the single-source shortest path problem for a graph with non-negative edge weights $w(u, v) \geq 0$. To find the actual least weight path tree (rather than just the scalar distances), the algorithm maintains two primary values for every node $v \in V$: the tentative distance $d(v)$ and the predecessor $p(v)$.

The algorithm operates by partitioning nodes into two sets: those whose shortest path from the source $s$ is already known (the "settled" set $S$) and those still being evaluated (the "unsettled" set $Q$). Initially, $d(s) = 0$ and $d(v) = \infty$ for all other nodes. In each iteration, the algorithm selects the node $u \in Q$ with the minimum $d(u)$. This selection is the "greedy" step. Once $u$ is selected, it is moved to $S$, and all its neighbors $v$ are "relaxed."

Relaxation is the process of checking if passing through $u$ offers a shorter path to $v$ than currently known. Specifically, if $d(u) + w(u, v) < d(v)$, we update $d(v)$ and set $p(v) = u$. By the time all nodes reachable from $s$ are processed, the set of edges $\{(p(v), v) \mid v \in V \setminus \{s\}\}$ defines the Shortest Path Tree (SPT). This tree is a subgraph that contains a path from the source to every other node such that the sum of weights along that path is minimized.

### Steps / Derivation
1. **Initialization:** Assign $d(s) = 0$ and $d(v) = \infty$ for all $v \neq s$. Initialize an empty predecessor map $p(v) = \text{null}$ and a priority queue $Q$ containing all vertices.
2. **Node Selection:** While $Q$ is not empty:
   - Extract the vertex $u$ with the minimum $d(u)$ from $Q$.
   - Add $u$ to the set of settled nodes $S$.
3. **Edge Relaxation:** For each neighbor $v$ of $u$ still in $Q$:
   - Calculate the tentative distance: $dist\_temp = d(u) + w(u, v)$.
   - If $dist\_temp < d(v)$:
     - Update $d(v) \leftarrow dist\_temp$.
     - Update the predecessor: $p(v) \leftarrow u$.
4. **Tree Reconstruction:** After the loop finishes, the Shortest Path Tree is formed by the edges linking each node $v$ to its predecessor $p(v)$.

$$
d(v) = \min(d(v), d(u) + w(u, v))
$$

## Related Concepts
- [[bellman_ford_algorithm]]
- [[greedy_heuristics]]
- [[spanning_trees]]