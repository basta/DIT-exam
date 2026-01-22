---
id: efd_030
course: Estimation, Filtration, and Detection
tags: [least-squares, orthogonality-principle, linear-estimation]
difficulty: 2
type: open
status: to_learn
---

# Question
State the Geometric Orthogonality Principle of Least Squares. Which two vectors must be orthogonal?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** The Orthogonality Principle states that for the optimal estimate, the error vector must be orthogonal to the subspace spanned by the observations (or the data matrix columns). The two vectors that must be orthogonal are the **error vector** ($e$) and the **observation vector** (or any vector in the column space of $H$).

## Explanation
The Geometric Orthogonality Principle is a fundamental cornerstone of linear estimation theory, particularly in the context of Least Squares (LS) and Minimum Mean Square Error (MMSE) estimation. In a linear model represented by $y = H\theta + v$, where $y$ is the observation vector, $H$ is the observation matrix, and $\theta$ is the parameter vector to be estimated, we seek an estimate $\hat{y} = H\hat{\theta}$ that minimizes the squared Euclidean norm of the residual.

Geometrically, the vector of observations $y$ lives in an $n$-dimensional space, while the estimate $\hat{y}$ is constrained to lie within the subspace spanned by the columns of the matrix $H$ (often called the range or column space). The estimation error is defined as the difference between the actual observation and its projection: $e = y - \hat{y}$. 

The principle asserts that the "shortest distance" from the point $y$ to the subspace $H$ is achieved if and only if the error vector $e$ is perpendicular (orthogonal) to every vector in that subspace. If the error were not orthogonal, there would exist a component of the error still residing within the subspace that could be used to further reduce the magnitude of the error. Therefore, the condition for optimality is that the inner product of any vector in the column space of $H$ and the error vector $e$ must be zero. This leads directly to the Normal Equations used to solve for $\hat{\theta}$.

### Steps / Derivation
1. Define the error vector as the difference between the measurement and the projection onto the subspace:
$$
e = y - H\hat{\theta}
$$
2. Apply the orthogonality condition: the error vector must be orthogonal to the columns of $H$, meaning $H^T e = 0$.
3. Substitute the error definition into the orthogonality condition to derive the Normal Equations:
$$
H^T(y - H\hat{\theta}) = 0 \implies H^T H \hat{\theta} = H^T y
$$

## Related Concepts
- [[projection_theorem]]
- [[normal_equations]]
- [[linear_minimum_mean_square_error]]