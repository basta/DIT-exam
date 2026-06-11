---
id: nno_009
course: Nonsmooth Nonconvex Optimization
tags: [definability, functions, structures]
difficulty: 2
type: open
status: to_learn
---

# Question
What is a **definable function** in a structure $\mathcal{R}$? (HW3/4 Ex 0.2)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** A function $f : A \to \mathbb{R}^m$ (with $A \subseteq \mathbb{R}^n$) is **definable in $\mathcal{R}$** if its **graph** $\Gamma(f) = \{(x,y) \in A\times\mathbb{R}^m : y = f(x)\}$ is a definable set, i.e. $\Gamma(f) \in \mathcal{R}_{n+m}$.

## Explanation
Definability of a function is reduced to definability of a set (its graph) — this is the standard move throughout the course.

📖 Wiki: [Definable functions](https://basta.github.io/nno-wiki/concepts/definable-functions)

Consequences and uses:

- The **domain** $A = \pi(\Gamma(f))$ and **image** $f[A]$ are definable (projections, S4).
- Compositions, sums, products, and inverses (where they exist) of definable functions are definable.
- In an **o-minimal** structure, a definable $f:(a,b)\to\mathbb{R}$ is piecewise continuous and monotone (**Monotonicity Theorem**), and even piecewise $C^k$ — but note HW2 Ex 0.11: a definable continuous Fréchet-differentiable $f$ is automatically $C^1$, a statement that can *fail* without definability.

To show a given function (e.g. an activation function ReLU, sigmoid, $\tanh$, or a loss) is definable in a structure, exhibit its graph as a definable set — e.g. ReLU has graph $\{(x,y): (x\le 0 \wedge y=0)\vee(x\ge 0\wedge y=x)\}$, semialgebraic, hence definable in every structure. By contrast $\exp$ is definable only from $\mathbb{R}_{\exp}$ upward.

## Related Concepts
- [[definable_set]]
- [[definable_set_valued_map]]
- [[monotonicity_theorem]]
- [[universe_of_structures]]
