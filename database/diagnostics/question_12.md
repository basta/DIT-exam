---
id: 20260106_diagnostics_012
course: Diagnostika a testování
tags: [in-circuit test, měření odporu, guarding, operační zesilovač]
difficulty: 4
type: derivation
status: to_learn
---

# Question
Nakreslete princip in-circuit měření odporu R1 v dané impedanční síti při metodě připojením na zemní potenciál (2b.), navrhněte velikosti potřebných veličin a hodnoty použitých pasivních prvků (součástek) tak, aby při rozsahu R1 od $100\Omega$ do $1k\Omega$ byl úbytek napětí na R1 maximálně 1V (2b.). Napište konkrétní vzorec pro výpočet hodnoty odporu R1 z obvodových veličin měřicího zapojení, veličiny ve schématu označte (2b.).

*Obrázek:* Impedanční síť s odpory a kondenzátory, R1 je "nahoře".
![schema](image-2.png)

---
# Solution
**Vzorec:** $R_1 = - \frac{U_{zdroj}}{U_{out}} \cdot R_{ref}$ (nebo ekvivalentní podle zapojení).

## Explanation
Pro in-circuit měření součástky (R1), která je zapojena v mřížce s ostatními součástkami (paralelní cesty), se používá metoda **guarding** (stínění/uzemnění uzlů). Cílem je eliminovat vliv paralelních impedancí tím, že se uzly spojující tyto impedance připojí na virtuální zem.

### 1. Princip zapojení (Active Guarding)
Použijeme operační zesilovač v invertujícím zapojení.
- **R1 (měřený odpor):** Zapojíme ho jako zpětnovazební odpor operačního zesilovače. (Nebo jako vstupní, záleží na topologii, běžnější je R1 ve zpětné vazbě pro linearitu s vodivostí, ale zde chceme měřit odpor).
- **Uzly:** Jeden konec R1 připojíme na vstup OZ (virtuální zem), druhý na výstup OZ.
- **Guard:** Všechny uzly, které by tvořily paralelní cestu k R1, připojíme na zemní potenciál. Tím pádem přes tyto paralelní větve neteče proud do měřicího uzlu (protože na obou koncích paralelní větve připojené k vstupu OZ je 0V - virtuální nula a skutečná nula).

**Návrh zapojení:**
1. Zdroj referenčního napětí $U_{ref}$ (nebo proudu).
2. Operační zesilovač.
3. Referenční odpor $R_{ref}$ (známý).
4. Zapojení: $U_{ref}$ přes $R_{ref}$ na invertující vstup. Invertující vstup je virtuální zem. R1 je zapojen mezi invertující vstup a výstup OZ.
5. Všechny ostatní uzly spojené s invertujícím vstupem uzemníme.

### 2. Návrh hodnot
- **Podmínka:** $U_{R1} \le 1V$.
- Rozsah $R_1$: $100\Omega$ až $1000\Omega$.
- Pokud použijeme zdroj konstantního proudu $I_m$ tekoucí skrz R1:
    - $U_{R1} = R_1 \cdot I_m$.
    - $Max(U_{R1}) = 1000\Omega \cdot I_m \le 1V \implies I_m \le 1mA$.
- Volíme měřicí proud **$I_m = 1mA$**.
- Realizace proudu: Napěťový zdroj $U_{in}$ a vstupní odpor $R_{in}$.
    - Nechť $U_{in} = -1V$.
    - Pak $I = U_{in}/R_{in}$. Chceme 1mA. $\implies R_{in} = 1k\Omega$.
- Zapojení:
    - $U_{in} = -1V$ na vstupní odpor $R_{ref} = 1k\Omega$.
    - $R_1$ ve zpětné vazbě.
    - $U_{out} = - U_{in} \frac{R_1}{R_{ref}} = 1V \frac{R_1}{1000}$.
    - Pro $R_1=1000\Omega \to U_{out} = 1V$. (Splněno).
    - Pro $R_1=100\Omega \to U_{out} = 0.1V$.

### 3. Vzorec
$$
U_{out} = - U_{in} \frac{R_1}{R_{ref}} \implies R_1 = - \frac{U_{out}}{U_{in}} R_{ref}
$$
Kde $U_{in}$ je vstupní napětí, $R_{ref}$ je známý odpor, $U_{out}$ je měřené napětí.

## Related Concepts
- [[In-circuit test (ICT)]]
- [[Operační zesilovač - invertující zapojení]]
- [[Guarding (měření)]]
