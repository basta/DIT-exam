---
id: orr_quiz02_06
course: Optimal and Robust Control
tags: [MPC, sequential-formulation, constraints, true-false]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
If we formulate the MPC problem for a linear discrete-time system with a quadratic cost function in the sequential format, the optimization is only conducted over the control sequence. Is it then possible to include in the optimization also the constraints on the states and the outputs even if they do not explicitly appear among the optimization variables?

## Options
A) True (Pravda)
B) False (Nepravda)
C) —
D) —

---
# Solution
**Correct Answer:** A (True)

## Explanation
Yes. In the **sequential (single-shooting)** formulation the states are not free variables — they are written as an explicit (affine) function of the initial state and the control sequence:
$$
\mathbf{x}_k = \mathbf{A}^k \mathbf{x}_0 + \sum_{j=0}^{k-1}\mathbf{A}^{k-1-j}\mathbf{B}\,\mathbf{u}_j .
$$
Substituting this expression into a state/output constraint $\underline{\mathbf{x}} \le \mathbf{x}_k \le \overline{\mathbf{x}}$ turns it into a **linear inequality constraint on the control sequence** $\mathbf{u}_0,\dots,\mathbf{u}_{N-1}$. So even though the states are eliminated as decision variables, their constraints are still enforced — they just become (denser) constraints on the controls. The resulting problem is still a QP.

## Related Concepts
- [[single-shooting]]
- [[state-constraints]]
- [[MPC-QP-formulation]]
