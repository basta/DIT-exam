---
id: mpv_037
course: Methods of Computer Vision
tags: [hough-transform, voting, parameter-space, line-detection]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the **Hough transform** algorithm for detection of a parametrized structure (line, circle, …). Discuss the properties of the algorithm (time and memory requirements, parameters).

---
# Solution

## Idea
Each *evidence point* (e.g., an edge pixel) is compatible with an entire family of parameter values (every line through the point, every circle of unknown center through the point, …). Have each evidence point **vote for all consistent parameter sets**. The structures present in the image manifest as **maxima in the parameter-space accumulator**.

## Algorithm (general)
Inputs: edge / feature points $\mathcal{P} = \{\mathbf{p}_i\}$, parameterization of the target structure with parameter vector $\boldsymbol{\theta} \in \Theta$, and a quantization of $\Theta$ into discrete bins.

1. **Initialize accumulator** $A(\boldsymbol{\theta}) = 0$ for all discretized $\boldsymbol{\theta}$.
2. **For each evidence point** $\mathbf{p}_i$:
   - Compute the set $\Theta(\mathbf{p}_i) = \{\boldsymbol{\theta} : \mathbf{p}_i \text{ is on the structure } S(\boldsymbol{\theta})\}$.
   - For every discretized $\boldsymbol{\theta} \in \Theta(\mathbf{p}_i)$: $A(\boldsymbol{\theta}) \mathrel{+}= 1$ (or $w_i$ if a confidence weight is available, e.g., edge magnitude).
3. **Find local maxima** in $A$ above a threshold.
4. **Refine** the parameters (sub-bin interpolation, weighted centroid of the maximum).
5. **Output:** list of detected structures.

## Line Detection (Hough lines)
Lines are parameterized as
$$
\rho = x \cos\theta + y \sin\theta, \quad \rho \ge 0, \; \theta \in [0, \pi).
$$
For each edge pixel $(x, y)$, sweep $\theta$ over its discretized range, compute $\rho(\theta)$, vote into bin $(\rho, \theta)$. Maxima correspond to detected lines. Using the *gradient direction* at the edge point further restricts the votes to a small range of $\theta$, drastically reducing computation and noise.

## Circle Detection (Hough circles)
A circle has parameters $(a, b, r)$ — center and radius. Each edge pixel votes for all $(a, b, r)$ such that
$$
(x - a)^2 + (y - b)^2 = r^2.
$$
A 3-D accumulator. If the edge orientation is known, $(a, b)$ for a given $r$ lies on a line along the gradient direction — votes can be restricted accordingly, lowering complexity.

## Generalized Hough Transform (Ballard)
For arbitrary shapes given by a template, build an R-table indexed by gradient orientation pointing to displacements from each contour point to a reference center. Edge pixels vote for the reference location using the R-table — handles arbitrary closed shapes.

## Properties

### Memory
- Proportional to the **size of the parameter-space accumulator**.
- 2-D: $O(B_1 B_2)$ (e.g., lines: $\rho$ and $\theta$ → $O(B_\rho B_\theta)$).
- 3-D circles: $O(B_a B_b B_r)$ — can be hundreds of MB for full-resolution images and fine quantization.
- Generalized Hough adds a *translation $\times$ rotation $\times$ scale* space — typically 4-D or more.

### Time
- $O(N \cdot |\Theta(\mathbf{p})|)$ — number of evidence points times the average number of compatible parameters per point.
- Lines: $O(N B_\theta)$ — sweep angle for each pixel.
- Circles: $O(N B_r)$ if center is constrained by edge gradient direction; $O(N B_a B_b B_r)$ otherwise.
- Maximum-finding: linear in accumulator size.

### Parameters
- **Parameter-space quantization** (bin size for $\rho, \theta, r, \dots$): coarse → fewer bins, faster, but neighboring true lines merge; fine → many bins, slower, more memory, noisy peaks.
- **Vote threshold**: minimum accumulator value to declare a detection.
- **Edge detection upstream** (Canny threshold) → determines $|\mathcal{P}|$.
- **NMS radius** in parameter space (suppress duplicate peaks).
- **Use of gradient orientation** (greatly reduces votes per point).
- **Probabilistic / randomized Hough**: vote with only a random subset of edge pixels → much faster, slight loss of accuracy.

### Strengths
- **Robust to noise and partial occlusion** — missing pixels just reduce peak height but do not destroy it.
- **Detects multiple instances** of the structure in one pass.
- **Embarrassingly parallel** over evidence points.
- Works on edge-like, sparse, or texture-less data.

### Weaknesses
- Memory explodes for high-DOF structures.
- Discretization artifacts: peaks may split between neighboring bins.
- Time scales with parameter-space size; for >3 dimensions becomes impractical without aggressive constraints.
- A single line drawn by many pixels can produce a very tall, broad peak that masks weaker nearby structures.

## Related Concepts
- [[hough-lines]]
- [[generalized-hough]]
- [[parameter-space]]
- [[RANSAC]]
