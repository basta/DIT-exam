---
id: ssu_batch5_001
course: Statistical Machine Learning
tags: [sample-complexity, hoeffding-bound, hamming-distance, numerical-calculation]
difficulty: 4
type: derivation
status: to_learn
---

# Question
(6p) Let $\mathcal{X}$ be a set of input observations and $\mathcal{Y} = A^n$ a set of sequences of length $n$ defined over a finite alphabet $A$. Let $h: \mathcal{X} \to \mathcal{Y}$ be a prediction rule that for each $x \in \mathcal{X}$ returns a sequence $h(x) = (h_1(x), \dots, h_n(x))$. Assume that we want to measure the prediction accuracy of $h(x)$ by the expected Hamming distance
$$ R(h) = \mathbb{E}_{(x, y_1, \dots, y_n) \sim p} \left( \sum_{i=1}^n \mathbb{I}[h_i(x) \neq y_i] \right) $$
where $p(x, y_1, \dots, y_n)$ is a p.d.f. defined over $\mathcal{X} \times \mathcal{Y}$. As the distribution $p(x, y_1, \dots, y_n)$ is unknown, we estimate $R(h)$ by the test error
$$ R_{\mathcal{S}^l}(h) = \frac{1}{l} \sum_{j=1}^l \sum_{i=1}^n \mathbb{I}[y_i^j \neq h_i(x^j)] $$
where $\mathcal{S}^l = \{(x^j, y_1^j, \dots, y_n^j) \in (\mathcal{X} \times \mathcal{Y}) \mid j = 1, \dots, l\}$ is a set of examples drawn from i.i.d. random variables with the distribution $p(x, y_1, \dots, y_n)$.

**a)** Assume that the sequence length is $n = 10$ and that we compute the test error from $l = 1000$ examples. What is the minimal probability that $R(h)$ will be in the interval $(R_{\mathcal{S}^l}(h) - 1, R_{\mathcal{S}^l}(h) + 1)$?

**b)** What is the minimal number of the test examples $l$ which we need to collect in order to guarantee that $R(h)$ is in the interval $(R_{\mathcal{S}^l}(h) - \varepsilon, R_{\mathcal{S}^l}(h) + \varepsilon)$ with probability $\gamma$ at least? Write $l$ as a function of $\varepsilon, n$ and $\gamma$.

---
# Solution
## b) General Formula derivation (same as previous assignment)
We want $P(|R(h) - R_{\mathcal{S}^l}(h)| \ge \varepsilon) \le 1 - \gamma$.
Variable $Z_j = \sum_{i=1}^n \mathbb{I}[h_i(x^j) \neq y_i^j] \in [0, n]$.
Hoeffding bound:
$$ P\left( \left| \frac{1}{l}\sum Z_j - \mathbb{E}[Z] \right| \ge \varepsilon \right) \le 2 \exp\left( -\frac{2 l \varepsilon^2}{n^2} \right) $$
Setting LHS to $1 - \gamma$:
$$ 2 \exp\left( -\frac{2 l \varepsilon^2}{n^2} \right) \le 1 - \gamma $$
$$ l \ge \frac{n^2}{2\varepsilon^2} \ln\left( \frac{2}{1-\gamma} \right) $$
So for (b), the answer is $l \ge \frac{n^2}{2\varepsilon^2} \ln\left( \frac{2}{1-\gamma} \right)$.

## a) Numerical Calculation
Given: $n = 10, l = 1000, \varepsilon = 1$.
We want to find $\gamma$.
$$ 1 - \gamma = 2 \exp\left( -\frac{2 \cdot 1000 \cdot 1^2}{10^2} \right) $$
$$ 1 - \gamma = 2 \exp\left( -\frac{2000}{100} \right) = 2 \exp(-20) $$
$$ \gamma = 1 - 2 e^{-20} $$
$e^{-20} \approx 2.06 \times 10^{-9}$.
So $\gamma \approx 1 - 4.12 \times 10^{-9}$.
The probability is extremely close to 1 (virtually 100%).

## Related Concepts
- [[sample-complexity]]
- [[hoeffding-bound]]
- [[hamming-distance]]
