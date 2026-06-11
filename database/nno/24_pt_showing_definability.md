---
id: nno_024
course: Nonsmooth Nonconvex Optimization
tags: [proof-technique, definability, structures]
difficulty: 3
type: derivation
status: to_learn
---

# Question
**Proof technique.** You are asked to show a given set/function is **definable** in a structure $\mathcal{R}$. What is the general toolkit? (HW3/4 Ex 0.2)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Express the set by a **first-order formula** over the basic definable relations, then justify each connective via a closure axiom: boolean ops (S1), dummy variables/cylinders (S2), equalities (S3), $\exists$ = projection (S4), $<$ (S5), $+,\cdot$ (S6); reduce any transcendental piece to a function already known to be definable in $\mathcal{R}$.

## Explanation
📖 Wiki: [Definable sets](https://basta.github.io/nno-wiki/concepts/definable-sets) · [Definable functions](https://basta.github.io/nno-wiki/concepts/definable-functions)

### Steps / Derivation
1. **Write a defining formula.** Describe the set as $\{x : \varphi(x)\}$ where $\varphi$ uses $=, <, +, \cdot$, the extra primitives of $\mathcal{R}$ (e.g. $\exp$), boolean connectives, and quantifiers over real variables.
2. **Translate each connective to an axiom:**
   - $\wedge,\vee,\neg \rightarrow$ (S1) boolean algebra;
   - free/dummy variables $\rightarrow$ (S2) cylinders;
   - $x_i = x_j \rightarrow$ (S3) diagonals;
   - $\exists y\ \rightarrow$ (S4) projection; $\forall y$ via $\neg\exists\neg$;
   - $<, +, \cdot \rightarrow$ (S5),(S6).
3. **For functions:** show the **graph** $\{(x,y): y=f(x)\}$ is definable (a function is definable iff its graph is). Domain and image then follow by projection.
4. **Composition / reduction:** preimages and images under definable maps are definable; so reduce to known definable building blocks (polynomials always; $\exp$ from $\mathbb{R}_{\exp}$; restricted analytic from $\mathbb{R}_{\mathrm{an}}$; Pfaffian functions; etc.).
5. **Topological predicates are first-order:** "$x\in\mathrm{cl}(A)$", "$x\in\mathrm{int}(A)$", "$A$ is nowhere dense", "$f$ is continuous at $x$" all unwind to $\forall\varepsilon\exists\delta$ formulas, hence preserve definability (HW1 Ex 0.15).

**Pitfall:** only **finite** boolean combinations and **single** quantifiers are allowed. Anything requiring an *infinite* union or a *least-fixed-point* (e.g. transitive closure, "$n\in\mathbb{N}$") is generally **not** definable.

## Related Concepts
- [[definable_set]]
- [[structure_axioms_s1_s6]]
- [[pt_transitive_closure_not_definable]]
