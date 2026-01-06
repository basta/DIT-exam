---
id: 20260106_diagnostics_036
course: Diagnostika a testování
tags: [zpracování signálu, okna, dynamický rozsah]
difficulty: 4
type: multiple_choice
status: to_learn
---

# Question
Máte dva signály blízko sebe (frekvenční vzdálenost $1,5 \times \Delta f$). Jeden má silnou amplitudu a druhý je o $-50 \text{ dB}$ menší. Jaké okno použijete pro jejich rozlišení?

## Options
A) Obdélníkové (Rectangular)
B) Hanning
C) Blackman-Harris (nebo Flat-top)
D) Trojúhelníkové

---
# Solution
**Correct Answer:** C

## Explanation
Pro rozlišení velmi slabého signálu v blízkosti silného signálu (vysoký dynamický rozsah) je klíčové, aby **postranní laloky** okna silného signálu "nepřekryly" slabý signál.
- **Obdélníkové okno:** První postranní lalok je jen $-13 \text{ dB}$. Slabý signál (-50 dB) by byl zcela schován v "leakage" silného signálu.
- **Hanning:** Postranní laloky klesají rychleji, ale první je cca $-31 \text{ dB}$. Stále nemusí stačit na -50 dB těsně vedle.
- **Blackman-Harris:** Má o něco širší hlavní lalok, ale **extrémně nízké postranní laloky** (první pod $-90 \text{ dB}$). To bezpečně umožní detekovat signál o amplitudu -50 dB, i když je blízko.

Poznámka: I když je frekvenční rozlišení (šířka hlavního laloku) u Blackman-Harris horší, "vzdálenost 1,5f" (pokud je myšleno 1.5 binů, což je málo) by mohla být problém, ale prioritou zde je dynamika (-50dB), kterou jiné okno nezvládne. V praxi pro "blízké" signály chceme úzký lalok, ale pro "velký rozdíl amplitud" chceme nízké postranní laloky. Zadání naznačuje volbu B-K (Blackman-Harris), což je správná volba pro amplitudu.

## Related Concepts
- [[Okna (Windowing)]]
- [[Dynamický rozsah spektra]]
- [[Spectral Leakage]]
