---
id: ssu_batch3_003
course: Statistical Machine Learning
tags: [probabilistic-model, em-algorithm, change-point-detection, maximum-likelihood]
difficulty: 5
type: derivation
status: to_learn
---

# Question
(5p) Consider the following probabilistic model for real valued sequences $x = (x_1, \dots, x_n), x_i \in \mathbb{R}$ of fixed length $n$. Each sequence is a combination of a leading part $i \le k$ and a trailing part $i > k$. The boundary $k = 0, \dots, n$ is random with some categorical distribution $\pi \in \mathbb{R}_+^{n+1}, \sum_k \pi_k = 1$. The values $x_i$ in the leading and trailing part are statistically independent and distributed with some probability density function $p_1(x)$ and $p_2(x)$ respectively. Altogether the distribution for pairs $(x, k)$ reads
$$ p(x, k) = \pi_k \prod_{i=1}^k p_1(x_i) \prod_{j=k+1}^n p_2(x_j). \quad (2) $$
The densities $p_1$ and $p_2$ are known. Given an i.i.d. sample of sequences $\mathcal{T}^m = \{x^\ell \in \mathbb{R}^n \mid \ell = 1, \dots, m\}$, the task is to estimate the unknown boundary distribution $\pi$ by the EM-algorithm.

**a)** The E-step of the algorithm requires to compute the values of auxiliary variables $\alpha^\ell(k) = p(k \mid x^\ell)$ for each example $x^\ell$ given the current estimate $\pi^{(t)}$ of the boundary distribution. Give a formula for computing these values from model (2).

**b)** The M-step requires to solve the optimisation problem
$$ \frac{1}{m} \sum_{\ell=1}^m \sum_{k=0}^n \alpha_\ell^{(t)}(k) \log p(x^\ell, k) \to \max_{\pi}. $$
Substitute the model (2) and solve the optimisation task.

---
# Solution
## a) E-step: Computing $\alpha_\ell(k)$
Using Bayes' rule:
$$ \alpha_\ell(k) = p(k \mid x^\ell; \pi^{(t)}) = \frac{p(x^\ell, k; \pi^{(t)})}{p(x^\ell; \pi^{(t)})} $$
$$ p(x^\ell, k; \pi^{(t)}) = \pi_k^{(t)} \prod_{i=1}^k p_1(x_i^\ell) \prod_{j=k+1}^n p_2(x_j^\ell) $$
$$ p(x^\ell; \pi^{(t)}) = \sum_{j=0}^n p(x^\ell, j; \pi^{(t)}) $$
So:
$$ \alpha_\ell^{(t)}(k) = \frac{\pi_k^{(t)} \prod_{i=1}^k p_1(x_i^\ell) \prod_{j=k+1}^n p_2(x_j^\ell)}{\sum_{j=0}^n \pi_j^{(t)} \prod_{i=1}^j p_1(x_i^\ell) \prod_{h=j+1}^n p_2(x_h^\ell)} $$
This can be computed efficiently by precomputing prefix products of $p_1$ and suffix products of $p_2$.

## b) M-step: Estimating $\pi$
We want to maximize the Q-function with respect to $\pi$, subject to $\sum_{k=0}^n \pi_k = 1$.
$$ Q(\pi) = \sum_{\ell=1}^m \sum_{k=0}^n \alpha_\ell^{(t)}(k) \log p(x^\ell, k) $$
Substitute $\log p(x^\ell, k) = \log \pi_k + \sum_{i=1}^k \log p_1(x_i^\ell) + \sum_{j=k+1}^n \log p_2(x_j^\ell)$.
Terms not involving $\pi$ are constant with respect to the optimization.
$$ Q(\pi) = \sum_{\ell=1}^m \sum_{k=0}^n \alpha_\ell^{(t)}(k) \log \pi_k + \text{const} $$
$$ Q(\pi) = \sum_{k=0}^n (\sum_{\ell=1}^m \alpha_\ell^{(t)}(k)) \log \pi_k + \text{const} $$
Let $N_k = \sum_{\ell=1}^m \alpha_\ell^{(t)}(k)$. We maximize $\sum_{k=0}^n N_k \log \pi_k$ subject to $\sum \pi_k = 1$.
Using Lagrange multipliers:
$$ L(\pi, \lambda) = \sum_{k=0}^n N_k \log \pi_k - \lambda (\sum_{k=0}^n \pi_k - 1) $$
$$ \frac{\partial L}{\partial \pi_k} = \frac{N_k}{\pi_k} - \lambda = 0 \implies \pi_k = \frac{N_k}{\lambda} $$
Summing over $k$: $1 = \sum \pi_k = \frac{1}{\lambda} \sum N_k = \frac{1}{\lambda} m$. So $\lambda = m$.
$$ \pi_k^{(t+1)} = \frac{N_k}{m} = \frac{1}{m} \sum_{\ell=1}^m \alpha_\ell^{(t)}(k) $$

## Related Concepts
- [[em-algorithm]]
- [[change-point-detection]]
- [[maximum-likelihood]]
- [[constrained-optimization]]
