---
id: drs_034
course: Dynamics and Control of Networks
tags: [network-topology, structural-robustness, connectivity]
difficulty: 3
type: open
status: to_learn
---

# Question
Define k-components and compare them with connected components.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Open-ended definition and comparison.

## Explanation
In network science and graph theory, a **$k$-component** (also known as a $k$-core or $k$-connected subgraph) is a maximal subgraph in which all nodes are connected to each other by at least $k$ independent paths. More formally, a $k$-component is a maximal set of vertices such that the removal of any $k-1$ vertices from the subgraph does not disconnect it. This property is referred to as vertex connectivity. The value of $k$ serves as a measure of the "structural thickness" or robustness of that specific part of the network.

**Comparison with Connected Components:**
A **connected component** is actually a specific case of a $k$-component where $k=1$. A 1-component is a maximal subgraph where every pair of nodes is reached by at least one path; removing $0$ nodes leaves it connected, but removing certain single nodes (cut-vertices) might break it apart. 

The primary differences lie in **robustness** and **hierarchy**:
1. **Robustness:** Connected components ($k=1$) are vulnerable; the failure of a single node or edge can partition the component. In contrast, for $k \ge 2$, the component exhibits redundancy. A 2-component (biconnected) requires at least two node failures to be split, a 3-component requires three, and so on.
2. **Nesting Property:** $k$-components are nested. A $k$-component is always a subset of a $(k-1)$-component. For example, all nodes in a 3-component are, by definition, also part of a 2-component and the 1-component.
3. **Density:** Higher $k$ values typically imply a denser local structure. While a connected component can be a simple path or a tree, a $k$-component for $k \ge 3$ must have a significantly higher edge density to maintain multiple independent paths between all members.

### Steps / Derivation
1. **Define connectivity ($\kappa$):** For a graph $G$, $\kappa(G)$ is the minimum number of vertices whose removal disconnects the graph.
2. **Identify $k$-component:** A subgraph $H \subseteq G$ is a $k$-component if $\kappa(H) \ge k$ and there is no supergraph $H' \supset H$ that is also $k$-connected.
3. **Compare via Menger's Theorem:**
$$
\text{Connectivity } \kappa(u, v) \ge k \iff \text{There exist } k \text{ vertex-disjoint paths between } u \text{ and } v.
$$

## Related Concepts
- [[graph_connectivity]]
- [[mengers_theorem]]
- [[network_robustness]]