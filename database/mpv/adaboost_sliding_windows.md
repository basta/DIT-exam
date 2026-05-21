---
id: mpv_030
course: Methods of Computer Vision
tags: [AdaBoost, sliding-windows, weak-classifier, viola-jones]
difficulty: 3
type: open
status: to_learn
---

# Question
Why is the **AdaBoost** algorithm often used for the "sliding window" methods? Give **more than one reason**.

---
# Solution

## Quick Recap: AdaBoost
AdaBoost builds a strong classifier $H(x) = \text{sign}\!\left(\sum_t \alpha_t h_t(x)\right)$ from many weak learners $h_t$ (slightly-better-than-chance binary classifiers). In each round, it picks the weak learner with the lowest weighted error on a re-weighted training set; weights of misclassified examples grow, forcing later rounds to focus on hard cases.

## Reasons AdaBoost Fits Sliding-Window Detection (Viola–Jones)

### 1. Built-in Feature Selection
Each round of AdaBoost chooses **one** weak learner — a single (Haar) feature with an optimal threshold — and discards the rest. The library of candidate Haar features for a $24 \times 24$ window contains $\sim 180,000$ features. AdaBoost automatically selects the few hundred most informative ones, producing a sparse classifier that is fast at test time.

### 2. Each Weak Classifier Is Extremely Cheap
A weak learner is just "**feature $f_i$ above / below threshold $\theta_i$?**" — a comparison after a constant-time integral-image evaluation. The strong classifier is a weighted sum of a handful of such comparisons, evaluated in microseconds per window.

### 3. Naturally Enables a Cascade
AdaBoost's score is a *sum* of weak learners. Truncating after $K$ rounds yields a valid (weaker) classifier — useful for cascading:
- Train short cascade stages (~ 1–20 features each) with very high recall (~99 %) and modest precision.
- Each stage rejects > 90 % of candidate windows.
- Average cost per window is dominated by the early stages → orders-of-magnitude speed-up.

### 4. Excellent Generalization Despite Many Features
Boosting has a **margin-maximizing** effect: even after training error is zero, additional rounds still improve test margin and generalization. With millions of windows to classify, this robustness matters.

### 5. Asymmetric / Cost-Sensitive Versions Match the Task
Most windows are background. Standard AdaBoost minimizes overall error, but variants (**AsymBoost**, **Cost-Sensitive AdaBoost**) allow penalizing false negatives more than false positives — exactly what is needed for high-recall cascade stages.

### 6. Robustness and Simplicity
- No hyperparameters beyond the number of rounds and the weak-learner family.
- Stable in practice; less sensitive to hyperparameter tuning than SVM kernels.
- Convergence behaviour well understood.

### 7. Mining Hard Negatives Naturally
AdaBoost's re-weighting concentrates effort on the hardest examples per round. Combined with **bootstrapping** (after each cascade stage, scan large image collections to harvest false-positive windows and add them to the training set), it produces robust detectors with a relatively small initial training set.

### 8. Output Score Calibration
The boosted score $\sum \alpha_t h_t(x)$ is monotonically related to the log-odds of the class — useful for adjustable thresholds and for cascade design.

## Summary
AdaBoost (combined with Haar features and integral images) was the Viola–Jones recipe because it (a) **selects features** automatically, (b) produces **very cheap evaluations**, (c) directly supports **cascading**, (d) generalizes well, and (e) can be made **asymmetric** to favor recall — exactly the requirements of sliding-window detection over millions of windows.

## Related Concepts
- [[viola-jones]]
- [[boosting]]
- [[cascade]]
- [[haar-features]]
- [[margin-theory]]
