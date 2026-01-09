---
id: 20260106_diagnostics_061
course: Diagnostika a testování
tags: [vířivé proudy, hloubka vniku, výpočet]
difficulty: 3
type: multiple_choice
status: to_learn
---

# Question
Jaká je intenzita (hustota proudu) $H$ v hloubce $3\delta$ (trojnásobná hloubka vniku) pod povrchem měřeného objektu, pokud na povrchu je $H_0$?

## Options
A) $0.02 \cdot H_0$
B) $0.05 \cdot H_0$
C) $0.12 \cdot H_0$
D) $0.37 \cdot H_0$

---
# Solution
**Correct Answer:** B

## Explanation
Intenzita vířivých proudů klesá s hloubkou $x$ exponenciálně:
$$ H(x) = H_0 \cdot e^{-x/\delta} $$
Pokud dosadíme $x = 3\delta$:
$$ H(3\delta) = H_0 \cdot e^{-3\delta/\delta} = H_0 \cdot e^{-3} $$
Hodnota $e^{-3} \approx 0.0498 \approx 0.05$.
Tedy intenzita klesne na cca **5 %** hodnoty na povrchu.
(V hloubce $1\delta$ je to $e^{-1} \approx 0.37$, tj. 37 %).

## Related Concepts
- [[Standardní hloubka vniku]]
- [[Skin efekt]]
- [[Vířivé proudy]]
