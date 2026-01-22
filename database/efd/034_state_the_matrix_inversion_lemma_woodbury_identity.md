---
id: efd_034
course: Estimation, Filtration, and Detection
tags: [recursive-least-squares, woodbury-identity, matrix-analysis]
difficulty: 3
type: open
status: to_learn
---

# Question
State the Matrix Inversion Lemma (Woodbury Identity). Why is it crucial for deriving the Recursive Least Squares (RLS) algorithm?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** 
The Matrix Inversion Lemma states: $(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}$. It is crucial for RLS because it allows for the recursive update of the inverse covariance matrix without performing a full $O(N^3)$ matrix inversion at each time step.

## Explanation
The Matrix Inversion Lemma (specifically the Woodbury Identity) is a fundamental result in linear algebra that expresses the inverse of a rank-$k$ correction of a matrix in terms of the inverse of the original matrix. In the context of Signal Processing and Adaptive Filtering, specifically the Recursive Least Squares (RLS) algorithm, we are tasked with minimizing a weighted sum of square errors. This optimization requires the calculation of the inverse of the deterministic autocorrelation matrix, often denoted as $P(n) = \Phi^{-1}(n)$.

During the recursive step, the new autocorrelation matrix $\Phi(n)$ is updated by adding a rank-one term (the outer product of the new data vector $x(n)$ and its transpose) to the previous matrix $\Phi(n-1)$, such that $\Phi(n) = \lambda \Phi(n-1) + x(n)x^T(n)$. Without the lemma, computing the inverse of this $N \times N$ matrix at every iteration would require $O(N^3)$ operations, which is computationally prohibitive for real-time systems or large data dimensions.

The Woodbury Identity allows us to update the inverse matrix $P(n)$ directly using the previous inverse $P(n-1)$ and the new data vector. This reduces the computational complexity to $O(N^2)$, as it transforms a matrix inversion problem into a series of matrix-vector multiplications and a scalar division. This efficiency is what makes RLS a viable alternative to the Least Mean Squares (LMS) algorithm when faster convergence is required.

### Steps / Derivation
1. State the Woodbury Identity:
$$
(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}
$$
2. Match RLS variables to the identity. In the update $\Phi(n) = \lambda \Phi(n-1) + x(n)x^T(n)$:
   - Set $A = \lambda \Phi(n-1)$
   - Set $U = x(n)$, $V = x^T(n)$, and $C = 1$ (the identity scalar)
3. Substitute these into the lemma to find $P(n) = \Phi^{-1}(n)$:
$$
P(n) = \lambda^{-1} P(n-1) - \frac{\lambda^{-2} P(n-1)x(n)x^T(n)P(n-1)}{1 + \lambda^{-1}x^T(n)P(n-1)x(n)}
$$

## Related Concepts
- [[least_squares_estimation]]
- [[kalman_filter_gain]]
- [[computational_complexity]]