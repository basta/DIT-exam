---
id: 20260106_diagnostics_007
course: Diagnostika a testování
tags: [transformace signálů, nestacionární signály, HHT]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Které z následujících transformací pro analýzu nestacionárních signálů používají rozklad na monofrekvenční komponenty a výpočet okamžitých frekvencí komponent:

## Options
A) Hilbert-Huangova
B) STFT krátkodobá Fourierova
C) Vlnková (wavelet)
D) Vlnkové pakety (wavelet packets)

---
# Solution
**Correct Answer:** A

## Explanation
**Hilbert-Huangova transformace (HHT)** je metoda určená pro analýzu nelineárních a nestacionárních signálů. Skládá se ze dvou částí:
1. **Empirická modální dekompozice (EMD):** Rozkládá signál na sadu vnitřních modových funkcí (IMF - Intrinsic Mode Functions), které se chovají jako monofrekvenční komponenty (mají dobře definovanou okamžitou frekvenci).
2. **Hilbertova spektrální analýza:** Aplikuje Hilbertovu transformaci na jednotlivé IMF pro výpočet okamžité frekvence a amplitudy.

Ostatní metody (STFT, Wavelet) používají pevně dané bázové funkce (okna, vlnky) a nerozkládají signál adaptivně na "monofrekvenční" složky stejným způsobem.

### Steps / Derivation
1. EMD síto (sifting) získá $c_i(t)$ (IMF).
2. Hilbertova transformace $c_i(t) \to a_i(t) e^{j\theta_i(t)}$.
3. Okamžitá frekvence $\omega_i(t) = d\theta_i/dt$.
$$
x(t) = \sum_{i=1}^n c_i(t) + r_n(t)
$$

## Related Concepts
- [[Hilbert-Huangova transformace]]
- [[Časově-frekvenční analýza]]
