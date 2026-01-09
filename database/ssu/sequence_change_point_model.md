---
id: ssu_batch2_003
course: Statistical Machine Learning
tags: [probabilistic-model, change-point-detection, em-algorithm, maximum-likelihood]
difficulty: 5
type: derivation
status: to_learn
---

# Question
(8p) We consider the following probabilistic model for real valued sequences $x = (x_1, x_2, \dots, x_n)$ of length $n$. The elements of the leading part, up to some position $k$, are independent and normally distributed with mean $\mu_1$ and variance $\sigma_1^2$. The trailing elements are independent and normally distributed with mean $\mu_2$ and variance $\sigma_2^2$. The boundary position $y=k$ between the two parts is itself random and follows a categorical distribution with probabilities $p(y=k) = \pi_k$.

**a)** Give a formula for the conditional probability $p(y=k \mid x) = \frac{p(x, y=k)}{p(x)}$. Explain how to compute $p(x)$ efficiently, i.e. with run time complexity $\mathcal{O}(n)$.

**b)** Explain how to estimate the model parameters $\mu_{1,2}, \sigma_{1,2}$ and $\pi_k, k=1, \dots, n$ from i.i.d. training data $\mathcal{T} = \{(x^\ell, y^\ell) \mid \ell = 1, \dots, m\}$.

**c)** Given i.i.d. training data $\mathcal{T} = \{x^\ell \mid \ell = 1, \dots, m\}$ without the respective boundary values, we want to estimate the model parameters by applying the EM-algorithm. Give the formulas for the E-step and the M-step applied to this model.

---
# Solution

## a) Conditional Probability
The joint probability density $p(x, y=k)$ given the model assumptions is:
$$ p(x, y=k) = p(y=k) p(x|y=k) = \pi_k \left( \prod_{i=1}^k \mathcal{N}(x_i; \mu_1, \sigma_1^2) \right) \left( \prod_{i=k+1}^n \mathcal{N}(x_i; \mu_2, \sigma_2^2) \right) $$
The marginal probability $p(x)$ is obtained by summing over all possible change points $k$:
$$ p(x) = \sum_{j=1}^n p(x, y=j) $$
Thus, the conditional probability is:
$$ p(y=k|x) = \frac{\pi_k \prod_{i=1}^k \mathcal{N}(x_i; \mu_1, \sigma_1^2) \prod_{i=k+1}^n \mathcal{N}(x_i; \mu_2, \sigma_2^2)}{\sum_{j=1}^n \pi_j \prod_{i=1}^j \mathcal{N}(x_i; \mu_1, \sigma_1^2) \prod_{i=j+1}^n \mathcal{N}(x_i; \mu_2, \sigma_2^2)} $$

**Efficient Computation:**
To compute $p(x)$ in $\mathcal{O}(n)$, we can precompute prefix and suffix products (or sums of log-probabilities for numerical stability).
Let $L_1(i) = \log \mathcal{N}(x_i; \mu_1, \sigma_1^2)$ and $L_2(i) = \log \mathcal{N}(x_i; \mu_2, \sigma_2^2)$.
Precompute cumsum arrays: $C_1(k) = \sum_{i=1}^k L_1(i)$ and $S_2(k) = \sum_{i=k+1}^n L_2(i)$.
Then $\log p(x, y=k) = \log \pi_k + C_1(k) + S_2(k)$.
We can evaluate this for all $k \in \{1, \dots, n\}$ in $\mathcal{O}(n)$ after $\mathcal{O}(n)$ precomputation. Summing the exponentials gives $p(x)$.

## b) Estimation from Complete Data
Given complete data $\{(x^\ell, y^\ell)\}_{\ell=1}^m$:
1.  **$\pi_k$:** Maximum Likelihood Estimator is the frequency of each boundary position.
    $$ \hat{\pi}_k = \frac{1}{m} \sum_{\ell=1}^m \mathbb{I}[y^\ell = k] $$
2.  **$\mu_1, \sigma_1^2$:** Use all data points *before* the boundary $y^\ell$ across all examples.
    Let $S_1 = \{(x^\ell)_i \mid \ell \in \{1,\dots,m\}, 1 \le i \le y^\ell\}$.
    $$ \hat{\mu}_1 = \frac{1}{|S_1|} \sum_{v \in S_1} v, \quad \hat{\sigma}_1^2 = \frac{1}{|S_1|} \sum_{v \in S_1} (v - \hat{\mu}_1)^2 $$
3.  **$\mu_2, \sigma_2^2$:** Use all data points *after* the boundary $y^\ell$.
    Let $S_2 = \{(x^\ell)_i \mid \ell \in \{1,\dots,m\}, y^\ell < i \le n\}$.
    $$ \hat{\mu}_2 = \frac{1}{|S_2|} \sum_{v \in S_2} v, \quad \hat{\sigma}_2^2 = \frac{1}{|S_2|} \sum_{v \in S_2} (v - \hat{\mu}_2)^2 $$

## c) EM Algorithm
**E-step:**
Compute the posterior probability (responsibility) $\gamma^\ell_k = p(y^\ell=k | x^\ell; \theta^{(t)})$ for each example $\ell$ and each possible boundary $k$, using the formula derived in (a).
$$ \gamma^\ell_k = \frac{p(x^\ell, y=k | \theta^{(t)})}{\sum_{j=1}^n p(x^\ell, y=j | \theta^{(t)})} $$

**M-step:**
Update parameters by maximizing the expected log-likelihood.
1.  **Update $\pi_k$:**
    $$ \pi_k^{(t+1)} = \frac{1}{m} \sum_{\ell=1}^m \gamma^\ell_k $$
2.  **Update $\mu_1, \mu_2$:**
    $$ \mu_1^{(t+1)} = \frac{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \sum_{i=1}^k x_i^\ell}{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \cdot k} $$
    $$ \mu_2^{(t+1)} = \frac{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \sum_{i=k+1}^n x_i^\ell}{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \cdot (n-k)} $$
3.  **Update $\sigma_1^2, \sigma_2^2$:**
    $$ (\sigma_1^2)^{(t+1)} = \frac{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \sum_{i=1}^k (x_i^\ell - \mu_1^{(t+1)})^2}{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \cdot k} $$
    $$ (\sigma_2^2)^{(t+1)} = \frac{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \sum_{i=k+1}^n (x_i^\ell - \mu_2^{(t+1)})^2}{\sum_{\ell=1}^m \sum_{k=1}^n \gamma^\ell_k \cdot (n-k)} $$

## Related Concepts
- [[em-algorithm]]
- [[change-point-detection]]
- [[mixture-model]]
- [[time-series]]
