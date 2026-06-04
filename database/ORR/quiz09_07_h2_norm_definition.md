---
id: orr_quiz09_07
course: Optimal and Robust Control
tags: [H2-norm, system-norms, impulse-response]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
The $\mathcal{H}_2$ norm of a linear (model of a) dynamical system is defined as

## Options
A) the 2-norm of the impulse response of the system.
B) the peak in the magnitude frequency response.
C) the max-norm of the step response of the system.
D) —

---
# Solution
**Correct Answer:** A

## Explanation
The $\mathcal{H}_2$ norm equals the **2-norm (energy) of the system's impulse response** $g(t)$:
$$
\|G\|_2 = \left(\int_0^\infty \|g(t)\|_F^2\,dt\right)^{1/2}
= \left(\frac{1}{2\pi}\int_{-\infty}^{\infty}\|G(j\omega)\|_F^2\,d\omega\right)^{1/2},
$$
the two expressions being equal by **Parseval's theorem** (time-domain energy = frequency-domain energy). Stochastically, $\|G\|_2^2$ is the **output variance** when the input is unit-intensity white noise — which is exactly why $\mathcal{H}_2$ optimal control corresponds to the LQG problem.

- **B (peak of the magnitude response)** is the **$\mathcal{H}_\infty$ norm**, a different system norm.
- **C** is not a standard system norm.

## Related Concepts
- [[H2-norm]]
- [[H-infinity-norm]]
- [[Parseval-theorem]]
- [[impulse-response]]
