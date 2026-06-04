---
id: orr_quiz08_01
course: Optimal and Robust Control
tags: [numerical-methods, shooting-method, BVP, sensitivity]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
One of the numerical methods for two-point boundary value problems is called the *shooting method*. What is the major disadvantage of the method?

## Options
A) The method is only applicable to linear systems and quadratic cost functions.
B) The differential equations that give the necessary conditions of optimality are very often very sensitive to changes in the initial conditions. Hence any slight perturbation in the initial value of the costate $\lambda$ can cause huge deviations in the value of the state $x$ and costate $\lambda$ at the end of the time interval.
C) The method imposes huge requirements on storing the data in memory. In particular, all the state, costate and control trajectories need to be stored.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
The **shooting method** turns a two-point BVP into an initial value problem: guess the unknown initial costate $\boldsymbol{\lambda}(0)$, integrate the canonical equations forward, and iterate on the guess until the terminal boundary condition is met.

Its major weakness is **extreme sensitivity to the initial guess**. The Hamiltonian (canonical) dynamics typically have **eigenvalues symmetric about the imaginary axis** — for every stable mode there is an unstable mirror mode. Integrating forward excites the **unstable** modes, so a tiny error in $\boldsymbol{\lambda}(0)$ is **exponentially amplified**, producing enormous deviations at $t_f$. This makes the iteration ill-conditioned and hard to converge.

The standard remedy is **multiple shooting**: split the interval into shorter sub-intervals (limiting how much error can grow on each) with matching/continuity constraints.

- **A** is false — shooting applies to general nonlinear problems.
- **C** is not the defining drawback (storage is modest; sensitivity is the real issue).

## Related Concepts
- [[shooting-method]]
- [[multiple-shooting]]
- [[Hamiltonian-system]]
- [[numerical-conditioning]]
