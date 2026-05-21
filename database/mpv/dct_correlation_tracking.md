---
id: mpv_035
course: Methods of Computer Vision
tags: [DCT, correlation-filter, MOSSE, KCF, tracking]
difficulty: 4
type: open
status: to_learn
---

# Question
**DCT — discriminative (kernel) correlation tracking.** The algorithm, representation of the object, the search method.

---
# Solution

## Setup
Track a single object across frames given its initial bounding box. **Discriminative Correlation Filter (DCF)** trackers (MOSSE, KCF / DCF, CSR-DCF, DiMP) learn a linear filter that, when correlated with the search image, produces a peak at the object's location.

Note: "DCT" here refers to **Discriminative (Kernel) Correlation Tracking**, not Discrete Cosine Transform.

## Object Representation
- **Image patch** centered on the object, of size $W \times H$ (somewhat larger than the bounding box to include context).
- Multi-channel features per pixel: HOG, color names, raw grayscale, or learned CNN features (DeepDCF / DiMP).
- A **Gaussian-shaped desired response** $g(\mathbf{x})$ peaked at the patch center serves as the target output.
- A **cosine window** is multiplied onto the patch to attenuate boundary effects (since correlation is performed circularly via FFT, large boundary values create wraparound artifacts).

## Learning the Filter
Find filter $h$ minimizing the regularized squared error between $g$ and the circular correlation $f \star h$:
$$
\min_h \; \|f \star h - g\|^2 + \lambda \|h\|^2.
$$
By Parseval / convolution theorem, this is solved per frequency:
$$
\hat H = \frac{\hat G \odot \overline{\hat F}}{\hat F \odot \overline{\hat F} + \lambda},
$$
where $\hat \cdot$ denotes 2-D DFT, $\odot$ element-wise multiplication, $\overline{\cdot}$ complex conjugation. Cost: $O(WH \log WH)$, *not* $O((WH)^2)$ — this is the key speed advantage. For multi-channel features the formula generalizes to a sum over channels in the numerator and the denominator.

## Kernelized Correlation Filter (KCF)
Henriques et al. exploit the structure of **circulant matrices** of shifted patches to apply a non-linear kernel (e.g., Gaussian) at the same per-frequency cost. The dual filter $\alpha$ is obtained from
$$
\hat \alpha = \frac{\hat y}{\hat k^{xx} + \lambda},
$$
where $k^{xx}$ is the kernel correlation of $x$ with itself; both $\hat y$ (target) and $\hat k^{xx}$ are precomputable per frame.

## Search Method (Detection)
For frame $t$:
1. Crop a search patch from the new frame at the previous object position, same size $W \times H$ (or scaled — see below).
2. Extract features and apply the cosine window: $z$.
3. Compute the **response map** by correlating with the learned filter:
$$
r = \mathcal{F}^{-1}\!\left( \hat Z \odot \hat H \right) \quad \text{(linear)},
$$
or, in the kernelized case,
$$
r = \mathcal{F}^{-1}\!\left( \hat k^{xz} \odot \hat \alpha \right).
$$
4. The new object position is the **argmax** of $r$.
5. Optionally refine the peak by sub-pixel interpolation.

## Online Update
After estimating the new position, extract the new patch $x_t$ and update the filter:
$$
\hat F_t = (1 - \eta) \hat F_{t-1} + \eta \hat F(x_t), \quad \hat G_t = (1 - \eta) \hat G_{t-1} + \eta \hat G(x_t),
$$
giving $\hat H_t$ as the ratio. Learning rate $\eta \in [0.01, 0.1]$. Adaptive variants stop updating when the response peak is low (likely occlusion).

## Properties
- **Real time** (hundreds of FPS for grayscale + HOG) thanks to FFT-based learning and detection.
- **Discriminative**: the filter learns to suppress background that resembles the object — far more robust than template matching (NCC).
- **Limited search range** by patch size: needs multi-scale search and per-frame update.
- **Drift** when the object changes appearance fast or is occluded — mitigated by adaptive update rules, scale modules, and confidence-based gating.

## Related Concepts
- [[MOSSE]]
- [[KCF]]
- [[circulant-matrices]]
- [[FFT-correlation]]
- [[correlation-filter]]
