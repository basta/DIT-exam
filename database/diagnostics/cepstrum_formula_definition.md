---
id: 20260106_diagnostics_060
course: Diagnostika a testování
tags: [zpracování signálu, kepstrum, definice]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Jak je definováno (reálné) kepstrum signálu $x(t)$? ($\mathcal{F}$ značí Fourierovu transformaci).

## Options
A) $\mathcal{F}^{-1} \{ \log |\mathcal{F}\{x(t)\}|^2 \}$
B) $\mathcal{F}^{-1} \{ |\mathcal{F}\{x(t)\}|^2 \}$
C) $\mathcal{F}^{-1} \{ \log |\mathcal{F}\{x(t)\}| \}$
D) $\mathcal{F}^{-1} \{ \log \mathcal{F}\{[x(t)]^2\} \}$

---
# Solution
**Correct Answer:** A (nebo C, záleží na tom, zda se bere Power nebo Amplitude spectrum, výsledek se liší jen faktorem 2)

## Explanation
Standardní definice (Power Cepstrum) vychází z výkonového spektra:
$$ C(\tau) = \mathcal{F}^{-1} \{ \log S_{xx}(f) \} = \mathcal{F}^{-1} \{ \log |\mathcal{F}\{x(t)\}|^2 \} $$
- Krok 1: FFT signálu.
- Krok 2: Absolutní hodnota na druhou (výkonové spektrum).
- Krok 3: Logaritmus (převedení násobení na sčítání, komprese dynamiky).
- Krok 4: Inverzní FFT (návrat do "kvazi-časové" domény = kvefrence).

Možnost C je "Amplitudové kepstrum", liší se jen konstantou ($\log x^2 = 2 \log x$). V kontextu testu je A nejpřesnější definice výkonového kepstra.

## Related Concepts
- [[Kepstrum (Cepstrum)]]
- [[Homomorfní filtrace]]
