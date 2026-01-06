---
id: 20260106_diagnostics_050
course: Diagnostika a testování
tags: [elektrická měření, in-circuit, guarding, odpor]
difficulty: 4
type: derivation
status: to_learn
---

# Question
Nakreslete zapojení pro **6-bodové in-circuit měření odporu** (měření součástky zapojené v síti rezistorů tak, aby okolní součástky neovlivnily výsledek).
*(Poznámka: Pozor na polaritu vstupů operačních zesilovačů ve schématu).*

---
# Solution
**Correct Answer:** (Schéma využívající metodu "Guarding" s dvěma operačními zesilovači pro izolaci měřeného rezistoru).

## Explanation
Při měření odporu $R_x$ zapojeného v obvodu (In-Circuit) je tento odpor ovlivněn paralelními cestami přes ostatní součástky ($R_a, R_b...$).
Pro eliminaci tohoto vlivu se používá **metoda Guarding (stínění/vnucení napětí)**.

### Princip 6-bodového měření (nebo obecně "Active Guarding"):
1.  **Zdroj proudu/napětí:** Aplikujeme testovací signál přímo na měřený rezistor $R_x$.
2.  **Virtuální zem (OZ1):** Jeden konec $R_x$ je připojen do uzlu s virtuální zemí (invertující vstup OZ). Tím je zajištěno, že tento uzel je na potenciálu 0V, ale proud teče do zpětné vazby.
3.  **Guarding (OZ2 - sledovač):** Napětí z druhého konce $R_x$ (budicího) je snímáno sledovačem a vnuceno do okolních uzlů (Guard points).
4.  **Výsledek:**
    - Protože je na Guard uzlech stejné napětí jako na budicím uzlu $R_x$, neteče paralelními cestami žádný proud (rozdíl potenciálů je 0).
    - Protože je druhý konec $R_x$ na virtuální zemi (0V) a ostatní uzly připojené k zemi jsou také na 0V (nebo Guardingem na 0V), neteče proud ani tudy.
    - Veškerý proud tekoucí přes $R_x$ teče do měřicího obvodu.

*(Pozor: Ve skriptech bývá u OZ ve zpětné vazbě prohozené plus/mínus, nutno zajistit negativní zpětnou vazbu).*

## Related Concepts
- [[In-Circuit Test (ICT)]]
- [[Guarding technique]]
- [[Operační zesilovač]]
