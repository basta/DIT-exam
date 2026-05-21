---
id: mpv_039
course: Methods of Computer Vision
tags: [hough-transform, RANSAC, robust-estimation, comparison]
difficulty: 3
type: open
status: to_learn
---

# Question
Compare the **Hough transformation** with **RANSAC**.

---
# Solution

## Common Goal
Both detect parametric structures (lines, circles, planes, homographies, …) in noisy data containing outliers. They are *robust* alternatives to least-squares fitting and arrive at the answer by very different means.

## Mechanisms
- **Hough.** Quantize the parameter space; each data point votes for all parameter values consistent with it. Detected models = maxima in the accumulator.
- **RANSAC.** Sample a minimal subset of data points uniformly at random; fit the model from the sample; count inliers. Repeat many times; keep the model with the most inliers.

## Comparison

| Aspect | Hough | RANSAC |
|---|---|---|
| Style | exhaustive voting in parameter space | random sampling in data space |
| Number of points used per hypothesis | one (votes from each individually) | minimal sample (e.g., 2 for line, 4 for homography) |
| Memory | $O(\prod B_i)$ — accumulator size grows with parameter dimensionality | $O(1)$ |
| Time | $O(N \cdot |\Theta(\mathbf{p})|)$; needs a fine enough accumulator | $O(T \cdot N)$, $T$ iterations from outlier ratio + confidence |
| Sensitivity to discretization | yes — accumulator binning affects accuracy and peak shape | no — parameters are continuous |
| Accuracy | limited by bin size; sub-bin refinement possible | high — model is fit from real data points (then refined on inliers) |
| Multiple instances | natural — multiple peaks in one pass | needs sequential RANSAC (remove inliers, repeat) |
| Scales to high-DOF parameter space | very poorly (memory + time explode) | well — only the *minimum sample size* and inlier ratio matter |
| Handles continuous noise distributions | implicit in bin size | explicit via inlier threshold $\tau$ |
| Termination | after going through all evidence | probabilistic stopping based on best inlier count |
| Output | accumulator + peaks | best model + inlier set |

## When Hough Wins
- Low-dimensional parameter space (2–3 DOF: lines, circles).
- The *number of models* to be detected is unknown and possibly large.
- Data is plentiful and one wants a single pass.
- Multi-instance detection in a single shot (e.g., many lines, many circles).
- Suitable for hardware acceleration (highly parallelizable voting).

## When RANSAC Wins
- High-dimensional models (homography 8-DOF, fundamental matrix 7-DOF, plane fits in 3-D scans).
- Continuous, noisy data where accumulator binning would be too coarse / too memory-heavy.
- A single model is sought (or models are extracted sequentially).
- Strong minimal solvers exist that give closed-form fits from a few points.

## Common Failure Modes
- **Hough**: spurious peaks from accumulator binning artifacts; quantization-induced peak splitting; memory blow-up for high-DOF.
- **RANSAC**: stochastic (different runs differ), inlier threshold $\tau$ must be set, degenerate samples can produce bad models (DEGENSAC fixes this), required iterations explode for very low inlier ratios + large $s$.

## Hybrid / Modern Variants
- **PROSAC** uses sorted match quality to sample better → fewer iterations.
- **MAGSAC** marginalizes over $\tau$ → no inlier-threshold tuning.
- **Random / Probabilistic Hough** uses only a random subset of points to vote → faster, less memory.
- For 2-D structures both can work; pipelines often **use Hough to seed candidates and RANSAC to refine** (e.g., detect approximate lines with Hough, then verify with RANSAC).

## Bottom Line
Both share the philosophy *"don't trust outliers"*. Hough is **deterministic** and **dense in parameter space**; RANSAC is **stochastic** and **dense in data space**. Choose Hough for low-DOF, multi-instance problems with plenty of evidence; choose RANSAC for higher-DOF problems with a small inlier set and a fast minimal solver.

## Related Concepts
- [[RANSAC]]
- [[hough-transform]]
- [[robust-estimation]]
- [[MAGSAC]]
