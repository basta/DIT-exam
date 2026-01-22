---
id: efd_005
course: Estimation, Filtration, and Detection
tags: [bayes-rule, probability-density-functions, statistical-inference]
difficulty: 2
type: open
status: to_learn
---

# Question
State Bayes' Theorem (Bayes' Rule) for probability density functions.

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** 
The posterior density is given by $f_{X|Y}(x|y) = \frac{f_{Y|X}(y|x) f_X(x)}{f_Y(y)}$, where $f_Y(y) = \int_{-\infty}^{\infty} f_{Y|X}(y|x) f_X(x) dx$.

## Explanation
In the context of Estimation, Filtration, and Detection, Bayes' Theorem provides the fundamental mechanism for updating our knowledge about an unknown parameter or state $X$ based on observed data $Y$. Unlike the discrete version of Bayes' rule involving events, the continuous version deals with probability density functions (PDFs). 

The term $f_X(x)$ represents the **prior distribution**, which encapsulates our beliefs about the random variable $X$ before any measurement is taken. The term $f_{Y|X}(y|x)$ is known as the **likelihood function** (or the observation model), describing how likely it is to observe the data $y$ given a specific realization of $x$. 

The product of the prior and the likelihood, $f_{Y|X}(y|x) f_X(x)$, yields the joint density $f_{X,Y}(x,y)$. To obtain the **posterior density** $f_{X|Y}(x|y)$, we must normalize this joint density by the **marginal density** (or evidence) $f_Y(y)$. This marginal density is often calculated using the law of total probability by integrating the numerator over the entire support of $X$. In many estimation problems, specifically MAP (Maximum A Posteriori) estimation, the denominator $f_Y(y)$ is treated as a normalizing constant because it does not depend on the parameter $x$ being estimated. This relationship is often summarized as "The posterior is proportional to the likelihood times the prior."

### Steps / Derivation
1. Start with the definition of conditional probability for joint densities:
$$
f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}
$$
2. Express the joint density $f_{X,Y}(x,y)$ using the conditional density of $Y$ given $X$:
$$
f_{X,Y}(x,y) = f_{Y|X}(y|x) f_X(x)
$$
3. Substitute the joint density back into the conditional probability formula to get the final form:
$$
f_{X|Y}(x|y) = \frac{f_{Y|X}(y|x) f_X(x)}{\int_{-\infty}^{\infty} f_{Y|X}(y|x') f_X(x') dx'}
$$

## Related Concepts
- [[maximum_a_posteriori_estimation]]
- [[minimum_mean_square_error]]
- [[recursive_bayesian_estimation]]