---
id: drs_041
course: Dynamics and Control of Networks
tags: [network-topology, node-equivalence, structural-analysis]
difficulty: 3
type: open
status: to_learn
---

# Question
Define structural and regular equivalence and explain the differences of them.

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** Structural equivalence requires nodes to share the exact same neighbors, while regular equivalence requires nodes to be connected to similar types of neighbors.

## Explanation
In network science and social network analysis, equivalence concepts are used to identify nodes that play similar roles within a graph.

**Structural Equivalence:** Two nodes $i$ and $j$ are said to be structurally equivalent if they have the exact same relationships with all other nodes in the network. Formally, for an adjacency matrix $A$, nodes $i$ and $j$ are structurally equivalent if $A_{ik} = A_{jk}$ for all $k \neq i, j$. In a visualized network, these nodes are "interchangeable" because they are connected to the same set of neighbors. This is a very restrictive definition as it requires a specific overlap in the neighborhood set $N(i) = N(j)$.

**Regular Equivalence:** This is a more relaxed and functional definition. Two nodes $i$ and $j$ are regularly equivalent if they are connected to neighbors who are themselves equivalent. Formally, if $i$ and $j$ are regularly equivalent, then for every neighbor $k$ of $i$, there exists at least one neighbor $m$ of $j$ such that $k$ and $m$ are also equivalent. It does not require nodes to share the same neighbors, but rather to occupy similar "positions" or "roles" (e.g., two different team leads in separate departments are regularly equivalent because they both manage employees, even if they manage different people).

**Key Differences:**
1. **Overlap:** Structural equivalence requires identical neighborhood sets ($N(i) = N(j)$). Regular equivalence does not require any shared neighbors.
2. **Mathematical Rigor:** Structural equivalence is a subset of regular equivalence; all structurally equivalent nodes are regularly equivalent, but the reverse is not true.
3. **Application:** Structural equivalence is useful for identifying redundancy or potential for substitution in a local cluster. Regular equivalence is better for identifying social roles or hierarchical positions across different parts of a large network.

### Steps / Derivation
1. **Identify Neighborhoods:** For structural equivalence, compare the adjacency vectors of node $i$ and node $j$ :
$$
\mathbf{a}_i = [A_{i1}, A_{i2}, \dots, A_{in}] = \mathbf{a}_j
$$
2. **Check for Isomorphism:** For regular equivalence, determine if there is a color-partitioning (equitable partition) such that nodes $i$ and $j$ have the same number of edges to each color class:
$$
\sum_{k \in \mathcal{C}_r} A_{ik} = \sum_{k \in \mathcal{C}_r} A_{jk}
$$
where $\mathcal{C}_r$ represents a specific equivalence class.

## Related Concepts
- [[block_modeling]]
- [[equitable_partitions]]
- [[isomorphism_and_automorphism]]