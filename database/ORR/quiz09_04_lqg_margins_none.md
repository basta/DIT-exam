---
id: orr_quiz09_04
course: Optimal and Robust Control
tags: [LQG, robustness, gain-margin, phase-margin, Doyle]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The gain and phase margins, GM and PM, respectively, for a feedback loop with an LQG-optimal feedback controller are

## Options
A) guaranteed to have the values of $GM = \infty, PM = 60^\circ$, but only in absence of noise entering the system at the input.
B) guaranteed to have the values of $GM = \infty, PM = 60^\circ$.
C) never guaranteed.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
While LQR (full state feedback) has guaranteed margins, **LQG has no guaranteed robustness margins whatsoever**. This is the famous conclusion of **John C. Doyle's 1978 paper "Guaranteed Margins for LQG Regulators,"** whose abstract reads in full: *"There are none."*

Inserting the Kalman filter between the measurements and the LQR gain breaks the return-difference property at the plant input, and the resulting output-feedback loop can have **arbitrarily small** gain and phase margins for particular plant/noise data. The estimator's dynamics destroy the guarantees that the state-feedback loop enjoyed.

- **A and B** wrongly carry the LQR margins over to LQG — exactly the misconception Doyle refuted.

This motivated the development of **LQG/LTR** (loop transfer recovery) and, more generally, $\mathcal{H}_\infty$ / $\mu$-synthesis robust control.

## Related Concepts
- [[LQG]]
- [[loop-transfer-recovery]]
- [[robustness-margins]]
