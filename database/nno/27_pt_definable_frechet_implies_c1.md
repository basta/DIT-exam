---
id: nno_027
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, o-minimal, differentiability, monotonicity]
difficulty: 3
type: derivation
status: to_learn
---

# Question
**Proof technique.** A **definable** $f:I\to\mathbb{R}$ on an open interval is continuous and Fréchet-differentiable. Sketch why it must be **$C^1$**, and why this fails without definability. (HW2 Ex 0.11)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** $f'$ is definable, so by the **Monotonicity Theorem** it is piecewise continuous and monotone with only finitely many possible discontinuities; but a derivative has the **Darboux (intermediate-value) property**, which rules out jump discontinuities — so $f'$ is continuous, i.e. $f\in C^1$.

## Explanation
📖 Wiki: [Monotonicity theorem](https://basta.github.io/nno-wiki/concepts/monotonicity-theorem) · [Definable functions](https://basta.github.io/nno-wiki/concepts/definable-functions)

### Steps / Derivation
1. **$f'$ is definable.** The derivative is a first-order limit: $f'(x)=v \iff \forall\varepsilon\exists\delta\,\forall h\,(0<|h|<\delta \Rightarrow |\tfrac{f(x+h)-f(x)}{h}-v|<\varepsilon)$. Quantifiers over reals preserve definability, so $\Gamma(f')$ is definable.
2. **Monotonicity Theorem.** In an o-minimal structure, a definable unary function is, off a finite set of breakpoints, continuous and either constant or strictly monotone on each subinterval. Hence $f'$ has at most finitely many discontinuities, all of "jump/removable" type.
3. **Darboux property.** Every derivative satisfies the intermediate value property (whether or not it is continuous). A function with the IVP cannot have a genuine jump discontinuity — at a jump it would skip intermediate values.
4. **Combine.** Finitely many possible discontinuities (step 2) all forbidden (step 3) $\Rightarrow$ $f'$ is continuous everywhere $\Rightarrow$ $f\in C^1$.
5. **Failure without definability.** $f(x)=x^2\sin(1/x)$, $f(0)=0$, is everywhere differentiable but $f'$ oscillates and is discontinuous at $0$. It is **not definable** in any o-minimal structure (infinite oscillation violates (O2)), so o-minimality is essential.

**Technique to name:** "definable $\Rightarrow$ Monotonicity Theorem $\Rightarrow$ finitely many discontinuities; kill them with Darboux."

## Related Concepts
- [[frechet_differentiable_c1]]
- [[monotonicity_theorem]]
- [[o_minimal_structure]]
