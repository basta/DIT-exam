---
id: 20260106_diagnostics_008
course: Diagnostika a testování
tags: [spolehlivost, redundance, hlasování]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
V systému složeném ze dvou stejných bloků a vyhodnocování výstupů hlasováním lze dosáhnout:

## Options
A) odolnosti vůči poruše jednoho bloku
B) odolnosti vůči současné poruše obou bloků
C) detekce poruchy jednoho bloku
D) detekce současných poruch obou bloků

---
# Solution
**Correct Answer:** C

## Explanation
Systém se dvěma moduly (Dual Modular Redundancy - DMR) s komparátorem (nebo "hlasováním", i když pro opravu chyb je potřeba 3 modulů - TMR) dokáže pouze **detekovat** neshodu mezi výstupy. Pokud se výstupy liší, víme, že došlo k poruše, ale nevíme, který blok je vadný, a proto nemůžeme chybu opravit (dosáhnout odolnosti/maskování poruchy).

Pro dosažení odolnosti (maskování chyby) by bylo potřeba alespoň tří bloků (TMR), aby většinové hlasování mohlo přehlasovat chybný blok.

### Steps / Derivation
1. Blok A = $y_A$.
2. Blok B = $y_B$.
3. Detekce chyby: $E = (y_A \neq y_B)$.
4. Pro opravu není dostatek informací (majority).
$$
R_{DMR} < R_{simplex} \quad (\text{z hlediska spolehlivosti bez opravy, ale zvyšuje bezpečnost})
$$

## Related Concepts
- [[Redundance]]
- [[TMR (Triple Modular Redundancy)]]
- [[Duplexní systém]]
