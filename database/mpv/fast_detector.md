---
id: mpv_008
course: Methods of Computer Vision
tags: [FAST, corner-detector, machine-learning, real-time]
difficulty: 2
type: open
status: to_learn
---

# Question
The **FAST** interest point detector.

---
# Solution

## Idea
**FAST** = **F**eatures from **A**ccelerated **S**egment **T**est. The detector looks at a discrete **Bresenham circle of 16 pixels** of radius 3 around the candidate pixel $p$, and declares $p$ a corner if there exist **$n$ contiguous pixels** on the circle that are all *significantly brighter* or all *significantly darker* than $p$ by a threshold $t$:
$$
p_i \ge I_p + t \quad \forall i \in S, \quad |S| \ge n, \quad S \text{ contiguous,}
$$
or
$$
p_i \le I_p - t \quad \forall i \in S, \quad |S| \ge n.
$$
Typical $n = 9$ (called FAST-9; original FAST-12 used $n = 12$).

## Speed-Up: High-Speed Test
Before the full test, examine pixels 1, 5, 9, 13 (top, right, bottom, left). For $n = 12$, at least 3 of these 4 must already pass the brightness condition — otherwise the pixel cannot be a corner. This rejects most non-corners after only 4 comparisons.

## Machine-Learned Decision Tree (Rosten & Drummond)
The full segment test has many redundant comparisons. Train an **ID3 decision tree** that:
- Inputs: ternary state of each of the 16 circle pixels (darker / similar / brighter).
- Output: corner / non-corner.
- Uses entropy (information gain) as the splitting criterion; trained on a labeled corner dataset.

The compiled tree gives the **minimum expected number of pixel queries** to classify a candidate. Runs at hundreds of FPS on a CPU.

## Non-Maximum Suppression
FAST produces many adjacent positive responses. Define a corner score
$$
V = \max\!\left( \sum_{i \in S_{\text{bright}}} |p_i - I_p| - t, \quad \sum_{i \in S_{\text{dark}}} |I_p - p_i| - t \right)
$$
and keep only local maxima of $V$.

## Properties
- **Very fast** — its primary advantage, used in real-time SLAM (ORB-SLAM), AR, tracking.
- **Not scale-invariant** by itself → typically wrapped in an image pyramid (ORB does this).
- **Not rotation-invariant by construction**, but the response is approximately so for $n \ge 9$.
- **Sensitive to noise**, since it relies on a fixed threshold $t$.
- **No information at multiple scales** unless combined with a pyramid + Harris score for ranking (ORB).

## Parameters
- $n$ — required arc length (commonly 9).
- $t$ — intensity threshold (controls density).
- NMS radius.

## Related Concepts
- [[ORB]]
- [[corner-detection]]
- [[real-time-vision]]
