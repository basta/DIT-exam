---
id: 20260106_diagnostics_044
course: Diagnostika a testování
tags: [zpracování signálu, časově-frekvenční analýza, STFT, neurčitost]
difficulty: 2
type: open
status: to_learn
---

# Question
V jaké transformaci si musíte pevně zvolit časovou (a tím i frekvenční) rozlišitelnost pro celou analýzu?

---
# Solution
**Short Answer:** Krátkodobá Fourierova transformace (STFT - Short Time Fourier Transform).

## Explanation
- **STFT:** Používá okno s **fixní délkou** (např. 100 ms).
    - Krátké okno $\to$ dobré časové rozlišení, špatné frekvenční rozlišení.
    - Dlouhé okno $\to$ špatné časové rozlišení, dobré frekvenční rozlišení.
    - Toto rozlišení je **stejné pro všechny frekvence** v spektrogramu. Musíte si vybrat kompromis.
- **Vlnková transformace (Wavelet):** Je to multiresoluční analýza. Používá krátká okna pro vysoké frekvence a dlouhá okna pro nízké frekvence. Rozlišení se tedy mění automaticky ("adaptuje") podél frekvenční osy.

## Related Concepts
- [[Short-Time Fourier Transform (STFT)]]
- [[Heisenbergův princip neurčitosti v signálech]]
- [[Spektrogram]]
