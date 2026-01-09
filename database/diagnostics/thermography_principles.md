---
id: 20260106_diagnostics_027
course: Diagnostika a testování
tags: [termografie, emisivita, Kirchhoffův zákon]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Při měření termovizí se projeví (je vidět) následující:

## Options
A) Měřený objekt, pokud $\varepsilon = 1$
B) Měřený objekt, pokud $\varepsilon = 0$
C) Okolní objekt (odraz), pokud $\varepsilon = 1$
D) Okolní objekt (odraz), pokud $\varepsilon < 1$ (resp. blízké 0)

---
# Solution
**Correct Answer:** A, D

## Explanation
Termokamera měří celkové dopadající záření, které je součtem vyzařovaného záření objektu a odraženého záření okolí.
Vztah pro intenzitu záření:
$$ W_{celk} = \varepsilon \cdot W_{obj} + (1 - \varepsilon) \cdot W_{okol} $$

1.  **Pokud $\varepsilon = 1$ (Černé těleso):**
    - $W_{celk} = 1 \cdot W_{obj} + 0 \cdot W_{okol} = W_{obj}$.
    - Vidíme **pouze měřený objekt** (jeho skutečnou teplotu).

2.  **Pokud $\varepsilon = 0$ (Ideální zrcadlo):**
    - $W_{celk} = 0 \cdot W_{obj} + 1 \cdot W_{okol} = W_{okol}$.
    - Vidíme **pouze odraz okolí**. Měřený objekt se "neprojeví" svým teplem.

3.  **Reálné objekty ($0 < \varepsilon < 1$):**
    - Vidíme kombinaci obou. Čím nižší emisivita, tím více se projevuje vliv okolí (odrazy).

## Related Concepts
- [[Emisivita]]
- [[Odražená zdánlivá teplota]]
- [[Termografie]]
