---
id: 20260106_diagnostics_037
course: Diagnostika a testování
tags: [akustika, lokalizace, korelace, zpoždění]
difficulty: 2
type: open
status: to_learn
---

# Question
Jak zjistíme zpoždění (a tím směr/polohu) zdroje zvuku při měření přes dva mikrofony?

---
# Solution
**Short Answer:** Pomocí vzájemné korelace (Cross-Correlation) signálů.

## Explanation
Máme-li dva mikrofony snímající stejný zdroj hluku se zpožděním $\tau$ (daným rozdílnou vzdáleností od zdroje):
$$ R_{xy}(\tau) = \int_{-\infty}^{\infty} x(t) \cdot y(t+\tau) dt $$
- Funkce vzájemné korelace bude mít **maximum** v čase, který odpovídá vzájemnému zpoždění ($\Delta t$) signálů mezi mikrofony.
- Z tohoto zpoždění a známé rychlosti zvuku lze určit rozdíl vzdáleností od zdroje (a tím úhel příchodu).

## Related Concepts
- [[Korelace]]
- [[TDOA (Time Difference of Arrival)]]
- [[Identifikace zdrojů hluku]]
