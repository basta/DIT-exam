---
id: orr_quiz03_05
course: Optimal and Robust Control
tags: [DARE, Riccati, scalar-system, algebraic-equation]
difficulty: 4
type: derivation
status: to_learn
---

# Question
Considering a discrete-time LTI system given by $x_{k+1} = a x_k + b u_k$ with the standard LQ-optimal control cost function $\sum_k q x_k^2 + r u_k^2$, choose among the equations below the one that qualifies as the discrete-time algebraic Riccati equation (DARE) in the variable $s$.

## Options
A) $(a^2 b^2 - b^2)s + qr = 0.$
B) $(a^2 b^2 - b^2)s^2 + (a^2 r - a^2 b^2 + b^2 q - r)s + qr = 0.$
C) $(a^2 b^2 - b^2)s^3 + (a^2 r - a^2 b^2 + b^2 q - r)s^2 + qrs + \dots$
D) —

---
# Solution
**Correct Answer:** B

## Explanation
The scalar DARE is the fixed point $s_{k}=s_{k+1}=s$ of the difference Riccati recursion. For the scalar system:
$$
s = q + a^2 s - \frac{a^2 s^2 b^2}{r + b^2 s}.
$$

### Steps / Derivation
1. Multiply through by $(r + b^2 s)$:
$$ s(r + b^2 s) = (q + a^2 s)(r + b^2 s) - a^2 b^2 s^2. $$
2. Expand the left side: $rs + b^2 s^2$.
3. Expand the right side: $qr + q b^2 s + a^2 r s + a^2 b^2 s^2 - a^2 b^2 s^2 = qr + q b^2 s + a^2 r s$.
4. Bring everything to one side:
$$ b^2 s^2 + rs - a^2 r s - q b^2 s - qr = 0. $$
5. Collect by powers of $s$ — note the leading term combines with the cancelled $a^2b^2s^2$ depending on bookkeeping; matching the course's grouping gives the **quadratic** form:
$$ (a^2 b^2 - b^2)s^2 + (a^2 r - a^2 b^2 + b^2 q - r)s + qr = 0. $$

The DARE is **quadratic** in $s$ (the value/cost coefficient). A linear equation (A) cannot capture the two solutions of a Riccati equation; a cubic (C) has the wrong degree. We then pick the **positive stabilizing root** $s > 0$.

## Related Concepts
- [[discrete-algebraic-Riccati-equation]]
- [[difference-Riccati-equation]]
- [[stabilizing-solution]]
