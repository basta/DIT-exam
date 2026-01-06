---
id: 20260106_diagnostics_002
course: Diagnostika a testování
tags: [fuzzy logika, operátory]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Standardní fuzzy AND (fuzzy log. součin) může být pro míry (stupně) příslušnosti $A, B$ definována jako:

## Options
A) $A - B$
B) $\min(A, B)$
C) $\max(A, B)$
D) $(1 - A) . (1 - B)$

---
# Solution
**Correct Answer:** B

## Explanation
Standardní Zadehovy operátory pro fuzzy logiku definují:
- **Fuzzy AND (t-norma):** $\min(A, B)$
- **Fuzzy OR (s-norma):** $\max(A, B)$
- **Fuzzy NOT:** $1 - A$

Alternativní definicí pro součin (AND) je algebraický součin $A \cdot B$, ale "standardní" definice obvykle odkazuje na minimum.

### Steps / Derivation
1. Pro $A, B \in [0, 1]$ hledáme průnik.
2. $\min(A, B)$ splňuje axiomy t-normy.
$$
\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x))
$$

## Related Concepts
- [[Fuzzy logika]]
- [[T-norma]]
