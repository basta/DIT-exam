---
id: mpv_004
course: Methods of Computer Vision
tags: [affine-invariance, harris-affine, hessian-affine, shape-adaptation]
difficulty: 4
type: open
status: to_learn
---

# Question
Describe steps to generalize Harris/Hessian detector to become **affine invariant**.

---
# Solution

## Motivation
Harris-Laplace and Hessian-Laplace are similarity-covariant: they handle translation, rotation and isotropic scaling. Under a perspective view of a planar surface, however, the local transformation is approximated by an **affine** transformation. We need to estimate not just a scalar scale, but an *anisotropic* shape (an ellipse).

## Affine Shape Adaptation (Lindeberg & Gårding / Mikolajczyk & Schmid)
The key tool is the second moment matrix computed at scales $\sigma_D$ (differentiation) and $\sigma_I$ (integration):
$$
\mu(\mathbf{x}; \sigma_D, \sigma_I) = G(\sigma_I) * \begin{pmatrix} L_x^2 & L_x L_y \\ L_x L_y & L_y^2 \end{pmatrix}.
$$
If $\mu = U \Lambda U^\top$, then warping the patch by $\mu^{-1/2}$ makes its local second moment matrix isotropic (a multiple of the identity). Iterating this procedure converges to an affine-covariant ellipse.

## Algorithm
1. **Initial detection.** Detect a Harris-Laplace / Hessian-Laplace point: position $\mathbf{x}_0$ and characteristic scale $\sigma^*$. Initialize the shape $U = I$ (circle).
2. **Iterate:**
   a. Warp the local image patch around $\mathbf{x}$ using current $U^{-1/2}$ to make it (approximately) isotropic.
   b. In the warped frame, recompute $\mu$ at scales $\sigma_D, \sigma_I$.
   c. Update $U \leftarrow \mu^{-1/2} U$.
   d. Re-localize the keypoint to the maximum of the Harris / Hessian response in the warped frame.
   e. Re-select scale by Laplacian extremum (only along the scale axis in the normalized frame).
3. **Convergence:** stop when the ratio of eigenvalues of $\mu$ is close to 1 (e.g., $\lambda_{\max}/\lambda_{\min} < 1.05$), i.e., the local second moment matrix is essentially isotropic.
4. **Output:** for each point, an elliptical region $(\mathbf{x}, U)$ — affine-covariant.

## Why It Works
Under an affine transformation $A$, the second moment matrices in the two views satisfy $\mu' = A^{-\top} \mu A^{-1}$. The fixed point of the iteration is the shape whose pre-image is the isotropic Gaussian, i.e., the unique elliptical region that is affine-covariant between the two views (up to rotation, which is resolved by orientation estimation).

## Notes
- Orientation must be resolved separately (e.g., by gradient-orientation histogram on the normalized patch).
- The resulting detectors are **Harris-Affine** and **Hessian-Affine** (Mikolajczyk & Schmid, 2002).
- Iterations may diverge → reject the point if it does not converge in a bounded number of steps or if the ellipse becomes too elongated.

## Related Concepts
- [[harris-affine]]
- [[hessian-affine]]
- [[affine-shape-adaptation]]
- [[second-moment-matrix]]
