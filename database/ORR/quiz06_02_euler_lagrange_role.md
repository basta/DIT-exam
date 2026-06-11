---
id: orr_quiz06_02
course: Optimal and Robust Control
tags: [calculus-of-variations, Euler-Lagrange, necessary-condition]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Choose the correct description of the role of the Euler-Lagrange equation
$$
\frac{\partial L(x,y,y')}{\partial y} - \frac{d}{dx}\frac{\partial L(x,y,y')}{\partial y'} = 0
$$
in the calculus of variations.

## Options
A) It represents a first-order necessary condition of optimality for the cost function $J(y) = L(x,y,y')$.
B) It represents a first-order necessary condition of optimality for the cost function $J(y) = \int_a^b L(x,y,y')\,dx$.
C) It represents a condition of stability of a closed-loop system.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
The Euler-Lagrange equation is the **first-order necessary condition** for a function $y(x)$ to be an extremal of an **integral functional**
$$
J(y) = \int_a^b L(x,y,y')\,dx .
$$
It is derived by setting the variation $\delta J = 0$ for all admissible variations and applying integration by parts (using fixed-endpoint boundary conditions). Any minimizer must satisfy it (it is necessary, not sufficient).

- **A is wrong:** the cost is a *functional defined by an integral* of $L$, not the integrand $L$ itself.
- **C is wrong:** the Euler-Lagrange equation is about optimality of a functional, not closed-loop stability.

## Related Concepts
- [[Euler-Lagrange-equation]]
- [[integral-functional]]
- [[necessary-condition-of-optimality]]
