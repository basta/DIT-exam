---
id: orr_quiz09_06
course: Optimal and Robust Control
tags: [LQG, block-diagram, output-feedback, generalized-plant]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Consider the configuration in the figure below.

![[quiz09_06_lqg_artificial_plant.png]]

*(An "Artificial plant" block diagram: external inputs $v(t)$, $w(t)$ and control $u(t)$ enter through gains $\sqrt{S_v}$, $B_w\sqrt{S_w}$ and $B_u$ respectively; an integrator $\int dt$ produces the state $x(t)$ with feedback through $A$; outputs are formed as performance channels $z_1(t)=\sqrt{R}\,u$, $z_2(t)=\sqrt{Q}\,x$, and a measured output $y(t)=C_y x + \text{noise}$; a Controller closes the loop from $y$ to $u$.)*

It corresponds to which of the following problems?

## Options
A) LQR-optimal **state-feedback** control with the external disturbance by white and Gaussian noise with spectral density $S_w$.
B) LQG-optimal **output-feedback** control with the external disturbance and measurement noise modeled by white and Gaussian noises with spectral densities $S_w$ and $S_v$, respectively.
C) the technique called Loop Transfer Recovery (LTR) for robustification of LQG-optimal feedback control.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
The diagram is the **generalized-plant** representation of the **LQG** problem:
- **Two noise inputs** are present: process disturbance $w$ shaped by $B_w\sqrt{S_w}$ (spectral density $S_w$) and **measurement noise** $v$ shaped by $\sqrt{S_v}$ (spectral density $S_v$) added to the measured output $y$.
- The controller only sees the **measured output $y$** (not the full state) — hence **output feedback**, the hallmark of LQG.
- The performance outputs $z_1=\sqrt{R}\,u$ and $z_2=\sqrt{Q}\,x$ encode the LQ cost weights $\mathbf{R},\mathbf{Q}$, so that minimizing $\|z\|_2^2$ reproduces the quadratic criterion.

- **A is wrong:** there is a measurement-noise channel ($\sqrt{S_v}$) and the controller uses $y$, not $x$ — so it is *output* feedback, not state feedback, and not pure LQR.
- **C is wrong:** LTR is a *design tuning* procedure, not this interconnection itself.

## Related Concepts
- [[LQG]]
- [[generalized-plant]]
- [[output-feedback]]
