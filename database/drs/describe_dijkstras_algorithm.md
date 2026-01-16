---
id: drs_058
course: Dynamics and Control of Networks
tags: [shortest-path, greedy-algorithms, graph-theory]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe Dijkstra's algorithm, explain why it works and analyze its computational complexity.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Descriptive Answer (Open Response)

## Explanation
Dijkstra's algorithm is a fundamental greedy algorithm used to find the shortest path from a single source node to all other nodes in a weighted graph with non-negative edge weights. In the context of Network Dynamics and Control, it serves as the basis for routing protocols (like OSPF) and optimal path planning in static network topologies.

**Why it works:**
The algorithm operates on the principle of **Greedy Choice** and **Optimal Substructure**. It maintains a set of visited nodes whose shortest distance from the source is already known. In each iteration, it selects an unvisited node with the smallest tentative distance, adds it to the visited set, and relaxes its neighbors. 

The mathematical justification for its correctness relies on the non-negativity of edge weights. Because all weights $w(u, v) \geq 0$, once a node $u$ is "closed" (added to the visited set), any other path to $u$ via a currently unvisited node would necessarily have a cost greater than or equal to the current known distance. This ensures that the first time a node is extracted from the priority queue, the path found is indeed the global minimum. If negative weights were allowed, a later path could "reduce" the cost, violating the greedy assumption.

**Computational Complexity:**
The complexity depends on the data structures used:
1.  **Array/List:** $O(V^2)$, where $V$ is the number of vertices. Each of the $V$ nodes is selected once, and for each, we scan the whole list to find the minimum.
2.  **Binary Heap:** $O((V + E) \log V)$, where $E$ is the number of edges. This is efficient for sparse graphs.
3.  **Fibonacci Heap:** $O(E + V \log V)$, which is theoretically the fastest for dense graphs because the "decrease key" operation is $O(1)$ amortized.

### Steps / Derivation
1. **Initialization:** Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. Set the initial node as current.
2. **Visit Neighbors:** For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
3. **Mark Visited:** When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited. A visited node will never be checked again.
4. **Selection:** If the destination node has been marked visited or if the smallest tentative distance among the nodes in the unvisited set is infinity, then stop. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 2.

$$
d(v) = \min(d(v), d(u) + w(u, v))
$$

## Related Concepts
- [[bellman_ford_algorithm]]
- [[greedy_strategies]]
- [[graph_theory_optimization]]