---
id: ssu_batch2_002
course: Statistical Machine Learning
tags: [sample-complexity, hoeffding-bound, hamming-distance, structured-prediction]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(5p) Let $\mathcal{X}$ be a set of input observations and $\mathcal{Y} = A^n$ a set of sequences of length $n$ defined over a finite alphabet $A$. Let $h: \mathcal{X} \to \mathcal{Y}$ be a prediction rule that for each $x \in \mathcal{X}$ returns a sequence $h(x) = (h_1(x), \dots, h_n(x))$. Assume that we want to measure the prediction accuracy of $h(x)$ by the expected Hamming distance
$$ R(h) = \mathbb{E}_{(x, y_1, \dots, y_n) \sim p} \left( \sum_{i=1}^n \mathbb{I}[h_i(x) \neq y_i] \right) $$
where $p(x, y_1, \dots, y_n)$ is a p.d.f. defined over $\mathcal{X} \times \mathcal{Y}$. As the distribution $p(x, y_1, \dots, y_n)$ is unknown, we estimate $R(h)$ by the (empirical) test error
$$ R_{\mathcal{S}^l}(h) = \frac{1}{l} \sum_{j=1}^l \sum_{i=1}^n \mathbb{I}[y_i^j \neq h_i(x^j)], $$
where $\mathcal{S}^l = \{(x^j, y_1^j, \dots, y_n^j) \in (\mathcal{X} \times \mathcal{Y}) \mid j = 1, \dots, l\}$ is a set of examples drawn from i.i.d. random variables with the distribution $p(x, y_1, \dots, y_n)$. What is the minimal number of test examples $l$, which we need to collect in order to guarantee that $R(h)$ is in the interval $(R_{\mathcal{S}^l}(h) - \varepsilon, R_{\mathcal{S}^l}(h) + \varepsilon)$ with probability $\delta$ at least? Write $l$ as a function of $\varepsilon, n$ and $\delta$.

---
# Solution
We want to bound the probability that the empirical risk differs from the true risk by more than $\varepsilon$:
$$ P(|R(h) - R_{\mathcal{S}^l}(h)| \ge \varepsilon) \le 1 - \delta $$
Wait, the question asks for "probability $\delta$ at least" that it IS in the interval. So $P(|\dots| < \varepsilon) \ge \delta$. This means $P(|\dots| \ge \varepsilon) \le 1 - \delta$. Let's denote the failure probability as $\delta' = 1 - \delta$.

**1. Define Random Variables:**
Let $Z_j$ be the loss on the $j$-th example:
$$ Z_j = \sum_{i=1}^n \mathbb{I}[y_i^j \neq h_i(x^j)] $$
$Z_j$ are i.i.d. random variables.
The range of $Z_j$ is $[0, n]$ because the Hamming distance on length $n$ sequences is at most $n$.

**2. Scale to [0, 1]:**
Hoeffding's inequality applies to variables in $[0, 1]$. Let $Z'_j = \frac{Z_j}{n} \in [0, 1]$.
The expectation is $\mathbb{E}[Z'_j] = \frac{R(h)}{n}$.
The empirical mean is $\bar{Z}' = \frac{R_{\mathcal{S}^l}(h)}{n}$.

**3. Apply Hoeffding's Inequality:**
We want:
$$ P(|R(h) - R_{\mathcal{S}^l}(h)| \ge \varepsilon) = P\left( n \left| \frac{R(h)}{n} - \frac{R_{\mathcal{S}^l}(h)}{n} \right| \ge \varepsilon \right) $$
$$ = P\left( \left| \mathbb{E}[Z'] - \bar{Z}' \right| \ge \frac{\varepsilon}{n} \right) \le 2 \exp\left( -2l \left(\frac{\varepsilon}{n}\right)^2 \right) $$

**4. Solve for $l$:**
We want this probability to be at most $1 - \delta$:
$$ 2 \exp\left( -\frac{2l \varepsilon^2}{n^2} \right) \le 1 - \delta $$
$$ \exp\left( -\frac{2l \varepsilon^2}{n^2} \right) \le \frac{1 - \delta}{2} $$
$$ -\frac{2l \varepsilon^2}{n^2} \le \ln\left( \frac{1 - \delta}{2} \right) $$
$$ \frac{2l \varepsilon^2}{n^2} \ge \ln\left( \frac{2}{1 - \delta} \right) $$
$$ l \ge \frac{n^2}{2\varepsilon^2} \ln\left( \frac{2}{1 - \delta} \right) $$

**Answer:**
$$ l \ge \frac{n^2}{2\varepsilon^2} \ln\left( \frac{2}{1 - \delta} \right) $$

## Related Concepts
- [[hoeffding-bound]]
- [[sample-complexity]]
- [[hamming-distance]]
