---
id: efd_028
course: Estimation, Filtration, and Detection
tags: [linear-regression, parameter-estimation, least-squares]
difficulty: 1
type: open
status: to_learn
---

# Question
Define the standard Linear Regression Model in the form $y = \phi^T \theta + e$. What do $\phi$, $\theta$, and $e$ represent?

## Options
N/A (Open-ended question)

---
# Solution
**Correct Answer:** 
The variables represent:
- $y$: The observed output or measurement (scalar). 
- $\phi$: The vector of regressors or basis functions (input data).
- $\theta$: The vector of unknown parameters to be estimated.
- $e$: The observation noise or residual error.

## Explanation
The linear regression model is the foundational bedrock of estimation theory. It describes a linear relationship between a dependent variable $y$ and a set of independent variables or features. In the context of signal processing and control theory, this model is often used for system identification, where we attempt to characterize a system's behavior based on observed input-output data.

In the equation $y = \phi^T \theta + e$:
1. **The measurement ($y$):** This represents the actual signal received or the output measured from a process. In a sequence of $N$ observations, this becomes a vector $\mathbf{y}$.
2. **The regressor vector ($\phi$):** These are the known quantities. They can be direct inputs, previous outputs (in ARX models), or nonlinear transformations of inputs. The "linear" in linear regression refers to the linearity in the parameters $\theta$, not necessarily the inputs $\phi$.
3. **The parameter vector ($\theta$):** These are the "weights" or constants that we aim to find using estimation techniques like Ordinary Least Squares (OLS) or Maximum Likelihood Estimation (MLE). The goal of the filter or estimator is to produce an estimate $\hat{\theta}$ that minimizes the influence of $e$.
4. **The error term ($e$):** This accounts for modeling inaccuracies and measurement noise. Typically, in classical estimation, $e$ is assumed to be white Gaussian noise with $E[e] = 0$ and $Var(e) = \sigma^2$.

### Steps / Derivation
1. Identify the relationship between the observed output and the known inputs.
2. Structure the unknown coefficients into a vector $\theta \in \mathbb{R}^n$.
3. Formulate the regressor vector $\phi \in \mathbb{R}^n$ such that:
$$
y = \sum_{i=1}^{n} \phi_i \theta_i + e = \phi^T \theta + e
$$

## Related Concepts
- [[least_squares_estimation]]
- [[system_identification]]
- [[gauss_markov_theorem]]