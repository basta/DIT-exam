---
id: drs_092
course: Dynamics and Control of Networks
tags: [synchronization, matrix-pencils, homogeneous-agents, laplacian-spectrum]
difficulty: 4
type: open
status: to_learn
---

# Question
Show how to use complex matrix pencils for investigating state synchronization of homogeneous agents.

## Options
N/A (Open-ended derivation)

---
# Solution
**Correct Answer:** The stability of synchronization is determined by the spectrum of the complex matrix pencil $(sI - (A - \lambda_i BK))$, where $\lambda_i$ are the eigenvalues of the network Laplacian.

## Explanation
In a network of $N$ homogeneous agents, each agent $i$ follows the linear dynamics $\dot{x}_i = Ax_i + Bu_i$, where $x_i \in \mathbb{R}^n$. To achieve state synchronization, a diffusive coupling control law is typically employed: $u_i = K \sum_{j=1}^N a_{ij}(x_j - x_i)$, where $a_{ij}$ are the elements of the adjacency matrix. This can be expressed using the Graph Laplacian $L$ as $u = -(L \otimes BK)x$.

The global dynamics of the error vectors (defining synchronization as $x_1 = x_2 = \dots = x_N$) can be decoupled into $N$ independent modes using the spectral properties of the Laplacian matrix $L$. If $L$ is diagonalizable, there exists a transformation such that the system decomposes into $N$ subsystems of the form $\dot{\xi}_i = (A - \lambda_i BK)\xi_i$, where $\lambda_i$ are the eigenvalues of $L$. 

The investigation of synchronization then shifts to analyzing the stability of these decoupled systems. This is where the concept of a **complex matrix pencil** becomes essential. Since the eigenvalues $\lambda_i$ can be complex (for directed graphs), the term $(A - \lambda_i BK)$ represents a family of matrices parameterized by $\lambda$. The complex matrix pencil $sI - (A - \sigma BK)$ must be Hurwitz for all $\sigma$ in the set of non-zero Laplacian eigenvalues $\{\lambda_2, \dots, \lambda_N\}$. This approach allows one to define a "Synchronizability Region" in the complex plane; if all relevant eigenvalues of the Laplacian fall within this region (where the pencil remains stable), the network achieves global state synchronization.

### Steps / Derivation
1. Define the local agent dynamics and the diffusive coupling control law using the Kronecker product:
$$
\dot{x} = (I_N \otimes A - L \otimes BK)x
$$
2. Perform a coordinate transformation $z = (T^{-1} \otimes I_n)x$, where $T$ diagonalizes $L$ such that $T^{-1}LT = \Lambda = \text{diag}(\lambda_1, \dots, \lambda_N)$.
3. Obtain the decoupled modal equations for each eigenvalue $\lambda_i$:
$$
\dot{z}_i = (A - \lambda_i BK)z_i
$$
4. Analyze the stability of the synchronization manifold (associated with $\lambda_1 = 0$) by ensuring the remaining $N-1$ modes are asymptotically stable. This requires the characteristic roots of the matrix pencil to have negative real parts:
$$
\det(sI - (A - \lambda_i BK)) = 0 \implies \text{Re}(s) < 0, \forall i \in \{2, \dots, N\}
$$

## Related Concepts
- [[master_stability_function]]
- [[kronecker_product_dynamics]]
- [[graph_laplacian_spectrum]]