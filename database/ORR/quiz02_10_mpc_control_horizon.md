---
id: orr_quiz02_10
course: Optimal and Robust Control
tags: [MPC, control-horizon, prediction-horizon, tuning]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
One of the parameters of a Model Predictive Controller (MPC) is the *control horizon*. The rule of thumb is to set it

## Options
A) a bit higher than the prediction horizon.
B) equal to the prediction horizon.
C) as low as possible. Setting it to 2 is not uncommon.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
The **control horizon** $N_c$ is the number of future control moves that are actually optimized as free variables (after $N_c$ the input is held constant or set to the terminal feedback). The **prediction horizon** $N_p \ge N_c$ is how far ahead the response is evaluated.

The rule of thumb is to keep $N_c$ **small** (e.g., 1–3; "2 is not uncommon") while keeping $N_p$ large enough to capture the dominant dynamics:
- Each control move is a block of decision variables, so a small $N_c$ **drastically reduces the QP size** and computational load.
- A short control horizon also tends to give **smoother, less aggressive** control and improves numerical conditioning.
- Most of the closed-loop performance is determined by a long prediction horizon, not by many free control moves.

- **A is impossible** ($N_c$ cannot exceed $N_p$), and **B** is wasteful (large QP, little benefit).

## Related Concepts
- [[control-horizon]]
- [[prediction-horizon]]
- [[MPC-tuning]]
