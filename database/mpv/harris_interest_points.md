---
id: mpv_002
course: Methods of Computer Vision
tags: [harris, corner-detector, second-moment-matrix, invariance]
difficulty: 3
type: open
status: to_learn
---

# Question
**Harris interest points** — definition, algorithm for detection, parameters. Explain the motivation behind the definition. Describe the effects of the parameters on the number of detected points. To which transformation (geometric/photometric) is this detector invariant?

---
# Solution

## Motivation
A "good" feature is a location where the image intensity changes significantly in *multiple* directions. Such points are stable under small shifts → repeatable. Harris formalized this via the autocorrelation of intensity changes under small window shifts $(u, v)$:
$$
E(u, v) = \sum_{x,y} w(x, y) \, [I(x+u, y+v) - I(x, y)]^2.
$$
A first-order Taylor expansion gives
$$
E(u, v) \approx \begin{pmatrix} u & v \end{pmatrix} M \begin{pmatrix} u \\ v \end{pmatrix},
$$
where $M$ is the **second moment (structure) matrix**:
$$
M = \sum_{x,y} w(x,y) \begin{pmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{pmatrix}.
$$
The eigenvalues $\lambda_1, \lambda_2$ of $M$ describe how intensity varies along the two principal directions:
- both small → flat region,
- one large, one small → edge,
- both large → corner / interest point.

## Harris Response
To avoid explicit eigendecomposition, Harris proposed:
$$
R = \det(M) - k \cdot \text{tr}(M)^2 = \lambda_1 \lambda_2 - k(\lambda_1 + \lambda_2)^2.
$$
$R$ is large positive at corners, negative at edges, small at flat regions.

## Algorithm
1. Compute image gradients $I_x, I_y$ (e.g., with Sobel, after smoothing with $\sigma_D$).
2. Compute products $I_x^2, I_y^2, I_x I_y$.
3. Smooth them with a Gaussian window of scale $\sigma_I$ (integration scale).
4. Compute the response $R$ at every pixel.
5. Threshold $R > T$.
6. Non-maximum suppression in a local neighborhood.

## Parameters and Their Effects
- **$\sigma_D$ (differentiation scale):** scale at which gradients are computed. Larger $\sigma_D$ → fewer, more stable points; finer detail is lost.
- **$\sigma_I$ (integration scale):** size of the Gaussian window summing the outer products. Larger $\sigma_I$ → larger support, fewer detected points, more robust to noise.
- **$k$ (sensitivity, typically 0.04–0.06):** larger $k$ → more conservative, fewer detections (edges and weaker corners are rejected).
- **Threshold $T$:** higher $T$ → fewer points.
- **NMS radius:** larger radius → fewer (more spread) points.

## Invariances
- **Rotation invariant** — eigenvalues of $M$ are rotation invariant.
- **Invariant to additive illumination change** ($I \to I + c$) — only gradients are used.
- **Partially invariant to multiplicative scaling** ($I \to aI$): the response scales by $a^4$, so *ranking* is preserved but the threshold must be adapted.
- **NOT invariant to image scale** — Harris alone is not scale-invariant; combine with Laplacian scale selection → Harris-Laplace.
- **NOT invariant to affine** — combine with affine adaptation → Harris-Affine.

## Related Concepts
- [[second-moment-matrix]]
- [[harris-laplace]]
- [[harris-affine]]
- [[corner-detection]]
