---
id: 20260106_diagnostics_018
course: Diagnostika a testování
tags: [zpracování signálu, filtrace, aliasing, vzorkování]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Jaký filtr (a s jakými parametry) použijete pro $100 \text{ Hz}$ trojúhelníkový signál s různou amplitudou, abyste jej správně analyzovali?

## Options
A) Dolní propust s $f_z = 200 \text{ Hz}, f_{vz} = 500 \text{ Hz}$
B) Dolní propust s $f_z = 5 \text{ kHz}, f_{vz} = 10 \text{ kHz}$
C) Horní propust s $f_z = 100 \text{ Hz}$
D) Pásmová propust $90-110 \text{ Hz}$

---
# Solution
**Correct Answer:** B

## Explanation
Trojúhelníkový signál obsahuje kromě základní harmonické frekvence ($100 \text{ Hz}$) také nekonečnou řadu lichých vyšších harmonických ($300 \text{ Hz}, 500 \text{ Hz}, 700 \text{ Hz} \dots$), jejichž amplituda klesá s druhou mocninou řádu harmonické ($1/n^2$).

Abychom signál věrně reprodukovali nebo analyzovali jeho tvar (např. pro diagnostiku zkreslení), musíme zachovat dostatečný počet vyšších harmonických.
- Volba **B (Dolní propust 5 kHz, vzorkování 10 kHz)** umožňuje zachytit harmonické složky až do 50. harmonické ($50 \times 100 \text{ Hz} = 5000 \text{ Hz}$), což je pro rekonstrukci tvaru trojúhelníku dostatečné.
- Volba A by ořízla vše nad 200 Hz (zůstala by jen 1. harmonická), z trojúhelníku by se stal sinus.
- Volba D by propustila jen základní frekvenci.

Poznámka: $f_{vz}$ značí vzorkovací frekvenci, která musí být min. 2x vyšší než mezní frekvence filtru (Nyquist), což zde platí ($10 \text{ kHz} \ge 2 \times 5 \text{ kHz}$).

## Related Concepts
- [[Fourierova řada]]
- [[Vzorkovací teorém]]
- [[Antialiasingový filtr]]
