---
id: mpv_032
course: Methods of Computer Vision
tags: [tracking, good-features, shi-tomasi, aperture-problem]
difficulty: 3
type: open
status: to_learn
---

# Question
Which image patches are **suitable for tracking**? Why? Which patches are **not** suitable?

---
# Solution

## Tracking Setup (gradient methods like KLT / Lucas–Kanade)
For a patch $W$, the motion $(u, v)$ between consecutive frames is estimated by minimizing
$$
\sum_{\mathbf{x} \in W} \big[I_x u + I_y v + I_t\big]^2,
$$
giving the normal equations $M (u, v)^\top = -\mathbf{b}$ with
$$
M = \sum_W \begin{pmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{pmatrix}.
$$
The 2-D motion can be reliably recovered **iff $M$ is well-conditioned**.

## Shi–Tomasi Criterion: "Good Features to Track"
A patch is trackable iff
$$
\min(\lambda_1, \lambda_2) > \tau,
$$
where $\lambda_1 \ge \lambda_2$ are the eigenvalues of $M$ and $\tau$ is a noise-dependent threshold. Intuitively this requires *significant intensity variation in two different directions* within the patch.

## Categorization of Patches
Sketches:
```
(a) Flat region       (b) Edge              (c) Corner / Textured patch
+--------+            +--------+            +------+----+
|        |            |█       |            |    █ |█    |
|        |            |█       |            |    █████   |
|        |            |█       |            |  ████      |
+--------+            +--------+            +------+----+
λ1 ≈ λ2 ≈ 0           λ1 ≫ λ2 ≈ 0          λ1 ≈ λ2 ≫ 0
```

### (a) Uniform / Flat Patch — Not Suitable
- Both eigenvalues are near zero; $M$ is singular.
- No gradient information at all → motion completely undetermined.
- Result: the tracker drifts arbitrarily; estimated displacement is pure noise.

### (b) Edge — Partially Suitable
- One eigenvalue large (across the edge), one near zero (along the edge).
- The motion *across* the edge can be recovered, but motion *along* the edge cannot — the **aperture problem**.
- A patch on a long straight wire or a horizontal/vertical line is poorly suited to general 2-D tracking; it may suffice if the motion direction is known and matches the edge gradient.

### (c) Corner / Distinctive Texture — Suitable
- Both eigenvalues are large.
- Strong gradients in two different directions → unique 2-D solution.
- Typical examples: Harris/Shi–Tomasi corners, intersections, T-junctions, well-textured regions (e.g., brick walls, foliage).

## Other Properties of a Good Tracking Patch
- **High contrast** — strong gradient magnitude → favorable SNR.
- **Locally unique** — distinctive enough that the SSD/NCC error landscape has a clear minimum (no repetitive structure causing many local minima).
- **Stable structure over time** — not at object boundaries that change shape, not in regions with specular highlights, not in repetitive textures (fences) which alias under motion.
- **Not too small** — small patches are noisy; not too large — large patches violate the locally constant-motion assumption (homogeneous within a patch) and may straddle motion boundaries.

## Unsuitable Patches
- **Flat regions** (uniform sky, blank wall): no gradient.
- **1-D edges** (long straight lines): only one direction observable → aperture problem.
- **Repetitive textures** (regularly spaced fence rails, periodic floor tiles): many equally good matches → tracker can jump between candidates.
- **Occlusion / motion boundaries**: appearance changes drastically frame-to-frame.
- **Specular / saturated highlights**: violate brightness constancy.
- **Noise-dominated patches**: low contrast, sensor noise overwhelms the signal.

## Practical Use
The Shi–Tomasi (or Harris) detector is run once on the first frame to select trackable feature points; KLT then tracks them frame-to-frame. Lost / drifted features are periodically replaced by re-detection.

## Related Concepts
- [[shi-tomasi]]
- [[harris-corner]]
- [[KLT-tracker]]
- [[aperture-problem]]
