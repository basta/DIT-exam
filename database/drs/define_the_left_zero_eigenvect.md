---
id: drs_023
course: Dynamics and Control of Networks
tags: [linear-algebra, spectral-theory, eigenvalue-problem]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the left zero eigenvector.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A row vector $\mathbf{w}^\top$ such that $\mathbf{w}^\top A = \mathbf{0}^\top$ (or $\mathbf{0}^\top \mathbf{w} = 0$), where $A$ is a square matrix with at least one eigenvalue equal to zero.

## Explanation
In the study of linear systems and network dynamics, eigenvectors are typically categorized as "right" or "left." While the standard (right) eigenvector $\mathbf{v}$ satisfies $A\mathbf{v} = \lambda\mathbf{v}$, the left eigenvector $\mathbf{w}^\top$ satisfies the equation $\mathbf{w}^\top A = \lambda \mathbf{w}^\top$. A **left zero eigenvector** specifically refers to the case where the associated eigenvalue $\lambda$ is equal to zero.

Mathematically, if a square matrix $A$ is singular (i.e., $\det(A) = 0$), it possesses at least one zero eigenvalue. The left zero eigenvector is the row vector that lies in the left nullspace of $A$. In the context of Network Dynamics, particularly when $A$ represents a Graph Laplacian matrix $L$, the left zero eigenvector carries significant physical meaning. For a standard directed graph Laplacian, the vector of all ones $\mathbf{1}$ is always a right zero eigenvector ($L\mathbf{1} = \mathbf{0}$), but the left zero eigenvector $\mathbf{w}^\top$ corresponds to the stationary distribution or the weights of nodes in a consensus protocol. 

If the network is strongly connected, the left zero eigenvector is unique (up to scaling) and has strictly positive entries (Perron-Frobenius Theorem). In consensus dynamics, the left zero eigenvector determines the final "agreement" value of the system, acting as a weighting vector that defines how much influence each agent's initial state has on the final steady state.

### Steps / Derivation
1. Start with the general definition of a left eigenvector for a square matrix $A \in \mathbb{R}^{n \times n}$:
$$
\mathbf{w}^\top A = \lambda \mathbf{w}^\top
$$
2. Set the eigenvalue $\lambda$ to zero to find the specific definition for the zero eigenvector:
$$
\mathbf{w}^\top A = 0 \cdot \mathbf{w}^\top \implies \mathbf{w}^\top A = \mathbf{0}^\top
$$
3. Note that this is equivalent to taking the transpose of the right nullspace problem for $A^\top$:
$$
A^\top \mathbf{w} = \mathbf{0}
$$

## Related Concepts
- [[graph_laplacian]]
- [[consensus_protocols]]
- [[spectral_properties]]