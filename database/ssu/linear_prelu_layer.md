---
id: ssu_batch3_006
course: Statistical Machine Learning
tags: [neural-networks, backpropagation, prelu, linear-layer]
difficulty: 3
type: derivation
status: to_learn
---

# Question
(5p) Define a neural module (layer) joining a linear layer and a PReLU (Parametric Rectified Linear Unit) layer. Give the forward, backward and parameter messages.
Consider $n$ inputs, $K$ units of the linear layer and $K$ units of the PReLU layer each processing the output of the corresponding unit of the preceding linear layer. Each PReLU unit applies the non-linearity $f(s) = \max(s, as)$, where $a \in \mathbb{R}$ is a trainable parameter.
*   The forward message is defined as a function of layer outputs w.r.t. its inputs.
*   The backward message is defined as the set of derivatives of all layer outputs w.r.t. all layer inputs.
*   Finally, the parameter message is defined as the set of derivatives of all layer outputs w.r.t. all layer parameters.

---
# Solution
We assume the question asks for derivatives of class loss $L$ using chain rule components provided by this layer, or just the Jacobian of the layer transformation itself. The phrasing "derivatives of all layer outputs w.r.t all layer inputs" suggests a Jacobian matrix or simply the backpropagation formulation. I will provide standard backprop messages.

**Definitions:**
Input $x \in \mathbb{R}^n$.
Weights $W \in \mathbb{R}^{K \times n}$. (Bias is typically included, let's assume $W$ includes bias or just weights).
Linear output: $s = Wx$.
PReLU Parameter $a$. (Typically shared or channel-wise. The problem says "$a \in \mathbb{R}$ is a trainable parameter", singular, so likely shared across the $K$ units, or one per unit? "Each PReLU unit applies... where a is...". Usually PReLU has one $a$ per channel. Let's assume one $a$ shared for simplicity, or denote $a_k$. The question says "where $a \in \mathbb{R}$", singular. I will assume single scalar $a$).

## Forward Message
$$ s_k = \sum_{j=1}^n W_{kj} x_j $$
$$ y_k = \max(s_k, a s_k) = \begin{cases} s_k & \text{if } s_k > 0 \\ a s_k & \text{if } s_k \le 0 \end{cases} $$

## Backward Message (Gradient w.r.t Input)
Given $\delta_y = \frac{\partial L}{\partial y}$, we want $\delta_x = \frac{\partial L}{\partial x}$.
$$ \frac{\partial L}{\partial x_j} = \sum_{k=1}^K \frac{\partial L}{\partial y_k} \frac{\partial y_k}{\partial s_k} \frac{\partial s_k}{\partial x_j} $$
$$ \frac{\partial y_k}{\partial s_k} = \begin{cases} 1 & \text{if } s_k > 0 \\ a & \text{if } s_k \le 0 \end{cases} $$
$$ \frac{\partial s_k}{\partial x_j} = W_{kj} $$
$$ \delta_{x,j} = \sum_{k=1}^K \delta_{y,k} \cdot \mathbb{I}(s_k > 0 \text{ or } a) \cdot W_{kj} $$
(Ideally written in vector form: $\delta_x = W^T (\delta_y \odot \mathbb{I}'(s, a))$ where $\mathbb{I}'$ is the derivative of PReLU).

## Parameter Message
**Gradient w.r.t $W$:**
$$ \frac{\partial L}{\partial W_{kj}} = \frac{\partial L}{\partial y_k} \frac{\partial y_k}{\partial s_k} \frac{\partial s_k}{\partial W_{kj}} $$
$$ \delta_{W, kj} = \delta_{y,k} \cdot \frac{\partial y_k}{\partial s_k} \cdot x_j $$

**Gradient w.r.t $a$:**
$$ \frac{\partial L}{\partial a} = \sum_{k=1}^K \frac{\partial L}{\partial y_k} \frac{\partial y_k}{\partial a} $$
$$ \frac{\partial y_k}{\partial a} = \begin{cases} 0 & \text{if } s_k > 0 \\ s_k & \text{if } s_k \le 0 \end{cases} $$
$$ \delta_a = \sum_{k=1}^K \delta_{y,k} \cdot \min(0, s_k) $$

## Related Concepts
- [[neural-networks]]
- [[activation-function]]
- [[backpropagation]]
- [[prelu]]
