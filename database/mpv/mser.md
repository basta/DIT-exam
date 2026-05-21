---
id: mpv_007
course: Methods of Computer Vision
tags: [MSER, extremal-regions, watershed, affine-invariance]
difficulty: 4
type: open
status: to_learn
---

# Question
Define **Maximally Stable Extremal Regions (MSER)**. Describe the algorithm for their detection. Properties of extremal regions and the maximally stable subset.

---
# Solution

## Extremal Regions
For a grayscale image $I: D \to \{0, \dots, 255\}$, an **extremal region** $R$ at threshold $t$ is a connected component of either
- $\{ \mathbf{x} : I(\mathbf{x}) \le t \}$ — *lower* extremal region (dark region), or
- $\{ \mathbf{x} : I(\mathbf{x}) \ge t \}$ — *upper* extremal region (bright region).

"Extremal" means every pixel inside $R$ is darker (or brighter) than every pixel on its outer boundary.

## Maximally Stable Extremal Regions
Consider a nested sequence $R_{t-\Delta} \subset R_t \subset R_{t+\Delta}$ of regions evolving with the threshold $t$. Define the *stability function*
$$
q(t) = \frac{|R_{t+\Delta} \setminus R_{t-\Delta}|}{|R_t|},
$$
i.e., the relative area change of the region over a threshold window of width $2\Delta$. A region is **maximally stable** at threshold $t^*$ if $q(t)$ has a **local minimum** there. Intuitively: the region's area barely changes when the threshold is perturbed — its boundary lies in a high-contrast image structure.

## Detection Algorithm (Matas et al., 2002)
1. **Sort pixels** by intensity (256 bins → bucket sort, linear time).
2. **Sweep threshold $t$** from 0 to 255 (for dark MSERs; reverse for bright).
3. Maintain a **union-find** of connected components: as each new pixel is added (in intensity order), union it with neighbors already added.
4. For each component, store its area as a function of $t$, building an **evolution tree** (component tree).
5. After the sweep, for every component traverse $|R_t|$ vs. $t$ and find local minima of $q(t)$ → maximally stable thresholds.
6. Apply a few filters: minimum area, maximum area, maximum $q$ (only sufficiently stable), and a *diversity* criterion to suppress overlapping near-duplicate MSERs.

Complexity: $O(n \log\log n)$ (Matas et al.) or $O(n)$ with appropriate union-find.

## Properties
- **Affine invariant** (intensity-monotonic + connected-component definition is preserved under affine warps of $D$).
- **Invariant to monotonic intensity transforms** $I \to f(I)$ with $f$ strictly increasing — much stronger than affine illumination invariance.
- **Multi-scale by construction**: a region's size is whatever the connected component is at the stable threshold — no scale parameter to tune.
- **Repeatable** under viewpoint change and illumination change; excellent on text, signs, and high-contrast blobs.
- **Limitations:** poor on blurred images (the level sets become unstable), on low-contrast / smoothly varying regions, and on textured natural scenes (too many small noisy components).

## Output for Matching
Each MSER is parameterized by fitting an ellipse to its second moment matrix → an affine-covariant region, then described by SIFT / RootSIFT etc.

## Related Concepts
- [[extremal-regions]]
- [[component-tree]]
- [[affine-invariant-detectors]]
