---
id: drs_014
course: Dynamics and Control of Networks
tags: [flow-networks, optimization, graph-theory, cut-sets]
difficulty: 2
type: open
status: to_learn
---

# Question
State the min-cut max-flow theorem.

![[question_image.png]]

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The maximum amount of flow passing from a source node $s$ to a sink node $t$ in a directed network is equal to the minimum capacity that, when removed, disconnects the source from the sink.

## Explanation
The Max-Flow Min-Cut Theorem is a fundamental principle in optimization and network theory. It establishes a deep structural equivalence between two seemingly different problems: maximizing the throughput of a network and finding the bottleneck that limits that throughput. In the context of dynamics and control, this theorem is critical for understanding the robustness of communication networks, supply chains, and power grids.

Formally, consider a flow network $G=(V, E)$ with a capacity function $c: e \to \mathbb{R}^+$ for every edge $e \in E$, a source $s$, and a sink $t$. A **flow** is an assignment of values to edges that satisfies capacity constraints ($0 \leq f(e) \leq c(e)$) and flow conservation (the sum of flow entering a node equals the sum of flow leaving it, except for $s$ and $t$). An **$s-t$ cut** is a partition of the vertices into two sets $S$ and $T$ such that $s \in S$ and $t \in T$. The capacity of the cut is the sum of the capacities of all edges originating in $S$ and terminating in $T$.

The theorem asserts that the maximum value of an $s-t$ flow is exactly equal to the minimum capacity of an $s-t$ cut. This is a specific instance of the strong duality theorem in linear programming. If one views the flow as "traffic" and the cut as "congestion points," the theorem proves that the only way to increase the total flow is to increase the capacity of the specific edges belonging to the minimum cut.

### Steps / Derivation
1. Define the Feasible Flow: Ensure all $f(u,v) \leq c(u,v)$ and conservation $\sum_v f(u,v) - \sum_v f(v,u) = 0$ for $u \neq s, t$.
2. Define the Residual Graph: Construct $G_f$ which represents the available capacity remaining on edges and the potential to "undo" flow.
3. Apply the Ford-Fulkerson Algorithm: Recognize that flow is maximal if and only if there is no augmenting path in the residual graph $G_f$.
$$
\max_{f} |f| = \min_{S,T} \text{cap}(S, T) = \min_{S,T} \sum_{u \in S, v \in T, (u,v) \in E} c(u,v)
$$

## Related Concepts
- [[ford_fulkerson_algorithm]]
- [[linear_programming_duality]]
- [[network_robustness]]