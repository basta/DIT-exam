---
id: nno_001
course: Nonsmooth Nonconvex Optimization
tags: [prerequisites, set-theory, boolean-algebra]
difficulty: 1
type: open
status: to_learn
---

# Question
Define a **boolean algebra of subsets** of a set $X$, and state the equivalent characterizations in terms of closure operations. (HW1 Ex 0.2)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A nonempty collection $\mathcal{C} \subseteq \mathcal{P}(X)$ is a boolean algebra of subsets of $X$ if it is closed under finite intersection and under complement (relative to $X$).

## Explanation
A **boolean algebra of subsets** is the basic algebraic object the whole course is built on: the "definable sets" of a structure form one in each dimension. Given a set $X$ with power set $\mathcal{P}(X)$, a nonempty $\mathcal{C} \subseteq \mathcal{P}(X)$ is a boolean algebra if it is closed under the boolean operations.

HW1 Ex 0.2 asks you to prove that the following are equivalent for a nonempty $\mathcal{C}$:

1. $\mathcal{C}$ is a boolean algebra of subsets of $X$;
2. for every $A, B \in \mathcal{C}$, both $A \cap B \in \mathcal{C}$ and $X \setminus A \in \mathcal{C}$;
3. for every $A, B \in \mathcal{C}$, $X \setminus (A \cap B) \in \mathcal{C}$.

From closure under $\cap$ and complement one recovers $\cup$ via De Morgan, and $\varnothing, X \in \mathcal{C}$ (since $\mathcal{C}$ is nonempty: take any $A$, then $A \cap (X\setminus A) = \varnothing$ and its complement $X$).

**Proof technique (for the equivalences):** push everything through De Morgan's laws; (3) is a compact single-operation axiomatization (a "Sheffer-stroke" style condition) from which (2) is recovered by setting $A=B$.

## Related Concepts
- [[atom_boolean_algebra]]
- [[semialgebraic_set]]
- [[definable_set]]
