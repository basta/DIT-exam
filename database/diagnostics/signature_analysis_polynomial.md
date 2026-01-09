---
id: 20260106_diagnostics_062
course: Diagnostika a testování
tags: [testování číslicových obvodů, signaturová analýza, LFSR]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Čím je dán **příznak** (signatura) při dělení polynomů v signaturové analýze (LFSR)? (Polynomy: $P(x)$ vstupní data, $G(x)$ generující polynom).

## Options
A) $G(x)$
B) $P(x)$
C) $Z(x)$
D) $R(x)$ (zbytek po dělení)

---
# Solution
**Correct Answer:** D

## Explanation
Signaturová analýza (pomocí LFSR/MISR) matematicky odpovídá dělení vstupního polynomu $P(x)$ (reprezentujícího sekvenci dat z testovaného obvodu) charakteristickým (generujícím) polynomem $G(x)$ (daným zapojením zpětných vazeb LFSR).
$$ \frac{P(x)}{G(x)} = Q(x) + \frac{R(x)}{G(x)} $$
- $Q(x)$ je podíl (který "vypadne" pryč a ztratí se).
- $R(x)$ je **zbytek po dělení** (Remainder), který zůstane v registru LFSR po skončení testu.
- Tento zbytek $R(x)$ tvoří výslednou **signaturu**.

## Related Concepts
- [[Signaturová analýza]]
- [[Polynomiální dělení v GF(2)]]
- [[CRC (Cyclic Redundancy Check)]]
