---
id: ssu_batch3_004
course: Statistical Machine Learning
tags: [markov-chain, marginal-probability, forward-pass, dynamic-programming]
difficulty: 3
type: derivation
status: to_learn
---

# Question
(3p) Let us consider the following standard Markov chain model for sequences $s = (s_1, \dots, s_n)$ of length $n$ with states $s_i \in K$ given by:
$$ p(s) = p(s_1) \prod_{i=2}^n p(s_i \mid s_{i-1}). $$
The conditional probabilities $p(s_i \mid s_{i-1})$ and the marginal probability $p(s_1)$ for the first element are assumed to be known.
Describe an efficient algorithm for computing the marginal probabilities $p(s_i)$ for all $i = 2, \dots, n$. What complexity has it?

---
# Solution
We want to compute $p(s_i)$ for $i=2, \dots, n$.
We can do this recursively using the properties of the Markov chain (Sum-Product rule).

## Algorithm (Forward Pass)
1.  **Initialization:**
    We are given $p(s_1)$.

2.  **Recursion:**
    For $i = 2$ to $n$:
    $$ p(s_i) = \sum_{s_{i-1} \in K} p(s_i, s_{i-1}) = \sum_{s_{i-1} \in K} p(s_i \mid s_{i-1}) p(s_{i-1}) $$

    This basically computes the marginal $\alpha_i(s_i) = p(s_i)$. (Note: This is a simplified Forward algorithm where observations are not involved, just state evolution).

3.  **Output:**
    The stored values $p(s_i)$ for all states $s_i \in K$ and all positions $i$.

## Complexity
Let $|K|$ be the number of states (size of the alphabet).
-   In each step $i$, for each state $s_i \in K$, we sum over all possible previous states $s_{i-1} \in K$.
-   This involves $|K|$ multiplications and sums for one $s_i$.
-   There are $|K|$ states for $s_i$. So one step takes $\mathcal{O}(|K|^2)$ operations.
-   There are $n-1$ steps.

**Total Complexity:** $\mathcal{O}(n \cdot |K|^2)$.

## Related Concepts
- [[markov-chain]]
- [[dynamic-programming]]
- [[forward-algorithm]]
- [[marginal-probability]]
