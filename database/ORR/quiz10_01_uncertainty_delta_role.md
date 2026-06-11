---
id: orr_quiz10_01
course: Optimal and Robust Control
tags: [robust-control, uncertainty, delta-block]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
For the purpose of characterizing (or bounding) uncertainty in models of dynamical systems, we introduced an object labelled $\Delta$. What is its role in uncertainty characterization?

## Options
A) It can make the phase completely arbitrary. The gain is only partially arbitrary since it must be bounded by one.
B) It can make the gain completely arbitrary. The phase is fixed.
C) It introduces an unknown delay into the system.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
The uncertainty block $\Delta$ is a **norm-bounded** but otherwise **unknown** stable operator, normalized so that $\|\Delta\|_\infty \le 1$. The actual size/shape of the uncertainty is pulled out into a known **weighting filter** $W$, leaving $\Delta$ to represent "anything of unit norm."

Because $\|\Delta\|_\infty \le 1$:
- the **gain** of $\Delta$ is constrained — it can be anything **up to magnitude one** ("partially arbitrary, bounded by one"), and
- the **phase** of $\Delta$ is **completely unconstrained** — it can take any value.

This is exactly what makes $W\Delta$ a powerful uncertainty model: the weight $W$ sets the frequency-dependent magnitude envelope, while $\Delta$ realizes any phase and any gain within that envelope — covering the worst case.

- **B** has it backwards (gain is the bounded quantity, not the phase).
- **C** describes a specific delay uncertainty, not the general normalized $\Delta$ block.

## Related Concepts
- [[norm-bounded-uncertainty]]
- [[weighting-filter]]
- [[unstructured-uncertainty]]
