---
id: orr_quiz11_01
course: Optimal and Robust Control
tags: [H-infinity-control, mixed-sensitivity, weighting-filters, performance]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
One popular control design methodology is based on minimization of
$$
\left\lVert \begin{bmatrix} W_1 S \\ W_2 KS \\ W_3 T \end{bmatrix} \right\rVert_\infty .
$$
What is the role of $W_1$?

## Options
A) to guarantee closed-loop stability.
B) to express the requirements on the closed-loop performance such as bandwidth, disturbance attenuation, overshoot, ...
C) to express the requirements on the robustness with respect to input multiplicative uncertainty.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
This is the **mixed-sensitivity $\mathcal{H}_\infty$** problem ($S/KS/T$ stacking). Each weight shapes one closed-loop transfer function:
- **$W_1$ weights the sensitivity $S = (I+L)^{-1}$** — i.e., the **performance** channel (reference tracking, **disturbance attenuation**, **bandwidth**, low-frequency error, overshoot). Making $\|W_1 S\|$ small forces $S$ small where $W_1$ is large (typically low frequencies).
- **$W_2$ weights $KS$** (control effort / actuator activity, input-multiplicative robustness at the plant input).
- **$W_3$ weights $T = I-S$** (the complementary sensitivity → **robustness to output multiplicative uncertainty**, noise rejection at high frequency).

So $W_1$ is the **performance weight**. 
- **A is wrong:** stability is enforced by requiring the controller to *internally stabilize* the loop (a constraint of the problem), not by $W_1$.
- **C** is the role of $W_3$ (and partly $W_2$), not $W_1$.

## Related Concepts
- [[mixed-sensitivity]]
- [[sensitivity-function]]
- [[loop-shaping]]
- [[H-infinity-control]]
