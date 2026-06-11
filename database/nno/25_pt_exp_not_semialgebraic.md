---
id: nno_025
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, semialgebraic, exp]
difficulty: 3
type: derivation
status: to_learn
---

# Question
**Proof technique.** Sketch a proof that the total exponential $\exp:\mathbb{R}\to\mathbb{R}$ is **not a semialgebraic** function. (HW1 Ex 0.5)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** If $\Gamma(\exp)$ were semialgebraic it would lie in $\{P(x,y)=0\}$ for some nonzero polynomial $P$; substituting $y=e^x$ gives an exponential-polynomial identity with infinitely many zeros, forcing $P\equiv 0$ — contradiction. Equivalently, $\exp$ grows faster than every polynomial, contradicting the polynomial growth of semialgebraic functions.

## Explanation
📖 Wiki: [Semialgebraic sets](https://basta.github.io/nno-wiki/concepts/semialgebraic) · [Universe of structures](https://basta.github.io/nno-wiki/concepts/universe-of-structures)

### Steps / Derivation
1. **Use the structure of semialgebraic functions.** A semialgebraic $f:\mathbb{R}\to\mathbb{R}$ has a semialgebraic graph, so there is a nonzero $P\in\mathbb{R}[X,Y]$ vanishing on an infinite piece of $\Gamma(f)$; in $\mathbb{R}^1$ semialgebraic functions are **piecewise algebraic** and have **polynomially bounded growth**.
2. **Growth argument (cleanest):** every semialgebraic $f$ satisfies $|f(x)|\le C x^N$ for large $x$ (it is asymptotic to $c x^{q}$, $q\in\mathbb{Q}$). But $e^x / x^N \to \infty$ for every $N$. Hence $\exp$ is not semialgebraic.
3. **Algebraic-identity argument (alternative):** suppose $P(x,e^x)=0$ for all $x$, $P=\sum_j p_j(x) y^j$. Then $\sum_j p_j(x) e^{jx}=0$ identically. Distinct exponentials $e^{jx}$ are linearly independent over the polynomials (compare growth rates / Wronskian), so all $p_j\equiv 0$, i.e. $P\equiv 0$.
4. **Consequence:** $\exp$ is definable only from $\mathbb{R}_{\exp}$ upward; in particular any o-minimal structure defining $\exp$ is **not polynomially bounded** (Miller's dichotomy).

**Technique to name in the exam:** "compare asymptotic growth" and "linear independence of distinct exponentials."

## Related Concepts
- [[semialgebraic_set]]
- [[polynomially_exponentially_bounded]]
- [[universe_of_structures]]
