---
id: 20260106_diagnostics_026
course: Diagnostika a testování
tags: [zpracování signálu, synchronní průměrování, TSA]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
Jaké signály **nemohu** vyfiltrovat (odstranit) pomocí synchronizovaného průměrování (Time Synchronous Averaging)?

## Options
A) Synchronní deterministické
B) Synchronní náhodné
C) Nesynchronní deterministické
D) Nesynchronní nenahodne (stochastické)

---
# Solution
**Correct Answer:** A

## Explanation
**Synchronní průměrování (TSA)** slouží k **vytažení** (extrakci) užitečného signálu, který je synchronní s otáčkami (deterministický), z šumu a jiných vibrací.
- Principem je průměrování mnoha úseků signálu, spouštěných přesně ve stejný okamžik vůči natočení hřídele (trigger).
- **Synchronní deterministické** složky (např. nevývažek, zubová frekvence) se ve průměru sčítají a **zůstávají** zachovány. Tedy je "nelze vyfiltrovat" ve smyslu "odstranit z výsledku". Naopak, jsou to jediné složky, které zůstanou.
- Všechny ostatní složky (nesynchronní vibrace od jiných strojů, náhodný šum) se s rostoucím počtem průměrů limitně blíží nule (jsou potlačeny/vyfiltrovány).

**Pozor na formulaci:** Pokud je cílem "získat" synchronní signál, tak průměrování "odfiltruje" vše ostatní. Pokud se ptáme, co ve výsledku **zůstane**, je to synchronní deterministický signál.

## Related Concepts
- [[Synchronní průměrování (TSA)]]
- [[Signál vs Šum]]
