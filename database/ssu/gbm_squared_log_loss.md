---
id: ssu_batch3_005
course: Statistical Machine Learning
tags: [gradient-boosting, squared-logarithmic-loss, regression, pseudo-code]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(4p) Consider the squared logarithmic loss:
$$ \ell(y, h(x)) = (\log(1+y) - \log(1+h(x)))^2, $$
where $y$ is the target and $h(x)$ the output of the regression for input $x$. Give the pseudo code for the corresponding Gradient Boosting Machine using this loss and discuss differences to the squared loss GBM.

---
# Solution
## Gradient Boosting with Squared Logarithmic Loss

### Gradient Calculation
Let $\hat{y} = h(x)$.
$$ \ell(y, \hat{y}) = (\log(1+y) - \log(1+\hat{y}))^2 $$
Negative gradient w.r.t predictions (pseudo-residuals):
$$ r = -\frac{\partial \ell}{\partial \hat{y}} = -2 (\log(1+y) - \log(1+\hat{y})) \cdot \frac{\partial}{\partial \hat{y}}(-\log(1+\hat{y})) $$
$$ r = -2 (\log(1+y) - \log(1+\hat{y})) \cdot \frac{-1}{1+\hat{y}} $$
$$ r = \frac{2 (\log(1+y) - \log(1+\hat{y}))}{1+\hat{y}} $$

### Pseudo-code
**Input:** Training set $\mathcal{T} = \{(x_i, y_i)\}_{i=1}^m$.
**Initialize:** $f_0(x) = \arg\min_c \sum (\log(1+y_i) - \log(1+c))^2$. (Geometric mean-ish).
**For** $t = 1$ to $T$:
1. Compute pseudo-residuals for $i=1 \dots m$:
   $$ r_{it} = \frac{2 (\log(1+y_i) - \log(1+f_{t-1}(x_i)))}{1+f_{t-1}(x_i)} $$
2. Fit a weak learner $h_t(x)$ to $\{(x_i, r_{it})\}_{i=1}^m$ (usually minimizing squared error on residuals).
3. Find optimal step size $\gamma_t$ (via line search):
   $$ \gamma_t = \arg\min_\gamma \sum_{i=1}^m \ell(y_i, f_{t-1}(x_i) + \gamma h_t(x_i)) $$
4. Update:
   $$ f_t(x) = f_{t-1}(x) + \nu \gamma_t h_t(x) $$
**Output:** $f_T(x)$.

### Comparison to Squared Loss GBM
1.  **Use Case:** Squared Log Loss (MSLE) is generally used when the targets span several orders of magnitude and we care about relative errors rather than absolute errors. It penalizes under-predictions more than over-predictions (due to the log curve) but generally dampens the effect of large outliers compared to MSE.
2.  **Gradient:** The MSE gradient is simpler ($y - \hat{y}$). The MSLE gradient is scaled by $\frac{1}{1+\hat{y}}$, meaning updates are smaller for larger prediction values, preventing explosions for large targets.
3.  **Complexity:** Line search for optimal $\gamma$ is more complex than the analytic solution available for squared loss.

## Related Concepts
- [[gradient-boosting]]
- [[loss-functions]]
- [[regression]]
