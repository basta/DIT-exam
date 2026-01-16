---
id: drs_054
course: Dynamics and Control of Networks
tags: [graph-theory, traversal-algorithms, network-topology]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe the breadth-first search algorithm.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Breadth-First Search (BFS) is a fundamental graph traversal algorithm that explores a network layer by layer, starting from a source node and visiting all immediate neighbors before moving to nodes at the next distance level.

## Explanation
Breadth-First Search (BFS) is a systematic strategy for searching a graph $G = (V, E)$ or traversing the nodes of a network. The algorithm is characterized by its "level-order" approach: it starts at an arbitrary root node $s$ and explores all neighboring nodes at the current depth (distance $d$) before moving on to the nodes at the next depth level ($d+1$).

In the context of network dynamics, BFS is crucial for identifying the shortest path in unweighted graphs, as it guarantees that the first time a node is reached, it is via the minimum number of edges from the source. This property makes it essential for calculating the diameter of a network, average path lengths, and identifying connected components. 

The algorithm maintains three states for nodes: undiscovered, discovered (frontier), and processed. To manage the order of discovery, BFS utilizes a First-In-First-Out (FIFO) queue data structure. When a node is dequeued and processed, all of its undiscovered neighbors are added to the queue. This ensures that the exploration expands uniformly outward like a wave front. If the graph is represented by an adjacency matrix $A$, the state transition of BFS effectively explores the structural connectivity defined by the non-zero entries of the matrix.

### Steps / Derivation
1. **Initialization:** Assign a distance of $\infty$ to all nodes and $0$ to the source node $s$. Mark $s$ as "visited" and enqueue it into a FIFO queue $Q$.
2. **Exploration Loop:** While $Q$ is not empty, dequeue the head node $u$.
3. **Neighbor Inspection:** For each neighbor $v$ of node $u$, if $v$ has not been visited:
    - Mark $v$ as visited.
    - Set distance $d(v) = d(u) + 1$.
    - Enqueue $v$ into $Q$.
4. **Termination:** Once $Q$ is empty, all reachable nodes from $s$ have been processed, and their shortest paths in terms of hop-count are determined.

$$
L_k = \{v \in V \mid \text{dist}(s, v) = k\}
$$

## Related Concepts
- [[shortest_path_distance]]
- [[graph_traversal]]
- [[connected_components]]