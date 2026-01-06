---
id: 20260106_diagnostics_039
course: Diagnostika a testování
tags: [zpracování signálu, kepstrum, harmonické]
difficulty: 3
type: open
status: to_learn
---

# Question
Co je důležité (co vidíme) v kepstru (cepstrum) ze signálu?

---
# Solution
**Short Answer:** Periodicky se opakující složky ve spektru (rodiny harmonických nebo postranních pásem).

## Explanation
Kepstrum je definováno jako "inverzní Fourierova transformace logaritmu spektra".
- Pokud spektrum obsahuje řadu harmonických složek nebo postranních pásem s konstantním rozestupem $\Delta f$ (např. od poruchy ložiska, převodovky nebo ozvěny), je to ve frekvenční doméně "periodický" jev.
- Kepstrum analyzuje tuto periodicitu spektra.
- Jediná výrazná špička v kepstru (na kvefrenci $\tau = 1/\Delta f$) tak dokáže indikovat přítomnost celé rodiny harmonických nebo modulačních pásem, které by v klasickém spektru byly schované v šumu nebo těžko identifikovatelné jako skupina.
- Kepstrum "sesbírá" energii všech těchto souvisejících čar do jedné.

## Related Concepts
- [[Kepstrální analýza]]
- [[Rahmonics]]
- [[Diagnostika převodovek]]
