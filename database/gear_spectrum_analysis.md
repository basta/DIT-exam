---
id: 20260106_diagnostics_014
course: Diagnostika a testování
tags: [vibrodiagnostika, spektrální analýza, kepstrum, ozubená kola]
difficulty: 4
type: derivation
status: to_learn
---

# Question
Máte ozubená kola v převodu:
- Kolo 1: 50 zubů
- Kolo 2: 40 zubů
Ve spektru vibrací je významná složka na frekvenci **4000 Hz**. V kepstru (cepstrum) je lokální maximum na kvefrenci **0,01 s**.

1. Které kolo má poškozený zub? (2 body)
2. Nakreslete podrobne spektrum, ve kterém se projeví i 2. harmonické (2 body).
3. Nakreslete a okótujte obálku signálu (2 body).

---
# Solution
**Correct Answer:** Poškozeno je Kolo 2 (40 zubů).

## Explanation

1. **Určení poškozeného kola:**
   - Významná frekvence ve spektru $4000 \text{ Hz}$ odpovídá záběrové frekvenci $f_m$.
   - Maximum v kepstru na $\tau = 0,01 \text{ s}$ odpovídá modulační frekvenci $f_{mod} = 1/\tau = 1/0,01 = 100 \text{ Hz}$.
   - Tato modulační frekvence $100 \text{ Hz}$ musí odpovídat otáčkám poškozeného hřídele/kola.
   - Výpočet otáček (frekvencí otáčení) kol:
     - $f_m = f_{ot} \cdot z$
     - Pro Kolo 1 (50 zubů): $f_{ot1} = f_m / z_1 = 4000 / 50 = 80 \text{ Hz}$.
     - Pro Kolo 2 (40 zubů): $f_{ot2} = f_m / z_2 = 4000 / 40 = 100 \text{ Hz}$.
   - Modulační frekvence (z kepstra) je $100 \text{ Hz}$, což se shoduje s otáčkami Kola 2. **Tedy poškozeno je Kolo 2.**

2. **Nákres spektra:**
   - Nosné frekvence (záběrové harmonické):
     - 1. harmonická: $f_m = 4000 \text{ Hz}$
     - 2. harmonická: $2f_m = 8000 \text{ Hz}$
   - Postranní pásma (Sidebands) ve vzdálenosti $\pm f_{ot2} = \pm 100 \text{ Hz}$:
     - Okolo 4000 Hz: $3900, 4100$ Hz.
     - Okolo 8000 Hz: $7900, 8100$ Hz.

3. **Nákres obálky:**
   - Obálka časového signálu bude vykazovat rázy s periodou odpovídající otáčkám poškozeného kola.
   - Perioda rázů $T = 1 / f_{ot2} = 1 / 100 = 0.01 \text{ s}$.
   - Na ose X bude čas, píky se opakují každých 0.01 s.

### Steps / Derivation
$$
f_{mod} = \frac{1}{\tau_{cepstrum}} = \frac{1}{0.01} = 100 \text{ Hz}
$$
$$
n_2 = \frac{f_m}{z_2} = \frac{4000}{40} = 100 \text{ Hz}
$$

## Related Concepts
- [[Kepstrální analýza]]
- [[Vibrodiagnostika převodovek]]
- [[Amplitudová modulace]]
