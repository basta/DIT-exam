---
id: efd_071
course: Estimation, Filtration, and Detection
tags: [kalman-filter, multiple-model-estimation, bayesian-inference]
difficulty: 4
type: open
status: to_learn
---

# Question
In a bank of Kalman Filters used for detection, what does the "Model Probability" $\mu_j(k)$ represent, and how is it updated recursively?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** $\mu_j(k)$ represents the posterior probability that the $j$-th model is the correct model at time $k$, given all measurements up to that time. It is updated using Bayes' Rule based on the likelihood of the innovation from the $j$-th Kalman Filter.

## Explanation
In Multiple Model Estimation (MME) or bank-of-filters architectures, we assume the system behaves according to one of $N$ possible models (e.g., different maneuver modes for a target or different failure states). The model probability $\mu_j(k) = P(M_j | Z^k)$ quantifies the confidence that model $M_j$ is the active process governing the system's dynamics at time $k$, where $Z^k$ is the sequence of observations $\{z(1), \dots, z(k)\}$.

The recursive update relies on the **innovation** (or residual) $\tilde{z}_j(k) = z(k) - \hat{z}_j(k|k-1)$ produced by the $j$-th Kalman Filter in the bank. Under the assumption that the $j$-th model is correct, the innovation is a zero-mean Gaussian white noise process with covariance $S_j(k)$. The likelihood of the current measurement $z(k)$ given model $M_j$ is computed using the multivariate normal distribution:
$$ \mathcal{L}_j(k) = \frac{1}{\sqrt{|2\pi S_j(k)|}} \exp\left(-\frac{1}{2} \tilde{z}_j(k)^T S_j(k)^{-1} \tilde{z}_j(k)\right) $$

If we assume the models are static (they do not switch over time), we use a recursive Bayesian update. The probability is updated by multiplying the previous probability by the current likelihood and normalizing the result so that the sum of probabilities across all filters equals one. In the more complex **Interacting Multiple Model (IMM)** estimator, these probabilities also account for transition probabilities between models.

## Steps / Derivation
1. **Likelihood Calculation**: For each filter $j$, compute the likelihood $\mathcal{L}_j(k)$ of the observed measurement $z(k)$ based on its innovation $\tilde{z}_j(k)$ and innovation covariance $S_j(k)$:
$$ \mathcal{L}_j(k) = p(z(k) | M_j, Z^{k-1}) = \mathcal{N}(\tilde{z}_j(k); 0, S_j(k)) $$

2. **Recursive Bayesian Update**: Update the unnormalized probability using the prior probability from the previous step:
$$ \mu_j(k) = \frac{\mathcal{L}_j(k) \mu_j(k-1)}{\sum_{i=1}^{N} \mathcal{L}_i(k) \mu_i(k-1)} $$

3. **Normalization**: Ensure $\sum_{j=1}^{N} \mu_j(k) = 1$ to maintain a valid probability distribution across the model bank.

## Related Concepts
- [[interactng_multiple_model_imm]]
- [[innovation_covariance]]
- [[hybrid_system_estimation]]