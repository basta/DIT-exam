---
id: drs_061
course: Dynamics and Control of Networks
tags: [max-flow-min-cut, graph-algorithms, network-optimization]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the augmenting path algorithm (Ford-Fulkerson algorithm).

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The Ford-Fulkerson algorithm is a greedy iterative method used to compute the maximum flow in a flow network by repeatedly finding paths from a source to a sink that have available capacity.

## Explanation
The Ford-Fulkerson algorithm is a fundamental method in network science used to solve the Maximum Flow Problem. Given a directed graph $G = (V, E)$ with a capacity function $c(u, v) \geq 0$, a source node $s$, and a sink node $t$, the goal is to maximize the total flow from $s$ to $t$ without exceeding the capacity of any edge and maintaining flow conservation at every node (except $s$ and $t$).

The core intuition behind the algorithm is the concept of the **residual network**, $G_f$. For every edge in the original graph, the residual network tracks both the remaining capacity $(c(u, v) - f(u, v))$ and the "reverse" flow $(f(u, v))$ that can be pushed back to effectively cancel out previous flow assignments. An **augmenting path** is defined as any simple path from $s$ to $t$ in this residual network where all edges have a strictly positive residual capacity.

The algorithm proceeds iteratively: in each step, it searches for an augmenting path. If one is found, it determines the "bottleneck capacity"—the minimum residual capacity along that path—and increases the total flow by that amount while updating the residual capacities. This process continues until no more augmenting paths can be found. According to the **Max-Flow Min-Cut Theorem**, when no augmenting path exists, the current flow is the maximum flow, and its value is equal to the capacity of the minimum cut in the network. The efficiency of the algorithm depends on the method used to find the augmenting path; for instance, using Breadth-First Search (BFS) results in the Edmonds-Karp implementation, which guarantees polynomial time complexity.

### Steps / Derivation
1. **Initialize:** Set the initial flow $f(u, v) = 0$ for all edges $(u, v) \in E$.
2. **Find Path:** Search for an augmenting path $p$ from source $s$ to sink $t$ in the residual graph $G_f$.
3. **Determine Bottleneck:** Calculate the residual capacity $c_f(p) = \min \{c_f(u, v) : (u, v) \in p\}$.
4. **Augment Flow:** For each edge $(u, v)$ in path $p$, update the flow:
$$
f(u, v) \leftarrow f(u, v) + c_f(p) \quad \text{and} \quad f(v, u) \leftarrow f(v, u) - c_f(p)
$$
5. **Repeat:** Return to Step 2. If no augmenting path exists, the current flow is maximal.

## Related Concepts
- [[max_flow_min_cut_theorem]]
- [[residual_capacity_network]]
- [[edmonds_karp_algorithm]]