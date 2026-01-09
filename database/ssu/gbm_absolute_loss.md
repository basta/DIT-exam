---
id: ssu_batch2_005
course: Statistical Machine Learning
tags: [gradient-boosting, absolute-loss, regression, pseudo-code]
difficulty: 3
type: derivation
status: to_learn
---

# Question
(4p) Consider the absolute difference loss $\ell(y, h(x)) = |y - h(x)|$. Give the pseudo code for a Gradient Boosting Machine using this loss and discuss differences to the squared loss GBM.

---
# Solution
## Gradient Boosting with Absolute Loss (L1)

The negative gradient of the loss function $\ell(y, \hat{y}) = |y - \hat{y}|$ with respect to the prediction $\hat{y}$ is:
$$ -g_i = -\frac{\partial \ell(y_i, \hat{y}_i)}{\partial \hat{y}_i} = \text{sign}(y_i - \hat{y}_i) $$
(The derivative is undefined at 0, usually taken as 0 or handled by subgradient).

### Pseudo-code
**Input:** Training set $\mathcal{T} = \{(x_i, y_i)\}_{i=1}^m$, number of iterations $T$, learning rate $\nu$.
**Initialize:** $f_0(x) = \text{median}(y_1, \dots, y_m)$. (Median minimizes sum of absolute deviations).
**For** $t = 1$ to $T$:
1. Compute "pseudo-residuals" (negative gradients):
   $$ r_{it} = \text{sign}(y_i - f_{t-1}(x_i)) \quad \text{for } i=1, \dots, m $$
2. Fit a weak learner (e.g., decision tree) $h_t(x)$ to the pseudo-residuals $\{(x_i, r_{it})\}_{i=1}^m$.
   (Usually, trees are fitted to minimize squared error on these residuals).
3. Compute the optimal step size (or leaf values) $\gamma_t$:
   For L1 loss, finding the optimal step for a leaf region $R_j$ means finding $\gamma_{tj}$ minimizing $\sum_{x_i \in R_j} |y_i - (f_{t-1}(x_i) + \gamma_{tj})|$. This is the **median** of the residuals $y_i - f_{t-1}(x_i)$ in that leaf.
   $$ \gamma_{tj} = \text{median}(\{y_i - f_{t-1}(x_i) \mid x_i \in R_{tj}\}) $$
4. Update model:
   $$ f_t(x) = f_{t-1}(x) + \nu \cdot \gamma_t h_t(x) $$
**Output:** $f_T(x)$.

## Comparison to Squared Loss GBM
1.  **Robustness to Outliers:**
    -   **L1 (Absolute) Loss:** The gradient is constant ($\pm 1$). Outliers with large errors do not dominate the gradient update. It is robust.
    -   **L2 (Squared) Loss:** The gradient is proportional to the residual ($y - \hat{y}$). Large errors (outliers) produce very large gradients, causing the model to focus heavily on fitting these points, which can lead to overfitting or instability.
2.  **Leaf Value Calculation:**
    -   **L1:** Requires computing the median of residuals in each leaf.
    -   **L2:** Requires computing the mean of residuals in each leaf.
3.  **Optimization:**
    -   L2 gradient is smooth and easy to optimize. L1 gradient is discontinuous at 0, but works well for robust regression.

## Related Concepts
- [[gradient-boosting]]
- [[loss-functions]]
- [[robust-regression]]
- [[decision-trees]]
