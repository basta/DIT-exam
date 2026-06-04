---
id: orr_quiz02_03
course: Optimal and Robust Control
tags: [optimal-control, problem-formulation, simultaneous, sequential]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
The problem of finding the optimal control sequence for a discrete-time dynamical system can be formulated in two formats — *simultaneous* and *sequential*. Which one contains a smaller number of optimization variables?

## Options
A) Simultaneous.
B) Sequential.
C) Both formats have the same number of optimization variables.
D) —

---
# Solution
**Correct Answer:** B

## Explanation
- **Simultaneous (a.k.a. "full discretization"):** the optimizer treats **both** the control sequence $\mathbf{u}_0,\dots,\mathbf{u}_{N-1}$ **and** the state sequence $\mathbf{x}_1,\dots,\mathbf{x}_N$ as free variables, with the system dynamics $\mathbf{x}_{k+1}=f(\mathbf{x}_k,\mathbf{u}_k)$ enforced as **equality constraints**. More variables, but a sparse, structured problem.
- **Sequential (a.k.a. "single shooting"):** only the **controls** are optimization variables; the states are obtained by *simulating* the model forward from the controls. The dynamics are eliminated as constraints.

So the sequential format has **fewer optimization variables** (controls only). The trade-off: sequential gives a smaller but denser/more nonlinear problem and can be numerically ill-conditioned for unstable systems, whereas simultaneous gives a larger but sparser and better-conditioned problem.

## Related Concepts
- [[single-shooting]]
- [[multiple-shooting]]
- [[direct-transcription]]
