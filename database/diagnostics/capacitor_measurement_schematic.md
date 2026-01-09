---
id: 20260106_diagnostics_045
course: Diagnostika a testování
tags: [elektrická měření, kondenzátor, schéma]
difficulty: 3
type: derivation
status: to_learn
---

# Question
1. Nakreslete schéma pro měření kondenzátoru (nabíjení/vybíjení nebo střídavou metodu dle přednášek).
2. Nakreslete průběhy veličin (napětí, proud).
3. Uveďte vzorec pro výpočet kapacity $C$.

---
# Solution
**Correct Answer:** (Viz vysvětlení)

## Explanation
*(Poznámka: Typicky se v diagnostice probírá měření přechodového děje - nabíjení RC členu, nebo měření impedance.)*

### Varianta A: Nabíjení RC článku (Časová metoda)
1.  **Schéma:** Zdroj stejnosměrného napětí $U_0$, spínač, sériově rezistor $R$ a měřený kondenzátor $C$.
2.  **Průběhy:**
    - Napětí na kondenzátoru $u_c(t)$: Exponenciálně roste z 0 na $U_0$.
      $$ u_c(t) = U_0 (1 - e^{-t/\tau}) $$
    - Proud $i(t)$: Exponenciálně klesá (skokově na $U_0/R$ a pak k nule).
3.  **Vzorec:** Časová konstanta $\tau = R \cdot C$.
    - Pokud změříme čas $\tau$, kdy napětí dosáhne cca $63.2 \% U_0$:
    $$ C = \frac{\tau}{R} $$

### Varianta B: Měření střídavým proudem (Impedanční metoda)
- Reaktance kondenzátoru: $X_C = \frac{1}{2\pi f C}$.
- Ze změřeného napětí a proudu (a fáze) určíme $X_C$ a následně:
  $$ C = \frac{1}{2\pi f X_C} $$

## Related Concepts
- [[Přechodový děj RC]]
- [[Měření kapacity]]
- [[Časová konstanta]]
