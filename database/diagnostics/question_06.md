---
id: 20260106_diagnostics_006
course: Diagnostika a testování
tags: [signály, obálka, Hilbertova transformace]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Obálka signálu můžeme být vyjádřena:

## Options
A) derivací fáze analytického signálu
B) úhlem mezi imaginární a reálnou částí analytického signálu
C) derivací imaginární části Hilbertova obrazu signálu
D) absolutní hodnotou analytického signálu

---
# Solution
**Correct Answer:** D

## Explanation
Obálka (okamžitá amplituda) signálu se standardně získává pomocí **analytického signálu**. Analytický signál $z(t)$ je komplexní signál, jehož reálnou část tvoří původní signál $x(t)$ a imaginární část tvoří jeho Hilbertova transformace $\hat{x}(t)$.

Absolutní hodnota (modul) tohoto analytického signálu $|z(t)|$ představuje obálku signálu.

### Steps / Derivation
1. Analytický signál: $z(t) = x(t) + j\hat{x}(t)$.
2. Obálka: $A(t) = |z(t)| = \sqrt{x^2(t) + \hat{x}^2(t)}$.
$$
|z(t)| = \sqrt{x(t)^2 + \mathcal{H}[x(t)]^2}
$$

## Related Concepts
- [[Analytický signál]]
- [[Hilbertova transformace]]
