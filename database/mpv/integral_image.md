---
id: mpv_029
course: Methods of Computer Vision
tags: [integral-image, summed-area-table, variance, viola-jones]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe how to use an **integral image** for computing the **sum of the intensity** and the **intensity variance** for a rectangular region.

---
# Solution

## Integral Image (Summed-Area Table)
Define
$$
S(x, y) = \sum_{x' \le x, \; y' \le y} I(x', y').
$$
$S$ can be built in **a single pass** with the recurrence
$$
S(x, y) = I(x, y) + S(x-1, y) + S(x, y-1) - S(x-1, y-1),
$$
with $S(x, y) = 0$ if $x < 0$ or $y < 0$. Cost: $O(WH)$ time, $O(WH)$ memory.

## Rectangle Sum in $O(1)$
For a rectangle with top-left $(x_0+1, y_0+1)$ and bottom-right $(x_1, y_1)$ (inclusive):
$$
\sum_{x=x_0+1}^{x_1} \sum_{y=y_0+1}^{y_1} I(x, y) = S(x_1, y_1) - S(x_0, y_1) - S(x_1, y_0) + S(x_0, y_0).
$$
Four memory accesses and three additions/subtractions — independent of rectangle area.

## Rectangle **Variance** in $O(1)$
The variance is
$$
\sigma^2 = \frac{1}{n} \sum_{(x, y) \in R} I(x, y)^2 - \left( \frac{1}{n} \sum_{(x, y) \in R} I(x, y) \right)^2,
$$
where $n = |R|$ is the number of pixels in the rectangle.

Build a **second integral image** of squared intensities:
$$
S_2(x, y) = \sum_{x' \le x, y' \le y} I(x', y')^2.
$$
Same recurrence as $S$ but on $I^2$.

Then both required sums can be obtained in $O(1)$:
$$
\Sigma = \sum_R I = S(x_1, y_1) - S(x_0, y_1) - S(x_1, y_0) + S(x_0, y_0),
$$
$$
\Sigma_2 = \sum_R I^2 = S_2(x_1, y_1) - S_2(x_0, y_1) - S_2(x_1, y_0) + S_2(x_0, y_0).
$$
Variance:
$$
\sigma^2 = \frac{\Sigma_2}{n} - \left(\frac{\Sigma}{n}\right)^2.
$$

## Why It Matters
- **Haar-like features** are differences of sums over rectangles → constant-time per feature using $S$.
- **Window normalization** in Viola–Jones uses $\sigma$ to normalize the contrast of each window before classification (handles brightness/contrast variation).
- **LBP / texture features**, integral histograms generalize this to histogram bins.
- Useful for fast box filters, mean/variance maps, and adaptive thresholding.

## Numerical Notes
- $S$ and $S_2$ grow with image area; for $W \times H$ images up to $\sim 10^4 \times 10^4$, `int64` (or `float64` if intensities are floats) is safer than `int32`.
- $S$ is exact for integer intensities; $\sigma^2$ can become slightly negative due to cancellation — clip at zero before $\sqrt{\cdot}$.

## Related Concepts
- [[summed-area-table]]
- [[viola-jones]]
- [[haar-features]]
- [[integral-histogram]]
