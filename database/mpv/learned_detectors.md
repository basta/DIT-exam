---
id: mpv_013
course: Methods of Computer Vision
tags: [learned-features, R2D2, SuperPoint, self-supervised]
difficulty: 4
type: open
status: to_learn
---

# Question
**Learning local feature detectors** — describe the possible loss functions (R2D2, SuperPoint) and training data sources.

---
# Solution

## Goals
A learned detector should output, for each pixel/region, two things:
- A **keypoint-ness / saliency** score — high at locations that are stable under viewpoint change.
- (Often) a **descriptor** — discriminative against negative patches.

A learned detector + descriptor must satisfy two desiderata:
1. **Repeatability**: the same physical point fires in two views of the same scene.
2. **Reliability / matchability**: among repeatable points, prefer those that can be matched with low ambiguity.

## SuperPoint (DeTone et al., 2018)
A single CNN with two heads sharing a backbone:
- **Detector head:** softmax over an $8 \times 8$ grid producing a heatmap of keypoint probability per cell (+ a "dustbin" no-keypoint class).
- **Descriptor head:** dense descriptor map (then bilinearly sampled at keypoint locations).

### Training
- **Homographic adaptation:** for each image, sample many random homographies, run a base detector ("MagicPoint" pre-trained on synthetic corners of polyhedra), warp predictions back, aggregate → *pseudo-ground-truth* keypoints.
- **Loss = detector loss + descriptor loss**
  - **Detector loss:** cross-entropy between predicted heatmap and pseudo-GT labels.
  - **Descriptor loss:** **contrastive (hinge) loss** between corresponding patches (positives) and non-corresponding patches (negatives) using known homographies between two synthetic warps of the same image.

### Training Data
- COCO images warped by random homographies (self-supervised; no human labels).

## R2D2 (Revaud et al., 2019)
A single CNN producing three dense maps:
- **Descriptor** $D(x, y) \in \mathbb{R}^{128}$.
- **Repeatability** $R(x, y) \in [0, 1]$.
- **Reliability** $W(x, y) \in [0, 1]$.

### Losses
1. **Repeatability loss** — cosine-similarity of $R$ maps from two views (after warping by GT homography) should be high; *plus* a local **peakiness** loss that encourages $R$ to peak rather than be flat (otherwise the trivial $R \equiv 1$ would win).
2. **Reliability loss** — uses **Average Precision** of patch matching as a *differentiable* objective: maximize AP of descriptors at locations weighted by $W$. The descriptor at $(x, y)$ should be matchable, and $W$ is a learned confidence in this matchability. Implemented with a soft AP loss (List-wise AP).
3. **Descriptor loss** — implicitly trained by the AP loss above (no separate triplet loss).

Final keypoints chosen as local maxima of $R \cdot W$.

### Training Data
- Web images, image pairs related by either known homographies (warp augmentation) or by **structure-from-motion** correspondences (Aachen dataset, SfM models that give pixelwise GT correspondences).
- Some experiments use optical-flow GT (Sintel) for dense correspondence supervision.

## Other Loss Families
- **Triplet / contrastive descriptor loss** with hard-negative mining (HardNet) — uses the *hardest negative in the batch* for each anchor-positive pair.
- **Detector-as-keypoint-set:** *KeyNet, D2-Net* — joint detection-description where peaks of a learned saliency map double as keypoints.
- **Reinforcement learning–style detectors** (e.g., LF-Net) — sample keypoints, train via STN-based differentiable warping and matching loss.

## Training Data Sources (Common)
- **Synthetic / warp-augmented** data — cheap and unlimited, but lacks 3D viewpoint diversity.
- **SfM reconstructions** — Aachen Day-Night, MegaDepth, ScanNet — give pixelwise / region correspondences from real 3D scenes.
- **Optical flow datasets** — Sintel, KITTI — dense correspondences but limited motion variety.
- **Stereo + depth (RGB-D)** — for indoor scenes.

## Related Concepts
- [[SuperPoint]]
- [[R2D2]]
- [[HardNet]]
- [[homographic-adaptation]]
- [[differentiable-AP]]
