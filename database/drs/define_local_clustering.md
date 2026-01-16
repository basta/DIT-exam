---
id: drs_036
course: Dynamics and Control of Networks
tags: [network-topology, clustering-coefficient, graph-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
Define local clustering.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The local clustering coefficient $C_i$ of a node $i$ is the ratio of the number of actual links between its neighbors to the number of possible links that could exist between them.

## Explanation
Local clustering is an essential metric in network science used to quantify the "cliquishness" of a node's immediate neighborhood. In many real-world networks, such as social networks, if individual A is friends with B, and individual A is also friends with C, there is a high probability that B and C are also friends. This phenomenon is known as triadic closure.

Mathematically, for an undirected graph, let node $i$ have a degree $k_i$. The number of neighbors of node $i$ is $k_i$. The maximum possible number of edges that could exist between these $k_i$ neighbors is given by the binomial coefficient $\binom{k_i}{2}$, which simplifies to $\frac{k_i(k_i - 1)}{2}$. If $L_i$ represents the number of edges that actually exist between these neighbors, the local clustering coefficient $C_i$ is defined as the ratio of actual edges to potential edges.

The value of $C_i$ ranges from 0 to 1. A value of $C_i = 1$ implies that the node's neighborhood is a complete graph (clique), where every neighbor is connected to every other neighbor. A value of $C_i = 0$ implies that none of the node's neighbors are connected to each other, indicating a star-like local topology. In the context of network dynamics, high local clustering often affects the speed and efficiency of information diffusion and the robustness of the network against random failures.

### Steps / Derivation
1. Identify the degree $k_i$ of the node $i$ (number of immediate neighbors).
2. Calculate the number of actual links $L_i$ existing between those $k_i$ neighbors.
3. Divide $L_i$ by the total number of possible links between neighbors.
$$
C_i = \frac{2 L_i}{k_i(k_i - 1)}
$$

## Related Concepts
- [[transitivity]]
- [[small_world_networks]]
- [[triadic_closure]]