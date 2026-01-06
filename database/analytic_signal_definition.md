---
id: 20260106_diagnostics_017
course: Diagnostika a testování
tags: [zpracování signálu, hilbertova transformace, obálka]
difficulty: 3
type: open
status: to_learn
---

# Question
Co je to analytický signál?

---
# Solution
**Short Answer:** Komplexní signál, jehož reálná část je původní signál a imaginární část je jeho Hilbertova transformace.

## Explanation
Analytický signál $z(t)$ je komplexní reprezentace reálného signálu $x(t)$, která usnadňuje výpočet okamžité amplitudy (obálky) a okamžité fáze/frekvence.

Definice:
$$ z(t) = x(t) + j \cdot \mathcal{H}[x(t)] $$
kde $\mathcal{H}[x(t)]$ je Hilbertova transformace signálu $x(t)$ (což je v podstatě posun všech frekvenčních složek o $-90^\circ$ neboli $-\pi/2$).

Vlastnosti:
- **Absolutní hodnota** $|z(t)|$ představuje **obálku** signálu.
- **Argument** $\arg(z(t))$ představuje **okamžitou fázi**.
- Spektrum analytického signálu je nulové pro záporné frekvence (obsahuje pouze kladné frekvence původního spektra, vynásobené 2).

## Related Concepts
- [[Hilbertova transformace]]
- [[Obálková analýza]]
- [[Okamžitá frekvence]]
