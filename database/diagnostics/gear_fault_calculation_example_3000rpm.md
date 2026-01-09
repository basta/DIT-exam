---
id: 20260106_diagnostics_051
course: Diagnostika a testování
tags: [vibrodiagnostika, převodovky, výpočet, spektrum]
difficulty: 4
type: derivation
status: to_learn
---

# Question
Máte převod:
- Kolo 1 (větší): $z_1 = 60$ zubů, otáčky $n_1 = 3000 \text{ ot/min}$.
- Kolo 2 (menší): $z_2 = 50$ zubů.
Kolo 1 (větší) má poškozený jeden zub.

1. Určete důležité frekvence (rotační $f_1, f_2$, záběrovou $f_z$).
2. Nakreslete spektrum (v okolí záběrové frekvence), kde se projeví vada. Popište konkrétní frekvence píků.
3. Nakreslete kepstrum.
4. Nakreslete obálku signálu.

---
# Solution

### 1. Výpočty frekvencí
- **Rotační frekvence (Kolo 1):** $f_1 = \frac{3000}{60} = 50 \text{ Hz}$.
- **Záběrová frekvence (Mesh Frequency):** $f_z = f_1 \cdot z_1 = 50 \cdot 60 = 3000 \text{ Hz}$.
- **Rotační frekvence (Kolo 2):** $f_2 = \frac{f_z}{z_2} = \frac{3000}{50} = 60 \text{ Hz}$.

### 2. Spektrum
Vada na Kole 1 způsobuje modulaci záběrové frekvence jeho otáčkami ($f_1 = 50 \text{ Hz}$).
- **Nosná:** $3000 \text{ Hz}$ ($f_z$).
- **Dominantní postranní pásma (Sidebands):** $\pm f_1 = \pm 50 \text{ Hz}$.
    - $2950 \text{ Hz}, 3050 \text{ Hz}$.
- Dle poznámek se v případě vibrací převodovky mohou objevit i modulace od druhého hřídele ($f_2$) nebo součtové/rozdílové složky, zejména pokud dochází k přenosu vibrací. V zadání byly zmíněny i frekvence $2940, 3060$ Hz, což odpovídá modulaci $f_2 = 60 \text{ Hz}$ ($\pm 60 \text{ Hz}$).
- **Seznam píků v okolí 3000 Hz:**
    - $2940 \text{ Hz}$ ($f_z - f_2$)
    - $2950 \text{ Hz}$ ($f_z - f_1$)
    - $3000 \text{ Hz}$ ($f_z$)
    - $3050 \text{ Hz}$ ($f_z + f_1$)
    - $3060 \text{ Hz}$ ($f_z + f_2$)

### 3. Obálka
- Časový signál vykazuje rázy s periodou $T_{r1} = 1/50 = 0.02 \text{ s}$.
- Spektrum obálky bude mít dominantní čáru na $50 \text{ Hz}$ (a $60 \text{ Hz}$ pokud se projevuje i druhé kolo).

### 4. Kepstrum
- Kepstrum detekuje rozestupy sidebands.
- Pro $f_1$: Pík na kvefrenci $\tau_1 = 1/50 = 0.02 \text{ s}$.
- Pro $f_2$: Pík na kvefrenci $\tau_2 = 1/60 \approx 0.0167 \text{ s}$.

## Related Concepts
- [[Modulace vibrací]]
- [[Spektrum převodovky]]
- [[Sidebands]]
