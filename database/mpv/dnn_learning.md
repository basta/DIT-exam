---
id: mpv_041
course: Methods of Computer Vision
tags: [DNN, SGD, cross-entropy, dropout, batch-normalization]
difficulty: 3
type: open
status: to_learn
---

# Question
**Deep Neural Nets for image classification.** Learning — the **cost function**, the **SGD** (stochastic gradient method), **drop-out**, **batch normalization**. SGD parameters.

---
# Solution

## Cost Function (Classification)
For a $C$-class classification problem with one-hot label $\mathbf{y}$ and predicted softmax probabilities $\hat{\mathbf{p}} = \text{softmax}(\mathbf{z})$:
$$
\mathcal{L}_{\text{CE}} = -\sum_{c=1}^{C} y_c \log \hat p_c = -\log \hat p_{c^*},
$$
where $c^*$ is the ground-truth class. This is the **cross-entropy** (a.k.a. negative log-likelihood) loss.

Training minimizes the **empirical risk** on the training set
$$
\mathcal{R}(\theta) = \frac{1}{N} \sum_{i=1}^N \mathcal{L}_{\text{CE}}(\hat{\mathbf{p}}_i(\theta), \mathbf{y}_i) + \lambda \, \Omega(\theta),
$$
where $\Omega$ is a regularizer (e.g., $L_2$ weight decay $\|\theta\|^2$).

Other common losses:
- **Label smoothing:** replace the hard one-hot by $(1 - \epsilon)$ on the true class and $\epsilon / (C - 1)$ on others — regularizes overconfident predictions.
- **Focal loss:** down-weights easy examples — useful for class imbalance.
- **Hinge / multi-class SVM loss:** alternative, less common in deep nets.

## Stochastic Gradient Descent (SGD)
Compute the gradient of the loss on a **mini-batch** of $B$ samples and update:
$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta_t; \mathcal{B}_t).
$$
Why mini-batch:
- **Lower variance** than single-example SGD.
- **GPU-friendly** parallelism.
- **Cheaper** than full-batch GD.

### Momentum
Maintain a velocity vector that averages past gradients:
$$
\mathbf{v}_{t+1} = \mu \mathbf{v}_t + \nabla \mathcal{L}, \qquad \theta_{t+1} = \theta_t - \eta \mathbf{v}_{t+1}.
$$
Momentum $\mu \approx 0.9$. Damps oscillations along high-curvature directions and accelerates along low-curvature directions; standard default.

### Adaptive Methods
- **Adam:** maintains per-parameter first- and second-moment estimates; effectively adapts the learning rate per parameter. Good default for many tasks.
- **AdamW:** decouples weight decay from the gradient step — typically better generalization than vanilla Adam.
- **RMSProp**, **AdaGrad**: predecessors.

## Drop-out
During training, randomly **zero out** each unit independently with probability $p$ (e.g., 0.5 for FC layers, 0.1–0.3 for conv layers, often *not* used after batch normalization):
$$
\tilde h_i = \frac{1}{1 - p} \mathbb{1}[\xi_i = 0] \cdot h_i, \quad \xi_i \sim \text{Bernoulli}(p).
$$
- Equivalent to training an ensemble of exponentially many sub-networks that share weights.
- Strong regularizer; prevents co-adaptation of units.
- At test time, the full network is used (with the $1/(1-p)$ scaling already absorbed during training in modern implementations).
- Variants: DropConnect (drop weights), DropBlock (drop spatial blocks in conv maps), Stochastic Depth (drop entire residual blocks).

## Batch Normalization (BN)
For each channel, normalize over the mini-batch + spatial dimensions and learn a per-channel scale $\gamma$ and shift $\beta$:
$$
\hat x = \frac{x - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}}, \quad y = \gamma \hat x + \beta.
$$
- **Stabilizes training**: keeps activations in a well-conditioned regime, allowing higher learning rates.
- **Acts as a regularizer**: the mini-batch noise from $\mu_{\mathcal{B}}, \sigma_{\mathcal{B}}$ slightly perturbs each example.
- At inference, replace batch statistics with running estimates accumulated during training.
- **Combines uneasily with small batches** → alternatives: GroupNorm, LayerNorm, SyncBN for multi-GPU training.

## SGD Parameters (Hyperparameters)
- **Learning rate $\eta$** — single most important. Common: $10^{-1}$ for ResNet/SGD with momentum on ImageNet, $10^{-3}$ for Adam. Often tuned with a schedule (see below).
- **Batch size $B$** — typically 32–4096 for vision. Larger batches → less gradient noise but require LR scaling and warm-up.
- **Momentum $\mu$** — usually 0.9.
- **Weight decay $\lambda$** — typically $10^{-4}$ for vision. Adds $\lambda \theta$ to the gradient.
- **Learning rate schedule:**
  - **Step decay** — divide $\eta$ by 10 at fixed epochs.
  - **Cosine annealing** — smooth decay to (near) 0.
  - **Warm-up** — linearly increase from 0 to target $\eta$ over the first few epochs (stabilizes large-batch training).
  - **One-cycle, polynomial decay** — alternatives.
- **Initialization** (technically not an SGD parameter but critical): He / Xavier initialization for the weights.
- **Gradient clipping** — caps $\|\nabla\|$ to prevent rare exploding updates.
- **Epochs** — how many passes through the data; modern CNNs: 90–300 epochs on ImageNet.

## Training Loop Summary
```
for epoch in 1..E:
  for each mini-batch B in dataset:
    augment / shuffle B
    forward pass -> compute L
    backward pass -> compute grad L
    optimizer step (SGD+momentum or Adam) with weight decay
    (optional) update BN running stats
  evaluate on validation; checkpoint best
  update LR schedule
```

## Related Concepts
- [[cross-entropy]]
- [[momentum]]
- [[Adam]]
- [[dropout]]
- [[batch-normalization]]
- [[weight-decay]]
