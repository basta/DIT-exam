---
id: drs_045
course: Dynamics and Control of Networks
tags: [assortativity, network-topology, degree-correlation, mixing-patterns]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain assortative mixing with respect to the degree. Discuss what are its implications on the network topology.

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** Assortative mixing (by degree) is the tendency for nodes in a network to connect to other nodes with similar degrees. This leads to the formation of dense ornamental cores and affects network robustness and epidemic spreading.

## Explanation
Assortative mixing, specifically degree assortativity, refers to a preference for a network's nodes to attach to others that are "like" them in terms of their connectivity. In a degree-assortative network, high-degree nodes (hubs) tend to be connected to other high-degree nodes, while low-degree nodes tend to connect to other low-degree nodes. This is statistically quantified using the Pearson correlation coefficient ($r$) of the degrees at either ends of an edge.

When $r > 0$, the network is **assortative**, which is commonly observed in social networks (e.g., popular people tend to know other popular people). When $r < 0$, the network is **disassortative**, meaning hubs tend to connect to low-degree nodes, a pattern often seen in biological and technological networks like the Internet or protein interaction webs. When $r = 0$, the network is neutral.

### Implications on Network Topology:
1. **Core-Periphery Structure:** Assortative networks naturally develop a "dense core" of interconnected hubs. This core acts as a high-capacity backbone for the network.
2. **Robustness:** Assortative networks are generally more robust to the random removal of nodes because the core remains connected even if peripheral nodes are lost. however, they can be more vulnerable to targeted attacks if the core is breached.
3. **Epidemic Dynamics:** In assortative networks, diseases or information spread very quickly among the high-degree core (low epidemic threshold). However, because the hubs are primarily connected to each other, the spread to the rest of the network (the low-degree periphery) might be slower or more restricted compared to disassortative networks.
4. **Connectivity:** Disassortative networks tend to have a "star-like" local structure where hubs act as central connectors for many small nodes, leading to a more distributed but fragile global connectivity.

### Steps / Derivation
1. Define the degree-degree correlation function or the assortativity coefficient $r$.
2. The coefficient is calculated as:
$$
r = \frac{\sum_{jk} jk(e_{jk} - q_j q_k)}{\sigma_q^2}
$$
where $e_{jk}$ is the joint probability distribution of the degrees of the two nodes at the ends of a randomly chosen edge, and $q_k$ is the over-relaxed degree distribution.
3. Analyze the sign of $r$ to categorize the mixing pattern.
4. Relate the statistical measure back to physical topological features like clustering and path lengths.

## Related Concepts
- [[degree_correlation]]
- [[epidemic_threshold]]
- [[robustness_and_resilience]]