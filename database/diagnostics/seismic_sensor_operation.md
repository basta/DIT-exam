---
id: 20260106_diagnostics_024
course: Diagnostika a testování
tags: [senzory, vibrace, elektrodynamický snímač]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
U absolutního elektrodynamického senzoru (seizmického snímače rychlosti) je seizmická hmotnost v klidu (vůči inerciálnímu prostoru), když je poměr frekvence buzení k vlastní frekvenci ($\eta = f/f_0$):

## Options
A) $\eta \ll 1$ (frekvence hluboko pod rezonancí)
B) $\eta = 1$ (v rezonanci)
C) $\eta \gg 1$ (frekvence vysoko nad rezonancí)
D) $\eta = 0$

---
# Solution
**Correct Answer:** C

## Explanation
Seizmické snímače (pro měření absolutních vibrací) pracují v oblasti **nad rezonancí** (obvykle se uvádí $\eta > 3$, nebo symbolicky $\Psi \gg 1$ podle vaší notace).
- V této oblasti setrvačná síla hmotnosti převládá nad silou pružiny. Hmotnost "nestíhá" sledovat pohyb pouzdra senzoru a zůstává v prostoru prakticky "stát" (v klidu), zatímco pouzdro vibruje kolem ní.
- Relativní pohyb mezi cívkou (pevná s pouzdrem) a magnetem (seizmická hmotnost) pak generuje napětí úměrné rychlosti vibrací.
- Naopak akcelerometry (piezo) pracují pod rezonancí ($\eta \ll 1$), kde se hmotnost pohybuje spolu s pouzdrem a síla na krystal je úměrná zrychlení.

## Related Concepts
- [[Seizmický snímač]]
- [[Vlastní frekvence]]
- [[Přenosová charakteristika 2. řádu]]
