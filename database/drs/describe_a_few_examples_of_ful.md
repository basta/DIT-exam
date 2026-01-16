---
id: drs_078
course: Dynamics and Control of Networks
tags: [epidemiology, compartment-models, mass-action, network-dynamics]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe a few examples of fully mixed epidemics models, e.g. SI, SIR, SIS, SEIR.

## Options
N/A (Open Question)

---
# Solution
**Correct Answer:** Evaluation focuses on the definition of state transitions (Susceptible, Infectious, Recovered, Exposed) and the assumption of homogeneous mixing.

## Explanation
Fully mixed epidemic models, often referred to as compartmental models, operate on the "Mass Action" principle. This assumes that every individual in a population has an equal probability of coming into contact with every other individual, effectively ignoring the specific topology of a social network in favor of mean-field approximations. The population $N$ is divided into compartments based on disease status.

1. **SI Model**: The simplest form where individuals start as Susceptible ($S$) and, upon contact with an infected peer, move to the Infectious ($I$) state permanently. There is no recovery, meaning the entire population eventually becomes infected. It is described by $\frac{dI}{dt} = \beta S I / N$.

2. **SIS Model**: Suitable for diseases that do not confer long-term immunity (e.g., the common cold). Individuals transition from $S \to I \to S$. The system reaches an endemic equilibrium if the basic reproduction number $R_0 > 1$, otherwise the disease dies out.

3. **SIR Model**: The foundational model for conferring immunity. Individuals move from $S \to I \to R$ (Recovered/Removed). Once in $R$, they can no longer infect others or be reinfected. This model is characterized by a "spike" in infections that eventually subsides as the pool of susceptible individuals is depleted.

4. **SEIR Model**: Incorporates an "Exposed" ($E$) period. Individuals are infected but not yet infectious (latency). This adds a delay to the dynamics, often making the model more realistic for viral diseases like influenza or COVID-19.

### Steps / Derivation
1. Define the transmission rate $\beta$ (rate of $S+I \to 2I$) and recovery rate $\gamma$ (rate of $I \to R$).
2. Apply the conservation of mass: $N = S(t) + I(t) + R(t)$.
3. Formulate the Differential Equations (e.g., for SIR):
$$
\frac{dS}{dt} = -\frac{\beta S I}{N}
$$
$$
\frac{dI}{dt} = \frac{\beta S I}{N} - \gamma I
$$
$$
\frac{dR}{dt} = \gamma I
$$

## Related Concepts
- [[basic_reproduction_number]]
- [[mass_action_principle]]
- [[compartmental_modeling]]