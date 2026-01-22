---
id: efd_058
course: Estimation, Filtration, and Detection
tags: [change-detection, hypothesis-testing, statistical-inference, signal-detection]
difficulty: 2
type: open
status: to_learn
---

# Question
Formulate the change detection problem as a statistical hypothesis testing problem (Null Hypothesis H0 vs. Alternative Hypothesis H1).

## Options
A) $H_0: \theta = \theta_0$ for all $t$; $H_1: \theta = \theta_1$ for all $t$
B) $H_0: y_k = w_k$; $H_1: y_k = s_k + w_k$
C) $H_0: \theta = \theta_0$ for $1 \le k \le n$; $H_1: \exists k_0 < n$ s.t. $\theta = \theta_0$ for $k < k_0$ and $\theta = \theta_1$ for $k \ge k_0$
D) $H_0: E[x] = 0$; $H_1: E[x] \neq 0$

---
# Solution
**Correct Answer:** C

## Explanation
Change detection, often referred to as "Abrupt Change Detection" or "CUSUM" (Cumulative Sum) analysis in signal processing, differs from standard binary hypothesis testing. In standard testing, we usually decide between two fixed states that apply to the entire dataset. In change detection, the goal is to identify if and when the underlying statistical properties of a stochastic process have shifted.

The Null Hypothesis ($H_0$) represents the "status quo" or the "no-change" scenario. In this state, the sequence of observations $y_1, y_2, \dots, y_n$ is assumed to be governed by a constant parameter vector $\theta_0$ (which could represent the mean, variance, or coefficients of an AR model).

The Alternative Hypothesis ($H_1$) represents the occurrence of a change at some unknown time instant $k_0$, known as the change point. Before $k_0$, the process follows the distribution characterized by $\theta_0$. At $k = k_0$, the process undergoes a jump or transition to a new state characterized by parameter $\theta_1$. The detection problem involves not only deciding between $H_0$ and $H_1$ but often estimating the change point $k_0$. This is typically solved using the Likelihood Ratio Test (LRT) or recursive algorithms like the Page-Hinkley test to minimize the detection delay while maintaining a fixed false alarm rate.

### Steps / Derivation
1. Define the observation sequence:
$$
\mathcal{Y}_n = \{y_1, y_2, \dots, y_n\}
$$
2. Formulate the Null Hypothesis where the parameter remains constant:
$$
H_0: y_i \sim p_{\theta_0}(y) \quad \text{for } 1 \le i \le n
$$
3. Formulate the Alternative Hypothesis where a change occurs at $k_0$:
$$
H_1: \begin{cases} y_i \sim p_{\theta_0}(y) & \text{for } 1 \le i < k_0 \\ y_i \sim p_{\theta_1}(y) & \text{for } k_0 \le i \le n \end{cases}
$$
4. The decision is usually based on the Log-Likelihood Ratio (LLR):
$$
S_n = \max_{1 \le k_0 \le n} \sum_{i=k_0}^{n} \ln \frac{p_{\theta_1}(y_i)}{p_{\theta_0}(y_i)}
$$

## Related Concepts
- [[likelihood_ratio_test]]
- [[cusum_algorithm]]
- [[sequential_probability_ratio_test]]