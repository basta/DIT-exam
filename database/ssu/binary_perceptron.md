---
id: ssu_batch3_001
course: Statistical Machine Learning
tags: [perceptron, binary-classification, linear-classifier, online-learning]
difficulty: 2
type: derivation
status: to_learn
---

# Question
(3p) Consider a linear classifier $h: \mathcal{X} \to \mathcal{Y}$ assigning inputs $x \in \mathcal{X}$ into two classes $\mathcal{Y} = \{-1, +1\}$ based on the rule
$$ h(x; w, b) = \begin{cases} +1 & \text{if } \langle \phi(x), w \rangle + b \ge 0, \\ -1 & \text{if } \langle \phi(x), w \rangle + b < 0, \end{cases} \quad (1) $$
where $\phi: \mathcal{X} \to \mathbb{R}^n$ is a feature map and $(w, b) \in \mathbb{R}^{n+1}$ are parameters.
Let $\mathcal{T}^m = \{(x^j, y^j) \in (\mathcal{X} \times \mathcal{Y}) \mid j = 1, \dots, m\}$ be a set of training examples. Describe a variant of the Perceptron algorithm which finds the parameters $(w, b) \in \mathbb{R}^{n+1}$ so that the classifier (1) predicts all examples from $\mathcal{T}^m$ correctly provided such parameters exist.

---
# Solution
## Binary Perceptron Algorithm

**Input:** Training set $\mathcal{T}^m = \{(x^1, y^1), \dots, (x^m, y^m)\}$.
**Initialize:** $w = 0, b = 0$.
**Repeat** until no mistakes are made in a full pass through the training set:
1.  For each example $(x^j, y^j)$ in $\mathcal{T}^m$:
2.  Predict $\hat{y} = \text{sign}(\langle \phi(x^j), w \rangle + b)$.
    (Convention: $\text{sign}(z) = +1$ if $z \ge 0$, else $-1$).
3.  If $\hat{y} \neq y^j$:
    -   Update weights:
        $$ w \leftarrow w + y^j \phi(x^j) $$
        $$ b \leftarrow b + y^j $$

**Output:** Parameters $w, b$.

Note: The update rule works because if $y^j = +1$ and we predicted $-1$, we need to increase the score $\langle w, \phi(x) \rangle + b$, so we add $\phi(x)$. If $y^j = -1$ and we predicted $+1$, we need to decrease the score, so we subtract $\phi(x)$ (which is adding $y^j \phi(x)$).

## Related Concepts
- [[perceptron]]
- [[linear-classifier]]
- [[binary-classification]]
- [[margin]]
