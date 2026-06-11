---
id: nno_011
course: Nonsmooth Nonconvex Optimization
tags: [o-minimal, growth, dividing-lines, structures]
difficulty: 3
type: open
status: to_learn
---

# Question
Define what it means for an o-minimal structure to be **polynomially bounded** and **exponentially bounded**. (HW3/4 Ex 0.3 dividing lines)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** An o-minimal structure $\mathcal{R}$ is **polynomially bounded** if every definable $f:\mathbb{R}\to\mathbb{R}$ is eventually dominated by a power: there is $N\in\mathbb{N}$ with $|f(x)| \le x^N$ for all large $x$. It is **exponentially bounded** if every definable unary $f$ satisfies $|f(x)| \le \exp_k(x)$ for some finite iterate $\exp_k = \exp\circ\cdots\circ\exp$ for all large $x$.

## Explanation
These are the two main **dividing lines** (besides o-minimality itself) used to organize the universe of structures.

📖 Wiki: [Universe of structures](https://basta.github.io/nno-wiki/concepts/universe-of-structures) · [Tame geometry](https://basta.github.io/nno-wiki/concepts/tame-geometry)

- **Polynomially bounded:** ultimate growth of every definable function is polynomial. Examples: $\mathbb{R}_{\mathrm{alg}}$, $\mathbb{R}_{\mathrm{an}}$, $\mathrm{Pfaff}(\mathbb{R}_{\mathrm{alg}})$. **Miller's dichotomy:** an o-minimal structure is *either* polynomially bounded *or* it defines $\exp$ (so $\exp$ is definable as soon as you leave the polynomially bounded world).
- **Exponentially bounded:** growth is controlled by finitely-iterated exponentials. Examples: $\mathbb{R}_{\exp}$, $\mathbb{R}_{\mathrm{an,exp}}$. Whether *every* o-minimal structure is exponentially bounded is a known open-type question; some structures (e.g. ones built from fast-growing solutions) sit above this line.

**Field of exponents** ties in here: a polynomially bounded structure has a well-defined field of exponents (the set of admissible powers $x \mapsto x^\lambda$), whereas defining $\exp$ breaks polynomial boundedness.

These lines tell you *which functions are definable*: ReLU/polynomial losses live in the polynomially bounded zone; anything genuinely using $\exp$ (softmax, cross-entropy, sigmoid) requires at least $\mathbb{R}_{\exp}$.

## Related Concepts
- [[field_of_exponents]]
- [[universe_of_structures]]
- [[o_minimal_structure]]
