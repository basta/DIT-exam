---
id: 20260106_diagnostics_064
course: Diagnostika a testování
tags: [ultrazvuk, útlum, výpočet]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Vypočtěte koeficient útlumu ultrazvukové vlny $\alpha$ [dB/mm].
- Tloušťka materiálu (dráha mezi echy): $d = 300 \text{ mm}$.
- Ztráta (pokles) mezi 1. a 2. koncovým echem: $\Delta A = 19 \text{ dB}$.
- Korekce na odraz vlny (ztráta na rozhraní) je $k = 1 \text{ dB}$.

## Options
A) 0.04 dB/mm
B) 0.03 dB/mm
C) 0.02 dB/mm
D) 0.01 dB/mm

---
# Solution
**Correct Answer:** B

## Explanation
- Mezi 1. a 2. koncovým echem urazí vlna dráhu $2d$ (tam a zpět). Tedy $L = 2 \cdot 300 = 600 \text{ mm}$.
- Celková ztráta signálu $\Delta A_{total} = \Delta A = 19 \text{ dB}$.
- Tato ztráta se skládá z útlumu materiálu ($\alpha \cdot L$) a ztráty odrazem na zadní stěně ($k$).
- Rovnice: $\Delta A = \alpha \cdot L + k$.
- $19 = \alpha \cdot 600 + 1$.
- $18 = \alpha \cdot 600$.
- $\alpha = 18 / 600 = 0.03 \text{ dB/mm}$.

(Poznámka: Někdy se "mezi 1. a 2. echem" počítá dráha jen $2d$, protože 1. echo už prošlo $2d$ a 2. echo prošlo $4d$, rozdíl je $2d$. Pokud by $d$ v zadání byla "vzdálenost kterou urazila vlna mezi měřeními", tak se dělí $d$. Zde $d=300mm$ je tloušťka desky, rozdíl drah je $2d=600mm$).

## Related Concepts
- [[Měření útlumu]]
- [[Backwall echo]]
