---
id: efd_004
course: Estimation, Filtration, and Detection
tags: [probability-theory, correlation, statistical-independence, stochastic-processes]
difficulty: 2
type: open
status: to_learn
---

# Question
Explain the difference between statistical independence and uncorrelatedness of two random variables. Does uncorrelatedness imply independence?

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Uncorrelatedness does not generally imply independence (except in the specific case of jointly Gaussian variables).

## Explanation
In signal processing and estimation theory, understanding the relationship between independence and uncorrelatedness is fundamental for characterizing noise and system behaviors.

**Statistical Independence** is a much stronger condition. Two random variables $X$ and $Y$ are independent if their joint Probability Density Function (PDF) factors into the product of their marginal PDFs: $f_{X,Y}(x,y) = f_X(x)f_Y(y)$. This implies that the realization of one variable provides no information whatsoever about the distribution of the other. It affects all moments of the distributions.

**Uncorrelatedness** is a measure of the linear relationship between two variables. Two variables are uncorrelated if their covariance is zero, which is equivalent to saying that the expectation of their product equals the product of their expectations: $E[XY] = E[X]E[Y]$. This only addresses the second-order moments (linear dependence).

**Does uncorrelatedness imply independence?**
No. Two variables can be uncorrelated but still be highly dependent. For example, if $X$ is a symmetric random variable (like a standard normal) and $Y = X^2$, $Y$ is strictly determined by $X$ (not independent), yet they can have a covariance of zero. The only major exception in this field is the **Jointly Gaussian** case: if two variables are jointly Gaussian and uncorrelated, they are also statistically independent. This property is why Gaussian assumptions are so prevalent in the derivation of the Kalman Filter and MAP estimators.

### Steps / Derivation
1. **Definition of Independence:**
$$
P(X \in A, Y \in B) = P(X \in A)P(Y \in B) \implies f_{X,Y}(x,y) = f_X(x)f_Y(y)
$$

2. **Definition of Uncorrelatedness (Covariance):**
$$
Cov(X,Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y] = 0
$$

3. **Proof that Independence implies Uncorrelatedness:**
If independent, then:
$$
E[XY] = \int \int xy f_X(x)f_Y(y) dx dy = \left( \int x f_X(x) dx \right) \left( \int y f_Y(y) dy \right) = E[X]E[Y]
$$

## Related Concepts
- [[joint_gaussian_distribution]]
- [[covariance_matrix]]
- [[orthogonal_random_variables]]