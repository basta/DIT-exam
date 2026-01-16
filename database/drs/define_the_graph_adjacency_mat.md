---
id: drs_008
course: Dynamics and Control of Networks
tags: [graph-theory, adjacency-matrix, network-topology, linear-algebra]
difficulty: 1
type: open
status: to_learn
---

# Question
Define the graph adjacency matrix.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The adjacency matrix $A$ of a graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ with $n$ nodes is an $n \times n$ matrix where the element $a_{ij}$ represents the presence (and potentially weight) of an edge between nodes $i$ and $j$.

## Explanation
In the study of Network Dynamics and Control, the adjacency matrix is the foundational algebraic representation of a network's topology. It maps the discrete set of nodes and edges into a structure compatible with linear algebra and matrix differential equations. 

For a simple (unweighted and undirected) graph $\mathcal{G}$ consisting of a set of vertices $\mathcal{V} = \{v_1, v_2, \dots, v_n\}$ and edges $\mathcal{E}$, the adjacency matrix $A$ is defined such that $a_{ij} = 1$ if there exists an edge $(v_j, v_i) \in \mathcal{E}$, and $a_{ij} = 0$ otherwise. In an undirected graph, the matrix is always symmetric ($A = A^T$), meaning if node $i$ is connected to node $j$, node $j$ is also connected to node $i$. 

In the context of directed graphs (digraphs), the symmetry is generally lost; $a_{ij} = 1$ indicates a directed link from node $j$ to node $i$ (following the convention $\dot{x}_i = \sum a_{ij} x_j$ often used in consensus protocols). For weighted graphs, the binary values $\{0, 1\}$ are replaced by real numbers $w_{ij}$, representing the strength or capacity of the interaction. The spectral properties of $A$, such as its eigenvalues and eigenvectors, are critical for determining the stability and convergence rates of dynamical processes running over the network, such as synchronization or diffusion.

### Steps / Derivation
1. Identify the number of nodes $n$ in the graph to determine the matrix dimensions $n \times n$.
2. For every pair of nodes $(i, j)$, check for the existence of an edge.
3. Assign the value $1$ (or weight $w_{ij}$) for an existing edge and $0$ for no edge.
$$
A \in \mathbb{R}^{n \times n}, \quad [A]_{ij} = \begin{cases} 1 & \text{if } (j, i) \in \mathcal{E} \\ 0 & \text{otherwise} \end{cases}
$$

## Related Concepts
- [[graph_laplacian]]
- [[spectral_radius]]
- [[degree_matrix]]