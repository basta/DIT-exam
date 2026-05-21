---
id: mpv_011
course: Methods of Computer Vision
tags: [LBP, descriptor, binary-pattern, texture]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe **"Local Binary Patterns"-like descriptors**.

---
# Solution

## Local Binary Patterns (LBP)
For each pixel $c$ at intensity $I_c$, look at a circular neighborhood of $P$ pixels at radius $R$. Compare each neighbor $I_p$ to $I_c$ and produce a bit:
$$
b_p = \mathbb{1}[I_p \ge I_c], \quad p = 0, \dots, P-1.
$$
The bits form a $P$-bit binary number — the local pattern code:
$$
\text{LBP}_{P,R}(c) = \sum_{p=0}^{P-1} b_p \, 2^p.
$$
The full image descriptor is the **histogram of LBP codes** over the image (or region of interest), giving a $2^P$-dimensional feature.

## Properties
- **Invariant to monotonic intensity transforms** $I \to f(I)$ (only ordering matters).
- **Fast** (only comparisons + bit shifts); GPU-friendly.
- **Texture-oriented**, used extensively in face recognition (Ahonen), texture classification.

## Variants
- **Uniform LBP:** keep only codes with at most 2 transitions $0 \to 1$ or $1 \to 0$ (most natural texture patterns). Reduces the histogram from $2^P$ to $\binom{P}{2} + 2$ bins and improves robustness to noise.
- **Rotation-invariant LBP:** define the code as the lexicographically smallest cyclic shift.
- **Multiscale LBP:** concatenate histograms for several $(P, R)$.
- **Spatial LBP:** divide the image / region into a grid of cells, build per-cell histograms, concatenate (used in face recognition).

## Related Binary Descriptors
The "compare pixel pairs and produce a bit" idea is generalized in modern binary descriptors:
- **BRIEF:** $N$ (e.g., 256) pre-defined or learned **pixel-pair tests** $\mathbb{1}[I(p) < I(q)]$ over a smoothed patch. The descriptor is just the concatenation of the bits.
- **ORB:** BRIEF + steered by the patch orientation (rBRIEF) + Hamming distance matching + FAST keypoints.
- **BRISK / FREAK:** retina-like sampling pattern with pairs at different scales.
- **CENSUS transform:** like LBP but the result is treated as a bit-string (Hamming distance), used in stereo matching.

## Comparison & Matching
- **Distance:** Hamming distance, computable as `popcount(a XOR b)` — extremely fast on CPUs.
- **Memory:** 32–64 bytes per descriptor (vs. 128 floats / 512 bytes for SIFT).
- **Trade-off:** binary descriptors are faster and smaller but typically less discriminative than SIFT, especially under affine and severe illumination changes.

## Related Concepts
- [[BRIEF]]
- [[ORB]]
- [[census-transform]]
- [[hamming-distance]]
