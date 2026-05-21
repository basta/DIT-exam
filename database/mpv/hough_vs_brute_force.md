---
id: mpv_038
course: Methods of Computer Vision
tags: [hough-transform, brute-force, comparison, complexity]
difficulty: 2
type: open
status: to_learn
---

# Question
Compare the **Hough transformation** with a **brute-force** search algorithm.

---
# Solution

## Setting
We want to detect instances of a parameterized structure (e.g., a line $\rho = x \cos\theta + y \sin\theta$) in an image with $N$ edge pixels. Parameter space is discretized into $|\Theta| = B$ bins.

## Brute-Force Search
For each hypothesis $\boldsymbol{\theta}$ in the discretized parameter space:
1. Evaluate the structure $S(\boldsymbol{\theta})$.
2. Count how many evidence points lie on (or near) $S(\boldsymbol{\theta})$.
3. Keep $\boldsymbol{\theta}$ if the count exceeds a threshold.

Cost: $O(B \cdot N)$ — every bin is tested against every point.

## Hough Transform
For each evidence point $\mathbf{p}$:
1. Cast votes into every parameter bin compatible with $\mathbf{p}$ (subset $\Theta(\mathbf{p}) \subseteq \Theta$).
2. After all points have voted, find the maxima of the accumulator.

Cost: $O(N \cdot |\Theta(\mathbf{p})|)$. For lines with $\rho = x\cos\theta + y\sin\theta$ and a 2-D accumulator with $B = B_\rho B_\theta$, the per-point work is just $B_\theta$ (one vote per $\theta$ slice) — independent of $B_\rho$. So
$$
\text{Hough cost} = O(N B_\theta) \ll O(N B_\rho B_\theta) = \text{brute-force cost}.
$$

## Comparison

| Aspect | Brute force | Hough |
|---|---|---|
| Inner loop | hypothesis → points | point → compatible hypotheses |
| Time complexity (lines) | $O(N B_\rho B_\theta)$ | $O(N B_\theta)$ |
| Memory | $O(1)$ (only counters per hypothesis) | $O(B_\rho B_\theta)$ (accumulator) |
| Parallelism | trivial over hypotheses | trivial over evidence points |
| Multi-instance | needs a loop over all hypotheses + NMS | natural: all maxima in one pass |
| Use of gradient orientation | restricts hypotheses per point but still loop over them | directly restricts the votes |
| Noise tolerance | good (counting inliers) | good (votes still accumulate) |
| Sub-pixel accuracy | possible by per-hypothesis optimization | possible by interpolating around accumulator peak |
| Memory scaling for high-DOF | excellent (no accumulator) | poor — accumulator grows as $\prod B_i$ |
| Time scaling for high-DOF | bad ($O(N \prod B_i)$) | only $O(N \cdot$ compatible-set size$)$ — usually much smaller |

## Intuition
- Brute force is "for each model, count supporters." Hough flips the order: "for each supporter, list compatible models." The flip pays off when each point is compatible with **far fewer** parameter values than the total number of hypotheses (the typical case: a point lies on a 1-D curve in 2-D parameter space).
- Hough trades time for memory: it needs an accumulator the size of the discretized parameter space, brute force does not.

## When to Prefer Which
- **Hough** is preferred for low-dimensional parameter spaces (2–3) with many points each compatible with only a 1-D curve in $\Theta$.
- **Brute force** can be acceptable when $B$ is small, when only one model is sought, or when memory is constrained.
- For high-dimensional or noisy problems, **RANSAC** generally outperforms both: it doesn't enumerate $\Theta$ at all but samples models from minimal data subsets.

## Related Concepts
- [[hough-transform]]
- [[RANSAC]]
- [[accumulator]]
- [[parameter-space]]
