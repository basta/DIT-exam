---
id: ssu_batch2_001
course: Statistical Machine Learning
tags: [perceptron, multiclass-classification, kernel-methods, online-learning]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(7p) Consider a linear classifier $h: \mathcal{X} \to \mathcal{Y}$ assigning inputs $x \in \mathcal{X}$ to classes $\mathcal{Y} = \{1, \dots, Y\}$ based on the rule
$$ h(x; w_1, \dots, w_Y, b_1, \dots, b_Y) = \arg\max_{y \in \mathcal{Y}} (\langle \phi(x), w_y \rangle + b_y) \quad (1) $$
where $\phi: \mathcal{X} \to \mathbb{R}^n$ is a feature map and $(w_y \in \mathbb{R}^n, b_y \in \mathbb{R}), y \in \mathcal{Y}$, are parameters.

**a)** Let $\mathcal{T}^m = \{(x^j, y^j) \in (\mathcal{X} \times \mathcal{Y}) \mid j = 1, \dots, m\}$ be a set of training examples. Describe a variant of the Perceptron algorithm which finds the parameters $(w_y \in \mathbb{R}^n, b_y \in \mathbb{R}), y \in \mathcal{Y}$, such that the classifier (1) correctly predicts all examples from $\mathcal{T}^m$ provided such parameters exist.

**b)** Assume that you cannot evaluate the feature map $\phi(x)$ explicitly, however, you can evaluate a kernel function $k: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ such that $k(x, x') = \langle \phi(x), \phi(x') \rangle, \forall x, x' \in \mathcal{X}$. Show that you can still use the Perceptron algorithm to find a linear classifier (1) with zero training error and that you can evaluate this classifier on any $x \in \mathcal{X}$.
*Hint: Note that the parameter vectors $w_y, y \in \mathcal{Y}$, can be in each iteration of the Perceptron algorithm expressed as a linear combination of the inputs $\phi(x^j)$.*

---
# Solution

## a) Multi-class Perceptron Algorithm
Initialize $w_y = 0, b_y = 0$ for all $y \in \mathcal{Y}$.
Repeat until convergence (no mistakes made in a full pass over $\mathcal{T}^m$):
1. For each example $(x^j, y^j) \in \mathcal{T}^m$:
2. Predict $\hat{y} = \arg\max_{y \in \mathcal{Y}} (\langle \phi(x^j), w_y \rangle + b_y)$.
3. If $\hat{y} \neq y^j$:
   - Update weights for the correct class: 
     $$ w_{y^j} \leftarrow w_{y^j} + \phi(x^j) $$
     $$ b_{y^j} \leftarrow b_{y^j} + 1 $$
   - Update weights for the predicted (wrong) class:
     $$ w_{\hat{y}} \leftarrow w_{\hat{y}} - \phi(x^j) $$
     $$ b_{\hat{y}} \leftarrow b_{\hat{y}} - 1 $$
   - Leave other classes unchanged.

## b) Kernel Perceptron
Since the initial weights are zero and updates only add/subtract $\phi(x^j)$, each $w_y$ can be represented as:
$$ w_y = \sum_{j=1}^m \alpha_{y,j} \phi(x^j) $$
where $\alpha_{y,j}$ accounts for how many times $x^j$ was added to or subtracted from class $y$'s weight vector.

We can rewrite the dot product using the kernel trick:
$$ \langle \phi(x), w_y \rangle = \left\langle \phi(x), \sum_{j=1}^m \alpha_{y,j} \phi(x^j) \right\rangle = \sum_{j=1}^m \alpha_{y,j} \langle \phi(x), \phi(x^j) \rangle = \sum_{j=1}^m \alpha_{y,j} k(x, x^j) $$

**Algorithm with Kernels:**
Initialize $\alpha_{y,j} = 0$ and $b_y = 0$ for all $y \in \mathcal{Y}, j \in \{1,\dots,m\}$.
Repeat until convergence:
1. For each example $(x^j, y^j)$:
2. Compute scores for all $y$:
   $$ s_y = \sum_{k=1}^m \alpha_{y,k} k(x^j, x^k) + b_y $$
3. Predict $\hat{y} = \arg\max_{y \in \mathcal{Y}} s_y$.
4. If $\hat{y} \neq y^j$:
   - $\alpha_{y^j, j} \leftarrow \alpha_{y^j, j} + 1$
   - $b_{y^j} \leftarrow b_{y^j} + 1$
   - $\alpha_{\hat{y}, j} \leftarrow \alpha_{\hat{y}, j} - 1$
   - $b_{\hat{y}} \leftarrow b_{\hat{y}} - 1$

**Evaluation on new $x$:**
$$ h(x) = \arg\max_{y \in \mathcal{Y}} \left( \sum_{j=1}^m \alpha_{y,j} k(x, x^j) + b_y \right) $$
This allows evaluating the classifier using only kernel evaluations.

## Related Concepts
- [[perceptron]]
- [[kernel-methods]]
- [[multiclass-classification]]
- [[online-learning]]
