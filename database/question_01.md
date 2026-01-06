---
id: 20260106_diagnostics_001
course: Diagnostika a testování
tags: [spektrální analýza, okna]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Které okno pro spektrální analýzu má nejužší hlavní lalok (oblouk)?

## Options
A) exponenciální
B) Flat-top
C) Blackman-Harris
D) obdélníkové nebo Rectangular

---
# Solution
**Correct Answer:** D

## Explanation
Obdélníkové okno (Rectangular window) má nejužší hlavní lalok, což poskytuje nejlepší frekvenční rozlišení pro oddělení blízkých frekvencí. Jeho nevýhodou je však největší postranní lalok (cca -13 dB), což způsobuje značný spektrální únik (spectral leakage) a zkreslení amplitud slabších signálů.

Ostatní okna (Hanning, Hamming, Blackman-Harris, Flat-top) rozšiřují hlavní lalok, aby potlačila postranní laloky.

### Steps / Derivation
1. Šířka hlavního laloku obdélníkového okna je $4\pi/N$.
2. Ostatní okna mají hlavní lalok širší (např. Hanning $8\pi/N$).
$$
W_{rect}(n) = 1, \quad 0 \leq n \leq N-1
$$

## Related Concepts
- [[Okno (zpracování signálu)]]
- [[Spektrální analýza]]
