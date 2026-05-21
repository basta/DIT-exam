---
id: mpv_043
course: Methods of Computer Vision
tags: [detection, proposals, RPN, YOLO, end-to-end]
difficulty: 4
type: open
status: to_learn
---

# Question
**Deep Neural Nets for detection.** **Proposal-based** and **end-to-end** methods. **Class label** and **bounding box** prediction.

---
# Solution

## Object Detection Problem
Output, for an image, a set of objects with both:
- **Class label** $c \in \{1, \dots, C\}$ (often plus a background class).
- **Bounding box** $(x, y, w, h)$ — position and size.

Each image can contain a variable number of objects → output is a **set**, not a fixed-size vector. Two main detector families address this differently.

## Proposal-Based (Two-Stage) Detectors
Classic recipe: first propose candidate object regions, then classify each candidate and refine its box.

### R-CNN (Girshick et al., 2014)
1. Generate ~2000 region proposals (Selective Search — class-agnostic external method).
2. For each proposal, warp to fixed size and run a CNN → feature vector.
3. Per-class linear SVMs classify each proposal.
4. Per-class bounding box regression refines the proposal.

### Fast R-CNN (2015)
- Single CNN forward pass per *image* (not per proposal).
- **RoI pooling** extracts a fixed-size feature for each proposal from the shared feature map.
- One network outputs both classification (softmax over $C+1$ classes) and bounding-box regression.

### Faster R-CNN (Ren et al., 2015)
- Replaces Selective Search with a learned **Region Proposal Network (RPN)**.
- RPN slides a small network over the shared feature map; at each spatial location it predicts, for $A$ anchor boxes (typically 9 = 3 scales × 3 aspect ratios):
  - **Objectness** (foreground vs. background).
  - **Anchor → proposal** bounding-box offsets $(t_x, t_y, t_w, t_h)$.
- Top-$K$ proposals (post NMS) are passed to a second-stage head:
  - Per-class softmax classification.
  - Per-class bbox refinement.
- **Mask R-CNN** adds an instance-segmentation head.

### Class & Box Prediction (Two-Stage)
- Classification head: softmax over $C+1$ logits per RoI → cross-entropy loss.
- Box-regression head: predicts $(t_x, t_y, t_w, t_h)$ that parameterize a *relative* offset from the anchor / proposal:
$$
\hat x = x_a + w_a t_x, \quad \hat w = w_a e^{t_w}, \dots
$$
Loss: smooth $L_1$ (Huber) on $(t_x, t_y, t_w, t_h)$, only for matched positives.

## End-to-End (One-Stage) Detectors
Predict class + box directly from a dense set of locations on a feature map, in a single forward pass — no separate proposal stage.

### Anchor-Based One-Stage
- **YOLO v1**: divide image into $S \times S$ cells; each cell predicts a fixed number of boxes + per-cell class probabilities.
- **YOLO v2–v5/v8, SSD**: predict at multiple scales using dense anchors / grid cells; per-anchor classification and box regression.
- **RetinaNet** (Lin et al.): one-stage detector with **Focal Loss** to handle the extreme foreground/background imbalance from dense anchors.
- Output per anchor: $C$ class scores + $(t_x, t_y, t_w, t_h)$.
- After NMS → final detections.

### Anchor-Free
- **FCOS, CenterNet, FoveaBox**: each pixel of the output map predicts a class score and 4 distances $(l, t, r, b)$ to the box sides — no anchors.
- Simpler design; competitive accuracy.

### Set-Prediction (Transformer-Based)
- **DETR** (Carion et al., 2020): a Transformer encoder-decoder consumes CNN features and produces a *fixed-size set* of object queries, each predicting class and box.
- Training uses **bipartite matching (Hungarian algorithm)** between predicted queries and ground-truth objects, then per-match cross-entropy + box regression (with GIoU loss).
- Removes NMS, anchors, and proposals entirely.
- Successors: **Deformable DETR, DINO, Co-DETR, RT-DETR** — faster convergence and higher accuracy.

## Class & Box Prediction (One-Stage)
- Per anchor / per pixel / per query: a vector of class logits (sigmoid for one-stage, since each anchor may match one class independently) + 4 box parameters.
- Classification losses: cross-entropy / sigmoid CE / focal loss.
- Box losses: smooth $L_1$, IoU loss, **GIoU**, **DIoU**, or **CIoU** — directly optimize overlap.

## Post-Processing
- **Non-Maximum Suppression (NMS)** removes near-duplicate boxes for the same object.
- **Soft-NMS**, **DIoU-NMS**: smoother alternatives.
- **DETR-style** detectors avoid NMS via set prediction + bipartite matching.

## Pros and Cons
| | Proposal-based | End-to-end (anchor-based) | DETR-style |
|---|---|---|---|
| Speed | slower (two stages) | fast (single pass) | moderate, query-based attention |
| Accuracy | usually highest at the same compute | competitive (RetinaNet, YOLOv8) | competitive, simpler pipeline |
| Pipeline complexity | several modules, anchors, NMS, RoI pooling | simpler, anchors + NMS | minimal post-processing, no anchors |
| Imbalance handling | sampling per stage | needs focal loss | bipartite matching |
| Small object recall | strong (RoIAlign + FPN) | weaker, mitigated by FPN | improving (Deformable DETR) |

## Modern Best Practices
- Multi-scale features via **Feature Pyramid Network (FPN)** in all families.
- **GIoU/DIoU/CIoU** losses for boxes.
- **Data augmentation**: mosaic, mix-up, copy-paste — strong gains.
- **Anchor-free** + **transformer-based** detectors dominate recent leaderboards but anchor-based YOLO variants remain the default in production due to speed and ecosystem.

## Related Concepts
- [[Faster-R-CNN]]
- [[RPN]]
- [[YOLO]]
- [[RetinaNet]]
- [[DETR]]
- [[focal-loss]]
- [[IoU-loss]]
