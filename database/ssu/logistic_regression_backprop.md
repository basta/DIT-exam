---
id: ssu_batch6_005
course: Statistical Machine Learning
tags: [neural-networks, logistic-regression, backpropagation, binary-cross-entropy, gradient-descent]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(6p) Consider the following simple neural network having $n$ inputs:
$$ \hat{y}(x, w) = \sigma \left( \sum_{i=1}^n w_i x_i \right), $$
where $\sigma$ is the logistic sigmoid function:
$$ \sigma(s) = \frac{1}{1+e^{-s}}. $$
The network is trained using Stochastic Gradient Descent where the training set can be described as $\mathcal{T}^m = \{(x^i, y^i) \in (\mathbb{R}^n \times \{0, 1\}) \mid i = 1, \dots, m\}$. The loss function is the binary cross-entropy:
$$ \ell(y, \hat{y}) = y \log \hat{y} + (1-y) \log(1-\hat{y}). $$
(1) Use the back-propagation algorithm and derive the gradient for a single sample:
$$ \nabla \ell(w) = \left( \frac{\partial \ell}{\partial w_1}, \dots, \frac{\partial \ell}{\partial w_n} \right). $$
(2) Reuse the neuron activity computed during the forward pass and simplify the result.

---
# Solution
## (1) Derivation
Let $s = \sum w_i x_i = w^T x$.
Then $\hat{y} = \sigma(s)$.
The loss is $\ell(y, \hat{y}) = y \log \hat{y} + (1-y) \log(1-\hat{y})$. (Note: Usually Cross Entropy is defined with a minus sign: $-[y \log \hat{y} + (1-y) \dots]$. The question omits the minus, maximizing likelihood instead of minimizing loss? Or just typo. I will assume the standard NEGATIVE Likelihood for loss, or derive gradient for this expression directly.
Given "Loss function", typically we minimize.
If $\ell = y \log \hat{y} + \dots$, then $\ell$ is maximized when $\hat{y}=y$.
Standard BCE loss: $L = - \ell$.
Let's differentiate the expression given:
$$ \frac{\partial \ell}{\partial \hat{y}} = \frac{y}{\hat{y}} - \frac{1-y}{1-\hat{y}} = \frac{y(1-\hat{y}) - (1-y)\hat{y}}{\hat{y}(1-\hat{y})} = \frac{y - \hat{y}}{\hat{y}(1-\hat{y})} $$

Derivative of sigmoid: $\sigma'(s) = \sigma(s)(1-\sigma(s)) = \hat{y}(1-\hat{y})$.

Chain rule:
$$ \frac{\partial \ell}{\partial w_j} = \frac{\partial \ell}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial s} \frac{\partial s}{\partial w_j} $$
$$ \frac{\partial \ell}{\partial w_j} = \left( \frac{y - \hat{y}}{\hat{y}(1-\hat{y})} \right) \cdot (\hat{y}(1-\hat{y})) \cdot x_j $$
$$ \frac{\partial \ell}{\partial w_j} = (y - \hat{y}) x_j $$

*Note:* If the loss was defined as $-\ell$ (standard minimization), the gradient would be $(\hat{y} - y)x_j$. Since the question defines $\ell$ as the quantity $y \log \hat{y} \dots$, maximizing this is equivalent to minimizing negative.
The gradient of the given expression is $(y - \hat{y}) x_j \cdot [1 \text{ or } -1]$.
Assuming standard Gradient Descent (minimization) on Negative Log Likelihood:
Gradient $g = (\hat{y} - y) x$.
Assuming Gradient Ascent (maximization) on the given Log Likelihood:
Gradient $g = (y - \hat{y}) x$.
The question asks for $\nabla \ell(w)$. So straight derivative is $(y - \hat{y}) x$.

## (2) Simplified Result
Using the activity $\hat{y}$ from forward pass:
$$ \nabla \ell(w) = (y - \hat{y}) x $$
(or $(\hat{y}-y)x$ depending on sign convention of loss).

## Related Concepts
- [[logistic-regression]]
- [[backpropagation]]
- [[gradient-descent]]
- [[binary-cross-entropy]]
