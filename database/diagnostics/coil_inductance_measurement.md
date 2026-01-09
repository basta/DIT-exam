---
id: 20260106_diagnostics_015
course: Diagnostika a testování
tags: [elektrická měření, indukčnost, cívka]
difficulty: 3
type: derivation
status: to_learn
---

# Question
1. Nakreslete zapojení pro měření parametrů cívky (viz slajdy) (3 body).
2. Uveďte, jak se počítá neznámá indukčnost $L_x$ (3 body).

---
# Solution
**Correct Answer:** (Viz vysvětlení)

## Explanation
*(Poznámka: Přesné zapojení závisí na konkrétních "slajdech" z přednášek, ale standardně se pro měření indukčnosti používá **Maxwellův-Wienův můstek** nebo rezonanční metoda. Zde předpokládáme můstkovou metodu nebo U-I metodu pro střídavý proud, pokud jde o impedanční měření v diagnostice.)*

### Typické řešení (Maxwellův-Wienův můstek):
1. **Zapojení:**
   - V jedné větvi je neznámá cívka ($L_x, R_x$).
   - V protější větvi je paralelní kombinace kondenzátoru ($C_n$) a rezistoru ($R_n$).
   - Ve zbylých dvou větvích jsou rezistory ($R_2, R_3$).
   - Můstek je napájen střídavým zdrojem a nulový indikátor je uprostřed.

2. **Výpočet $L_x$:**
   - Podmínka rovnováhy můstku: $Z_1 Z_4 = Z_2 Z_3$.
   - Pro Maxwellův můstek platí:
     $$ L_x = R_2 R_3 C_n $$
     $$ R_x = \frac{R_2 R_3}{R_n} $$

*(Alternativa: Pokud jde o vířivé proudy a impedanční rovinu, vzorec by vycházel z komplexní impedance $Z = R + j\omega L$.)*

## Related Concepts
- [[Měření indukčnosti]]
- [[Maxwellův můstek]]
- [[Impedance cívky]]
