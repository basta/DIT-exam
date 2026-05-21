---
id: mpv_028
course: Methods of Computer Vision
tags: [sliding-windows, detection, cascade, integral-image]
difficulty: 3
type: open
status: to_learn
---

# Question
Describe the steps for **object detection** using "sliding windows" ("scanning windows"). **How is the reasonable speed achieved?**

---
# Solution

## Idea
Slide a fixed-size window over the image at all positions and (multiple) scales. At each location, evaluate a binary classifier "object vs. background". Detections are positions where the classifier responds positively. The approach was historically very successful for face detection (Viola–Jones).

## Pipeline
1. **Training.**
   - Collect positive examples (object) and negative examples (background) at a fixed window size $W \times H$.
   - Extract features and train a classifier (HOG + linear SVM, Haar + AdaBoost, CNN sliding window, …).
2. **Image pyramid.** Resize the image at multiple scales $s = s_0, s_0 \cdot r, s_0 \cdot r^2, \dots$ to detect objects at different sizes with a fixed-size window.
3. **Scan.** At every scale and every $(x, y)$ position (often with stride $\Delta$), crop the window, compute features, run the classifier, record the score.
4. **Threshold.** Keep windows with score $\ge \theta$.
5. **Non-Maximum Suppression (NMS).** Multiple nearby windows fire on the same object → suppress overlapping detections, keeping the highest-scoring one (or a weighted average / soft-NMS).
6. **Output:** list of bounding boxes + class scores.

## Why Brute Force Is Slow
- Number of windows $\propto$ image area $\times$ number of scales $\times$ aspect ratios → $10^5$–$10^7$ windows per image.
- Most of them are trivially negative (sky, road, uniform background).
- Evaluating a strong classifier on each window is prohibitive.

## How Reasonable Speed Is Achieved

### 1. Cheap Features
- **Haar features** with the **integral image**: each Haar feature is computed in $O(1)$ once the integral image is built.
- **Integral image** allows constant-time computation of the **sum** and **variance** of intensities over any rectangle.
- **HOG** features can be sped up using integral images of histograms / block decomposition.

### 2. Cascade of Classifiers (Viola–Jones)
- Train a **cascade**: a sequence of classifiers $C_1, C_2, \dots, C_L$ of increasing complexity.
- A window is rejected as soon as any $C_l$ classifies it negative.
- Early stages are very fast (a handful of features) and reject >90 % of windows.
- Average evaluation cost per window is tiny because only the few windows that survive several stages pay the full cost.
- **Calibration**: each stage is tuned for very high recall (e.g., $\ge 99 \%$ of positives kept) and modest precision; the cascade as a whole achieves high precision and recall.

### 3. AdaBoost for Feature Selection
- AdaBoost chooses, in each round, the **single most informative weak classifier** (one Haar feature with threshold).
- The final boosted classifier is a weighted sum of a few hundred such features — very fast to evaluate.

### 4. Image-Pyramid Reuse
- Compute integral images once per scale; reuse across all windows at that scale.
- Pyramid construction can be done with cheap downsampling.

### 5. Stride / Skipping
- Use stride $\Delta > 1$ (e.g., 2 or 4 pixels) so the classifier is not evaluated at every pixel — typically without loss in detection rate.
- Search in a region of interest (e.g., for pedestrians, only on the ground plane).

### 6. Modern Variants
- **Feature pyramids on CNN feature maps** (FPN): one network forward pass produces multi-scale features and the classifier is applied densely with shared computation.
- **One-stage detectors (YOLO, SSD, RetinaNet)** are sliding-window detectors in spirit but implemented as a single CNN forward pass producing classification + box regression for a dense grid of anchor windows.
- **Two-stage detectors (R-CNN family)** start from a sparse set of *proposals* instead of every window, drastically reducing the number of evaluations.

## Summary
Sliding window = classifier evaluated on every position × scale + NMS. Speed comes from (a) **integral-image based cheap features**, (b) **cascaded classifiers** that reject easy negatives early, (c) **AdaBoost feature selection**, and (d) **shared computation** via CNN feature maps in modern detectors.

## Related Concepts
- [[viola-jones]]
- [[AdaBoost]]
- [[integral-image]]
- [[NMS]]
- [[anchor-detectors]]
