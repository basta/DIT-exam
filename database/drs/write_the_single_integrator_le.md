---
id: drs_089
course: Dynamics and Control of Networks
tags: [consensus-protocol, algebraic-graph-theory, leader-follower-dynamics]
difficulty: 2
type: open
status: to_learn
---

# Question
Write the single-integrator leaderless consensus dynamics in continuous time. How to include a leader?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The leaderless dynamics are $\dot{x}_i(t) = \sum_{j \in \mathcal{N}_i} a_{ij} (x_j(t) - x_i(t))$. A leader is included by making one node's state independent of its neighbors (static leader) or by adding a pinning control term to a subset of nodes.

## Explanation
In network dynamics, the **leaderless consensus protocol** describes a distributed control law where agents reach a common state purely through local interactions. For a network of $n$ agents with states $x_i \in \mathbb{R}$, the single-integrator dynamics rely on the relative state information between an agent and its neighbors. If the graph is undirected and connected, the system will converge to the average of the initial conditions: $\frac{1}{n}\sum x_i(0)$. In matrix form, this is expressed using the Graph Laplacian $L$, where $\dot{x} = -Lx$.

To include a **leader**, the topology or the control law must be modified to break the symmetry of the network. There are two primary ways to implement this:

1.  **Stationary/Independent Leader:** One specific node (the leader, $x_L$) does not update its state based on its neighbors (i.e., $\dot{x}_L = 0$). Because the other "follower" nodes are still running the consensus protocol and the leader is part of the graph, the followers will eventually be "pulled" toward the leader's constant state.
2.  **Pinning Control:** A subset of nodes is "pinned" to a leader. The dynamics become $\dot{x}_i = \sum_{j \in \mathcal{N}_i} a_{ij} (x_j - x_i) + b_i(x_L - x_i)$, where $b_i > 0$ if node $i$ can see the leader, and $b_i = 0$ otherwise. In this scenario, the leader can be dynamic ($\dot{x}_L = f(x_L, t)$), and if the graph containing the leader as a root is sufficiently connected (e.g., contains a spanning tree), all followers will track the leader.

### Steps / Derivation
1. **Leaderless Formulation:** Define the state update for node $i$ based on the adjacency weights $a_{ij}$:
$$
\dot{x}_i(t) = \sum_{j=1}^{n} a_{ij} (x_j(t) - x_i(t))
$$
2. **Matrix Representation:** Collect all states into a vector $x = [x_1, \dots, x_n]^T$ and use the Laplacian matrix $L = D - A$:
$$
\dot{x} = -Lx
$$
3. **Leader-Follower Implementation:** Introduce a leader state $x_L$. For followers $i \in \{1, \dots, n\}$, add a pinning gain $b_i$:
$$
\dot{x}_i = \sum_{j=1}^{n} a_{ij} (x_j - x_i) + b_i(x_L - x_i)
$$

## Related Concepts
- [[graph_laplacian]]
- [[average_consensus]]
- [[pinning_control]]