---
id: orr_quiz04_01
course: Optimal and Robust Control
tags: [dynamic-programming, Bellman, principle-of-optimality]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Choose the correct statement of Bellman's principle of optimality.

## Options
A) An optimal policy has the property that no matter what the previous decisions (i.e., controls) have been, the remaining decisions must constitute an optimal policy with regard to the (current) state resulting from those previous decisions.
B) An optimal policy must take into consideration all the previous decisions (i.e., controls). It is not sufficient to base the remaining decisions just on the (current) state resulting from those previous decisions, if it is to constitute an optimal policy.
C) An optimal policy must always be found by exhaustive search over all possible states.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
Bellman's **principle of optimality** is the foundation of dynamic programming. It states that, whatever the initial state and initial decisions, the **remaining decisions form an optimal policy with respect to the state that results** from the first decision. In other words, **tails of optimal trajectories are themselves optimal**.

The deep consequence is that the optimal cost-to-go depends **only on the current state**, not on the history of how we arrived there (the Markov property of optimality). This is exactly what option B *denies* — making B the wrong (and crucially anti-DP) statement. Option C describes brute force, which the principle of optimality lets us *avoid* by recursively building the solution backward (the Bellman recursion $J_k^\star(x_k) = \min_{u_k}\{L_k + J_{k+1}^\star(x_{k+1})\}$).

## Related Concepts
- [[dynamic-programming]]
- [[principle-of-optimality]]
- [[cost-to-go]]
