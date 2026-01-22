---
id: efd_062
course: Estimation, Filtration, and Detection
tags: [detection-theory, roc-curve, hypothesis-testing, neyman-pearson]
difficulty: 2
type: open
status: to_learn
---

# Question
What is a Receiver Operating Characteristic (ROC) curve? What do the axes represent, and what constitutes a "better" detector on this plot?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
An ROC curve is a graphical plot that illustrates the diagnostic ability of a binary classifier system as its discrimination threshold is varied. The y-axis represents the Probability of Detection ($P_D$), and the x-axis represents the Probability of False Alarm ($P_{FA}$). A "better" detector is one whose curve is closer to the upper-left corner of the plot.

## Explanation
In detection theory, we often deal with binary hypothesis testing where we must decide between a null hypothesis $H_0$ (noise only) and an alternative hypothesis $H_1$ (signal + noise). To make this decision, a likelihood ratio test is typically employed, comparing a test statistic $L(y)$ against a threshold $\gamma$. 

The Receiver Operating Characteristic (ROC) curve is the fundamental tool used to evaluate the performance of such a detector. It shows the trade-off between the benefit of the detector (detecting a signal when it is present) and the cost (falsely claiming a signal is present when it is not). 

**The Axes:**
1. **Vertical Axis ($y$-axis):** Represents the **Probability of Detection ($P_D$)**, also known as Sensitivity or Hit Rate. Mathematically, $P_D = P(\text{decide } H_1 | H_1 \text{ is true})$.
2. **Horizontal Axis ($x$-axis):** Represents the **Probability of False Alarm ($P_{FA}$)**, also known as the Type I error or Size of the test. Mathematically, $P_{FA} = P(\text{decide } H_1 | H_0 \text{ is true})$.

**Comparison of Detectors:**
A "better" detector provides a higher $P_D$ for the same $P_{FA}$ compared to another detector. On the ROC plot, the ideal detector would reside at the point $(0, 1)$, meaning it achieves 100% detection with 0% false alarms. Therefore, as the curve "bows" toward the top-left corner, the performance improves. The Area Under the Curve (AUC) is a common scalar metric derived from the ROC; an AUC of 1.0 represents a perfect detector, while an AUC of 0.5 (the diagonal line $P_D = P_{FA}$) represents a detector that performs no better than random guessing.

### Steps / Derivation
1. Define the decision rule based on a threshold $\eta$:
$$
\text{Decide } H_1 \text{ if } \frac{p(y|H_1)}{p(y|H_0)} > \eta
$$
2. Calculate the coordinates for a specific $\eta$:
$$
P_D(\eta) = \int_{\gamma}^{\infty} p(L|H_1) dL, \quad P_{FA}(\eta) = \int_{\gamma}^{\infty} p(L|H_0) dL
$$
3. Sweep $\eta$ from $\infty$ to $0$ to generate the full curve from $(0,0)$ to $(1,1)$.

## Related Concepts
- [[binary_hypothesis_testing]]
- [[neyman_pearson_lemma]]
- [[likelihood_ratio_test]]