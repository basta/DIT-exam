---
id: ssu_batch5_004
course: Statistical Machine Learning
tags: [probabilistic-model, change-point-detection, maximum-likelihood, optimal-prediction, quadratic-loss]
difficulty: 5
type: derivation
status: to_learn
---

# Question
(6p) We consider the following probabilistic model for real valued sequences $x = (x_1, x_2, \dots, x_n)$ of length $n$. The elements of the leading part, up to some position $k$ are independent and normally distributed with mean $\mu_1$ and variance $\sigma_1^2$. The trailing elements are independent and normally distributed with mean $\mu_2$ and variance $\sigma_2^2$. The boundary position $k$ between the two parts is itself random and follows a categorical distribution with probabilities $p(k) = \pi_k$.

**a)** Explain how to estimate the model parameters $\mu_{1,2}, \sigma_{1,2}$ and $\pi_k, k = 1, \dots, n$ from i.i.d. training data $\mathcal{T}^m = \{(x^j, k_j) \mid j = 1, \dots, m\}$ by using the maximum likelihood estimator.

**b)** Assume now that the model parameters are known. Given a sequence $x$ we want to predict the boundary position between the leading and trailing part. We want to use the quadratic loss $\ell(k, k') = (k - k')^2$. Show that the optimal prediction for the boundary is given by
$$ k^* = \sum_{k=0}^n k p(k \mid x). $$

---
# Solution
## a) Maximum Likelihood Estimation
We are given supervised data (observed $k$). The log-likelihood decomposes:
$$ L(\theta) = \sum_{j=1}^m \ln p(x^j, k_j) = \sum_{j=1}^m \left( \ln p(k_j) + \ln p(x^j \mid k_j) \right) $$
$$ L(\theta) = \sum_{j=1}^m \ln \pi_{k_j} + \sum_{j=1}^m \left( \sum_{i=1}^{k_j} \ln \mathcal{N}(x_i^j; \mu_1, \sigma_1^2) + \sum_{i=k_j+1}^n \ln \mathcal{N}(x_i^j; \mu_2, \sigma_2^2) \right) $$

**Estimating $\pi$:**
Maximize $\sum \ln \pi_{k_j}$ subject to $\sum \pi_k = 1$.
$$ \pi_k = \frac{\text{Count}(k)}{m} = \frac{1}{m} \sum_{j=1}^m \mathbb{I}[k_j = k] $$

**Estimating $\mu_1, \sigma_1^2$:**
Pool all observations from the "leading parts" of all sequences.
Let $S_1 = \{(j, i) \mid 1 \le i \le k_j \}$. Let $N_1 = |S_1|$ be the total count.
$$ \mu_1 = \frac{1}{N_1} \sum_{(j, i) \in S_1} x_i^j $$
$$ \sigma_1^2 = \frac{1}{N_1} \sum_{(j, i) \in S_1} (x_i^j - \mu_1)^2 $$

**Estimating $\mu_2, \sigma_2^2$:**
Pool all observations from the "trailing parts".
Let $S_2 = \{(j, i) \mid k_j < i \le n \}$. Let $N_2 = |S_2|$.
$$ \mu_2 = \frac{1}{N_2} \sum_{(j, i) \in S_2} x_i^j $$
$$ \sigma_2^2 = \frac{1}{N_2} \sum_{(j, i) \in S_2} (x_i^j - \mu_2)^2 $$

## b) Optimal Prediction for Quadratic Loss
We aim to minimize the expected risk:
$$ R(k') = \mathbb{E}_{k \sim p(k \mid x)} [ (k - k')^2 ] $$
$$ R(k') = \sum_{k=0}^n (k - k')^2 p(k \mid x) $$
To find the minimum, take the derivative w.r.t $k'$ and set to 0.
$$ \frac{dR}{dk'} = \sum_{k=0}^n 2(k - k')(-1) p(k \mid x) = -2 \sum_{k=0}^n (k p(k \mid x) - k' p(k \mid x)) = 0 $$
$$ \sum_{k=0}^n k p(k \mid x) - k' \sum_{k=0}^n p(k \mid x) = 0 $$
Since $\sum p(k \mid x) = 1$:
$$ k' = \sum_{k=0}^n k p(k \mid x) = \mathbb{E}[k \mid x] $$
This is the posterior mean.

## Related Concepts
- [[maximum-likelihood]]
- [[change-point-detection]]
- [[bayes-estimator]]
- [[loss-functions]]
