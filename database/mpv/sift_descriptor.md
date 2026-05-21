---
id: mpv_009
course: Methods of Computer Vision
tags: [SIFT, descriptor, gradient-histogram, invariance]
difficulty: 3
type: open
status: to_learn
---

# Question
The **SIFT descriptor**. Describe the algorithm and its properties.

---
# Solution

## Setting
Given a keypoint with location, characteristic scale $\sigma$, and dominant orientation $\theta$, the SIFT descriptor is computed on a normalized patch around it.

## Algorithm
1. **Normalization.** Take a square patch of side $\approx 12\sigma$ (covering a $4 \times 4$ grid of $3\sigma \times 3\sigma$ cells), centered on the keypoint, oriented along $\theta$, scaled to a canonical size (e.g., $16 \times 16$ pixels, or higher when keypoint scale is large).
2. **Gradients.** Compute gradient magnitude $m(x, y)$ and orientation $\phi(x, y)$ at every pixel of the normalized patch. The orientation is measured **relative to $\theta$** (rotation invariance).
3. **Spatial grid.** Partition the patch into $4 \times 4 = 16$ cells.
4. **Orientation histograms.** In each cell, build an **8-bin** orientation histogram (45° per bin). Each pixel contributes weight $m(x, y) \cdot w(x, y)$ where $w$ is a Gaussian centered at the keypoint with $\sigma_w = $ half the patch width. Use **trilinear interpolation** (in $x, y, \phi$) so a single pixel contributes fractionally to up to 8 neighboring histogram bins — this avoids quantization artifacts under small geometric perturbations.
5. **Concatenation.** Concatenate the 16 histograms → a $16 \times 8 = 128$-dimensional vector $\mathbf{d}$.
6. **Normalization (illumination invariance):**
   a. $\mathbf{d} \leftarrow \mathbf{d} / \|\mathbf{d}\|_2$ (handles linear contrast change).
   b. Clip components above $0.2$ (suppress the influence of any single large gradient, e.g., from non-linear illumination or 3D structure changes).
   c. Re-normalize: $\mathbf{d} \leftarrow \mathbf{d} / \|\mathbf{d}\|_2$.

## Properties
- **Dimension:** 128. Often stored as `uint8` (×512).
- **Invariances:**
  - Translation, scale, rotation (by construction of the canonical frame).
  - Affine illumination $I \to aI + b$ (gradients remove $b$, normalization removes $a$).
  - Partial affine geometry — spatial pooling tolerates small affine distortions (≈ 30° viewpoint).
- **Distinctiveness:** very high; designed so that matching by nearest neighbor + Lowe's ratio test gives very few false matches.
- **Speed:** moderate. On CPU, ~10 ms per image for a few thousand keypoints. Fast GPU and integer variants exist (SIFT, BRIEF/ORB are alternatives).
- **Robustness:** robust to noise, JPEG compression, modest 3D viewpoint changes.

## Comparison Notes
- **RootSIFT**: $L_1$-normalize then take element-wise square root — using the **Hellinger kernel** instead of $L_2$ gives a noticeable boost in retrieval and matching at zero cost.
- **PCA-SIFT**: project to $\approx 36$ dims via PCA learned on patches.

## Related Concepts
- [[orientation-histogram]]
- [[trilinear-interpolation]]
- [[RootSIFT]]
- [[descriptor-normalization]]
