---
id: drs_020
course: Dynamics and Control of Networks
tags: [matrix-theory, stability-analysis, positive-systems]
difficulty: 2
type: open
status: to_learn
---

# Question
Define the M-matrix.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A matrix $A \in \mathbb{R}^{n \times n}$ is an M-matrix if it can be expressed in the form $A = sI - B$, where $B = (b_{ij})$ with $b_{ij} \geq 0$ for all $i, j$, and $s \geq \rho(B)$, where $\rho(B)$ is the spectral radius of $B$.

## Explanation
In the study of Network Dynamics and Control, M-matrices play a fundamental role, particularly when analyzing the stability of positive systems, consensus protocols, and compartmental models. An M-matrix is a type of Z-matrix (a matrix where all off-diagonal elements are less than or equal to zero) that satisfies additional positivity properties regarding its eigenvalues or its inverse.

There are several equivalent definitions for a matrix $A$ with $a_{ij} \leq 0$ for $i \neq n$ to be an M-matrix. A common definition used in control theory is that $A$ is a nonsingular M-matrix if all its eigenvalues have real parts that are strictly positive. If the real parts are non-negative (allowing for zero), it is referred to as a singular M-matrix. 

The importance of M-matrices in dynamics stems from their relationship to Lyapunov stability. For instance, if a system's Jacobian is the negative of an M-matrix, the system often exhibits "stiff" but stable behavior. Furthermore, M-matrices are monotone, meaning that if $A$ is a nonsingular M-matrix, then its inverse $A^{-1}$ exists and is a non-negative matrix ($A^{-1} \geq 0$). This property is crucial when ensuring that physical quantities like concentrations, probabilities, or populations remains non-negative over time.

### Steps / Derivation
1. Identify the off-diagonal structure: For $i \neq j$, $a_{ij} \leq 0$.
2. Decompose the matrix into a scalar multiple of the identity and a non-negative matrix $B$.
3. Check the condition on the scalar $s$ relative to the spectral radius:
$$
A = sI - B, \quad s \geq \rho(B), \quad B \geq 0
$$
4. If $s > \rho(B)$, the matrix is a non-singular M-matrix, implying $\text{Re}(\lambda_i) > 0$ for all $i$.

## Related Concepts
- [[perron_frobenius_theorem]]
- [[positive_systems]]
- [[laplacian_matrix]]