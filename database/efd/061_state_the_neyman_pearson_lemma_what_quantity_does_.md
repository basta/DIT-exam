---
id: efd_061
course: Estimation, Filtration, and Detection
tags: [hypothesis-testing, neyman-pearson, detection-theory, likelihood-ratio]
difficulty: 2
type: open
status: to_learn
---

# Question
State the Neyman-Pearson Lemma. What quantity does it maximize for a fixed False Alarm probability?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** The Neyman-Pearson Lemma states that the optimal decision rule to distinguish between a null hypothesis $H_0$ and an alternative hypothesis $H_1$ is a likelihood ratio test. It maximizes the **Detection Probability** ($P_D$ or power of the test) for a fixed **False Alarm Probability** ($\alpha$ or $P_{FA}$).

## Explanation
In statistical signal processing and detection theory, we often face the challenge of deciding between two hypotheses based on observed data $\mathbf{x}$. The Neyman-Pearson (NP) Lemma provides the fundamental framework for this decision-making process when we do not have prior probabilities for the hypotheses.

The lemma states that to maximize the probability of detection $P_D = P(\text{decide } H_1 | H_1 \text{ is true})$, subject to a constraint on the probability of false alarm $P_{FA} = P(\text{decide } H_1 | H_0 \text{ is true}) \leq \alpha$, the optimal decision rule is the Likelihood Ratio Test (LRT).

The likelihood ratio is defined as:
$$
L(\mathbf{x}) = \frac{p(\mathbf{x} | H_1)}{p(\mathbf{x} | H_0)}
$$
The decision rule is then formulated as:
1. If $L(\mathbf{x}) > \gamma$, decide $H_1$.
2. If $L(\mathbf{x}) < \gamma$, decide $H_0$.
3. If $L(\mathbf{x}) = \gamma$, decide $H_1$ with some probability (to achieve the exact size $\alpha$ if the distribution is discrete).

The threshold $\gamma$ is chosen such that the constraint $P(L(\mathbf{x}) > \gamma | H_0) = \alpha$ is satisfied. This lemma is "optimal" because no other test can achieve a higher $P_D$ for the same (or lower) $P_{FA}$. It essentially defines the boundary of the Receiver Operating Characteristic (ROC) curve.

### Steps / Derivation
1. **Define the objective function:** We use a Lagrange multiplier $\lambda$ to maximize $P_D$ subject to $P_{FA} = \alpha$.
2. **Formulate the Lagrangian:**
$$
J = P_D - \lambda(P_{FA} - \alpha) = \int_{R_1} p(\mathbf{x}|H_1) d\mathbf{x} - \lambda \left( \int_{R_1} p(\mathbf{x}|H_0) d\mathbf{x} - \alpha \right)
$$
3. **Rearrange the integral:**
$$
J = \lambda \alpha + \int_{R_1} [p(\mathbf{x}|H_1) - \lambda p(\mathbf{x}|H_0)] d\mathbf{x}
$$
4. **Determine the decision region $R_1$:** To maximize $J$, we must include every point $\mathbf{x}$ in the region $R_1$ where the integrand is positive:
$$
p(\mathbf{x}|H_1) - \lambda p(\mathbf{x}|H_0) > 0 \implies \frac{p(\mathbf{x}|H_1)}{p(\mathbf{x}|H_0)} > \lambda
$$

## Related Concepts
- [[binary_hypothesis_testing]]
- [[receiver_operating_characteristic]]
- [[likelihood_ratio_test]]