---
id: 20260106_diagnostics_040
course: Diagnostika a testování
tags: [elektronika, senzory, piezo, nábojový zesilovač]
difficulty: 3
type: derivation
status: to_learn
---

# Question
Nakreslete schéma nábojového zesilovače (pro piezoelektrický snímač).

---
# Solution
**Correct Answer:** (Schéma s operačním zesilovačem a kondenzátorem ve zpětné vazbě)

## Explanation
Nábojový zesilovač (Charge Amplifier) převádí náboj $Q$ z piezoelektrického senzoru na napětí $U_{out}$, přičemž výstupní napětí nezávisí na kapacitě kabelu.

### Zapojení:
1.  **Operační zesilovač (OZ):** Invertující zapojení.
2.  **Vstup:** Piezo senzor připojen na invertující vstup (-). Neinvertující vstup (+) uzemněn.
3.  **Zpětná vazba:** Mezi výstupem a invertujícím vstupem je zapojen **kondenzátor $C_f$** (feedback capacitor). (Paralelně k němu bývá velký odpor $R_f$ pro stabilizaci DC pracovního bodu/vybíjení).

### Princip:
- Díky virtuální nule na vstupu teče náboj ze senzoru do zpětnovazebního kondenzátoru.
- Výstupní napětí:
  $$ U_{out} = -\frac{Q}{C_f} $$
- Zisk je určen velikostí $C_f$. Čím menší $C_f$, tím vyšší citlivost (větší napětí). Kapacita kabelu $C_{kabel}$ je mezi vstupem a zemí (virtuální nula), takže se nenabíjí a neovlivňuje měření.

## Related Concepts
- [[Nábojový zesilovač]]
- [[Piezoelektrický senzor]]
- [[Operační zesilovač]]
