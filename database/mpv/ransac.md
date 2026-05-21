---
id: mpv_027
course: Methods of Computer Vision
tags: [RANSAC, robust-estimation, outliers, model-fitting]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the **RANSAC** algorithm, its properties, advantages and disadvantages. Which parameters it has?

---
# Solution

## Problem
Given a set of data points contaminated by outliers, robustly fit a parametric model (line, homography, fundamental matrix, …). Least squares is fatally sensitive to outliers; **RANSAC** (Random Sample Consensus, Fischler & Bolles, 1981) hypothesizes models from small random samples and keeps the one with the most support.

## Algorithm
Inputs: data set $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$, minimal sample size $s$ (e.g., 2 for a line, 4 for a homography, 7 or 8 for fundamental matrix), inlier threshold $\tau$, maximum iterations $T$.

Repeat for $t = 1, \dots, T$:
1. **Sample** $s$ data points uniformly at random.
2. **Fit** the model parameters $\theta_t$ from this minimal sample (closed-form when possible).
3. **Score** the model: count inliers — points whose residual under $\theta_t$ is below $\tau$:
$$
I_t = \{ i : r(x_i, \theta_t) < \tau \}.
$$
4. Keep $\theta_t$ if $|I_t|$ is larger than the current best.

After $T$ iterations, **refit** the model using least squares on the inliers of the best hypothesis (and optionally re-evaluate inliers).

## Adaptive Number of Iterations
To guarantee, with probability $\ge p$, that at least one all-inlier minimal sample is drawn:
$$
T = \frac{\log(1 - p)}{\log\!\left(1 - (1 - \varepsilon)^s\right)},
$$
where $\varepsilon$ is the (estimated) outlier ratio and $s$ is the minimal sample size. As we find better models we lower $\varepsilon$ and shrink $T$.

## Parameters
- **$s$:** minimal sample size (fixed by the model class).
- **$\tau$:** inlier threshold. Too small → throws away true inliers; too large → tolerates outliers. Often derived from noise standard deviation $\sigma$ (e.g., $\tau = 2\sigma$ or $3\sigma$, or from an asymptotic chi-square distribution of the residual).
- **$p$:** desired confidence (e.g., 0.99).
- **$T$:** maximum iterations (set adaptively or to a fixed cap).
- **Termination criterion:** stop early if a model with inlier ratio above a threshold is found.

## Properties
- **Robust to a large fraction of outliers** — works up to 50 % outliers easily, often beyond 70–80 %.
- **Probabilistic:** different runs can give different solutions; the success probability is controlled by $T$.
- **Non-parametric noise model** — inlier residuals must just be below a threshold; no Gaussian assumption.
- **Computationally efficient** for small $s$: drawing many samples is cheap, and minimal solvers are fast.

## Advantages
- Conceptually simple, easy to implement.
- Works for any model with a fast minimal solver.
- Tolerates very high outlier ratios (unlike least squares, M-estimators).
- Naturally handles structured outliers (e.g., epipolar geometry rejecting independently moving objects).

## Disadvantages
- **Stochastic** — solution depends on random samples (mitigated by running many iterations).
- The inlier threshold $\tau$ must be set carefully and is often application-specific.
- **Slow** for large $s$ (e.g., fundamental matrix with $s = 7$) or for very low inlier ratios — required $T$ explodes.
- May return a **degenerate** model fitted to a coincidental subset (planar scene fit by an essential matrix → degenerate). Variants (DEGENSAC) explicitly check for and recover from degeneracy.
- After the consensus step, the chosen model is fit from only $s$ points → noisy. A least-squares refit on inliers is standard; **LO-RANSAC** does multiple local optimization steps and significantly improves accuracy.

## Important Variants
- **MSAC / MLESAC:** instead of counting inliers, sum a robust cost over residuals — better accuracy, same complexity.
- **PROSAC:** sort matches by descriptor similarity and sample from the top first.
- **LO-RANSAC:** after each best update, run inner RANSAC iterations on inliers and refit.
- **MAGSAC / MAGSAC++:** marginalize over the inlier threshold instead of choosing one — sensitivity to $\tau$ removed.
- **GC-RANSAC:** use graph-cut for spatial consistency of inliers.

## Related Concepts
- [[robust-estimation]]
- [[LO-RANSAC]]
- [[MAGSAC]]
- [[outlier-rejection]]
