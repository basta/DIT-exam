---
id: 20260106_diagnostics_004
course: Diagnostika a testování
tags: [LFSR, testování, boundary scan]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Posuvný registr s lineární zpětnou vazbou LFSR (Linear Feedback Shift Register) může pracovat jako:

## Options
A) generátor pseudonáhodných posloupností testovacích vektorů
B) příznakový analyzátor číslicových posloupností
C) řídicí blok boundary scanu
D) buňka analogového boundary scanu

---
# Solution
**Correct Answer:** A

## Explanation
LFSR (Linear Feedback Shift Register) je základním stavebním blokem v testování a kryptografii. Jeho nejčastější použití v diagnostice (BIST - Built-In Self-Test) je ve funkci **generátoru pseudonáhodných posloupností** (PRPG - Pseudo-Random Pattern Generator), který generuje testovací vektory pro testovaný obvod.

LFSR lze také upravit na MISR (Multiple Input Signature Register) pro analýzu odezvy (signature analysis), ale samotný LFSR s lineární zpětnou vazbou bez vstupu dat je generátor.

### Steps / Derivation
1. LFSR cykluje přes stavy definované zpětnovazebním polynomem.
2. Maximální délka cyklu je $2^n - 1$.
$$
P(x) = 1 + c_1 x + \dots + c_n x^n
$$

## Related Concepts
- [[LFSR]]
- [[BIST]]
