---
id: drs_030
course: Dynamics and Control of Networks
tags: [link-analysis, centrality-measures, directed-graphs]
difficulty: 3
type: open
status: to_learn
---

# Question
Explain hubs and authorities and their relation to co-citation and bibliographic coupling.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Hubs and authorities represent a dual-reinforcement relationship in directed networks (HITS algorithm), where authorities are nodes pointed to by high-quality hubs, and hubs are nodes that point to high-quality authorities. This relationship is mathematically equivalent to the spectral analysis of co-citation and bibliographic coupling matrices.

## Explanation
The concept of **Hubs and Authorities** was introduced by Jon Kleinberg via the Hyperlink-Induced Topic Search (HITS) algorithm. This model acknowledges that in directed networks (like the World Wide Web or citation networks), nodes play two distinct roles. An **Authority** is a node that contains valuable primary information (e.g., a highly cited research paper), while a **Hub** is a node that acts as a directory or catalog, pointing to many good authorities (e.g., a review paper or a library portal).

The defining characteristic of HITS is the *mutually reinforcing* relationship: a good hub points to many good authorities, and a good authority is pointed to by many good hubs. This avoids the simplicity of in-degree by considering the quality of the neighbors.

This mechanism is deeply rooted in traditional bibliometrics. **Bibliographic coupling** occurs when two documents cite the same third document; it measures the similarity of the "outgoing" behavior. This corresponds to the Hub score calculation, as nodes with high bibliographic coupling often share common targets. **Co-citation** occurs when two documents are cited together by the same third document; it measures the similarity of the "incoming" prestige. This corresponds to the Authority score calculation. 

Mathematically, if $A$ is the adjacency matrix of the network, the authority scores are given by the principal eigenvector of $A^T A$ (the co-citation matrix), and the hub scores are given by the principal eigenvector of $AA^T$ (the bibliographic coupling matrix).

### Steps / Derivation
1. Define the Authority score $x_i$ and Hub score $y_i$ for node $i$. The authority score is the sum of hub scores of nodes pointing to it, and the hub score is the sum of authority scores of nodes it points to:
$$
x_i = \alpha \sum_{j \to i} y_j \quad \text{and} \quad y_i = \beta \sum_{i \to j} x_j
$$
2. In matrix form, where $A$ is the adjacency matrix ($A_{ij}=1$ if $i \to j$):
$$
\mathbf{x} = \alpha A^T \mathbf{y} \quad \text{and} \quad \mathbf{y} = \beta A \mathbf{x}
$$
3. Substitute $\mathbf{y}$ into the equation for $\mathbf{x}$ to find the authority vector:
$$
\mathbf{x} = \alpha \beta A^T A \mathbf{x}
$$
4. Substitute $\mathbf{x}$ into the equation for $\mathbf{y}$ to find the hub vector:
$$
\mathbf{y} = \alpha \beta A A^T \mathbf{y}
$$
5. Observe that $A^T A$ is the **co-citation matrix** and $AA^T$ is the **bibliographic coupling matrix**. The scores are the eigenvectors corresponding to the largest eigenvalues of these symmetric matrices.

## Related Concepts
- [[hits_algorithm]]
- [[eigenvector_centrality]]
- [[spectral_graph_theory]]