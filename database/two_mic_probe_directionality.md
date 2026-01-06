---
id: 20260106_diagnostics_052
course: Diagnostika a testování
tags: [akustika, senzory, směrovost]
difficulty: 2
type: open
status: to_learn
---

# Question
Máme dvojmikrofonní sondu (intenzitní sondu). V jakém směru vůči zdroji měříme **minimum** a v jakém **maximum**?

---
# Solution
**Short Answer:**
- **Maximum:** Osa sondy (spojnice mikrofonů) míří **přímo ke zdroji** (rovnoběžně se směrem šíření).
- **Minimum:** Osa sondy (spojnice mikrofonů) je **kolmá** na směr šíření zvuku.

## Explanation
K měření akustické intenzity (vektorová veličina) se používá gradientní metoda (p.u sonda), která počítá rozdíl tlaků mezi dvěma mikrofony.
- $I \approx -\frac{p_1 + p_2}{2\rho} \int \frac{p_2 - p_1}{\Delta r} dt$
- Rozdíl tlaků (a tedy fázový posun) je největší, když zvuková vlna dopadá ve směru osy mikrofonů (jeden zasáhne dříve než druhý).
- Pokud vlna dopadá kolmo na osu (z boku), dorazí k oběma mikrofonům současně $\to$ rozdíl je nulový $\to$ naměřená intenzita je nulová (minimum).
- Sonda má tedy "osmičkovou" směrovou charakteristiku ($\cos \theta$).

## Related Concepts
- [[Akustická intenzita]]
- [[PU sonda]]
- [[Směrová charakteristika]]
