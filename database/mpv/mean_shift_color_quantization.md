---
id: mpv_034
course: Methods of Computer Vision
tags: [mean-shift, color-quantization, RGB, clustering]
difficulty: 3
type: open
status: to_learn
---

# Question
**Mean-shift algorithm.** Color pixels $[R, G, B]$ represented in 3-D space. How can you reduce the color space into a **256-color space**?

---
# Solution

## Goal
Represent every pixel by one of (at most) 256 representative colors — an "indexed" / palettized image. Use mean-shift in the 3-D RGB (or Lab) feature space to discover natural color modes from the data itself rather than fixing a uniform grid.

## Approach: Mean-Shift Clustering in 3-D Color Space
1. **Treat each pixel's color as a 3-D point** $\mathbf{x}_i = (R_i, G_i, B_i) \in [0, 255]^3$ (or in normalized $[0, 1]^3$ or in Lab for perceptual uniformity).
2. **Choose a bandwidth $h$** (e.g., $h = 16$ in $[0, 255]^3$, or 8 in Lab — controls the granularity of the clusters).
3. **Run mean-shift from every (sub-sampled) pixel** until convergence; collect convergence points (modes).
4. **Merge nearby modes** (within $h$) to obtain the final palette $\{ \mathbf{c}_1, \dots, \mathbf{c}_M \}$.
5. **Assign each pixel** to the cluster of the mode it converged to → 1 byte per pixel index.

If $M > 256$, reduce by:
- Increasing $h$ and re-running (coarser modes).
- Merging the closest mode pairs greedily until $M \le 256$ (agglomerative post-processing).
- Discarding clusters with small population, reassigning their members to the nearest remaining mode.

If $M < 256$, simply use what you have — fewer entries waste table slots but cause no quality issue.

## Why Mean-Shift (Instead of $k$-means)?
- **Number of clusters is not fixed in advance** — useful when the natural number of colors in an image is unknown.
- **No initialization sensitivity** — every starting point converges to a unique mode (deterministic up to numerical precision).
- **Mode-seeking, not centroid-seeking**: discovers actual high-density colors in the image rather than abstract averages.
- Robust to outlier pixels (sparse colors).

## Practical Pipeline (256-Color Palette)
1. Convert image to a convenient color space (RGB or Lab). Lab gives perceptually better clustering.
2. Sub-sample pixels for speed (e.g., 5–10 % random sample, or one pixel per $8 \times 8$ block).
3. Optionally pre-quantize to a finer regular grid (e.g., $64^3$) to bin-count points → faster mean-shift on weighted bin centers.
4. Run mean-shift with chosen $h$.
5. Collect convergence points, merge to $M$ modes.
6. If $M > 256$: merge closest mode pairs until exactly 256.
7. Build the lookup table (palette).
8. Map every original pixel to the index of the nearest palette entry (NN search; can be done with a 3-D KD-tree or a precomputed $256^3$ LUT).

## Choice of Bandwidth
- Small $h$ → many small modes → many palette entries → image looks closer to original but more colors than wanted.
- Large $h$ → few coarse modes → cartoon-like / posterized appearance.
- Often chosen by iteration: try a value, count modes, adjust to land near 256.

## Comparison with $k$-means (Median-Cut)
- **$k$-means / median-cut** with $k = 256$ directly fixes the number of palette colors.
- **Mean-shift** discovers the structure first; matching 256 colors is an a-posteriori constraint.
- Mean-shift is more expensive ($O(N^2)$ or $O(NM)$ per iteration); $k$-means / median-cut is faster.
- For exact 256-color image quantization in practice, **median-cut** and **octree quantization** are more commonly used. Mean-shift is preferable when one wants the *natural* clustering of colors and the number of clusters is not pre-fixed.

## Related Concepts
- [[mean-shift]]
- [[color-quantization]]
- [[median-cut]]
- [[clustering]]
- [[k-means]]
