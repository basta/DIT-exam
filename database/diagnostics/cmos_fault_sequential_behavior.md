---
id: 20260106_diagnostics_035
course: Diagnostika a testování
tags: [testování číslicových obvodů, CMOS, poruchy]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
Jak se chová kombinační logický obvod CMOS, když má poruchu typu "Stuck-Open" (přerušený tranzistor)?

## Options
A) Chová se jako trvalá 0 nebo 1 (Stuck-at)
B) Nelze modelovat triviálním způsobem, může se začít chovat jako sekvenční obvod
C) Zvýší se jeho odběr proudu (IDDQ)
D) Obvod přestane fungovat úplně

---
# Solution
**Correct Answer:** B

## Explanation
U technologie CMOS, pokud dojde k přerušení (Stuck-Open) jednoho z tranzistorů v hradle (např. v pull-up nebo pull-down větvi):
- Pro určité vstupní kombinace se výstup odpojí od napájení i od země (stav vysoké impedance, Hi-Z).
- Díky parazitní kapacitě na výstupu si hradlo **pamatuje předchozí hodnotu** (náboj na kapacitě zůstane).
- Kombinační obvod se tak stává závislým na předchozím stavu $\to$ chová se jako **sekvenční obvod** (paměť).
- To komplikuje testování, protože pro detekci závady nestačí jeden vektor, ale je potřeba **sekvence dvou vektorů** (inicializace a test).

## Related Concepts
- [[Stuck-Open fault]]
- [[Testování CMOS]]
- [[Sekvenční chování při poruše]]
