---
id: mpv_031
course: Methods of Computer Vision
tags: [KLT, gradient-tracking, aperture-problem, horizontal-motion]
difficulty: 3
type: open
status: to_learn
---

# Question
For a static scene and viewing by a camera with **only horizontal movement**: draw / describe an image patch that will be useful for tracking with a **gradient method** (KLT tracker). Which properties should the image patch have to be suitable for tracking?

---
# Solution

## Why Some Patches Are Useless: The Aperture Problem
The KLT tracker assumes brightness constancy and solves a linearized least-squares problem for the displacement $(u, v)$ between two frames at a patch:
$$
\sum_{\mathbf{x} \in W} \big[I_x u + I_y v + I_t\big]^2 \to \min.
$$
Setting the gradient to zero gives
$$
\underbrace{\begin{pmatrix} \sum I_x^2 & \sum I_x I_y \\ \sum I_x I_y & \sum I_y^2 \end{pmatrix}}_{M} \begin{pmatrix} u \\ v \end{pmatrix} = -\begin{pmatrix} \sum I_x I_t \\ \sum I_y I_t \end{pmatrix}.
$$
A patch is well-tracked **iff $M$ is well-conditioned** — both eigenvalues $\lambda_1 \ge \lambda_2 \gg 0$ (Shi–Tomasi criterion).

## The Special Case: Horizontal-Only Motion
If we know that the camera moves only horizontally, the unknown is just $u$ (single DOF); the $v$ component is fixed at 0. The equation reduces to
$$
\sum I_x^2 \cdot u = -\sum I_x I_t.
$$
This is solvable as long as $\sum I_x^2 > 0$, i.e., **the patch has non-zero horizontal gradient** somewhere.

So for horizontal motion, the patch needs **structure (gradient) in the horizontal direction**. Vertical gradients alone are useless (a horizontal stripe shifted horizontally looks identical → aperture problem).

## Suitable Patches for Horizontal Motion
- **Vertical edges** (a vertical line / pole, the side of a building): strong $I_x$, weak $I_y$ — perfect, despite being a "bad" patch for general 2-D KLT.
- **Corners** (e.g., a window corner): even better, since they also give a horizontal gradient and additionally pin the vertical coordinate (if we want a 2-D solution as a sanity check).
- **Textured patches** with vertical structure: e.g., a fence post next to a brick wall.

## Unsuitable Patches
- **Uniform / flat patches** (sky, smooth walls): no gradient → cannot estimate motion in any direction.
- **Purely horizontal edges** (horizon line, a long shelf seen face-on): $I_x \approx 0$ everywhere, $I_y \ne 0$ — invisible to horizontal motion. Tracker has no signal: the horizontal edge looks the same after a horizontal shift.

## Sketch (textual)
```
GOOD patch:                      BAD patch:
+--------+                       +--------+
|       █|                       |        |
|       █|                       |█████████|
|       █|                       |        |
|       █|                       |        |
+--------+                       +--------+
strong horizontal gradient       only vertical gradient
along the vertical edge          (a horizontal line)
                                 → invisible to horizontal motion
```

## Properties of a "Trackable" Patch (KLT in General)
1. **Texture in the direction of motion**: nonzero gradient component along the direction in which motion is expected.
2. **Sufficient contrast**: large gradient magnitude → high signal-to-noise ratio.
3. **Well-conditioned $M$** (Shi–Tomasi): $\min(\lambda_1, \lambda_2) > \tau$. Avoids the aperture problem and noise sensitivity.
4. **Reasonable patch size**: too small ⇒ noisy; too large ⇒ violates the locally-constant-motion assumption.
5. **Stable structure across time**: not in regions with frequent occlusion, specular highlights, or strong illumination changes.
6. **Distinctive enough** that a small mismatch is detectable (no extreme self-similarity that would create local minima).

## Related Concepts
- [[aperture-problem]]
- [[shi-tomasi]]
- [[KLT-tracker]]
- [[lucas-kanade]]
