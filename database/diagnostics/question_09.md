---
id: 20260106_diagnostics_009
course: Diagnostika a testování
tags: [modely poruch, logické členy, ekvivalence poruch]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
U logického členu OR (log.součet) jsou ekvivalentní modely poruch:

## Options
A) stuck-at-0 na vstupech se stuck-at-0 na výstupu
B) stuck-at-1 na vstupech se stuck-at-0 na výstupu
C) stuck-at-1 na vstupech se stuck-at-1 na výstupu
D) stuck-at-1 na vstupech se stuck-open na výstupu

---
# Solution
**Correct Answer:** C

## Explanation
Pro hradlo OR platí, že pokud je alespoň jeden vstup log. 1, výstup je log. 1.
Pokud má hradlo poruchu typu **stuck-at-1 (trvalá nula)** na libovolném vstupu, chová se to stejně, jako by byl vstup trvale připojen na log. 1. Díky funkci OR ($Y = A + B$) bude výstup trvale log. 1, což je nerozlišitelné od poruchy **stuck-at-1 na výstupu**. Je to porucha dominance.

Naopak stuck-at-0 na jednom vstupu neovlivní výstup trvale (pokud druhý vstup funguje), takže není ekvivalentní se stuck-at-0 na výstupu.

### Steps / Derivation
1. Funkce: $Y = A + B$.
2. Porucha A/1 ($A=1$): $Y = 1 + B = 1$.
3. Porucha Y/1 ($Y=1$): $Y = 1$.
4. Z hlediska vstupně/výstupního chování jsou totožné.
$$
A=1 \implies Y=1 \iff Y=1
$$

## Related Concepts
- [[Ekvivalence poruch]]
- [[Stuck-at fault model]]
- [[Dominance poruch]]
