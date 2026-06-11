---
id: orr_quiz03_03
course: Optimal and Robust Control
tags: [LQ-control, fixed-final-state, open-loop, feedforward]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
When the final state is fixed in the popular LQ problem, the result from the optimization gives

## Options
A) a (pre)computed control sequence.
B) a feedback controller.
C) an unstable response.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
When the final state is **fixed** (a point-to-point transfer problem), the optimal solution is obtained by solving the two-point boundary value problem for the specific given initial and final states. The result is an **open-loop, precomputed control sequence** $\mathbf{u}_0^\star,\dots,\mathbf{u}_{N-1}^\star$ — a feedforward signal tailored to that particular boundary pair.

This is in contrast to the **free final state** case, where the optimization (via the Riccati recursion) yields a **state-feedback law** $\mathbf{u}_k = -\mathbf{K}_k\mathbf{x}_k$. Fixing the endpoint removes the clean feedback structure and produces a trajectory-specific open-loop plan instead. (C is wrong — the open-loop solution is the optimal one, not inherently unstable.)

## Related Concepts
- [[open-loop-control]]
- [[fixed-final-state]]
- [[two-point-boundary-value-problem]]
