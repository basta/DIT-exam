---
id: orr_quiz09_03
course: Optimal and Robust Control
tags: [LQG, Kalman-filter, LQR, separation-principle]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
What does LQG stand for?

## Options
A) LQ-optimal state feedback for a stochastic system.
B) Combination of an LQ-optimal state feedback (a.k.a. LQR) and a Kalman filter (serving as an observer here).
C) LQ-optimal static (or proportional) output feedback.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
**LQG = Linear–Quadratic–Gaussian.** It is the optimal **output-feedback** controller for a linear system with **Gaussian** process and measurement noise and a **quadratic** cost. By the **separation principle**, the optimal solution decomposes into two independently-designed parts:
1. a **Kalman filter** that produces the minimum-variance state estimate $\hat{\mathbf{x}}$ from the noisy outputs, and
2. the **LQR** state-feedback gain applied to the estimate: $\mathbf{u} = -\mathbf{K}\hat{\mathbf{x}}$.

So LQG is precisely the **interconnection of an LQR (optimal regulator) and a Kalman filter (optimal estimator)**. 
- **A** is too vague and ignores the estimator/output-feedback structure.
- **C** describes static output feedback — LQG is a dynamic (observer-based) controller, not a proportional output feedback.

## Related Concepts
- [[LQG]]
- [[Kalman-filter]]
- [[separation-principle]]
