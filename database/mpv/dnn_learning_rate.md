---
id: mpv_042
course: Methods of Computer Vision
tags: [learning-rate, scheduling, warmup, LR-finder]
difficulty: 2
type: open
status: to_learn
---

# Question
**Deep Neural Nets.** How do you **select the learning rate**?

---
# Solution

## Why It Matters
The learning rate $\eta$ controls how big a step the optimizer takes along the gradient direction. It is empirically the **most important hyperparameter** for deep nets.

- $\eta$ too **small** → very slow convergence; the model may underfit within the training budget.
- $\eta$ too **large** → loss oscillates, diverges, or settles in a poor local minimum (NaNs are a common symptom).
- The optimal $\eta$ depends on architecture, batch size, optimizer, loss scale, and dataset.

## Practical Methods to Choose It

### 1. Default-Based Starting Point
- SGD with momentum on ResNet/ImageNet: $\eta_0 \approx 0.1$ with batch size 256, momentum 0.9, weight decay $10^{-4}$.
- Adam / AdamW: $\eta_0 \approx 10^{-3}$ for most tasks; $\eta_0 \approx 10^{-4}$ for fine-tuning pretrained transformers.
- Scale with batch size: **linear scaling rule** — doubling batch size doubles the LR (Goyal et al., 2017). Hold true up to ~8K batch; combine with warm-up.

### 2. Learning-Rate Range Test (Smith, 2017)
- Run a short training (a few hundred iterations) with $\eta$ increasing **exponentially** from $10^{-7}$ to e.g. $10$.
- Plot training loss vs. $\eta$ on log scale.
- Choose the LR where the loss decreases fastest — typically about one order of magnitude **below** the point where the loss diverges.
- Cheap (one short run) and very effective.

### 3. Grid / Coarse Search
- Try $\eta \in \{3 \times 10^{-1}, 10^{-1}, 3 \times 10^{-2}, 10^{-2}, \dots\}$, train for one to a few epochs, pick the best.
- Combine with the LR range test for refinement.

### 4. Adaptive Optimizers
- Adam / AdamW adapt the effective per-parameter LR using running gradient statistics. They are far less sensitive to the *initial* LR than plain SGD — a default of $10^{-3}$ "just works" for many tasks, allowing you to skip extensive search.

### 5. Use a Schedule, Not a Single Value
Modern training picks a *peak* LR (e.g., from the range test) and a *schedule* rather than a constant:
- **Warm-up** at the start (linear ramp from 0 to peak over a few epochs) — stabilizes large-batch training, prevents early divergence.
- **Step decay:** drop LR by 10× at fixed epochs (e.g., epoch 30, 60, 90 in ImageNet schedules).
- **Cosine annealing:** $\eta_t = \frac{1}{2}\eta_0 (1 + \cos(\pi t / T))$ — smooth decay; widely used, often without restart.
- **Cosine with restarts (SGDR):** periodic restarts can escape local minima.
- **One-cycle policy** (Smith): warm-up to a high LR, then cool down — fast training with strong regularization.
- **ReduceLROnPlateau:** divide LR by a factor when validation loss stalls — robust default for many small/medium datasets.
- **Polynomial decay**, **linear decay** — common in segmentation / detection.

## Diagnostic Signs of Bad LR
- Loss explodes (NaN, very large): LR is too high — divide by 3–10.
- Loss is stuck (no decrease over thousands of steps): LR is too low — multiply by 3–10.
- Loss zig-zags strongly: LR slightly too high; add momentum or warm-up.
- Training loss decreases but validation loss does not improve and grows after a while: not necessarily LR — could be overfitting; consider regularization (dropout, weight decay, augmentation) rather than LR change.

## Layer-Wise / Differential Learning Rates
For fine-tuning a pretrained network, use:
- Lower LR (e.g., 10×–100× smaller) for backbone layers (general features).
- Higher LR for the task head (random init).
- "Discriminative LR" / "frozen-then-unfreeze" schedules in transfer learning.

## Practical Recipe
1. Pick an optimizer (SGD+momentum for vision baselines; AdamW for transformers / NLP / robust default).
2. Use the **LR range test** to find a peak LR.
3. Use **warm-up + cosine annealing** with that peak.
4. Adjust if you see the symptoms above.

## Related Concepts
- [[SGD]]
- [[Adam]]
- [[LR-finder]]
- [[cosine-annealing]]
- [[warm-up]]
- [[one-cycle]]
