---
id: mpv_003
course: Methods of Computer Vision
tags: [scale-selection, laplacian, scale-space, LoG]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the algorithm for the selection of interest point (region) scale using the **Laplacian**.

---
# Solution

## Idea (Lindeberg)
Build a scale space and pick, for each interest point, the scale at which a *normalized* differential operator attains a local extremum. The Laplacian-of-Gaussian (LoG) responds maximally to blob-like structures whose size matches the kernel scale, so its extrema in scale space give a characteristic scale of the underlying structure.

## Scale-Normalized Laplacian
The plain Laplacian decreases with scale because Gaussian smoothing reduces amplitude. To compare responses across scales we use the **$\gamma$-normalized Laplacian** (with $\gamma = 1$):
$$
\text{LoG}_{\text{norm}}(x, y; \sigma) = \sigma^2 \, \big( L_{xx}(x, y; \sigma) + L_{yy}(x, y; \sigma) \big),
$$
where $L(x, y; \sigma) = G(\sigma) * I$. The factor $\sigma^2$ compensates for amplitude decay so that maxima of $|\text{LoG}_{\text{norm}}|$ across $\sigma$ correspond to blobs.

## Algorithm
1. Build a discrete scale space $\sigma_n = \sigma_0 \, k^n$ (geometric progression, e.g., $k = 1.2$).
2. At each scale $\sigma_n$ compute $L(x, y; \sigma_n)$ and the normalized Laplacian
$$
\mathcal{L}(x, y; \sigma_n) = \sigma_n^2 |L_{xx} + L_{yy}|.
$$
3. For every candidate point $(x_0, y_0)$ (e.g., a Harris/Hessian point at *some* scale), evaluate $\mathcal{L}(x_0, y_0; \sigma_n)$ across $n$.
4. Select the scale $\sigma^*$ that gives a **local maximum** of $\mathcal{L}$ along the scale axis (require it to be larger than at $\sigma_{n-1}$ and $\sigma_{n+1}$).
5. Optionally refine $\sigma^*$ by quadratic interpolation around the discrete maximum.
6. Reject points whose maximum value is below a threshold or for which no clear maximum exists.

The selected $\sigma^*$ is the **characteristic scale** of the structure. The region radius is usually $r \approx 3\sigma^*$ for description.

## Properties
- Provides **scale covariance**: if the image is rescaled by $s$, $\sigma^*$ scales by $s$ as well.
- Same idea is at the heart of **Harris-Laplace**, **Hessian-Laplace**, and SIFT (which approximates LoG by Difference of Gaussians, DoG).

## Related Concepts
- [[scale-space]]
- [[LoG]]
- [[DoG]]
- [[harris-laplace]]
- [[hessian-laplace]]
