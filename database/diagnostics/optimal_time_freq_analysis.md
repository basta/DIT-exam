---
id: 20260106_diagnostics_016
course: Diagnostika a testování
tags: [zpracování signálu, časově-frekvenční analýza, vlnková transformace]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Jaká je optimální analýza z hlediska času i frekvence (poskytuje dobré rozlišení v obou doménách)?

## Options
A) Fourierova transformace (FFT)
B) Vlnková transformace (Wavelet transform)
C) Hilbertova transformace
D) Průměrování v časové oblasti

---
# Solution
**Correct Answer:** B

## Explanation
**Vlnková transformace (Wavelet transform)** je považována za optimální nástroj pro časově-frekvenční analýzu nestacionárních signálů.
- Na rozdíl od FFT (která ztrácí časovou informaci) nebo STFT (která má fixní rozlišení dané délkou okna), vlnková transformace používá krátká okna pro vysoké frekvence (dobré časové rozlišení) a dlouhá okna pro nízké frekvence (dobré frekvenční rozlišení).
- To řeší princip neurčitosti lépe než STFT pro signály, které obsahují jak rychlé přechodové děje, tak pomalé trendy.

## Related Concepts
- [[Vlnková transformace]]
- [[Short-Time Fourier Transform]]
- [[Heisenbergův princip neurčitosti v signálech]]
