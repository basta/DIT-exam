---
id: orr_quiz09_02
course: Optimal and Robust Control
tags: [LQR, gain-margin, phase-margin, robustness]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The gain and phase margins, GM and PM, respectively, for LQ-optimal state feedback regulation (a.k.a. LQR) are

## Options
A) only guaranteed in absence of disturbances.
B) not guaranteed at all.
C) guaranteed some concrete minimum values, namely $GM_+ = \infty, GM_- = 1/2, PM = \pm 60^\circ$, no matter what the actual system dynamics and cost function is.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
A celebrated result: **LQR has guaranteed robustness margins** that hold for *any* plant and *any* valid weighting matrices (with full state feedback). These follow from the **Kalman (return-difference) inequality** $|1 + L(j\omega)| \ge 1$ satisfied by the LQR loop gain $L$, which keeps the Nyquist plot out of the unit disc centred at $-1$. The guaranteed margins are:
$$
GM_+ = \infty,\quad GM_- = \tfrac{1}{2}\;(\text{i.e. }-6\text{ dB}),\quad PM = \pm 60^\circ.
$$
Interpretation: the loop gain can be **increased without bound** or **halved** without losing stability, and tolerates at least $\pm 60^\circ$ of phase lag/lead.

These hold regardless of disturbances (so A is wrong) and are very much guaranteed (so B is wrong). **Caveat:** they hold only when the loop is broken at the **plant input** with **full state feedback** — they are *lost* once an observer/Kalman filter is inserted (the LQG case, see quiz #9 Q4).

## Related Concepts
- [[LQR]]
- [[Kalman-inequality]]
- [[gain-and-phase-margins]]
