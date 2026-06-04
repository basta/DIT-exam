---
id: orr_quiz09_05
course: Optimal and Robust Control
tags: [LQG, LTR, loop-transfer-recovery, robustness]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
The key idea behind the technique of Loop Transfer Recovery (LTR) is

## Options
A) the unmeasured states of the system can be estimated from the (control) inputs and (measured) outputs to the system.
B) while *implementing* the optimal LQG controller, a physical noise must be created and injected into the system in the same manner as the control signal. The spectral density of this artificial noise is then used as a tuning parameter for robustness of the resulting feedback loop.
C) while *computing* the optimal LQG controller, an artificial noise is assumed to be entering the system in the same manner as the control signal. The spectral density of this artificial noise is then used as a tuning parameter for robustness of the resulting feedback loop.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
**LTR** is a procedure to recover the good robustness of the (full-state) LQR loop in the observer-based LQG controller, whose margins are otherwise lost. The trick: when **designing the Kalman filter**, pretend there is an extra **fictitious process noise entering at the plant input** with covariance $q\,\mathbf{B}\mathbf{B}^T$. As the tuning parameter $q \to \infty$, the Kalman gain grows so that the **LQG loop transfer function converges to the target LQR loop transfer function** — thereby "recovering" the desirable LQR margins.

The crucial word is **"computing/assuming"**: the noise is a **mathematical fiction used in the design equations only** — nothing is physically injected (so **B is wrong**). 
- **A** merely describes what an observer does — that's the principle of state estimation, not LTR.

Trade-off: large $q$ recovers robustness but makes the filter behave like a high-gain/inverse-dynamics observer, sensitive to real measurement noise — so LTR balances robustness recovery against noise amplification.

## Related Concepts
- [[loop-transfer-recovery]]
- [[LQG]]
- [[Kalman-filter]]
