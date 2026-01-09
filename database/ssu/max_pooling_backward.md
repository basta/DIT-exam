---
id: ssu_batch4_004
course: Statistical Machine Learning
tags: [cnn, max-pooling, backpropagation, gradients]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(5p) Consider the Max Pooling layer which reduces the dimensionality of a two dimensional input. The forward message of max pooling is
$$ f_{kl}(\boldsymbol{x}) = \max_{(i, j) \in \Omega(k, l)} x_{ij}, \quad (2) $$
where $(i, j)$ denotes the coordinates of the input, $(k, l)$ denotes the coordinates of the output and $\Omega(k, l)$ is the set of input coordinates covered by the receptive field of the output $(k, l)$ as shown in Figure 1.
(Figure 1 shows a 2x2 max pooling with stride 2).

Derive the backward message $\frac{\partial f_{kl}}{\partial x_{ij}}$ of the layer.

---
# Solution
We want to compute the backward message, which generally refers to how the loss gradient propagates back to the inputs $x_{ij}$. However, the question asks for $\frac{\partial f_{kl}}{\partial x_{ij}}$, which is simply the local derivative (Jacobian element) of the output w.r.t the input.

Let $(i^*, j^*) = \arg\max_{(i, j) \in \Omega(k, l)} x_{ij}$.
Then:
$$ f_{kl}(\boldsymbol{x}) = x_{i^*j^*} $$

The derivative is:
$$ \frac{\partial f_{kl}}{\partial x_{ij}} = \begin{cases} 1 & \text{if } (i, j) = (i^*, j^*) \\ 0 & \text{otherwise} \end{cases} $$
Essentially, the gradient passes through only to the element that was the maximum. If there are multiple maximums, the gradient is usually split or passed to one of them (subgradient).

If the question implies the full backward pass message $\delta_{x, ij} = \sum_{k,l} \frac{\partial L}{\partial f_{kl}} \frac{\partial f_{kl}}{\partial x_{ij}}$:
$$ \delta_{x, ij} = \sum_{(k, l) : (i, j) \in \Omega(k, l)} \delta_{f, kl} \cdot \mathbb{I}[(i, j) = \arg\max_{(i',j') \in \Omega(k, l)} x_{i'j'}] $$
For non-overlapping covariance (stride = kernel size), each $(i, j)$ belongs to exactly one $\Omega(k, l)$. In that case:
$$ \delta_{x, ij} = \begin{cases} \delta_{f, kl} & \text{if } x_{ij} \text{ was the max in its window } \Omega(k, l) \\ 0 & \text{otherwise} \end{cases} $$

## Related Concepts
- [[neural-networks]]
- [[cnn]]
- [[max-pooling]]
- [[backpropagation]]
