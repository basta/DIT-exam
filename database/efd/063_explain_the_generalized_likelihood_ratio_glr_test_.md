---
id: efd_063
course: Estimation, Filtration, and Detection
tags: [hypothesis-testing, glrt, fault-detection, parameter-estimation]
difficulty: 4
type: open
status: to_learn
---

# Question
Explain the Generalized Likelihood Ratio (GLR) Test. How do we handle unknown parameters (like the magnitude of the fault) in the likelihood ratio?

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** The GLR test handles unknown parameters by replacing them with their Maximum Likelihood Estimates (MLE) under each hypothesis.

## Explanation
The Generalized Likelihood Ratio Test (GLRT) is a statistical test used for hypothesis testing when the probability density functions (PDFs) under the null hypothesis ($H_0$) and the alternative hypothesis ($H_1$) contain unknown parameters. In classical detection theory, the Neyman-Pearson theorem provides the optimal test (the Likelihood Ratio Test) when the hypotheses are simple. However, in many engineering applications, such as fault detection or signal acquisition, we encounter composite hypotheses where parameters like the fault magnitude, arrival time, or signal phase are unknown.

Since the Likelihood Ratio (LR) cannot be computed directly without these values, the GLRT employs a "plug-in" approach. For each hypothesis, we calculate the Maximum Likelihood Estimate (MLE) of the unknown parameters based on the observed data $y$. The GLRT then forms a ratio using these maximized likelihoods. While the GLRT is not universally optimal (it is not always Uniformly Most Powerful), it is widely used because it typically performs well, is computationally tractable, and possesses desirable asymptotic properties (e.g., Wilks' Theorem). 

In the context of fault detection, if the nominal behavior is $H_0$ and the faulty behavior is $H_1$, and the fault magnitude $\theta$ is unknown, the GLRT compares the likelihood of the data assuming the most likely fault magnitude against the likelihood of the data assuming no fault.

### Steps / Derivation
1. Define the hypotheses with unknown parameter vectors $\theta_0$ and $\theta_1$:
$$
H_0: y \sim p(y; \theta_0), \quad \theta_0 \in \Theta_0
$$
$$
H_1: y \sim p(y; \theta_1), \quad \theta_1 \in \Theta_1
$$

2. Find the Maximum Likelihood Estimates (MLE) for the parameters under each hypothesis:
$$
\hat{\theta}_0 = \arg \max_{\theta_0 \in \Theta_0} p(y; \theta_0)
$$
$$
\hat{\theta}_1 = \arg \max_{\theta_1 \in \Theta_1} p(y; \theta_1)
$$

3. Construct the Generalized Likelihood Ratio $L_G(y)$:
$$
L_G(y) = \frac{p(y; \hat{\theta}_1)}{p(y; \hat{\theta}_0)} = \frac{\max_{\theta_1 \in \Theta_1} p(y; \theta_1)}{\max_{\theta_0 \in \Theta_0} p(y; \theta_0)}
$$

4. Compare the ratio (or its logarithm) to a threshold $\gamma$ to decide:
$$
L_G(y) \overset{H_1}{\underset{H_0}{\gtrless}} \gamma
$$

## Related Concepts
- [[maximum_likelihood_estimation]]
- [[neyman_pearson_lemma]]
- [[composite_hypothesis_testing]]