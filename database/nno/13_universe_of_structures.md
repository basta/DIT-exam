---
id: nno_013
course: Nonsmooth Nonconvex Optimization
tags: [structures, o-minimal, universe, dividing-lines]
difficulty: 4
type: open
status: to_learn
---

# Question
Name and define the structures in the **universe of structures on $\mathbb{R}$**, and their inclusions:
$\mathbb{R}_{\mathrm{alg}},\ \mathbb{R}_{\mathrm{RE}},\ \mathbb{R}_{\mathrm{an}},\ \mathbb{R}_{\exp},\ \mathbb{R}_{\mathrm{an,exp}},\ \mathrm{Pfaff}(\mathbb{R}_{\mathrm{alg}}),\ \mathrm{Pfaff}(\mathbb{R}_{\mathrm{an}}),\ (\mathbb{R}_{\mathrm{alg}},2^{\mathbb{Z}}),\ \mathbb{R}_{\mathrm{PH}},\ \mathcal{R}^{\top}$. (HW3/4 Ex 0.3)

## Options
A) N/A
B) N/A
C) N/A
D) N/A

---
# Solution
**Correct Answer:** Each is the smallest structure containing $\mathbb{R}_{\mathrm{alg}}$ together with extra definable functions; they are ordered by inclusion and stratified by the dividing lines (o-minimal / polynomially bounded / exponentially bounded).

## Explanation
📖 Wiki: [Universe of structures](https://basta.github.io/nno-wiki/concepts/universe-of-structures) · [Structures](https://basta.github.io/nno-wiki/concepts/structures) · [Pfaffian functions](https://basta.github.io/nno-wiki/concepts/pfaffian-functions) · [Real-analytic](https://basta.github.io/nno-wiki/concepts/real-analytic) · [Algebraic functions](https://basta.github.io/nno-wiki/concepts/algebraic-functions)

- **$\mathbb{R}_{\mathrm{alg}}$** — the real ordered field; definable = semialgebraic. Smallest o-minimal structure. Poly. bounded, exponents $\mathbb{Q}$.
- **$\mathbb{R}_{\mathrm{an}}$** — expansion by all **restricted analytic** functions (real-analytic on a neighborhood of $[-1,1]^n$, zero outside). O-minimal (Denef–van den Dries), poly. bounded, exponents $\mathbb{Q}$.
- **$\mathbb{R}_{\exp}$** — expansion by the total $\exp:\mathbb{R}\to\mathbb{R}$. O-minimal (Wilkie), **not** poly. bounded, exponentially bounded, exponents $\mathbb{R}$.
- **$\mathbb{R}_{\mathrm{an,exp}}$** — both restricted analytic functions and $\exp$. O-minimal, exponentially bounded; the "largest standard" tame structure for ML, contains $\log$, $\Gamma|_{(0,\infty)}$, sigmoid, softmax.
- **$\mathbb{R}_{\mathrm{RE}}$** — restricted elementary: $\exp|_{[a,b]}, \sin|_{[a,b]}, \cos|_{[a,b]}$ (HW1 Ex 0.17). O-minimal, poly. bounded (restricted, so no global $\exp$ growth). Lets you define $\arctan$.
- **$\mathrm{Pfaff}(\mathbb{R}_{\mathrm{alg}})$, $\mathrm{Pfaff}(\mathbb{R}_{\mathrm{an}})$** — expansions by **Pfaffian functions** (solutions of triangular polynomial ODE systems; Khovanskii finiteness). O-minimal, poly. bounded.
- **$(\mathbb{R}_{\mathrm{alg}}, 2^{\mathbb{Z}})$** — real field with the predicate for powers of two. **Not o-minimal** (defines a discrete infinite set), but still model-theoretically tame (d-minimal/structure satisfying (S*) but not (O2)).
- **$\mathbb{R}_{\mathrm{PH}} = (\mathbb{R}_{\mathrm{alg}}, \sin)$** — real field with the **total** sine. **Not o-minimal**: $\sin^{-1}(0) = \pi\mathbb{Z}$ is infinite discrete, violating (O2). Used (HW1 Ex 0.14) to show $\mathbb{R}_{\mathrm{PH}} = (\mathbb{R}_{\mathrm{alg}}, f)$ for a pathological $f$ — i.e. defining one wild function can define $\mathbb{Z}$.
- **$\mathcal{R}^{\top}$** — the "top" structure $\mathcal{R}_n = \mathcal{P}(\mathbb{R}^n)$: *everything* is definable. Satisfies (S1)–(S6) trivially but is maximally non-tame (not o-minimal).

**Inclusions (rough):** $\mathbb{R}_{\mathrm{alg}} \subseteq \mathbb{R}_{\mathrm{an}} \subseteq \mathbb{R}_{\mathrm{an,exp}}$, and $\mathbb{R}_{\mathrm{alg}} \subseteq \mathbb{R}_{\mathrm{RE}} \subseteq \mathbb{R}_{\exp} \subseteq \mathbb{R}_{\mathrm{an,exp}}$; Pfaffian structures sit between $\mathbb{R}_{\mathrm{alg}}$ and $\mathbb{R}_{\mathrm{an}}$-ish; non-o-minimal ones ($\mathbb{R}_{\mathrm{PH}}, (\mathbb{R}_{\mathrm{alg}},2^{\mathbb{Z}}), \mathcal{R}^{\top}$) lie outside the o-minimal region; all sit inside $\mathcal{R}^{\top}$.

## Related Concepts
- [[structure_axioms_s1_s6]]
- [[o_minimal_structure]]
- [[polynomially_exponentially_bounded]]
- [[field_of_exponents]]
