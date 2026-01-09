---
id: 20260106_diagnostics_043
course: Diagnostika a testování
tags: [zpracování signálu, okna, přesnost amplitudy]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Máte ve spektru (FFT) dva píky, které jsou od sebe frekvenčně **daleko**. Jaké okno použijete, pokud vám jde o co nejpřesnější určení **amplitudy** signálu?

## Options
A) Obdélníkové (Rectangular)
B) Flat-top
C) Hanning
D) Exponenciální

---
# Solution
**Correct Answer:** B (ale v kontextu dynamiky může být i Blackman-Harris)

## Explanation
- **Flat-top:** Toto okno má velmi široký hlavní lalok s plochým vrcholem. To zajišťuje, že i když frekvence signálu netrefí přesně "bin" (spektrální čáru), chyba určení amplitudy (Picket fence effect) je minimální (< 0.1 dB). Je tedy nejlepší pro **přesné měření amplitudy**.
- **Blackman-Harris:** Má také velmi dobrou přesnost amplitudy a hlavně výborný dynamický rozsah (potlačení postranních laloků).
- Pokud jsou píky "daleko od sebe", nehrozí tolik vzájemné ovlivnění postranními laloky (leakage), takže prioritou je minimalizace chyby amplitudy ("scalloping loss").
- Obdélníkové okno má sice úzký lalok, ale velkou chybu amplitudy (až 3.9 dB), pokud signál neleží přesně na binu.

Poznámka ze zadání: "uznal i Flat-top". Z hlediska teorie je pro amplitudu Flat-top "nejsprávnější", Blackman-Harris je kompromis pro dynamiku.

## Related Concepts
- [[Okna (Windowing)]]
- [[Picket fence effect]]
- [[Flat-top window]]
