---
id: ssu_batch5_006
course: Statistical Machine Learning
tags: [neural-networks, elu, backpropagation, activation-function]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(5p) Define a neural module (layer) joining a linear layer and an ELU (Exponential Linear Unit) layer. Give the forward, backward and parameter messages. Consider $n$ inputs, $K$ units of the linear layer and $K$ units of the ELU layer each processing the output of the corresponding unit of the preceding linear layer. Each ELU unit applies the non-linearity:
$$ f(x) = \begin{cases} x & \text{if } x > 0 \\ \exp(x) - 1 & \text{if } x \le 0 \end{cases} $$
*   The forward message is defined as a function of layer outputs w.r.t. its inputs.
*   The backward message is defined as the set of derivatives of all layer outputs w.r.t. all layer inputs.
*   Finally, the parameter message is defined as the set of derivatives of all layer outputs w.r.t. all layer parameters.

---
# Solution
We denote input $x \in \mathbb{R}^n$, weights $W \in \mathbb{R}^{K \times n}$.
Linear output: $s = Wx$.
Final output: $y = f(s)$ (element-wise).

## Forward Message
$$ s_k = \sum_{j=1}^n W_{kj} x_j $$
$$ y_k = \begin{cases} s_k & \text{if } s_k > 0 \\ \exp(s_k) - 1 & \text{if } s_k \le 0 \end{cases} $$

## Backward Message (Gradient w.r.t Input)
We want $\frac{\partial L}{\partial x}$. Let $\delta_y = \frac{\partial L}{\partial y}$.
$$ \frac{\partial y_k}{\partial s_k} = f'(s_k) = \begin{cases} 1 & \text{if } s_k > 0 \\ \exp(s_k) & \text{if } s_k \le 0 \end{cases} $$
Using chain rule:
$$ \frac{\partial L}{\partial x_j} = \sum_{k=1}^K \frac{\partial L}{\partial y_k} \frac{\partial y_k}{\partial s_k} \frac{\partial s_k}{\partial x_j} $$
$$ \delta_{x, j} = \sum_{k=1}^K \delta_{y, k} \cdot f'(s_k) \cdot W_{kj} $$
In vector form: $\delta_x = W^T (\delta_y \odot f'(s))$.

## Parameter Message (Gradient w.r.t Parameters)
$$ \frac{\partial L}{\partial W_{kj}} = \frac{\partial L}{\partial y_k} \frac{\partial y_k}{\partial s_k} \frac{\partial s_k}{\partial W_{kj}} $$
Since $\frac{\partial s_k}{\partial W_{kj}} = x_j$:
$$ \delta_{W, kj} = \delta_{y, k} \cdot f'(s_k) \cdot x_j $$

## Related Concepts
- [[neural-networks]]
- [[activation-function]]
- [[backpropagation]]
- [[elu]]
