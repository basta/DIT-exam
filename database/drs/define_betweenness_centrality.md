---
id: drs_032
course: Dynamics and Control of Networks
tags: [centrality-measures, network-topology, shortest-paths]
difficulty: 2
type: open
status: to_learn
---

# Question
Define betweenness centrality.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Betweenness centrality is a measure of a node's influence within a network based on the fraction of shortest paths between all pairs of nodes that pass through it.

## Explanation
Betweenness centrality is a fundamental metric in network science used to quantify the "brokerage" or "gatekeeping" role of a node within a graph. Unlike degree centrality, which simply counts the number of direct connections, or closeness centrality, which measures the average distance to all other nodes, betweenness centrality focuses on the flow of information or resources. It captures the extent to which a node lies on the communication paths between other members of the network.

A node with high betweenness centrality acts as a bridge; if such a node were removed, it would significantly disrupt the communication between various clusters or even disconnect the network entirely. This makes it a critical metric for identifying bottlenecks in traffic networks, key influencers in social networks, or vulnerable components in power grids. In the context of dynamics and control, nodes with high betweenness are often the most effective locations for deploying sensors or controllers to observe or influence the global state of the system, as they are naturally positioned to intercept the "signals" propagating through the network topology.

### Steps / Derivation
1. Identify all pairs of nodes $(s, t)$ in a graph $G = (V, E)$.
2. For each pair, calculate the total number of shortest paths $\sigma_{st}$.
3. Determine the number of those shortest paths that pass through node $v$, denoted as $\sigma_{st}(v)$.
4. Compute the ratio of shortest paths through $v$ to the total shortest paths for that pair.
5. Sum these ratios across all pairs of nodes $s$ and $t$ (where $s \neq t \neq v$).

The mathematical definition for the betweenness centrality $C_B(v)$ of a node $v$ is:
$$
C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}
$$
Note: In directed graphs, the order of $s$ and $t$ matters; in undirected graphs, the sum is typically divided by 2 to avoid double-counting. Results are often normalized by dividing by the number of possible pairs $(n-1)(n-2)$.

## Related Concepts
- [[degree_centrality]]
- [[closeness_centrality]]
- [[shortest_path_algorithms]]