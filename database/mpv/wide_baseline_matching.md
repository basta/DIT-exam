---
id: mpv_001
course: Methods of Computer Vision
tags: [wide-baseline, matching, correspondences, pipeline]
difficulty: 3
type: open
status: to_learn
---

# Question
**Wide-baseline matching.** Describe the steps for obtaining correspondences between a pair of images, which are taken from different viewpoints.

---
# Solution

## Pipeline Overview
The goal is to find point correspondences between two images of the same scene captured from significantly different viewpoints (large baseline → strong perspective and scale changes, occlusions).

### 1. Detection of Interest Regions
Detect *covariant* local features (regions/keypoints) in both images independently. Detectors must be repeatable under viewpoint change:
- **Similarity-invariant:** Harris-Laplace, Hessian-Laplace, DoG (SIFT), FAST.
- **Affine-invariant:** Harris-Affine, Hessian-Affine, MSER.

### 2. Canonical Frame / Normalization
For each detected region, estimate a *local affine frame* (or at least a scale and dominant orientation) so the patch can be warped into a canonical reference. This makes subsequent description invariant to the modeled transformation.

### 3. Description
Compute a descriptor on the normalized patch:
- SIFT / RootSIFT, SURF, ORB (hand-crafted)
- HardNet, SOSNet, L2-Net (learned)

The descriptor should be discriminative and robust to remaining photometric/geometric nuisances.

### 4. Tentative Matching
Match descriptors between the two images:
- **Mutual nearest neighbors** (cross-check).
- **Lowe's ratio test:** keep matches with $d_1/d_2 < 0.8$, where $d_1, d_2$ are distances to the 1st and 2nd nearest neighbor — filters ambiguous matches.

### 5. Geometric Verification (Robust Estimation)
Tentative matches still contain outliers. Fit a geometric model with **RANSAC** (or LO-RANSAC, MAGSAC, DEGENSAC):
- **Homography** $H$ (planar scene or rotation-only camera).
- **Fundamental / essential matrix** $F, E$ (general 3D scene).

Inliers consistent with the model are the final correspondences.

### 6. (Optional) Refinement
- Re-estimate the model from all inliers (least squares / iterative).
- Guided matching: search for additional inliers around the current estimate.

## Key Points
- Detection + description must be (approximately) **covariant / invariant** under the expected transformation class.
- The combination *detector + descriptor + RANSAC* is the canonical "wide-baseline" pipeline introduced by Schaffalitzky & Zisserman / Matas et al.

## Related Concepts
- [[harris-affine]]
- [[hessian-affine]]
- [[MSER]]
- [[SIFT]]
- [[RANSAC]]
- [[fundamental-matrix]]
