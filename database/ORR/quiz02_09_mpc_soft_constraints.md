---
id: orr_quiz02_09
course: Optimal and Robust Control
tags: [MPC, soft-constraints, feasibility, slack-variables]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
The key motivation for introducing *soft constraints* in the MPC problem is

## Options
A) to avoid problems with the real-time optimization encountering infeasibility.
B) to guarantee that the state or output variables will not break some important constraints.
C) to reduce the computational burden (the number of variables will be reduced).
D) —

---
# Solution
**Correct Answer:** A

## Explanation
**Hard** state/output constraints can become **infeasible** — e.g., a large disturbance pushes a state outside its allowed band, so no control sequence can satisfy all constraints. A real-time solver facing an infeasible QP has no valid solution to apply, which is unacceptable for online control.

**Soft constraints** relax the constraint by adding a non-negative **slack variable** $\varepsilon \ge 0$ and heavily penalizing it in the cost:
$$
\mathbf{x}_k \le \overline{\mathbf{x}} + \varepsilon, \qquad \text{cost} \mathrel{+}= \rho\,\varepsilon \;\; (\rho \text{ large}).
$$
The constraint is then satisfied whenever possible, but if it cannot be, the problem stays **feasible** (the slack absorbs the violation) and the controller keeps running — minimizing the violation. So the motivation is to **preserve recursive feasibility**, not to guarantee constraints (B — that is what hard constraints do) and not to reduce computation (C — slacks *add* variables).

## Related Concepts
- [[soft-constraints]]
- [[slack-variables]]
- [[recursive-feasibility]]
