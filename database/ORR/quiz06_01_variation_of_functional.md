---
id: orr_quiz06_01
course: Optimal and Robust Control
tags: [calculus-of-variations, variation, functional]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The variation of a (cost) functional $J(y(x))$ (as a function of a function $y(x)$) is defined (in our course) as

## Options
A) the first-order approximation to the increment in the cost functional as the function $y(x)$ is varied.
B) the derivative of the cost functional with respect to the real parameter $\alpha$ which determines the variation $\delta y(x) = \alpha\eta(x)$ of the function $y(x)$.
C) the left hand side of the Euler-Lagrange equation, that is, $\dfrac{\partial L}{\partial y} - \dfrac{d}{dx}\dfrac{\partial L}{\partial y'}$.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
The **variation** $\delta J$ is the functional analogue of the differential of a function. It is the **first-order (linear) part of the increment** $\Delta J = J(y + \delta y) - J(y)$ when the argument function is perturbed by $\delta y$:
$$
\Delta J = \underbrace{\delta J}_{\text{linear in }\delta y} + (\text{higher-order terms}).
$$
Just as a function is stationary where its differential vanishes, a functional is stationary where $\delta J = 0$ for all admissible $\delta y$ — this is the necessary condition that leads to the Euler-Lagrange equation.

- **B** describes the *Gâteaux derivative* computation $\frac{d}{d\alpha}J(y+\alpha\eta)\big|_{\alpha=0}$, which is one *way to compute* the variation, not its definition.
- **C** is the **Euler-Lagrange operator**, which is the *result* of setting the variation to zero, not the variation itself.

## Related Concepts
- [[calculus-of-variations]]
- [[Gateaux-derivative]]
- [[Euler-Lagrange-equation]]
