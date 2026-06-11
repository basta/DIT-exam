---
id: orr_quiz10_06
course: Optimal and Robust Control
tags: [robust-performance, mixed-sensitivity, sensitivity, complementary-sensitivity]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
Choose the correct condition for robust performance in the presence of multiplicative uncertainty.

## Options
A) $\lVert S\rVert_\infty < 1$
B) $\lVert WT\rVert_\infty < 1$
C) $|W_1(j\omega)S(j\omega)| + |W_2(j\omega)T(j\omega)| < 1$ for all $\omega$.
D) —

---
# Solution
**Correct Answer:** C

## Explanation
**Robust performance** demands *both* nominal performance *and* robust stability simultaneously, for **all** admissible uncertainties. For a SISO loop with multiplicative uncertainty (weight $W_2$) and a performance weight $W_1$ on the sensitivity, the necessary and sufficient condition is the **combined** spectral bound
$$
\big|W_1(j\omega)S(j\omega)\big| + \big|W_2(j\omega)T(j\omega)\big| < 1 \quad \text{for all } \omega,
$$
where $S=(1+L)^{-1}$ and $T=1-S$. The first term is the **nominal performance** requirement $|W_1 S|<1$; the second is **robust stability** $|W_2 T|<1$; robust performance requires their **sum** to stay below 1 at every frequency (the structured-singular-value / $\mu$ condition specialized to this $2$-block problem).

- **A ($\|S\|_\infty<1$)** is only (a weak form of) nominal performance.
- **B ($\|WT\|_\infty<1$)** is only robust **stability** (quiz #10 Q4).

Each alone is insufficient — robust performance is strictly stronger, hence the additive combination in C.

## Related Concepts
- [[robust-performance]]
- [[structured-singular-value]]
- [[mixed-sensitivity]]
- [[sensitivity-function]]
