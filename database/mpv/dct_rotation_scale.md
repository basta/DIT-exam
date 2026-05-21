---
id: mpv_036
course: Methods of Computer Vision
tags: [correlation-filter, scale, rotation, log-polar, tracking]
difficulty: 4
type: open
status: to_learn
---

# Question
**DCT (Discriminative Correlation) tracking** in the presence of **rotation and scale change**.

---
# Solution

## Limitation of Basic DCF
A basic DCF tracker estimates **translation only**. Its filter is learned on a fixed-orientation, fixed-scale patch; large rotations or scale changes degrade the response map (peak shrinks or disappears) and cause drift.

## Handling Scale: Scale Search / Scale Filter
### (1) Brute-Force Scale Pyramid
- At each frame, after estimating translation, resample the target patch at $S$ scales ($s = a^k, k = -\lfloor S/2 \rfloor, \dots, \lfloor S/2 \rfloor$, $a \approx 1.02$).
- Apply the translation filter to each scaled patch; pick the scale with the highest peak response.
- Update the filter at the chosen scale.

### (2) DSST — Dedicated Scale Filter (Danelljan et al.)
- A separate **1-D correlation filter on a scale pyramid** is trained.
- The "patch" for the scale filter is a **vector of feature responses sampled from $S$ scale levels**; the target is a 1-D Gaussian peaked at the current scale.
- At test time, the scale filter is correlated with the new vector and the peak gives the new scale factor — all done with 1-D FFTs.
- Decouples translation and scale, much faster than running the 2-D filter $S$ times.

## Handling Rotation: Two Common Strategies
### (1) Log-Polar Sampling
- Resample a polar (or log-polar) window centered at the current object location: angle along one axis, radius (log-radius) along the other.
- **Rotation in Cartesian = translation in angular axis** of the log-polar map.
- **Scale change in Cartesian = translation in log-radius axis**.
- Apply a correlation filter in the log-polar space — the peak in the angular dimension is the rotation; the peak in the log-radius dimension is the scale. Same FFT-based machinery as DCT translation tracking.
- Recover the new orientation and scale, then update the appearance filter in Cartesian coordinates at the corrected pose.

### (2) Brute-Force Rotation Search
- Pre-rotate the search patch (or filter) over $R$ candidate angles ($r \cdot \Delta\theta$).
- Run the DCT detector for each angle; choose the angle with the largest peak.
- Simple, but $R$-fold cost.

### (3) Joint Translation/Rotation/Scale Filter
- Extend the feature representation to be invariant or covariant to small rotations (e.g., concatenate HOG channels at multiple orientations, or use rotation-equivariant CNN features).
- Run multiple correlation filters tuned to different orientations and pick the best.

## Combined Pipeline
1. **Detection (translation):** Run translation filter on the search window in the new frame → peak = new $(x, y)$.
2. **Scale:** Run scale filter (DSST) at the new $(x, y)$ → scale factor $s_t$.
3. **Rotation:** Sample log-polar window at $(x_t, y_t)$ with radius $\propto s_t$; correlate with the rotation filter → rotation angle $\theta_t$.
4. **Update appearance filter** in the new pose (rotate and rescale the search patch back to canonical pose before update).
5. **Failure handling:** monitor the **Peak-to-Sidelobe Ratio** (PSR) — sudden drops indicate occlusion / large appearance change; pause updating to avoid drift.

## Modern Extensions
- **CSR-DCF (Spatial Reliability):** masks out background pixels during filter learning, robust under occlusion.
- **CCOT / ECO (Danelljan):** continuous-domain DCFs with multi-resolution feature maps and CNN features.
- **DiMP, ATOM, KYS (deep DCF):** the filter is predicted by a small "filter-prediction" network; rotation and scale handled by a separate bounding-box regressor that is trained end-to-end. State-of-the-art accuracy.
- **End-to-end CNN trackers (SiamRPN++, OSTrack):** use anchor / transformer modules to predict rotation and scale directly; they have largely replaced classical DCT trackers in benchmarks while retaining the FFT correlation idea in the matching head.

## Related Concepts
- [[DSST]]
- [[CCOT]]
- [[ECO]]
- [[log-polar-transform]]
- [[rotation-equivariance]]
