---
id: mpv_006
course: Methods of Computer Vision
tags: [hessian, DoG, blob-detector, scale-space]
difficulty: 3
type: open
status: to_learn
---

# Question
**Hessian and Difference of Gaussian interest points.** Definition, properties.

---
# Solution

## Hessian Detector
The Hessian matrix of $L(\cdot; \sigma) = G(\sigma) * I$ is
$$
H(\mathbf{x}; \sigma) = \begin{pmatrix} L_{xx} & L_{xy} \\ L_{xy} & L_{yy} \end{pmatrix}.
$$
Interest points are local extrema (in space, and optionally in scale) of
$$
\det H = L_{xx} L_{yy} - L_{xy}^2,
$$
which responds strongly to **blob-like** structures where intensity changes simultaneously in two directions. Edges are suppressed because along an edge one principal curvature is small, so $\det H \to 0$.

### Variants
- **Hessian** at a single scale: position-only detector.
- **Hessian-Laplace:** extrema of $\det H$ in space, scale selected by the (normalized) Laplacian.
- **Hessian-Affine:** Hessian-Laplace + affine shape adaptation.

### Scale Normalization
For scale-space comparisons use the $\gamma$-normalized determinant: $\sigma^4 \det H$. The factor $\sigma^4$ compensates for amplitude decay so that the extrema across scale correspond to blob size.

## Difference of Gaussians (DoG)
DoG approximates the (scale-normalized) Laplacian of Gaussian:
$$
G(\sigma_2) - G(\sigma_1) \approx (\sigma_2 - \sigma_1) \, \sigma \, \nabla^2 G(\sigma), \quad \sigma_2 = k \sigma_1.
$$
Hence
$$
\text{DoG}(\mathbf{x}, \sigma) = L(\mathbf{x}; k\sigma) - L(\mathbf{x}; \sigma).
$$
Used in **SIFT**: keypoints are local extrema of DoG in a 3×3×3 neighborhood in (x, y, σ).

### Why DoG?
- Cheap: subtraction of two already-computed pyramid levels.
- Approximation error to $\sigma^2 \nabla^2 G$ is small; Lowe showed that the loss of stability vs. exact LoG is negligible.
- Naturally yields a *scale-covariant* detector.

## Common Properties
- Both detect **blob-like** structures (extrema of intensity over some support).
- **Rotation invariant** (Hessian: trace/det are invariants; DoG: isotropic Gaussian).
- **Scale covariant** when combined with scale-space extrema.
- **Invariant to additive illumination changes** and partially to multiplicative changes.
- Edges produce ridge-like elongated responses; SIFT removes them by checking the ratio of eigenvalues of the spatial Hessian of DoG and rejecting points with high ratio.

## Hessian vs. Harris
- **Harris** uses the second moment matrix of *first* derivatives → good for corners.
- **Hessian** uses *second* derivatives → good for blobs.
- Empirically Hessian-based detectors tend to be more repeatable for textured / blob-rich images; Harris is preferred for corner-rich, structured scenes.

## Related Concepts
- [[hessian-laplace]]
- [[hessian-affine]]
- [[DoG]]
- [[SIFT]]
- [[blob-detector]]
