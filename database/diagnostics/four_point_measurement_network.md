---
id: 20260106_diagnostics_063
course: Diagnostika a testování
tags: [elektrická měření, in-circuit, jehlové pole]
difficulty: 3
type: derivation
status: to_learn
---

# Question
Nakreslete princip 4-bodového zapojení jehel (Kelvinovo měření) v libovolné impedanční síti při měření hodnoty rezistoru.

---
# Solution
**Correct Answer:** Schéma se dvěma páry vodičů (Force a Sense) připojenými k jednomu rezistoru.

## Explanation
4-bodové měření (Kelvin sensing) slouží k eliminaci vlivu přechodových odporů kontaktů a odporu přívodních vodičů (důležité pro malé odpory).
- **Par 1 (Force/Source):** Zdroj proudu ($I$) je připojen na konce rezistoru. Těmito vodiči teče měřicí proud, vzniká na nich úbytek napětí, který ale neměříme.
- **Par 2 (Sense/Measure):** Voltmetr (vysokoimpedanční) je připojen přímo na vývody rezistoru (uvnitř proudových svorek). Těmito vodiči neteče téměř žádný proud, takže na nich nevzniká úbytek.
- Voltmetr změří přesně napětí na rezistoru $R_x$. Hodnota $R = U_{sense} / I_{force}$.

(V kontextu impedanční sítě se může kombinovat s Guardingem - viz 6-bodové měření).

## Related Concepts
- [[4-vodičové měření (Kelvin)]]
- [[Bed-of-Nails tester]]
