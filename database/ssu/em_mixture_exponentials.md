---
id: 2016_ssu_003
course: Statistical Machine Learning
tags: [em-algorithm, mixture-model, exponential-distribution, maximum-likelihood]
difficulty: 5
type: derivation
status: to_learn
---

# Question
(8p) The probability density of the real valued random variable $X > 0$ is a mixture of two exponential distributions
$$ p(x) = c \lambda_1 e^{-\lambda_1 x} + (1-c) \lambda_2 e^{-\lambda_2 x}, $$
where $c$ and $(1-c)$ are the mixture weights of the two components. Given and i.i.d. training set $\mathcal{T}_m = \{x_i \in \mathbb{R}_+ \mid i = 1, 2, \dots, m\}$, the task is to estimate the parameters $c, \lambda_1, \lambda_2$ by the maximum likelihood estimator. Derive an EM-algorithm for this task.

**a)** Formulate the algorithm. Solve the E-step and give a formula for the auxiliary variables $\alpha(x_i)$ describing the posterior probability for $x_i$ to belong to first component of the distribution. (The probability to belong to second component is given by $1 - \alpha(x_i)$.)

**b)** Show that the optimisation w.r.t. the unknown parameters $c, \lambda_1, \lambda_2$ in the M-step decomposes into independent tasks.

**c)** Derive a solution for each of them. Are these tasks concave?

---
# Solution

## a) E-step
Let $z_i \in \{1, 2\}$ be the latent variable indicating which component generated $x_i$.
The expected complete log-likelihood is:
$$ Q(\theta, \theta^{(t)}) = \sum_{i=1}^m \mathbb{E}_{z_i|x_i, \theta^{(t)}} [\log p(x_i, z_i | \theta)] $$
Auxiliary variable $\alpha(x_i) = p(z_i=1 | x_i, \theta^{(t)})$.
Using Bayes' rule:
$$ \alpha_i^{(t)} = \frac{p(x_i | z_i=1, \theta^{(t)}) p(z_i=1 | \theta^{(t)})}{p(x_i | \theta^{(t)})} $$
$$ \alpha_i^{(t)} = \frac{c^{(t)} \lambda_1^{(t)} e^{-\lambda_1^{(t)} x_i}}{c^{(t)} \lambda_1^{(t)} e^{-\lambda_1^{(t)} x_i} + (1-c^{(t)}) \lambda_2^{(t)} e^{-\lambda_2^{(t)} x_i}} $$
The E-step computes these $\alpha_i^{(t)}$ for all $i=1, \dots, m$.

## b) M-step Decomposition
The Q-function expands to:
$$ Q = \sum_{i=1}^m \left[ \alpha_i^{(t)} \log(c \lambda_1 e^{-\lambda_1 x_i}) + (1-\alpha_i^{(t)}) \log((1-c) \lambda_2 e^{-\lambda_2 x_i}) \right] $$
$$ Q = \sum_{i=1}^m \left[ \alpha_i^{(t)} (\log c + \log \lambda_1 - \lambda_1 x_i) + (1-\alpha_i^{(t)}) (\log(1-c) + \log \lambda_2 - \lambda_2 x_i) \right] $$
Rearranging terms by parameters:
$$ Q = \underbrace{\sum_{i=1}^m [\alpha_i^{(t)} \log c + (1-\alpha_i^{(t)}) \log(1-c)]}_{Q_c(c)} + \underbrace{\sum_{i=1}^m \alpha_i^{(t)} (\log \lambda_1 - \lambda_1 x_i)}_{Q_{\lambda_1}(\lambda_1)} + \underbrace{\sum_{i=1}^m (1-\alpha_i^{(t)}) (\log \lambda_2 - \lambda_2 x_i)}_{Q_{\lambda_2}(\lambda_2)} $$
Since $Q$ is a sum of terms involving only $c$, only $\lambda_1$, and only $\lambda_2$ separately, the optimization decomposes into independent tasks:
1. $\max_c Q_c(c)$
2. $\max_{\lambda_1} Q_{\lambda_1}(\lambda_1)$
3. $\max_{\lambda_2} Q_{\lambda_2}(\lambda_2)$

## c) Solution and Concavity

### Optimization for $c$
$$ \frac{\partial Q_c}{\partial c} = \frac{\sum \alpha_i^{(t)}}{c} - \frac{\sum (1-\alpha_i^{(t)})}{1-c} = 0 $$
Let $N_1 = \sum_{i=1}^m \alpha_i^{(t)}$ and $N_2 = \sum_{i=1}^m (1-\alpha_i^{(t)}) = m - N_1$.
$$ \frac{N_1}{c} = \frac{N_2}{1-c} \implies N_1(1-c) = N_2 c \implies N_1 = (N_1 + N_2)c = mc $$
$$ c^{(t+1)} = \frac{1}{m} \sum_{i=1}^m \alpha_i^{(t)} $$
This is a standard MLE for binomial distribution, which is concave.

### Optimization for $\lambda_1$
$$ Q_{\lambda_1} = \sum \alpha_i^{(t)} \log \lambda_1 - \lambda_1 \sum \alpha_i^{(t)} x_i $$
$$ Q_{\lambda_1} = N_1 \log \lambda_1 - \lambda_1 S_1 \quad \text{where } S_1 = \sum_{i=1}^m \alpha_i^{(t)} x_i $$
$$ \frac{\partial Q_{\lambda_1}}{\partial \lambda_1} = \frac{N_1}{\lambda_1} - S_1 = 0 \implies \lambda_1^{(t+1)} = \frac{\sum_{i=1}^m \alpha_i^{(t)}}{\sum_{i=1}^m \alpha_i^{(t)} x_i} $$
Second derivative: $\frac{\partial^2 Q_{\lambda_1}}{\partial \lambda_1^2} = -\frac{N_1}{\lambda_1^2} < 0$. The function is strictly concave.

### Optimization for $\lambda_2$
Similarly for $\lambda_2$:
$$ \lambda_2^{(t+1)} = \frac{\sum_{i=1}^m (1-\alpha_i^{(t)})}{\sum_{i=1}^m (1-\alpha_i^{(t)}) x_i} $$
This task is also strictly concave.

## Related Concepts
- [[em-algorithm]]
- [[mixture-model]]
- [[maximum-likelihood]]
