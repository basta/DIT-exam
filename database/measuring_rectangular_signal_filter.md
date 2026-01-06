---
id: 20260106_diagnostics_031
course: Diagnostika a testování
tags: [zpracování signálu, filtrace, aliasing, obdélníkový signál]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Máte obdélníkový signál s frekvencí $f = 3 \text{ Hz}$. Jaký analogový filtr použijete, aby nedocházelo k aliasingu (při následném vzorkování, např. $f_{vz} = 20 \text{ Hz}$)?

## Options
A) Dolní propust $f_m = 10 \text{ Hz}$
B) Dolní propust $f_m = 3 \text{ Hz}$
C) Horní propust $f_m = 3 \text{ Hz}$
D) Žádný filtr není potřeba

---
# Solution
**Correct Answer:** A

## Explanation
Pro vzorkování frekvencí $f_{vz} = 20 \text{ Hz}$ musí být podle Nyquistova teorému ze signálu odstraněny všechny složky nad $f_{Nyquist} = f_{vz} / 2 = 10 \text{ Hz}$.
- Obdélníkový signál ($3 \text{ Hz}$) obsahuje základní harmonickou ($3 \text{ Hz}$) a liché násobky ($9 \text{ Hz}, 15 \text{ Hz}, 21 \text{ Hz} \dots$).
- Složky $15 \text{ Hz}$ a vyšší by způsobily aliasing (překlopily by se do pásma $0-10 \text{ Hz}$).
- Proto je nutné použít **Dolní propust (Low Pass)** s mezní frekvencí $f_m \le 10 \text{ Hz}$ (ideálně těsně pod, aby filtr stihl utlumit složky nad 10 Hz).
- Tím sice signál zkreslíme (ořízneme vyšší harmonické, z obdélníku se stane "vlnovka"), ale zabráníme vzniku falešných frekvencí (aliasingu).

Poznámka: Zadání zmiňuje "Dolní propust f=10Hz fz=20Hz", což přesně odpovídá antialiasingovému filtru na polovině vzorkovací frekvence.

## Related Concepts
- [[Aliasing]]
- [[Nyquistův teorém]]
- [[Obdélníkový signál - spektrum]]
