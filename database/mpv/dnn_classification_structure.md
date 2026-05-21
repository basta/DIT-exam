---
id: mpv_040
course: Methods of Computer Vision
tags: [DNN, CNN, convolution, pooling, activation]
difficulty: 3
type: open
status: to_learn
---

# Question
**Deep Neural Nets for image classification.** Structure — **convolutional**, **pooling**, **fully connected** layers. **Non-linearities**.

---
# Solution

## Overall Architecture
A typical CNN for image classification stacks several convolutional blocks (each with non-linearity, optional pooling and normalization), followed by a small fully-connected classifier head:
$$
\text{Image} \to \big[\text{Conv} \to \text{BN} \to \text{ReLU} \to (\text{Pool})\big]^L \to \text{Flatten / GAP} \to \text{FC} \to \text{Softmax}.
$$

## Convolutional Layer
- A bank of $K$ learnable filters, each of size $k \times k \times C_{\text{in}}$, slides over the spatial dimensions of the input feature map.
- Output: $K$ channels (feature maps), one per filter.
- **Parameters:** $K$ filters times $k^2 C_{\text{in}}$ weights + $K$ biases. Much fewer than a fully-connected layer because of **weight sharing** (the same filter is applied at every spatial location).
- **Key properties:**
  - **Local connectivity:** each output depends only on a small spatial neighborhood (receptive field).
  - **Translation equivariance:** shifting the input shifts the output identically.
- **Stride** $s$: down-sampling factor; output spatial size is $\lfloor (H + 2p - k)/s \rfloor + 1$ with padding $p$.
- **Padding** keeps spatial size or shrinks it deliberately.
- Variants: dilated convolution (larger receptive field at no parameter cost), depthwise-separable convolution (MobileNet, fewer parameters), grouped convolution (ResNeXt), $1 \times 1$ convolution (cheap channel mixing).

## Pooling Layer
- Down-samples spatial dimensions; commonly $2 \times 2$ with stride 2.
- **Max pooling:** output is the max within each window — keeps strongest activation.
- **Average pooling:** mean over the window — more conservative.
- **Global Average Pooling (GAP):** average over the entire spatial map → one value per channel; used in modern architectures instead of a flatten+FC.
- **Purposes:** spatial dimensionality reduction, increase of receptive field, modest translation invariance.
- Strided convolution often *replaces* pooling in modern designs.

## Fully Connected (Dense) Layer
- Every input neuron connects to every output neuron: $\mathbf{y} = W \mathbf{x} + \mathbf{b}$.
- Used at the top of the network as the classifier head: maps the flattened feature vector (or GAP output) to $C$ class scores.
- Parameter-heavy; modern architectures (ResNet, MobileNet) often use only **one** FC layer after GAP to limit parameters.

## Non-Linearities (Activations)
- **ReLU**: $\max(0, x)$. Cheap, mitigates vanishing gradients (gradient is 1 in the positive regime), introduces sparsity. Standard default.
  - Drawback: **dying ReLU** problem (units stuck at zero output) — addressed by Leaky ReLU, PReLU, ELU, GELU.
- **Leaky ReLU** $\max(\alpha x, x)$, $\alpha = 0.01$: small slope on the negative side.
- **PReLU**: $\alpha$ is learnable.
- **ELU / SELU**: smooth on the negative side; can help with training dynamics.
- **GELU** $x \Phi(x)$ (Gaussian CDF): smooth, popular in Transformers.
- **Sigmoid / tanh**: historically used; both saturate (gradients vanish at the tails), used today only in specific places (gating, binary outputs).
- **Softmax** at the output layer: turns scores into a probability distribution over $C$ classes; paired with cross-entropy loss.

## Normalization Layers
Not in the original question but invariably present:
- **Batch Normalization:** normalize each channel over the batch + spatial dims, then learn a scale and shift; stabilizes training and allows larger learning rates.
- **LayerNorm / GroupNorm / InstanceNorm**: alternatives for small batches or generative tasks.

## Architectural Building Blocks
- **VGG**: stacks of $3 \times 3$ convs and $2 \times 2$ pools.
- **ResNet**: residual blocks with skip connections enabling very deep networks.
- **Inception / GoogLeNet**: parallel branches of different filter sizes.
- **DenseNet**: concatenative skip connections.
- **EfficientNet**: depthwise-separable + compound scaling.
- **Vision Transformers (ViT)**: replace conv blocks with self-attention over image patches; still use FC layers and softmax classifier at the end.

## Effective Receptive Field
Each conv layer adds locally; stacking many small convs (e.g., $L$ layers of $3 \times 3$) gives a receptive field of roughly $1 + 2L$ pixels, growing further with strided convs / pooling. By the classifier head, the receptive field typically covers the whole image.

## Related Concepts
- [[convolution]]
- [[batch-normalization]]
- [[ReLU]]
- [[ResNet]]
- [[receptive-field]]
