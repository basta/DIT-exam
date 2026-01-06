---
id: 20260106_diagnostics_030
course: Diagnostika a testování
tags: [vibrodiagnostika, senzory, akcelerometr, piezo]
difficulty: 2
type: multiple_choice
status: to_learn
---

# Question
V jaké oblasti (poměrné frekvence $\eta = f/f_0$) se používají piezoelektrické akcelerometry?

## Options
A) $\eta \ll 1$ (hluboko pod rezonancí)
B) $\eta \gg 1$ (vysoko nad rezonancí)
C) $\eta = 1$ (v rezonanci)
D) $\eta = 0.7$

---
# Solution
**Correct Answer:** A

## Explanation
Piezoelektrické akcelerometry jsou systémy typu "hmota na pružině" (krystal funguje jako tuhá pružina).
- Měřená veličina (výstupní náboj/napětí) je úměrná síle působící na krystal ($F = m \cdot a$).
- Tato proporcionalita platí v oblasti tuhosti, tj. **pod rezonanční frekvencí**.
- Typicky se používají do cca $1/3$ až $1/2$ vlastní frekvence snímače (v lineární části charakteristiky).
- Pro $\eta \ll 1$ je přenos rovný jedné (koeficientu citlivosti) a fázový posun je nulový.

Naopak elektrodynamické snímače rychlosti (seizmické) pracují v oblasti $\eta \gg 1$ (nad rezonancí, oblast hmotnosti).

## Related Concepts
- [[Piezoelektrický jev]]
- [[Akcelerometr]]
- [[Frekvenční charakteristika snímačů]]
