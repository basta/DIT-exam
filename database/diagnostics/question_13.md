---
id: 20260106_diagnostics_013
course: Diagnostika a testování
tags: [vibrodiagnostika, spektrální analýza, kepstrum, převodovky]
difficulty: 4
type: derivation
status: to_learn
---

# Question
1. Nakreslete základní spektrální čáry, které se objeví na obrazovce spektrálního analyzátoru při analýze signálu vibrací převodu, u kterého je poškozen 1 zub na kole s 60 zuby, které se otáčí rychlostí 1200 otáček za minutu (1b.). Druhé kolo má 50 zubů. U každé čáry uveďte její frekvenci, u neharmonických průběhu uvažujte jen první dvě harmonické frekvence (2b.). Znázorněte obálku uvedeného signálu (1b.).
2. Dále nakreslete přibližný průběh kepstra uvedeného signálu a okótujte osu $x$ (1b.).
3. Nakreslete spektrum vibrací stejného převodu ale bez poškození (uvažujte první dvě harmonické frekvence) (1b.).

---
# Solution

### Výpočty frekvencí
- **Otáčky kola 1:** $n_1 = 1200 \text{ ot/min}$.
- **Rotační frekvence 1:** $f_{r1} = \frac{1200}{60} = 20 \text{ Hz}$.
- **Počet zubů:** $z_1 = 60, z_2 = 50$.
- **Záběrová frekvence (Meshing frequency):** $f_m = f_{r1} \cdot z_1 = 20 \cdot 60 = 1200 \text{ Hz}$.
- (Kontrola pro kolo 2: $f_{r2} = f_m / z_2 = 1200 / 50 = 24 \text{ Hz}$.)

### 1. Spektrum poškozeného převodu (1 zub na kole 1)
Poškození jednoho zubu způsobuje amplitudovou a frekvenční modulaci záběrové frekvence $f_m$ rotační frekvencí poškozeného kola $f_{r1}$.
- **Nosné frekvence:** $f_m (1200 \text{ Hz})$ a $2f_m (2400 \text{ Hz})$ (první dvě harmonické záběru).
- **Postranní pásma (Sidebands):** Vznikají ve vzdálenosti $\pm k \cdot f_{r1}$ od nosných.
    - Okolo 1. harmonické ($1200 \text{ Hz}$):
        - $1200 \pm 20 \to 1180, 1220 \text{ Hz}$.
        - $1200 \pm 40 \to 1160, 1240 \text{ Hz}$.
    - Okolo 2. harmonické ($2400 \text{ Hz}$):
        - $2400 \pm 20 \to 2380, 2420 \text{ Hz}$.
- **Obálka:** V časovém průběhu jsou viditelné pravidelné rázy s periodou $T_{r1} = 1/20 = 0.05 \text{ s}$.

### 2. Kepstrum (Cepstrum)
Kepstrum (inverzní FT logaritmu spektra) slouží k detekci periodicity ve spektru (tedy postranních pásem).
- Periodicita postranních pásem je $f_{r1} = 20 \text{ Hz}$.
- V kepstru se objeví dominantní čára (rahmonic) na "kvefrencí" odpovídající této periodě.
- **Poloha čáry:** $\tau = 1 / f_{r1} = 1 / 20 = 0.05 \text{ s}$.
- Osa x je čas (kvefrence) [s]. Čára bude na **0.05 s**.

### 3. Spektrum bez poškození
Zdravá převodovka generuje vibrace hlavně na záběrové frekvenci a jejích harmonických. Postranní pásma jsou zanedbatelná.
- Čára 1: $1200 \text{ Hz}$ ($f_m$)
- Čára 2: $2400 \text{ Hz}$ ($2f_m$)

## Explanation
Lokální závada (zub) generuje krátký impuls při každém kontaktu, což moduluje záběrový signál. Ve spektru se to projeví jako "hřeben" postranních pásem kolem $f_m$ s rozestupem rovným otáčkám vadného kola. Kepstrum je ideální nástroj pro separaci těchto rodin postranních pásem.

## Related Concepts
- [[Vibrodiagnostika]]
- [[Záběrová frekvence]]
- [[Kepstrální analýza]]
- [[Amplitudová modulace]]
