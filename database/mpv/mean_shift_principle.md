---
id: mpv_033
course: Methods of Computer Vision
tags: [mean-shift, mode-seeking, kernel-density, 1D-example]
difficulty: 3
type: open
status: to_learn
---

# Question
**Mean-shift algorithm.** Describe the principles and simulate calculation for a **1-D example**.

---
# Solution

## Principle
Mean-shift is a non-parametric iterative procedure for finding the **modes** (local maxima) of a kernel density estimate constructed from data points $\{\mathbf{x}_i\}_{i=1}^N$:
$$
\hat f(\mathbf{x}) = \frac{1}{N h^d} \sum_{i=1}^N K\!\left( \frac{\mathbf{x} - \mathbf{x}_i}{h} \right).
$$
Bandwidth $h > 0$ controls smoothness. For a symmetric kernel with profile $k$ ($K(\mathbf{u}) \propto k(\|\mathbf{u}\|^2)$), the gradient of $\hat f$ is proportional to the **mean-shift vector**
$$
\mathbf{m}(\mathbf{x}) = \frac{\sum_i \mathbf{x}_i \, g(\|(\mathbf{x} - \mathbf{x}_i)/h\|^2)}{\sum_i g(\|(\mathbf{x} - \mathbf{x}_i)/h\|^2)} - \mathbf{x}, \quad g = -k'.
$$
The iteration $\mathbf{x} \leftarrow \mathbf{x} + \mathbf{m}(\mathbf{x})$ is a gradient ascent on $\hat f$ with adaptive step size — it always moves toward a denser region and converges to a mode.

## Common Kernels
- **Flat (Epanechnikov-type) window:** $K(\mathbf{u}) = 1$ for $\|\mathbf{u}\| \le 1$, else 0 → mean-shift step = mean of all points within distance $h$ minus current position.
- **Gaussian:** $K(\mathbf{u}) \propto e^{-\|\mathbf{u}\|^2/2}$ → mean-shift step = Gaussian-weighted average minus current position.

## Algorithm
1. Initialize $\mathbf{x}$ (e.g., at every data point or on a grid).
2. Repeat:
   a. Compute weighted mean $\bar{\mathbf{x}} = \frac{\sum_i w_i \mathbf{x}_i}{\sum_i w_i}$, $w_i = g(\|(\mathbf{x} - \mathbf{x}_i)/h\|^2)$.
   b. Set $\mathbf{x} \leftarrow \bar{\mathbf{x}}$.
3. Stop when $\|\Delta \mathbf{x}\| < \epsilon$ — current position is a mode estimate.

Points converging to the same mode form a **cluster** (no $K$ to set in advance).

## 1-D Worked Example
Data: $X = \{1, 2, 3, 9, 10, 11\}$. Use a **flat kernel** with bandwidth $h = 2$ (include points within $\pm 2$ of the current position).

### Starting Point $x_0 = 1$
- Neighbors within $\pm 2$: $\{1, 2, 3\}$.
- Mean: $(1 + 2 + 3)/3 = 2$.
- Update: $x_1 = 2$.

### $x_1 = 2$
- Neighbors: $\{1, 2, 3\}$ (4 is outside the window).
- Mean: $2$. Converged. Mode 1 ≈ 2.

### Starting Point $x_0 = 9$
- Neighbors: $\{9, 10, 11\}$.
- Mean: $10$. Update $x_1 = 10$.
- Neighbors of $10$: $\{9, 10, 11\}$. Mean = 10. Converged. Mode 2 ≈ 10.

### Starting Point $x_0 = 6$ (in the gap)
- Neighbors within $\pm 2$ of 6: none of the data → empty window.
- A practical fix: if the window is empty, expand it slightly or leave the point unassigned (label as outlier).

Result: two clusters $\{1, 2, 3\}$ and $\{9, 10, 11\}$ around modes 2 and 10.

### With a Gaussian Kernel ($h = 2$)
Starting at $x_0 = 6$, weights are
$$
w_i \propto \exp\!\left(- (x_i - 6)^2 / (2 \cdot 4)\right),
$$
giving roughly $\{0.04, 0.14, 0.32, 0.32, 0.14, 0.04\}$ for $X = \{1, 2, 3, 9, 10, 11\}$ — symmetric, so the new $x \approx 6$. The point sits on a saddle/minimum between the two modes; the result depends on the noise direction at $x_0 = 6$. A small perturbation toward 3 sends it to mode ≈ 2; toward 9 sends it to mode ≈ 10.

## Properties
- No assumption about shape or number of modes.
- Bandwidth $h$ is crucial: too small → many spurious modes; too large → modes merge.
- Convergence is monotonic (for convex profiles).
- Cost per iteration $O(N)$, can be accelerated with KD-trees / locality-sensitive hashing.
- Widely used for **segmentation**, **tracking** (Mean-Shift / CamShift), **clustering** in arbitrary feature spaces.

## Related Concepts
- [[kernel-density-estimation]]
- [[mode-seeking]]
- [[mean-shift-tracking]]
- [[bandwidth-selection]]
