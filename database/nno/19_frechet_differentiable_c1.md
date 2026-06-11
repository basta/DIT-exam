---
id: nno_019
course: Nonsmooth Nonconvex Optimization
tags: [differentiability, smoothness, definability]
difficulty: 2
type: open
status: to_learn
---

# Question
Define **Fréchet-differentiable** and **$C^1$-smooth** for $f:I\to\mathbb{R}$, and state the o-minimal regularity phenomenon. (HW2 Ex 0.11)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $f$ is **Fréchet-differentiable** at $x$ if there is a linear map $Df(x)$ with $\lim_{h\to 0}\frac{\|f(x+h)-f(x)-Df(x)h\|}{\|h\|}=0$. $f$ is **$C^1$-smooth** if it is Fréchet-differentiable everywhere and $x\mapsto Df(x)$ is continuous.

## Explanation
Fréchet differentiability is the genuine (basis-free) notion of differentiability: a linear approximation with error $o(\|h\|)$. $C^1$ adds continuity of the derivative map.

**The o-minimal phenomenon (HW2 Ex 0.11):** if $f$ is **definable** in an o-minimal structure and $I\subseteq\mathbb{R}$ is an open interval on which $f$ is continuous and (everywhere) Fréchet-differentiable, then $f$ is automatically **$C^1$-smooth**.

- *Why it holds in the definable world:* $f'$ is itself definable, hence (Monotonicity Theorem) piecewise continuous and monotone with only finitely many discontinuities — but a derivative has the Darboux (intermediate value) property, so it cannot have jump discontinuities; therefore $f'$ is continuous.
- *Why it fails without definability:* the classical example $f(x)=x^2\sin(1/x)$ (with $f(0)=0$) is everywhere differentiable but $f'$ is discontinuous at $0$ — and $x^2\sin(1/x)$ is **not** definable in any o-minimal structure (it oscillates infinitely).

This is a recurring exam point: **o-minimality upgrades pointwise regularity to uniform/continuous regularity.**

## Related Concepts
- [[monotonicity_theorem]]
- [[definable_function]]
- [[c1_manifold_tangent_space]]
- [[rademacher_theorem]]
