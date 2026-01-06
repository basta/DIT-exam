---
id: 20260106_diagnostics_047
course: Diagnostika a testování
tags: [vibrodiagnostika, řádová analýza, zpracování signálu]
difficulty: 2
type: open
status: to_learn
---

# Question
Co je to (z čeho se dělá) řádová analýza?

---
# Solution
**Short Answer:** Analýza vibračního signálu v závislosti na otáčkách, kde na ose X jsou vyneseny "řády" (násobky otáčkové frekvence) místo frekvence v Hz.

## Explanation
- **Vstup:** Vibrační signál + signál otáček (tacho).
- **Princip:** Převzorkování signálu z časové domény (konstantní $\Delta t$) do úhlové domény (konstantní $\Delta \phi$, vzorky na otáčku).
- **Výsledek:** Spektrum, kde na ose X je **řád (Order)**.
  - 1. řád = 1 vzr/otáčku (nevývažek).
  - $N$-tý řád = $N$ vzr/otáčku (např. zubová frekvence).
- Pořádí se nemění s rychlostí otáčení, což umožňuje analyzovat stroje při rozběhu/doběhu.

## Related Concepts
- [[Řádová analýza (Order Analysis)]]
- [[Computed Order Tracking]]
