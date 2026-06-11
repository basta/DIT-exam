---
id: orr_quiz02_08
course: Optimal and Robust Control
tags: [MPC, preview-control, anticipatory-control, reference-tracking]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
With the MPC strategy it is possible to implement *anticipatory* (or *preview*) control, which means that the system is then capable of

## Options
A) finding the optimal control sequence while taking into consideration the provided a-priori knowledge of the reference signal.
B) attenuating unanticipated but measured disturbances acting on the system.
C) predicting (anticipating) the future values of the reference signal.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
**Preview (anticipatory) control** exploits the fact that, in many applications, **future values of the reference are known in advance** (e.g., a robot trajectory, a CNC tool path, a road profile in a vehicle). Because MPC optimizes over a future horizon, it can **use this known future reference inside the optimization** and start acting *before* the reference changes — improving tracking and reducing lag.

- **C is the key distractor:** preview does **not** mean the controller *predicts* an unknown reference. It means the future reference is **given/known** and fed into the optimizer. Anticipating an unknown future is impossible; the benefit comes from a-priori knowledge.
- **B** describes (measured/feedforward) disturbance rejection, a different (though related) capability.

## Related Concepts
- [[preview-control]]
- [[feedforward-control]]
- [[reference-trajectory]]
