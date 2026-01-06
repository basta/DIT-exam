---
id: 20260106_diagnostics_041
course: Diagnostika a testování
tags: [zpracování signálu, řádová analýza, tracking]
difficulty: 3
type: open
status: to_learn
---

# Question
Jaké jsou podmínky (nebo kdy se používá) pro řádovou analýzu (Order Analysis)?

---
# Solution
**Short Answer:** Používá se pro stroje s proměnnými otáčkami. Podmínkou je měření otáček (tacho) a synchronní vzorkování.

## Explanation
Klasická FFT selhává, pokud se během měření mění otáčky stroje (frekvenční složky se "rozmažou").
**Řádová analýza** mapuje vibrace z časové oblasti (vzorky v čase) do úhlové oblasti (vzorky na otáčku).

### Podmínky/Principy:
1.  **Proměnné otáčky:** Metoda je nutná při rozběhu, doběhu nebo kolísání rychlosti.
2.  **Měření otáček:** Je nutný tacho signál (referenční impuls na otáčku) pro synchronizaci.
3.  **Computed Order Tracking (COT):** Signál se převzorkuje tak, aby byl konstantní počet vzorků na jednu otáčku (nikoliv za sekundu).
4.  **Výsledek:** Osa X není frekvence [Hz], ale **řád** (násobek otáček). Spektrální čáry vázané na rotaci zůstanou ostré a na stálé pozici (např. 1. řád, 3. řád) i při změně rychlosti.

## Related Concepts
- [[Řádová analýza (Order Analysis)]]
- [[Computed Order Tracking]]
- [[Run-up / Coast-down test]]
