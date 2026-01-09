---
id: ssu_batch3_002
course: Statistical Machine Learning
tags: [empirical-risk-minimization, sample-complexity, hoeffding-bound, union-bound, model-selection]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(5p) We are given a set $\mathcal{H} = \{h_i: \mathcal{X} \to \{0, \dots, 100\} \mid i = 1, \dots, 100\}$ containing 100 Convolution Neural Networks, each being trained to predict a biological age $y \in \mathcal{Y} = \{0, \dots, 100\}$ from a facial image $x \in \mathcal{X}$. The goal is to select a CNN with the minimal expected absolute deviation between the predicted and the true age
$$ R(h) = \mathbb{E}_{(x,y)\sim p}(|y - h(x)|), $$
where the expectation is w.r.t. an unknown distribution $p(x, y)$ generating the images. Because $p(x, y)$ is unknown, we approximate $R(h)$ by the empirical risk
$$ R_{\mathcal{T}^m}(h) = \frac{1}{m} \sum_{i=1}^m |y^j - h(x^j)|, $$
computed from a set $\mathcal{T}^m = \{(x^i, y^i) \in (\mathcal{X} \times \mathcal{Y}) \mid i = 1, \dots, m\}$ containing $m$ examples i.i.d. drawn from $p(x, y)$.

**a)** Define a method based on the Empirical Risk Minimization which uses $\mathcal{T}^m$ to select the best CNN out of the given options $\mathcal{H}$.

**b)** What is the minimal number of the training examples $m$ we need to collect in order to have a guarantee that $R(h)$ is in the interval $(R_{\mathcal{T}^m}(h) - 1, R_{\mathcal{T}^m}(h) + 1)$ for every $h \in \mathcal{H}$ with probability at least 95%?

---
# Solution
## a) Empirical Risk Minimization (ERM)
The ERM method selects the hypothesis $\hat{h}$ from the set $\mathcal{H}$ that minimizes the empirical risk on the training set $\mathcal{T}^m$.
$$ \hat{h} = \arg\min_{h \in \mathcal{H}} R_{\mathcal{T}^m}(h) = \arg\min_{h \in \mathcal{H}} \frac{1}{m} \sum_{j=1}^m |y^j - h(x^j)| $$
(Note: $i$ and $j$ indices in the problem description for sums seem interchangeable, I used $j$ here to match the sum definition).

## b) Sample Complexity
We need to bound $P(\exists h \in \mathcal{H} : |R(h) - R_{\mathcal{T}^m}(h)| \ge \varepsilon) \le \delta$.
Here $\varepsilon = 1$ and target probability is $1 - \delta = 0.95 \implies \delta = 0.05$.
The random variable is the absolute loss $L = |y - h(x)|$. Since $y, h(x) \in \{0, \dots, 100\}$, the max loss is $M = 100$.

1.  **Hoeffding's Inequality for one $h$:**
    The loss takes values in $[0, 100]$.
    $$ P(|R(h) - R_{\mathcal{T}^m}(h)| \ge \varepsilon) \le 2 \exp\left( -\frac{2m\varepsilon^2}{M^2} \right) $$

2.  **Union Bound over $\mathcal{H}$:**
    Size of hypothesis class $|\mathcal{H}| = 100$.
    $$ P(\exists h \in \mathcal{H} : \dots) \le \sum_{h \in \mathcal{H}} P(\dots) \le 2|\mathcal{H}| \exp\left( -\frac{2m\varepsilon^2}{M^2} \right) $$

3.  **Solve for $m$:**
    $$ 2|\mathcal{H}| \exp\left( -\frac{2m\varepsilon^2}{M^2} \right) \le \delta $$
    $$ \exp\left( -\frac{2m\varepsilon^2}{M^2} \right) \le \frac{\delta}{2|\mathcal{H}|} $$
    $$ -\frac{2m\varepsilon^2}{M^2} \le \ln\left( \frac{\delta}{2|\mathcal{H}|} \right) $$
    $$ m \ge \frac{M^2}{2\varepsilon^2} \ln\left( \frac{2|\mathcal{H}|}{\delta} \right) $$

4.  **Substitute Values:**
    $M=100, \varepsilon=1, |\mathcal{H}|=100, \delta=0.05$.
    $$ m \ge \frac{100^2}{2 \cdot 1^2} \ln\left( \frac{2 \cdot 100}{0.05} \right) $$
    $$ m \ge 5000 \ln\left( \frac{200}{0.05} \right) = 5000 \ln(4000) $$
    $$ \ln(4000) \approx 8.294 $$
    $$ m \ge 5000 \cdot 8.294 = 41470 $$

    So we need at least **41470** examples.

## Related Concepts
- [[empirical-risk-minimization]]
- [[model-selection]]
- [[sample-complexity]]
- [[hoeffding-bound]]
- [[union-bound]]
