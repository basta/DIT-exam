---
id: ssu_batch5_003
course: Statistical Machine Learning
tags: [neural-networks, prior-shift, bayes-rule, posterior-probability]
difficulty: 3
type: derivation
status: to_learn
---

# Question
(4p) Suppose you have learned a neural network classifier that predicts the posterior class probabilities $p(k \mid x)$ for an unknown distribution
$$ p(x, k) = p(x \mid k) p(k). $$
The network uses softmax activation in the last layer and has been learned on an i.i.d. training set $\mathcal{T}^m = \{(x^j, k^j) \mid j = 1, \dots, m\}$. You want to apply the classifier in some application domain with "shifted" class priors $p(k) \to p_a(k)$. The appearance probabilities $p(x \mid k)$ remain unchanged. Explain how to utilise the classifier for this domain without retraining it.
*Remark*: We assume that the shifted class priors $p_a(k)$ are known.

---
# Solution
We are given a model that outputs $p(k \mid x)$ where:
$$ p(k \mid x) = \frac{p(x \mid k) p(k)}{p(x)} \propto p(x \mid k) p(k) $$
We assume we know the training priors $p(k)$ (estimated from the training set frequencies) and the new priors $p_a(k)$.

We want to compute the new posterior $p_a(k \mid x)$:
$$ p_a(k \mid x) \propto p(x \mid k) p_a(k) $$

From the original model output, we can recover a term proportional to the likelihood $p(x \mid k)$:
$$ p(x \mid k) \propto \frac{p(k \mid x)}{p(k)} $$

Substitute this into the expression for the new posterior:
$$ p_a(k \mid x) \propto \left( \frac{p(k \mid x)}{p(k)} \right) p_a(k) $$

**Algorithm:**
1.  Run the input $x$ through the network to get outputs $y_k = p(k \mid x)$.
2.  Compute the unnormalized scores for the new domain:
    $$ s_k' = y_k \frac{p_a(k)}{p(k)} $$
3.  Normalize to get the valid probability distribution:
    $$ p_a(k \mid x) = \frac{s_k'}{\sum_j s_j'} = \frac{y_k \frac{p_a(k)}{p(k)}}{\sum_j y_j \frac{p_a(j)}{p(j)}} $$

This allows us to correct the predictions for the prior shift without retraining.

## Related Concepts
- [[neural-networks]]
- [[prior-shift]]
- [[bayes-rule]]
