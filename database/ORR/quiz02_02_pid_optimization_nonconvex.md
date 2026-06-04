---
id: orr_quiz02_02
course: Optimal and Robust Control
tags: [controller-tuning, nonconvexity, stability, optimization]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
One approach to optimal control is to do the numerical optimization directly over the controller coefficients. Say, we decide to find the optimal coefficients for a PID controller. What are the key computational challenges?

## Options
A) It is generally impossible to relate the values of the controller parameters to the value of the cost functions.
B) The set of controller parameters that guarantee closed-loop stability is in general nonconvex, which renders the optimization nonconvex too.
C) The number of parameters of a typical controller is too high.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
Optimizing directly over controller coefficients (a "fixed-structure" controller such as PID) is attractive but hard, because the **set of stabilizing controller parameters is generally nonconvex** (and may even be disconnected). Since any meaningful cost only makes sense over stabilizing controllers, the feasible region is nonconvex, so the optimization is nonconvex — it can have multiple local minima and no guarantee that a solver finds the global optimum.

- **A is false:** the cost *can* be evaluated for any given parameter set by simulating/computing the closed loop; the issue is the shape of the feasible set, not computability.
- **C is false:** a PID has only 3 parameters — the difficulty is not dimensionality but nonconvexity.

This is exactly why methods like LQ/LQG/$\mathcal{H}_\infty$, which reformulate the design as a convex or analytically solvable problem, are preferred over brute-force coefficient search.

## Related Concepts
- [[fixed-structure-control]]
- [[nonconvex-optimization]]
- [[closed-loop-stability]]
