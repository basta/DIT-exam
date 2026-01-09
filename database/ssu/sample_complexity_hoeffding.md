---
id: 2016_ssu_001
course: Statistical Machine Learning
tags: [learning-theory, sample-complexity, hoeffding-bound, union-bound]
difficulty: 3
type: derivation
status: to_learn
---

# Question
(6p) We are given a set $\mathcal{H} = \{h_i: \mathcal{X} \to \{1, \dots, 100\} \mid i = 1, \dots, 1000\}$ containing 1000 strategies each predicting the human age $y \in \{1, \dots, 100\}$ from a facial image $x \in \mathcal{X}$. The quality of a single strategy is measured by the expected absolute deviation between the predicted age and the true age
$$ R^{\text{MAE}}(h) = \mathbb{E}_{(x,y)\sim p}(|y - h(x)|) $$
where the expectation is computed w.r.t. an unknown distribution $p(x, y)$. The empirical estimate of $R^{\text{MAE}}(h)$ reads
$$ R_{\mathcal{T}^m}(h) = \frac{1}{m} \sum_{j=1}^m |y^j - h(x^j)| $$
where $\mathcal{T}^m = \{(x^j, y^j) \in (\mathcal{X} \times \mathcal{Y}) \mid j = 1, \dots, m\}$ is a set of examples drawn from i.i.d. random variables with the distribution $p(x, y)$. 

What is the minimal number of training examples $m$ which guarantees that $R^{\text{MAE}}(h)$ is in the interval $[R_{\mathcal{T}^m}(h) - 1, R_{\mathcal{T}^m}(h) + 1]$ for every $h \in \mathcal{H}$ with probability at least 95%?

## Options
A) Open derivation
B) ...

---
# Solution
**Correct Answer:** $m \ge \frac{99^2}{2} \ln(40000) \approx 51929$

## Explanation
We need to bound the probability that the empirical risk deviates from the true risk by more than $\epsilon = 1$ for any hypothesis in $\mathcal{H}$.

### Steps / Derivation
1. **Identify the variables:**
   - Hypothesis space size: $|\mathcal{H}| = 1000$.
   - Confidence level: $1 - \delta = 0.95 \implies \delta = 0.05$.
   - Error tolerance: $\epsilon = 1$.
   - Range of the loss function: Since $y, h(x) \in \{1, \dots, 100\}$, the absolute difference $|y - h(x)|$ is in $[0, 99]$. Let $R = 99$.

2. **Apply Hoeffding's Inequality for a single hypothesis:**
   For a single $h$, the probability of deviation greater than $\epsilon$ is:
   $$ P(|R^{\text{MAE}}(h) - R_{\mathcal{T}^m}(h)| > \epsilon) \le 2 \exp\left(-\frac{2m\epsilon^2}{R^2}\right) $$

3. **Apply Union Bound over $\mathcal{H}$:**
   We want the condition to hold for *all* $h$, so we consider the probability that *at least one* $h$ fails:
   $$ P(\exists h \in \mathcal{H} : |R^{\text{MAE}}(h) - R_{\mathcal{T}^m}(h)| > \epsilon) \le \sum_{h \in \mathcal{H}} P(|R^{\text{MAE}}(h) - R_{\mathcal{T}^m}(h)| > \epsilon) $$
   $$ \le |\mathcal{H}| \cdot 2 \exp\left(-\frac{2m\epsilon^2}{R^2}\right) $$

4. **Set the bound to $\le \delta$ and solve for $m$:**
   $$ 2|\mathcal{H}| \exp\left(-\frac{2m\epsilon^2}{R^2}\right) \le \delta $$
   $$ \exp\left(-\frac{2m\epsilon^2}{R^2}\right) \le \frac{\delta}{2|\mathcal{H}|} $$
   $$ -\frac{2m\epsilon^2}{R^2} \le \ln\left(\frac{\delta}{2|\mathcal{H}|}\right) $$
   $$ \frac{2m\epsilon^2}{R^2} \ge \ln\left(\frac{2|\mathcal{H}|}{\delta}\right) $$
   $$ m \ge \frac{R^2}{2\epsilon^2} \ln\left(\frac{2|\mathcal{H}|}{\delta}\right) $$

5. **Substitute values:**
   $$ m \ge \frac{99^2}{2 \cdot 1^2} \ln\left(\frac{2 \cdot 1000}{0.05}\right) $$
   $$ m \ge \frac{9801}{2} \ln(40000) $$
   $$ \ln(40000) \approx 10.5966 $$
   $$ m \ge 4900.5 \cdot 10.5966 \approx 51928.8 $$
   
   So, we need at least **51929** examples.

## Related Concepts
- [[learning-theory]]
- [[hoeffding-bound]]
- [[union-bound]]
