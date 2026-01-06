---
id: 20260106_diagnostics_055
course: Diagnostika a testování
tags: [testování číslicových obvodů, LFSR, generování testů]
difficulty: 3
type: open
status: to_learn
---

# Question
K čemu může sloužit číslicový obvod se zpětnou vazbou (posuvný registr s lineární zpětnou vazbou - LFSR)?

---
# Solution
**Short Answer:** K generování pseudonáhodných testovacích vektorů (PRPG) nebo k analýze odezvy (Signaturová analýza / MISR).

## Explanation
**LFSR (Linear Feedback Shift Register)** je posuvný registr, kde vstup je tvořen XOR kombinací (zpětnou vazbou) výstupů určitých klopných obvodů.
- **Generátor (PRPG):** LFSR dokáže generovat dlouhou sekvenci pseudonáhodných čísel (vzorů), která se opakuje až po $2^n - 1$ cyklech. To se využívá v **BIST (Built-In Self-Test)** pro rychlé generování testovacích vektorů přímo na čipu bez potřeby externí paměti.
- **Analyzátor (Signatura):** LFSR (resp. MISR) dokáže "komprimovat" dlouhou sekvenci výstupních dat z testovaného obvodu do jednoho finálního čísla (signatury), které se porovná se správnou hodnotou.

## Related Concepts
- [[LFSR]]
- [[BIST (Built-In Self-Test)]]
- [[Pseudonáhodný generátor]]
