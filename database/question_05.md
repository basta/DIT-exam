---
id: 20260106_diagnostics_005
course: Diagnostika a testování
tags: [termovize, měření teploty]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Které veličiny z uvedených je nutno znát při termovizním určování teploty tělesa:

## Options
A) hustotu tělesa
B) emisivitu tělesa
C) prostupnost prostředí
D) barvu tělesa

---
# Solution
**Correct Answer:** B

## Explanation
Při bezkontaktním měření teploty termokamerou je klíčovým parametrem **emisivita** ($\varepsilon$) povrchu tělesa. Emisivita určuje, jak moc těleso vyzařuje tepelné záření v porovnání s ideálním černým tělesem.

Kamera měří celkové dopadající záření, které se skládá z vlastního vyzařování objektu a odraženého záření okolí. Bez znalosti emisivity nelze z naměřeného radiačního toku správně vypočítat povrchovou teplotu.

### Steps / Derivation
1. Stefan-Boltzmannův zákon pro reálné těleso: $P = \varepsilon \sigma T^4$.
2. Korekce na odraženou teplotu vyžaduje $\varepsilon$.
$$
W_{tot} = \varepsilon W_{obj} + (1-\varepsilon) W_{refl}
$$

## Related Concepts
- [[Termografie]]
- [[Emisivita]]
