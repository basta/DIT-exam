---
id: 20260106_diagnostics_021
course: Diagnostika a testování
tags: [zpracování signálu, průměrování, šum]
difficulty: 2
type: open
status: to_learn
---

# Question
Jak snížit nejistotu (rozptyl) u synchronního průměrování v čase?

---
# Solution
**Short Answer:** Zvýšením počtu průměrovaných vzorků (cyklů) a přesnou synchronizací (triggerováním).

## Explanation
Synchronní průměrování (Time Synchronous Averaging - TSA) slouží k potlačení nesynchronních složek (šumu, vibrací od jiných strojů) a zvýraznění periodického signálu vázaného na otáčky/fázi.

1.  **Počet průměrů ($N$):** Poměr signál/šum (SNR) se zlepšuje s druhou odmocninou počtu průměrů ($\sqrt{N}$). Tedy více vzorků = menší náhodná chyba (nejistota).
2.  **Přesnost spouštění (Triggering):** Pokud spouštěcí impuls (např. z tacho sondy) není přesný (jitter), dochází k "rozmazání" průměrovaného signálu na vysokých frekvencích, což zvyšuje nejistotu.

## Related Concepts
- [[Synchronní průměrování (TSA)]]
- [[Improvement of SNR]]
