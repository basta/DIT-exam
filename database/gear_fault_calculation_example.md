---
id: 20260106_diagnostics_046
course: Diagnostika a testování
tags: [vibrodiagnostika, převodovky, výpočet, spektrum]
difficulty: 4
type: derivation
status: to_learn
---

# Question
Máte převod:
- Kolo 1 (vadné): $z_1 = 20$ zubů, otáčky $n_1 = 6000 \text{ ot/min}$.
- Kolo 2: $z_2 = 80$ zubů.
Kolo 1 má poškozený jeden zub.

1. Vypočítejte záběrovou frekvenci ($f_z$ neboli $f_m$) a rotační frekvence ($f_1, f_2$).
2. Nakreslete spektrum (FFT), kde se projeví vada. **Pozor:** Která modulační frekvence tam bude?
3. Nakreslete obálku signálu.
4. Nakreslete kepstrum.

---
# Solution

### 1. Výpočty
- **Rotační frekvence Kola 1:** $f_1 = \frac{6000}{60} = 100 \text{ Hz}$.
- **Záběrová frekvence:** $f_z = f_1 \cdot z_1 = 100 \cdot 20 = 2000 \text{ Hz}$.
- **Rotační frekvence Kola 2:** $f_2 = \frac{f_z}{z_2} = \frac{2000}{80} = 25 \text{ Hz}$ (nebo přes převodový poměr $1:4$).

### 2. Spektrum (FFT)
Vada je na Kole 1. Modulace bude probíhat frekvencí otáčení Kola 1 ($f_1 = 100 \text{ Hz}$).
- **Nosná:** $f_z = 2000 \text{ Hz}$ (vysoká amplituda).
- **Postranní pásma (Sidebands):** Vzdálená o $\pm f_1 = 100 \text{ Hz}$.
    - $1900 \text{ Hz}$ ($f_z - f_1$)
    - $2100 \text{ Hz}$ ($f_z + f_1$)
- Mohou být vidět i 2. harmonické sidebads ($\pm 200 \text{ Hz}$): $1800, 2200 \text{ Hz}$.
- *(Poznámka ze zadání: "ne tech 25 Hz" - to by bylo, kdyby bylo vadné Kolo 2).*
- Dále se ve spektru objeví 2. harmonická záběru ($2f_z = 4000 \text{ Hz}$) opět s postranními pásmy $\pm 100 \text{ Hz}$.

### 3. Obálka
- V časovém signálu jsou rázy s periodou otáčení vadného kola.
- Perioda rázů $T = 1/f_1 = 1/100 = 0.01 \text{ s}$.
- Spektrum obálky by obsahovalo čistou čáru na $100 \text{ Hz}$ (a harmonické).

### 4. Kepstrum
- Kepstrum ukazuje periodicitu spektra (rozestup sidebands).
- Rozestup sidebands je $100 \text{ Hz}$.
- Dominantní rahmonic peak bude na kvefrenci:
  $$ \tau = \frac{1}{100} = 0.01 \text{ s} $$

## Related Concepts
- [[Vibrodiagnostika převodovek]]
- [[Výpočet frekvencí převodu]]
- [[Modulace v diagnostice]]
