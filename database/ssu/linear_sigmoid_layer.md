---
id: ssu_batch2_004
course: Statistical Machine Learning
tags: [neural-networks, backpropagation, logistic-sigmoid, linear-layer]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(4p) Define a neural module (layer) joining a linear layer and a logistic sigmoid layer, where the logistic sigmoid function is defined as:
$$ \sigma(s) = \frac{1}{1 + e^{-s}}. $$
Give the forward, backward and parameter messages.

---
# Solution
We define a module $f(x; w, b)$ which computes $y = \sigma(w^T x + b)$.
Let $x \in \mathbb{R}^n$ be the input, $w \in \mathbb{R}^n$ be the weight vector, and $b \in \mathbb{R}$ be the bias.
The forward operation consists of a linear part $s = w^T x + b$ and an activation part $y = \sigma(s)$.

## Forward Message
$$ s = w^T x + b $$
$$ y = \sigma(s) = \frac{1}{1 + e^{-(w^T x + b)}} $$

## Backward Message
Given the gradient of the loss with respect to the output, $\delta_y = \frac{\partial L}{\partial y}$, we compute the gradient w.r.t the input $x$.
First, derivatives of sigmoid: $\sigma'(s) = \sigma(s)(1 - \sigma(s)) = y(1-y)$.
$$ \frac{\partial L}{\partial x} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial s} \frac{\partial s}{\partial x} $$
$$ \frac{\partial y}{\partial s} = y(1-y) $$
$$ \frac{\partial s}{\partial x} = w $$
$$ \text{Backward (w.r.t input): } \delta_x = \delta_y \cdot y(1-y) \cdot w $$

## Parameter Message
We compute gradients w.r.t parameters $w$ and $b$.
$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial s} \frac{\partial s}{\partial w} $$
$$ \frac{\partial s}{\partial w} = x $$
$$ \text{Gradient w.r.t } w: \delta_w = \delta_y \cdot y(1-y) \cdot x $$

$$ \frac{\partial L}{\partial b} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial s} \frac{\partial s}{\partial b} $$
$$ \frac{\partial s}{\partial b} = 1 $$
$$ \text{Gradient w.r.t } b: \delta_b = \delta_y \cdot y(1-y) $$

## Related Concepts
- [[neural-networks]]
- [[backpropagation]]
- [[activation-function]]
