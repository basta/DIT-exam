---
id: ssu_batch4_002
course: Statistical Machine Learning
tags: [model-selection, sample-complexity, hoeffding-bound, union-bound, validation-set]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(6p) Assume we are training a Convolution Neural Network (CNN) based classifier $h: \mathcal{X} \to \mathcal{Y}$ to predict a digit $y \in \mathcal{Y} = \{0, 1, \dots, 9\}$ from an image $x \in \mathcal{X}$. We train the CNN by the Stochastic Gradient Descent (SGD) algorithm using 100 epochs. After each epoch we save the current weights so that at the end of training we have a set $\mathcal{H} = \{h_i: \mathcal{X} \to \mathcal{Y} \mid i = 1, \dots, 100\}$ containing 100 CNN classifiers. The goal is to select the best CNN out of $\mathcal{H}$ that has the minimal classification error
$$ R(h) = \mathbb{E}_{(x, y) \sim p}(\mathbb{I}[y \neq h(x)]), $$
where the expectation is w.r.t. an unknown distribution $p(x, y)$ generating the data. Because $p(x, y)$ is unknown, we approximate $R(h)$ by the empirical risk
$$ R_{\mathcal{V}^m}(h) = \frac{1}{m} \sum_{i=1}^m \mathbb{I}[y^j \neq h(x^j)], $$
computed from a validation set $\mathcal{V}^m = \{(x^i, y^i) \in (\mathcal{X} \times \mathcal{Y}) \mid i = 1, \dots, m\}$ containing $m$ examples i.i.d. drawn from $p(x, y)$.

**a)** Define a method based on the Empirical Risk Minimization which uses $\mathcal{V}^m$ to select the best CNN out of a finite hypothesis class $\mathcal{H}$.

**b)** What is the minimal number of validation examples $m$ we need to collect in order to have a guarantee that $R(h)$ is in the interval $(R_{\mathcal{V}^m}(h) - 0.01, R_{\mathcal{V}^m}(h) + 0.01)$ for every $h \in \mathcal{H}$ with probability at least 95%?

---
# Solution

## a) Validation Set ERM
We calculate the empirical risk (classification error) for each of the stored hypothesis $h_i \in \mathcal{H}$ on the validation set $\mathcal{V}^m$.
$$ \hat{h} = \arg\min_{h \in \mathcal{H}} R_{\mathcal{V}^m}(h) = \arg\min_{h \in \mathcal{H}} \frac{1}{m} \sum_{j=1}^m \mathbb{I}[y^j \neq h(x^j)] $$
This strategy selects the model that performed best on the validation data.

## b) Sample Complexity
We want to guarantee:
$$ P(\exists h \in \mathcal{H} : |R(h) - R_{\mathcal{V}^m}(h)| \ge \varepsilon) \le \delta $$
Here $\varepsilon = 0.01$ and $1 - \delta = 0.95 \implies \delta = 0.05$.
The loss function is the 0/1 loss, which is bounded in $[0, 1]$.

1.  **Hoeffding's Inequality:**
    $$ P(|R(h) - R_{\mathcal{V}^m}(h)| \ge \varepsilon) \le 2 \exp(-2m\varepsilon^2) $$
    (Note: Range $R=1$, so divisor is $1^2 = 1$).

2.  **Union Bound:**
    $$ P(\text{failure}) \le |\mathcal{H}| \cdot 2 \exp(-2m\varepsilon^2) \le \delta $$

3.  **Solve for $m$:**
    $$ 2|\mathcal{H}| \exp(-2m\varepsilon^2) \le \delta $$
    $$ \exp(-2m\varepsilon^2) \le \frac{\delta}{2|\mathcal{H}|} $$
    $$ -2m\varepsilon^2 \le \ln\left( \frac{\delta}{2|\mathcal{H}|} \right) $$
    $$ m \ge \frac{1}{2\varepsilon^2} \ln\left( \frac{2|\mathcal{H}|}{\delta} \right) $$

4.  **Substitute Values:**
    $|\mathcal{H}| = 100$.
    $$ m \ge \frac{1}{2 \cdot (0.01)^2} \ln\left( \frac{200}{0.05} \right) $$
    $$ m \ge \frac{1}{0.0002} \ln(4000) $$
    $$ m \ge 5000 \cdot \ln(4000) $$
    $$ \ln(4000) \approx 8.294 $$
    $$ m \ge 5000 \cdot 8.294 = 41470 $$

    We need at least **41470** examples.

## Related Concepts
- [[model-selection]]
- [[empirical-risk-minimization]]
- [[sample-complexity]]
- [[hoeffding-bound]]
- [[union-bound]]
