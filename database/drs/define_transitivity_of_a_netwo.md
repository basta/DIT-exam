---
id: drs_035
course: Dynamics and Control of Networks
tags: [network-topology, clustering-coefficient, graph-theory]
difficulty: 2
type: open
status: to_learn
---

# Question
Define transitivity of a network in any of equivalent ways.

## Options
N/A

---
# Solution
**Correct Answer:** The transitivity (or global clustering coefficient) of a network is the ratio of three times the number of triangles to the number of connected triples of nodes in the graph.

## Explanation
In the study of complex networks, transitivity measures the tendency of nodes to cluster together. It is based on the sociological observation that "the friend of my friend is also likely to be my friend." In graph-theoretic terms, if there is an edge between node $u$ and node $v$, and an edge between node $v$ and node $w$, transitivity quantifies the probability that an edge exists between $u$ and $w$.

A common way to define this is through the **Global Clustering Coefficient**. A "triple" (or "connected triple") consists of three nodes connected by at least two edges. A "closed triple" (or "triangle") is a triple where all three possible edges exist. The transitivity $C$ is defined as the fraction of triples that are closed.

Mathematically, it is expressed as:
$$ C = \frac{3 \times \text{number of triangles}}{\text{number of connected triples}} $$

The factor of 3 in the numerator is necessary because each triangle contains three connected triples (one centered at each of the three vertices). This scaling ensures that $0 \le C \le 1$. A value of $C=1$ implies a perfectly transitive network where every component is a clique, whereas $C=0$ describes a network with no triangles, such as a tree or a bipartite graph. This global measure differs from the average local clustering coefficient, as it gives more weight to high-degree nodes.

### Steps / Derivation
1. Identify all connected triples in the network (paths of length 2).
2. Count the number of triangles (cycles of length 3).
3. Apply the ratio formula:
$$
C = \frac{3 \sum_{i>j>k} A_{ij}A_{jk}A_{ki}}{\sum_{i} \binom{k_i}{2}}
$$
Where $A$ is the adjacency matrix and $k_i$ is the degree of node $i$.

## Related Concepts
- [[clustering_coefficient]]
- [[triadic_closure]]
- [[graph_topology]]