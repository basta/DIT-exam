---
id: 20260106_diagnostics_054
course: Diagnostika a testování
tags: [zpracování signálu, šum, spektrální hustota]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Jak správně charakterizujeme šum (stochastický signál)?

## Options
A) Pomocí (výkonové) spektrální hustoty (PSD - Power Spectral Density)
B) Pomocí amplitudového spektra (FFT)
C) Pomocí okamžité hodnoty
D) Pomocí Fourierovy řady

---
# Solution
**Correct Answer:** A

## Explanation
Náhodný (stochastický) šum nemá periodický charakter, takže nemá diskrétní čárové spektrum (jako by dala Fourierova řada) a jeho "amplituda" v konkrétním bodě FFT závisí na délce záznamu/šířce binu (energie je rozprostřena přes celé pásmo).
- Proto se používá **Výkonová spektrální hustota (PSD)**, která vyjadřuje výkon signálu připadající na 1 Hz šířky pásma ($W/Hz$ nebo $V^2/Hz$).
- PSD je nezávislá na frekvenčním rozlišení analýzy a umožňuje objektivně porovnávat hladinu šumu.

## Related Concepts
- [[Power Spectral Density (PSD)]]
- [[Stochastické signály]]
- [[Bílý šum]]
