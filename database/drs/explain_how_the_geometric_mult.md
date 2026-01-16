---
id: drs_021
course: Dynamics and Control of Networks
tags: [linear-algebra, spectral-theory, stability-analysis]
difficulty: 2
type: open
status: to_learn

---
# Question
Explain how the geometric multiplicity of eigenvalues differ from the algebraic one.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The algebraic multiplicity is the number of times an eigenvalue appears as a root of the characteristic polynomial, while the geometric multiplicity is the dimension of the associated eigenspace (the number of linearly independent eigenvectors).

## Explanation
In the study of network dynamics, the spectral properties of matrices (such as the Laplacian or Adjacency matrix) determine the system's stability and convergence rates. Understanding the distinction between algebraic and geometric multiplicity is fundamental to determining if a system matrix is diagonalizable or if it requires a Jordan Normal Form representation.

**Algebraic Multiplicity ($m_\lambda$):**
When we solve for the eigenvalues of a square matrix $A \in \mathbb{R}^{n \times n}$, we compute the characteristic polynomial $p(\lambda) = \det(A - \lambda I) = 0$. The algebraic multiplicity of a specific eigenvalue $\lambda_i$ is the number of times the factor $(\lambda - \lambda_i)$ appears in the factored characteristic polynomial. Essentially, it represents the "theoretical" count of that specific eigenvalue.

**Geometric Multiplicity ($g_\lambda$):**
The geometric multiplicity refers to the number of linearly independent eigenvectors associated with $\lambda_i$. Formally, it is the dimension of the null space (kernel) of $(A - \lambda_i I)$. In network control, this tells us how many independent directions in the state space are directly scaled by the eigenvalue $\lambda_i$ without rotating.

**Relationship and Implications:**
A critical theorem in linear algebra states that for any eigenvalue, $1 \leq g_\lambda \leq m_\lambda$. If $g_\lambda < m_\lambda$ for any eigenvalue, the matrix is said to be **defective**. Defective matrices cannot be diagonalized, which in network dynamics implies the presence of secular terms (terms like $t e^{\lambda t}$) in the system's impulse response, often leading to slower convergence or specific types of instability in consensus protocols.

### Steps / Derivation
1. **Define the Characteristic Equation:**
Find the roots of the polynomial to determine algebraic multiplicity.
$$
\text{det}(A - \lambda I) = (\lambda - \lambda_1)^{m_1}(\lambda - \lambda_2)^{m_2}...
$$

2. **Calculate the Eigenspace Dimension:**
Determine the rank of the shifted matrix to find the geometric multiplicity via the Rank-Nullity Theorem.
$$
g_{\lambda_i} = \dim(\text{ker}(A - \lambda_i I)) = n - \text{rank}(A - \lambda_i I)
$$

## Related Concepts
- [[jordan_canonical_form]]
- [[diagonalizability_condition]]
- [[spectral_radius]]