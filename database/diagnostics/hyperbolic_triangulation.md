---
id: 20260106_diagnostics_019
course: Diagnostika a testování
tags: [akustická emise, lokalizace zdroje, NDT]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Pomocí čeho lze určit umístění zdroje signálu (např. akustické emise) v rovině (v ploše)?

## Options
A) Lineární lokace
B) Hyperbolická triangulace
C) Zónová lokace
D) Spektrální analýza

---
# Solution
**Correct Answer:** B

## Explanation
Pro lokalizaci zdroje v rovině (2D) pomocí časových rozdílů příchodu signálu (TDOA - Time Difference of Arrival) na minimálně 3 senzory se používá **hyperbolická triangulace**.
- Pro každou dvojici senzorů definuje časový rozdíl hyperbolu, na které musí ležet zdroj.
- Průsečík těchto hyperbol (z více dvojic senzorů) určuje polohu zdroje.

Lineární lokace se používá pro 1D (trubky, tyče). Zónová lokace je pouze hrubá (určí senzoru nejblíže zdroji).

## Related Concepts
- [[Akustická emise]]
- [[TDOA lokalizace]]
- [[Nedestruktivní testování (NDT)]]
