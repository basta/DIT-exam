---
id: drs_016
course: Dynamics and Control of Networks
tags: [gersgorin-theory, algebraic-graph-theory, laplacian-spectrum]
difficulty: 3
type: open
status: to_learn

---
# Question
State the Geršgorin disc theorem and explain how it is applied to the graph Laplacian.

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The theorem states that all eigenvalues of a square matrix lie within the union of discs centered at its diagonal elements with radii equal to the sum of the absolute values of the off-diagonal elements in that row. For a graph Laplacian $L$, this proves $L$ is positive semi-definite with all eigenvalues in the range $[0, 2\max(d_i)]$.

## Explanation
The Geršgorin Disc Theorem is a fundamental result in matrix analysis used to bound the spectrum (eigenvalues) of a square matrix. For a complex $n \times n$ matrix $A$, the theorem defines a disc $R_i$ in the complex plane for each row $i$:
$$R_i = \left\{ z \in \mathbb{C} : |z - a_{ii}| \leq \sum_{j \neq i} |a_{ij}| \right\}$$
The theorem asserts that all eigenvalues $\lambda$ of $A$ lie within the union of these discs: $\sigma(A) \subseteq \bigcup_{i=1}^n R_i$.

When applied to the **Graph Laplacian** $L = D - A$ (where $D$ is the degree matrix and $A$ is the adjacency matrix), the theorem provides immediate insights into the network's stability and connectivity properties. For a Laplacian matrix:
1. The diagonal elements $l_{ii}$ are the degrees of the nodes, $d_i$.
2. The off-diagonal elements $l_{ij}$ (where $i \neq j$) are $-1$ if an edge exists and $0$ otherwise.
3. The sum of the absolute values of the off-diagonal elements in row $i$ is exactly $\sum_{j \neq i} |-A_{ij}| = d_i$.

According to the theorem, every eigenvalue $\lambda$ of $L$ must satisfy:
$$| \lambda - d_i | \leq d_i$$
This inequality implies that $0 \leq \text{Re}(\lambda) \leq 2d_i$. Since the Laplacian is a real symmetric matrix, its eigenvalues are real, so we conclude $0 \leq \lambda_i \leq 2 \max(d_j)$. This proves that the Laplacian is positive semi-definite ($L \succeq 0$). Furthermore, since the row sums of a Laplacian are always zero, $z=0$ is always on the boundary of every disc, consistent with the fact that $\mathbf{1}$ is the eigenvector associated with the eigenvalue $0$.

### Steps / Derivation
1. **State the general disc definition**: Define the center as the diagonal element $a_{ii}$ and the radius $r_i$ as the sum of absolute values of off-diagonal entries.
2. **Apply to Laplacian Entries**: Substitute $l_{ii} = d_i$ and $\sum_{j \neq i} |l_{ij}| = \sum_{j \neq i} A_{ij} = d_i$.
3. **Formulate the Laplacian Inequality**:
$$ |\lambda - d_i| \leq d_i \implies d_i - d_i \leq \lambda \leq d_i + d_i $$
4. **Identify the Spectrum Bounds**: Conclude that $\lambda \in [0, 2d_{max}]$, confirming all eigenvalues are non-negative.

## Related Concepts
- [[spectral_graph_theory]]
- [[positive_semi_definite_matrices]]
- [[algebraic_connectivity]]