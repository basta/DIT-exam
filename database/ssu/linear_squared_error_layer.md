---
id: 2016_ssu_004
course: Statistical Machine Learning
tags: [neural-networks, backpropagation, linear-layer, squared-error]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(4p) Define a module (layer) joining a linear layer and a squared error layer. Give the forward, backward and parameter messages.

---
# Solution
We define a module $f(x; w, y)$ which computes the squared error between a linear transformation of input $x$ and a target $y$.
Let $x \in \mathbb{R}^n$ be the input, $w \in \mathbb{R}^n$ be the weight vector (assuming bias is absorbed or ignored for simplicity, or we can treat $x$ as augmented), and $y \in \mathbb{R}$ be the target.
The operation is:
$$ z = \langle w, x \rangle $$
$$ L = (z - y)^2 $$
Combined: $L(x, y; w) = (\langle w, x \rangle - y)^2$.

## Forward Message
The forward pass computes the loss $L$ given inputs $x$, target $y$, and parameters $w$.
$$ \text{Forward: } L = (w^T x - y)^2 $$

## Backward Message
The backward pass computes the gradient of the loss with respect to the input $x$. This is needed if this module is part of a larger network and we need to propagate error to previous layers.
$$ \frac{\partial L}{\partial x} = \frac{\partial L}{\partial z} \frac{\partial z}{\partial x} $$
$$ \frac{\partial L}{\partial z} = 2(z - y) = 2(w^T x - y) $$
$$ \frac{\partial z}{\partial x} = w $$
$$ \text{Backward (w.r.t input): } \delta_x = \frac{\partial L}{\partial x} = 2(w^T x - y) w $$

## Parameter Message
The parameter message computes the gradient of the loss with respect to the parameters $w$, used for updating $w$ (e.g., in SGD).
$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \frac{\partial z}{\partial w} $$
$$ \frac{\partial z}{\partial w} = x $$
$$ \text{Parameter Gradient: } \delta_w = \frac{\partial L}{\partial w} = 2(w^T x - y) x $$

## Related Concepts
- [[neural-networks]]
- [[backpropagation]]
- [[gradient-descent]]
