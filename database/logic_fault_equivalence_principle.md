---
id: 20260106_diagnostics_048
course: Diagnostika a testování
tags: [testování číslicových obvodů, poruchy, ekvivalence]
difficulty: 2
type: open
status: to_learn
---

# Question
V čem spočívá princip ekvivalence u zjišťování poruch logických obvodů (a k čemu slouží)?

---
# Solution
**Short Answer:** Umožňuje sloučit nerozlišitelné poruchy do jedné třídy a tím snížit počet nutných testů (zkrátit dobu testování).

## Explanation
- **Princip:** Dvě poruchy jsou ekvivalentní, pokud se obvod při jejich výskytu chová navenek (na výstupech) naprosto stejně pro všechny možné vstupní kombinace.
- Např. u hradla AND:
  - Vstup A Stuck-at-0 (SA0).
  - Vstup B Stuck-at-0 (SA0).
  - Výstup Y Stuck-at-0 (SA0).
  - Tyto tři poruchy způsobí, že výstup je trvale 0. Jsou funkčně ekvivalentní.
- **Význam:** Stačí vygenerovat test pouze pro jednu poruchu z dané třídy ekvivalence a tím odhalíme (pokryjeme) všechny poruchy v této třídě. To výrazně redukuje velikost seznamu poruch (Fault collapsing) a zrychluje generování testů i samotné testování.

## Related Concepts
- [[Fault Equivalence]]
- [[Fault Collapsing]]
- [[Stuck-at Fault]]
